# ============================================================================
# 📚 LEARNING GUIDE: Prediction Service (app/services/prediction_service.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This service orchestrates the complete prediction pipeline.
# It coordinates scraping, AI analysis, and consensus calculation
# to provide final betting recommendations.
#
# 🔧 TECHNOLOGIES USED:
# - Service orchestration: Coordinating multiple services
# - Database operations: Storing and retrieving predictions
# - Caching: Redis for performance optimization
# - Background tasks: Celery for async processing
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Service Orchestration Pattern:**
# - Coordinates multiple microservices
# - Handles business logic and workflows
# - Manages data flow between services
# - Provides high-level API for complex operations
# - Implements error handling and retry logic
#
# 💡 HINTS:
# - Use dependency injection for services
# - Implement proper error handling
# - Add caching for expensive operations
# - Use background tasks for long-running processes
# - Include comprehensive logging
#
# 🧪 TEST YOUR CODE:
# service = PredictionService()
# result = await service.get_consensus("Lakers vs Warriors")

# YOUR IMPLEMENTATION HERE:
# (Write your PredictionService class below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

import asyncio
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from app.services.scraper_service import ScraperService
from app.services.ai_analysis_service import AIAnalysisService

class PredictionService:
    """
    Main service that orchestrates the prediction pipeline
    """
    
    def __init__(self):
        self.scraper_service = ScraperService()
        self.ai_service = AIAnalysisService()
        self.logger = logging.getLogger(__name__)
    
    async def get_consensus(self, game_query: str, game_date: datetime = None) -> Dict:
        """
        Get consensus prediction for a game
        
        Args:
            game_query: Game query string (e.g., "Lakers vs Warriors")
            game_date: Game date (defaults to tomorrow)
            
        Returns:
            Dict containing consensus prediction and metadata
        """
        if not game_date:
            game_date = datetime.now() + timedelta(days=1)
        
        try:
            # Step 1: Scrape betting sites
            self.logger.info(f"🕷️ Starting scraping for: {game_query}")
            scraped_data = await self.scraper_service.scrape_all_sources(game_query, game_date)
            
            if not scraped_data:
                raise ValueError("No data could be scraped from betting sites")
            
            # Step 2: AI analysis and consensus
            self.logger.info(f"🤖 Starting AI analysis for: {game_query}")
            consensus = await self.ai_service.analyze_all_predictions(scraped_data, game_query)
            
            # Step 3: Format response
            result = {
                "game": {
                    "query": game_query,
                    "date": game_date.isoformat(),
                    "sport": "NBA"  # Could be dynamic
                },
                "consensus": {
                    "predicted_winner": consensus.predicted_winner,
                    "confidence": consensus.confidence,
                    "consensus_percentage": consensus.consensus_percentage,
                    "recommendation": consensus.recommendation,
                    "risk_level": consensus.risk_level,
                    "explanation": consensus.explanation
                },
                "sources_analyzed": len(scraped_data),
                "processing_time": datetime.utcnow().isoformat(),
                "key_factors": consensus.key_factors
            }
            
            self.logger.info(f"✅ Consensus generated for {game_query}: {consensus.predicted_winner}")
            return result
            
        except Exception as e:
            self.logger.error(f"❌ Prediction failed for {game_query}: {e}")
            raise
    
    async def get_historical_accuracy(self, source: str = None) -> Dict:
        """Get historical accuracy metrics for sources"""
        # Mock implementation - replace with real database queries
        return {
            "overall_accuracy": 0.73,
            "total_predictions": 1250,
            "correct_predictions": 912,
            "by_source": {
                "ESPN": {"accuracy": 0.75, "predictions": 300},
                "CBS Sports": {"accuracy": 0.71, "predictions": 280},
                "The Athletic": {"accuracy": 0.78, "predictions": 250},
                "Bleacher Report": {"accuracy": 0.69, "predictions": 220},
                "Sports Illustrated": {"accuracy": 0.74, "predictions": 200}
            }
        }

# ============================================================================
