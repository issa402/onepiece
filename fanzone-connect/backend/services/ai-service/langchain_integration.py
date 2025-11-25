"""
🏆 FANZONE CONNECT - LANGCHAIN AI INTEGRATION
Learning Modules: 23 (LangChain AI), 36 (AI/LLM Integration)
World Cup 2026 Fan Platform - Advanced AI-Powered Fan Assistance and Content Generation
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
import json
import os

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import BaseTool
from langchain.callbacks.manager import CallbackManagerForToolRun

import redis.asyncio as redis
from pydantic import BaseModel, Field
import httpx

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# MODULE 23: LANGCHAIN AI - ADVANCED AI CHAINS
# =====================================================

class WorldCupAIConfig:
    """Configuration for World Cup 2026 AI services"""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-api-key")
    MODEL_NAME = "gpt-4"
    EMBEDDING_MODEL = "text-embedding-ada-002"
    MAX_TOKENS = 2000
    TEMPERATURE = 0.7
    
    # Vector store settings
    VECTOR_STORE_PATH = "./data/worldcup_vectorstore"
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # Memory settings
    MEMORY_WINDOW = 10
    
    # Redis for caching
    REDIS_URL = "redis://redis:6379"

class WorldCupKnowledgeBase:
    """
    World Cup 2026 knowledge base using LangChain vector stores
    Stores and retrieves information about teams, matches, venues, history
    """
    
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=WorldCupAIConfig.OPENAI_API_KEY,
            model=WorldCupAIConfig.EMBEDDING_MODEL
        )
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=WorldCupAIConfig.CHUNK_SIZE,
            chunk_overlap=WorldCupAIConfig.CHUNK_OVERLAP,
            separators=["\n\n", "\n", " ", ""]
        )
        
    async def initialize_knowledge_base(self):
        """Initialize vector store with World Cup 2026 knowledge"""
        logger.info("🧠 Initializing World Cup 2026 Knowledge Base...")
        
        # World Cup 2026 knowledge documents
        knowledge_docs = [
            {
                "content": """
                FIFA World Cup 2026 will be held in the United States, Canada, and Mexico.
                It will be the first World Cup hosted by three countries and the first with 48 teams.
                The tournament will feature 104 matches across 16 host cities.
                Key cities include: New York/New Jersey, Los Angeles, Mexico City, Toronto, Vancouver.
                The final will be held at MetLife Stadium in New York/New Jersey.
                """,
                "metadata": {"type": "tournament_info", "category": "general"}
            },
            {
                "content": """
                World Cup 2026 Host Cities and Venues:
                USA: New York/New Jersey (MetLife Stadium), Los Angeles (SoFi Stadium), 
                Dallas (AT&T Stadium), San Francisco Bay Area (Levi's Stadium), 
                Miami (Hard Rock Stadium), Atlanta (Mercedes-Benz Stadium),
                Seattle (Lumen Field), Philadelphia (Lincoln Financial Field),
                Kansas City (Arrowhead Stadium), Boston (Gillette Stadium)
                
                Canada: Toronto (BMO Field), Vancouver (BC Place)
                
                Mexico: Mexico City (Estadio Azteca), Guadalajara (Estadio Akron), 
                Monterrey (Estadio BBVA)
                """,
                "metadata": {"type": "venues", "category": "locations"}
            },
            {
                "content": """
                World Cup 2026 Format:
                - 48 teams divided into 16 groups of 3 teams each
                - Top 2 teams from each group advance to Round of 32
                - Single elimination from Round of 32 onwards
                - Total of 104 matches (increased from 64 in previous tournaments)
                - Tournament duration: approximately 39 days
                - Group stage: 3 matchdays
                - Knockout stage: Round of 32, Round of 16, Quarter-finals, Semi-finals, Final
                """,
                "metadata": {"type": "format", "category": "tournament_structure"}
            },
            {
                "content": """
                Fan Zone Events and Activities:
                - Official FIFA Fan Festivals in each host city
                - Cultural celebrations showcasing local traditions
                - Interactive football experiences and skills challenges
                - Live match screenings with thousands of fans
                - Food festivals featuring cuisine from all three host countries
                - Music concerts and entertainment shows
                - Meet and greet opportunities with football legends
                - Virtual reality experiences and gaming zones
                """,
                "metadata": {"type": "fan_activities", "category": "entertainment"}
            }
        ]
        
        # Convert to LangChain documents
        documents = []
        for doc in knowledge_docs:
            # Split large documents into chunks
            chunks = self.text_splitter.split_text(doc["content"])
            for chunk in chunks:
                documents.append(Document(
                    page_content=chunk,
                    metadata=doc["metadata"]
                ))
        
        # Create vector store
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=WorldCupAIConfig.VECTOR_STORE_PATH
        )
        
        logger.info(f"✅ Knowledge base initialized with {len(documents)} document chunks")
    
    async def search_knowledge(self, query: str, k: int = 5) -> List[Document]:
        """Search knowledge base for relevant information"""
        if not self.vector_store:
            await self.initialize_knowledge_base()
        
        results = self.vector_store.similarity_search(query, k=k)
        return results

class WorldCupChatBot:
    """
    Advanced World Cup 2026 chatbot using LangChain conversational AI
    Provides personalized fan assistance and information
    """
    
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=WorldCupAIConfig.OPENAI_API_KEY,
            model_name=WorldCupAIConfig.MODEL_NAME,
            temperature=WorldCupAIConfig.TEMPERATURE,
            max_tokens=WorldCupAIConfig.MAX_TOKENS
        )
        
        self.knowledge_base = WorldCupKnowledgeBase()
        self.memory = ConversationBufferWindowMemory(
            k=WorldCupAIConfig.MEMORY_WINDOW,
            memory_key="chat_history",
            return_messages=True
        )
        
        self.redis_client = None
        self.conversation_chain = None
        
    async def initialize(self):
        """Initialize chatbot components"""
        logger.info("🤖 Initializing World Cup 2026 AI Chatbot...")
        
        # Initialize knowledge base
        await self.knowledge_base.initialize_knowledge_base()
        
        # Initialize Redis for caching
        self.redis_client = redis.from_url(WorldCupAIConfig.REDIS_URL, decode_responses=True)
        
        # Create conversational retrieval chain
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.knowledge_base.vector_store.as_retriever(search_kwargs={"k": 5}),
            memory=self.memory,
            verbose=True,
            return_source_documents=True
        )
        
        logger.info("✅ World Cup 2026 AI Chatbot ready!")
    
    async def chat(self, user_id: str, message: str) -> Dict[str, Any]:
        """Process user message and generate AI response"""
        if not self.conversation_chain:
            await self.initialize()
        
        try:
            # Check cache first
            cache_key = f"chat_response:{hash(message)}"
            cached_response = await self.redis_client.get(cache_key)
            
            if cached_response:
                logger.info("📋 Returning cached response")
                return json.loads(cached_response)
            
            # Generate response using LangChain
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.conversation_chain({
                    "question": message,
                    "chat_history": self.memory.chat_memory.messages
                })
            )
            
            response_data = {
                "response": result["answer"],
                "sources": [doc.metadata for doc in result.get("source_documents", [])],
                "timestamp": datetime.utcnow().isoformat(),
                "user_id": user_id
            }
            
            # Cache response for 1 hour
            await self.redis_client.setex(cache_key, 3600, json.dumps(response_data, default=str))
            
            logger.info(f"🤖 Generated AI response for user {user_id}")
            return response_data
            
        except Exception as e:
            logger.error(f"❌ Error generating AI response: {e}")
            return {
                "response": "I apologize, but I'm experiencing technical difficulties. Please try again later.",
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }

# =====================================================
# MODULE 36: AI/LLM INTEGRATION - CUSTOM TOOLS
# =====================================================

class MatchInfoTool(BaseTool):
    """Custom LangChain tool for fetching live match information"""
    
    name = "match_info"
    description = "Get information about World Cup 2026 matches, including live scores, schedules, and team details"
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Fetch match information from our API"""
        try:
            # In production, this would call our Match Service API
            # For now, return mock data
            return f"Match information for query '{query}': Brazil vs Argentina, June 15, 2026, MetLife Stadium, New York. Current score: 2-1 to Brazil."
        except Exception as e:
            return f"Error fetching match information: {e}"

class FanZoneEventsTool(BaseTool):
    """Custom tool for Fan Zone events and activities"""
    
    name = "fan_zone_events"
    description = "Get information about Fan Zone events, activities, and celebrations in World Cup 2026 host cities"
    
    def _run(
        self, 
        query: str, 
        run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Fetch Fan Zone events information"""
        try:
            return f"Fan Zone events for '{query}': Live music concerts, food festivals, interactive football games, and cultural celebrations. Check the FANZONE CONNECT app for specific times and locations."
        except Exception as e:
            return f"Error fetching Fan Zone events: {e}"

class WorldCupAgent:
    """
    Advanced World Cup 2026 AI agent with custom tools
    Handles complex queries and multi-step reasoning
    """
    
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=WorldCupAIConfig.OPENAI_API_KEY,
            model_name=WorldCupAIConfig.MODEL_NAME,
            temperature=0.3  # Lower temperature for more focused responses
        )
        
        # Custom tools for World Cup information
        self.tools = [
            MatchInfoTool(),
            FanZoneEventsTool(),
        ]
        
        self.agent = None
    
    def initialize_agent(self):
        """Initialize the AI agent with tools"""
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            max_iterations=3,
            early_stopping_method="generate"
        )
        
        logger.info("🤖 World Cup 2026 AI Agent initialized with custom tools")
    
    async def process_complex_query(self, query: str) -> str:
        """Process complex queries using the AI agent"""
        if not self.agent:
            self.initialize_agent()
        
        try:
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.agent.run(query)
            )
            return result
        except Exception as e:
            logger.error(f"❌ Error processing complex query: {e}")
            return f"I apologize, but I couldn't process your request: {e}"

class ContentGenerator:
    """
    AI-powered content generation for World Cup 2026
    Creates match previews, fan guides, and social media content
    """
    
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=WorldCupAIConfig.OPENAI_API_KEY,
            model_name=WorldCupAIConfig.MODEL_NAME,
            temperature=0.8  # Higher temperature for creative content
        )
        
        # Content generation prompts
        self.match_preview_prompt = ChatPromptTemplate.from_template("""
        Create an engaging match preview for the World Cup 2026 match between {home_team} and {away_team}.
        
        Match Details:
        - Date: {match_date}
        - Venue: {venue}
        - Phase: {phase}
        
        Include:
        1. Team analysis and key players
        2. Historical head-to-head record
        3. What's at stake in this match
        4. Prediction and key factors to watch
        
        Write in an exciting, fan-friendly tone that builds anticipation.
        """)
        
        self.fan_guide_prompt = ChatPromptTemplate.from_template("""
        Create a comprehensive fan guide for visiting {city} during World Cup 2026.
        
        Include:
        1. Best places to watch matches
        2. Local food and drink recommendations
        3. Cultural attractions and activities
        4. Transportation tips
        5. Fan Zone locations and events
        6. Safety and practical information
        
        Write in a helpful, enthusiastic tone for international visitors.
        """)
    
    async def generate_match_preview(self, match_data: Dict[str, Any]) -> str:
        """Generate AI-powered match preview"""
        try:
            chain = LLMChain(llm=self.llm, prompt=self.match_preview_prompt)
            
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: chain.run(**match_data)
            )
            
            logger.info(f"📝 Generated match preview for {match_data.get('home_team')} vs {match_data.get('away_team')}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error generating match preview: {e}")
            return "Unable to generate match preview at this time."
    
    async def generate_fan_guide(self, city: str) -> str:
        """Generate AI-powered fan guide for host cities"""
        try:
            chain = LLMChain(llm=self.llm, prompt=self.fan_guide_prompt)
            
            result = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: chain.run(city=city)
            )
            
            logger.info(f"📖 Generated fan guide for {city}")
            return result
            
        except Exception as e:
            logger.error(f"❌ Error generating fan guide: {e}")
            return f"Unable to generate fan guide for {city} at this time."

# =====================================================
# MAIN AI SERVICE CLASS
# =====================================================

class WorldCupAIService:
    """
    Main AI service for World Cup 2026 fan platform
    Orchestrates all AI capabilities
    """
    
    def __init__(self):
        self.chatbot = WorldCupChatBot()
        self.agent = WorldCupAgent()
        self.content_generator = ContentGenerator()
        
    async def initialize(self):
        """Initialize all AI components"""
        logger.info("🚀 Initializing World Cup 2026 AI Service...")
        
        await self.chatbot.initialize()
        self.agent.initialize_agent()
        
        logger.info("✅ World Cup 2026 AI Service ready!")
    
    async def process_fan_query(self, user_id: str, message: str, query_type: str = "chat") -> Dict[str, Any]:
        """Process different types of fan queries"""
        
        if query_type == "chat":
            return await self.chatbot.chat(user_id, message)
        
        elif query_type == "complex":
            response = await self.agent.process_complex_query(message)
            return {
                "response": response,
                "type": "agent_response",
                "timestamp": datetime.utcnow().isoformat()
            }
        
        else:
            return {
                "response": "I'm not sure how to handle that type of query.",
                "error": f"Unknown query type: {query_type}",
                "timestamp": datetime.utcnow().isoformat()
            }

# Example usage
async def main():
    """Example usage of World Cup 2026 AI service"""
    
    ai_service = WorldCupAIService()
    await ai_service.initialize()
    
    # Test chatbot
    response = await ai_service.process_fan_query(
        user_id="fan123",
        message="Tell me about the World Cup 2026 venues in the USA",
        query_type="chat"
    )
    
    print("🤖 AI Response:", response["response"])
    
    # Test content generation
    match_preview = await ai_service.content_generator.generate_match_preview({
        "home_team": "Brazil",
        "away_team": "Argentina",
        "match_date": "July 14, 2026",
        "venue": "MetLife Stadium, New York",
        "phase": "Final"
    })
    
    print("📝 Match Preview:", match_preview[:200] + "...")

if __name__ == "__main__":
    asyncio.run(main())
