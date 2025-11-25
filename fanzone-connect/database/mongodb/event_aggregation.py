"""
🏆 FANZONE CONNECT - MONGODB EVENT AGGREGATION
Combines Multiple Learning Modules:
- Module 12: NoSQL Databases (MongoDB, document storage, aggregation)
- Module 48: Data Science Mastery (data analysis, statistical modeling)
- Module 49: AI Machine Learning (predictive analytics, recommendation systems)

World Cup 2026 Fan Platform - Advanced Event Analytics & Recommendations
"""

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import statistics

import motor.motor_asyncio
from pymongo import ASCENDING, DESCENDING
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 12: NOSQL DATABASES - MONGODB OPERATIONS
# =====================================================

class MongoEventAnalytics:
    """
    Advanced MongoDB operations for World Cup event analytics
    Handles millions of fan interactions and event data
    """
    
    def __init__(self, connection_string: str = "mongodb://fanzone_admin:worldcup2026@mongodb:27017/fanzone_events"):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
        self.db = self.client.fanzone_events
        
        # Collections
        self.events = self.db.events
        self.user_interactions = self.db.user_interactions
        self.fan_preferences = self.db.fan_preferences
        self.match_analytics = self.db.match_analytics
        self.recommendation_cache = self.db.recommendation_cache
        
        logger.info("🍃 MongoDB Event Analytics initialized for World Cup 2026")
    
    async def create_indexes(self):
        """Create optimized indexes for World Cup queries"""
        
        # Events collection indexes
        await self.events.create_index([("event_type", ASCENDING), ("start_time", ASCENDING)])
        await self.events.create_index([("location.city", ASCENDING), ("start_time", ASCENDING)])
        await self.events.create_index([("tags", ASCENDING)])
        await self.events.create_index([("capacity", ASCENDING), ("current_attendees", ASCENDING)])
        
        # User interactions indexes
        await self.user_interactions.create_index([("user_id", ASCENDING), ("timestamp", DESCENDING)])
        await self.user_interactions.create_index([("event_id", ASCENDING), ("interaction_type", ASCENDING)])
        await self.user_interactions.create_index([("timestamp", DESCENDING)])
        
        # Geospatial index for location-based queries
        await self.events.create_index([("location.coordinates", "2dsphere")])
        
        logger.info("📊 MongoDB indexes created successfully")
    
    async def aggregate_event_popularity(self, time_range_hours: int = 24) -> List[Dict[str, Any]]:
        """
        Aggregate event popularity using MongoDB aggregation pipeline
        Returns trending events for World Cup dashboard
        """
        
        start_time = datetime.utcnow() - timedelta(hours=time_range_hours)
        
        pipeline = [
            # Match recent interactions
            {
                "$match": {
                    "timestamp": {"$gte": start_time},
                    "interaction_type": {"$in": ["view", "like", "share", "attend"]}
                }
            },
            
            # Group by event and calculate metrics
            {
                "$group": {
                    "_id": "$event_id",
                    "total_interactions": {"$sum": 1},
                    "unique_users": {"$addToSet": "$user_id"},
                    "views": {
                        "$sum": {"$cond": [{"$eq": ["$interaction_type", "view"]}, 1, 0]}
                    },
                    "likes": {
                        "$sum": {"$cond": [{"$eq": ["$interaction_type", "like"]}, 1, 0]}
                    },
                    "shares": {
                        "$sum": {"$cond": [{"$eq": ["$interaction_type", "share"]}, 1, 0]}
                    },
                    "attendees": {
                        "$sum": {"$cond": [{"$eq": ["$interaction_type", "attend"]}, 1, 0]}
                    }
                }
            },
            
            # Calculate engagement score
            {
                "$addFields": {
                    "unique_user_count": {"$size": "$unique_users"},
                    "engagement_score": {
                        "$add": [
                            {"$multiply": ["$views", 1]},
                            {"$multiply": ["$likes", 3]},
                            {"$multiply": ["$shares", 5]},
                            {"$multiply": ["$attendees", 10]}
                        ]
                    }
                }
            },
            
            # Lookup event details
            {
                "$lookup": {
                    "from": "events",
                    "localField": "_id",
                    "foreignField": "_id",
                    "as": "event_details"
                }
            },
            
            # Unwind event details
            {"$unwind": "$event_details"},
            
            # Project final results
            {
                "$project": {
                    "event_id": "$_id",
                    "event_title": "$event_details.title",
                    "event_type": "$event_details.event_type",
                    "location": "$event_details.location",
                    "start_time": "$event_details.start_time",
                    "total_interactions": 1,
                    "unique_users": "$unique_user_count",
                    "engagement_score": 1,
                    "metrics": {
                        "views": "$views",
                        "likes": "$likes",
                        "shares": "$shares",
                        "attendees": "$attendees"
                    }
                }
            },
            
            # Sort by engagement score
            {"$sort": {"engagement_score": DESCENDING}},
            
            # Limit to top 50 events
            {"$limit": 50}
        ]
        
        results = []
        async for doc in self.user_interactions.aggregate(pipeline):
            results.append(doc)
        
        logger.info(f"📈 Aggregated popularity for {len(results)} trending events")
        return results
    
    async def get_city_event_distribution(self) -> Dict[str, Any]:
        """Get event distribution across World Cup host cities"""
        
        pipeline = [
            # Group by city
            {
                "$group": {
                    "_id": "$location.city",
                    "total_events": {"$sum": 1},
                    "event_types": {"$push": "$event_type"},
                    "avg_capacity": {"$avg": "$capacity"},
                    "total_capacity": {"$sum": "$capacity"}
                }
            },
            
            # Calculate event type distribution
            {
                "$addFields": {
                    "event_type_counts": {
                        "$reduce": {
                            "input": "$event_types",
                            "initialValue": {},
                            "in": {
                                "$mergeObjects": [
                                    "$$value",
                                    {
                                        "$arrayToObject": [
                                            [{"k": "$$this", "v": {"$add": [{"$ifNull": [{"$getField": {"field": "$$this", "input": "$$value"}}, 0]}, 1]}}]
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            
            # Sort by total events
            {"$sort": {"total_events": DESCENDING}}
        ]
        
        results = {}
        async for doc in self.events.aggregate(pipeline):
            city = doc["_id"]
            results[city] = {
                "total_events": doc["total_events"],
                "avg_capacity": round(doc["avg_capacity"], 2),
                "total_capacity": doc["total_capacity"],
                "event_types": doc["event_type_counts"]
            }
        
        logger.info(f"🏙️ Analyzed event distribution for {len(results)} cities")
        return results

# =====================================================
# MODULE 48: DATA SCIENCE MASTERY - STATISTICAL ANALYSIS
# =====================================================

class FanBehaviorAnalytics:
    """
    Advanced data science analytics for World Cup fan behavior
    Statistical modeling and trend analysis
    """
    
    def __init__(self, mongo_client: MongoEventAnalytics):
        self.mongo = mongo_client
        self.scaler = StandardScaler()
        
    async def analyze_fan_engagement_patterns(self, days: int = 7) -> Dict[str, Any]:
        """Analyze fan engagement patterns using statistical methods"""
        
        start_date = datetime.utcnow() - timedelta(days=days)
        
        # Get user interaction data
        interactions = []
        async for doc in self.mongo.user_interactions.find({
            "timestamp": {"$gte": start_date}
        }):
            interactions.append({
                "user_id": doc["user_id"],
                "event_id": doc["event_id"],
                "interaction_type": doc["interaction_type"],
                "timestamp": doc["timestamp"],
                "hour": doc["timestamp"].hour,
                "day_of_week": doc["timestamp"].weekday()
            })
        
        if not interactions:
            return {"error": "No interaction data found"}
        
        # Convert to DataFrame for analysis
        df = pd.DataFrame(interactions)
        
        # Hourly engagement analysis
        hourly_engagement = df.groupby('hour').size().to_dict()
        
        # Daily engagement analysis
        daily_engagement = df.groupby('day_of_week').size().to_dict()
        
        # User engagement distribution
        user_engagement = df.groupby('user_id').size()
        engagement_stats = {
            "mean": float(user_engagement.mean()),
            "median": float(user_engagement.median()),
            "std": float(user_engagement.std()),
            "min": int(user_engagement.min()),
            "max": int(user_engagement.max())
        }
        
        # Interaction type distribution
        interaction_distribution = df['interaction_type'].value_counts().to_dict()
        
        # Peak engagement times
        peak_hour = max(hourly_engagement, key=hourly_engagement.get)
        peak_day = max(daily_engagement, key=daily_engagement.get)
        
        return {
            "analysis_period": f"{days} days",
            "total_interactions": len(interactions),
            "unique_users": df['user_id'].nunique(),
            "unique_events": df['event_id'].nunique(),
            "hourly_engagement": hourly_engagement,
            "daily_engagement": daily_engagement,
            "user_engagement_stats": engagement_stats,
            "interaction_distribution": interaction_distribution,
            "peak_engagement": {
                "hour": peak_hour,
                "day_of_week": peak_day
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    
    async def calculate_event_success_metrics(self, event_id: str) -> Dict[str, Any]:
        """Calculate comprehensive success metrics for an event"""
        
        # Get event details
        event = await self.mongo.events.find_one({"_id": event_id})
        if not event:
            return {"error": "Event not found"}
        
        # Get all interactions for this event
        interactions = []
        async for doc in self.mongo.user_interactions.find({"event_id": event_id}):
            interactions.append(doc)
        
        if not interactions:
            return {"error": "No interaction data found for event"}
        
        df = pd.DataFrame(interactions)
        
        # Calculate metrics
        total_interactions = len(interactions)
        unique_users = df['user_id'].nunique()
        
        # Engagement rate (if capacity is available)
        engagement_rate = None
        if event.get('capacity'):
            engagement_rate = (unique_users / event['capacity']) * 100
        
        # Interaction breakdown
        interaction_counts = df['interaction_type'].value_counts().to_dict()
        
        # Time-based analysis
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hour'] = df['timestamp'].dt.hour
        
        # Peak engagement hour
        hourly_distribution = df['hour'].value_counts().to_dict()
        peak_hour = max(hourly_distribution, key=hourly_distribution.get) if hourly_distribution else None
        
        # User retention (users who interacted multiple times)
        user_interaction_counts = df['user_id'].value_counts()
        retention_rate = (user_interaction_counts[user_interaction_counts > 1].count() / unique_users) * 100
        
        return {
            "event_id": event_id,
            "event_title": event.get('title', 'Unknown'),
            "total_interactions": total_interactions,
            "unique_users": unique_users,
            "engagement_rate": round(engagement_rate, 2) if engagement_rate else None,
            "retention_rate": round(retention_rate, 2),
            "interaction_breakdown": interaction_counts,
            "peak_engagement_hour": peak_hour,
            "hourly_distribution": hourly_distribution,
            "analysis_timestamp": datetime.utcnow().isoformat()
        }

# =====================================================
# MODULE 49: AI MACHINE LEARNING - RECOMMENDATION SYSTEM
# =====================================================

class AIRecommendationEngine:
    """
    AI-powered recommendation system for World Cup events
    Uses machine learning for personalized fan experiences
    """
    
    def __init__(self, mongo_client: MongoEventAnalytics):
        self.mongo = mongo_client
        self.kmeans_model = None
        self.scaler = StandardScaler()
        
    async def train_user_clustering_model(self):
        """Train K-means clustering model for user segmentation"""
        
        # Get user interaction data
        user_features = {}
        
        async for doc in self.mongo.user_interactions.find():
            user_id = doc['user_id']
            interaction_type = doc['interaction_type']
            
            if user_id not in user_features:
                user_features[user_id] = {
                    'views': 0, 'likes': 0, 'shares': 0, 'attends': 0,
                    'total_interactions': 0, 'unique_events': set()
                }
            
            user_features[user_id][interaction_type + 's'] = user_features[user_id].get(interaction_type + 's', 0) + 1
            user_features[user_id]['total_interactions'] += 1
            user_features[user_id]['unique_events'].add(doc['event_id'])
        
        # Convert to feature matrix
        feature_matrix = []
        user_ids = []
        
        for user_id, features in user_features.items():
            feature_vector = [
                features['views'],
                features['likes'],
                features['shares'],
                features['attends'],
                features['total_interactions'],
                len(features['unique_events'])
            ]
            feature_matrix.append(feature_vector)
            user_ids.append(user_id)
        
        if len(feature_matrix) < 5:  # Need minimum data for clustering
            logger.warning("⚠️ Insufficient data for user clustering")
            return
        
        # Scale features
        X_scaled = self.scaler.fit_transform(feature_matrix)
        
        # Train K-means model
        n_clusters = min(5, len(feature_matrix) // 2)  # Adaptive cluster count
        self.kmeans_model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = self.kmeans_model.fit_predict(X_scaled)
        
        # Save user clusters to MongoDB
        for user_id, cluster in zip(user_ids, clusters):
            await self.mongo.fan_preferences.update_one(
                {"user_id": user_id},
                {
                    "$set": {
                        "cluster": int(cluster),
                        "updated_at": datetime.utcnow()
                    }
                },
                upsert=True
            )
        
        logger.info(f"🤖 Trained user clustering model with {n_clusters} clusters for {len(user_ids)} users")
    
    async def get_personalized_recommendations(self, user_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Generate personalized event recommendations for a user"""
        
        # Get user's cluster
        user_prefs = await self.mongo.fan_preferences.find_one({"user_id": user_id})
        if not user_prefs:
            # Return popular events for new users
            return await self._get_popular_events(limit)
        
        user_cluster = user_prefs.get('cluster')
        
        # Get events liked by similar users (same cluster)
        similar_users = []
        async for doc in self.mongo.fan_preferences.find({"cluster": user_cluster}):
            if doc['user_id'] != user_id:
                similar_users.append(doc['user_id'])
        
        if not similar_users:
            return await self._get_popular_events(limit)
        
        # Get events that similar users liked
        recommended_events = {}
        async for doc in self.mongo.user_interactions.find({
            "user_id": {"$in": similar_users},
            "interaction_type": {"$in": ["like", "attend"]}
        }):
            event_id = doc['event_id']
            if event_id not in recommended_events:
                recommended_events[event_id] = 0
            recommended_events[event_id] += 1
        
        # Get user's past interactions to avoid recommending same events
        user_interacted_events = set()
        async for doc in self.mongo.user_interactions.find({"user_id": user_id}):
            user_interacted_events.add(doc['event_id'])
        
        # Filter out already interacted events
        filtered_recommendations = {
            event_id: score for event_id, score in recommended_events.items()
            if event_id not in user_interacted_events
        }
        
        # Sort by recommendation score
        sorted_recommendations = sorted(
            filtered_recommendations.items(),
            key=lambda x: x[1],
            reverse=True
        )[:limit]
        
        # Get event details
        recommendations = []
        for event_id, score in sorted_recommendations:
            event = await self.mongo.events.find_one({"_id": event_id})
            if event:
                recommendations.append({
                    "event_id": event_id,
                    "title": event.get('title'),
                    "event_type": event.get('event_type'),
                    "location": event.get('location'),
                    "start_time": event.get('start_time'),
                    "recommendation_score": score,
                    "reason": f"Recommended based on similar fans in cluster {user_cluster}"
                })
        
        logger.info(f"🎯 Generated {len(recommendations)} personalized recommendations for user {user_id}")
        return recommendations
    
    async def _get_popular_events(self, limit: int) -> List[Dict[str, Any]]:
        """Get popular events as fallback recommendations"""
        
        pipeline = [
            {"$match": {"start_time": {"$gte": datetime.utcnow()}}},
            {"$sort": {"current_attendees": DESCENDING}},
            {"$limit": limit}
        ]
        
        popular_events = []
        async for event in self.mongo.events.aggregate(pipeline):
            popular_events.append({
                "event_id": str(event['_id']),
                "title": event.get('title'),
                "event_type": event.get('event_type'),
                "location": event.get('location'),
                "start_time": event.get('start_time'),
                "current_attendees": event.get('current_attendees', 0),
                "reason": "Popular event"
            })
        
        return popular_events

# Example usage
async def main():
    """Example usage of MongoDB analytics and AI recommendations"""
    
    # Initialize analytics
    mongo_analytics = MongoEventAnalytics()
    await mongo_analytics.create_indexes()
    
    fan_analytics = FanBehaviorAnalytics(mongo_analytics)
    ai_engine = AIRecommendationEngine(mongo_analytics)
    
    # Run analytics
    popular_events = await mongo_analytics.aggregate_event_popularity()
    city_distribution = await mongo_analytics.get_city_event_distribution()
    engagement_patterns = await fan_analytics.analyze_fan_engagement_patterns()
    
    # Train AI model
    await ai_engine.train_user_clustering_model()
    
    logger.info("🏆 World Cup 2026 analytics and AI system ready!")

if __name__ == "__main__":
    asyncio.run(main())
