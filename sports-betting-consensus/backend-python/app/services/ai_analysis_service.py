# ============================================================================
# 📚 LEARNING GUIDE: AI/LLM Analysis Service (services/ai_analysis_service.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This service uses AI/LLM APIs to analyze scraped sports betting predictions.
# It transforms unstructured text into structured data and insights:
# - Extracts predictions from natural language text
# - Calculates confidence scores and sentiment analysis
# - Generates consensus recommendations
# - Provides reasoning and explanations for predictions
# - Handles multiple AI providers with fallback logic
#
# 🔧 TECHNOLOGIES USED:
# - OpenAI GPT-4: Advanced language understanding and reasoning
# - Anthropic Claude: Alternative LLM with strong analytical capabilities
# - LangChain: Framework for building LLM applications
# - Pydantic: Data validation for structured AI responses
# - Tenacity: Retry logic for API failures
# - Asyncio: Concurrent AI API calls for performance
#
# 📖 IN-DEPTH EXPLANATION:
#
# **AI/LLM Integration Fundamentals:**
# Large Language Models can:
# 1. Understand natural language predictions from sports sites
# 2. Extract structured data (team names, confidence, reasoning)
# 3. Analyze sentiment and bias in predictions
# 4. Generate human-readable explanations
# 5. Combine multiple predictions into consensus
#
# **Prompt Engineering Strategies:**
# 1. **Few-Shot Learning**: Provide examples of good extractions
# 2. **Chain-of-Thought**: Ask AI to explain its reasoning step-by-step
# 3. **Structured Output**: Use JSON schemas to ensure consistent responses
# 4. **Context Injection**: Include game context, team stats, recent performance
#
# **Multi-Provider Architecture:**
# - Primary: OpenAI GPT-4 (most capable, higher cost)
# - Fallback: Anthropic Claude (good alternative, different strengths)
# - Local: Open-source models (cost-effective, privacy)
# - Provider abstraction allows easy switching
#
# **Data Flow:**
# 1. Raw scraped text → AI analysis → Structured prediction
# 2. Multiple predictions → Consensus calculation → Recommendation
# 3. Historical data → Accuracy tracking → Provider weighting
#
# **Consensus Algorithm:**
# 1. Weight predictions by source reliability
# 2. Calculate agreement percentage
# 3. Factor in AI confidence scores
# 4. Generate final recommendation with risk assessment
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 36 (AI/LLM Integration): Lines 100-300 - Provider abstraction patterns
# - Module 36 (AI/LLM Integration): Lines 400-600 - Prompt engineering techniques
# - Module 36 (AI/LLM Integration): Lines 700-900 - Structured data extraction
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Create AIAnalysisService class with provider abstraction
# [ ] Implement prompt templates for different analysis types
# [ ] Add structured data extraction with Pydantic models
# [ ] Create consensus calculation algorithm
# [ ] Implement multi-provider fallback logic
# [ ] Add retry logic with exponential backoff
# [ ] Create confidence scoring system
# [ ] Add sentiment analysis for predictions
# [ ] Implement batch processing for multiple predictions
# [ ] Add cost tracking and optimization
# [ ] Create explanation generation for recommendations
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - LLM API integration patterns (OpenAI, Anthropic)
# - Prompt engineering best practices
# - Structured data extraction from unstructured text
# - Consensus algorithms and weighted voting
# - Error handling for AI API failures
# - Cost optimization strategies for LLM usage
# - Async programming for concurrent API calls
# - Data validation with Pydantic models
#
# 🚀 REAL-WORLD EXAMPLES:
# - Financial services: AI-powered investment analysis
# - Healthcare: Medical diagnosis assistance
# - Legal: Contract analysis and review
# - Customer service: Automated response generation
#
# 💡 PROMPT ENGINEERING EXAMPLES:
#
# **Prediction Extraction Prompt:**
# ```
# You are an expert sports analyst. Extract the prediction from this text:
# 
# Text: "I think the Lakers will win tonight. They've been playing great defense 
# and LeBron looks healthy. I'm 80% confident in this pick."
# 
# Extract:
# - Team predicted to win
# - Confidence level (0-100%)
# - Key reasoning factors
# 
# Respond in JSON format.
# ```
#
# **Consensus Generation Prompt:**
# ```
# You are a sports betting advisor. Given these 5 predictions, generate a consensus:
# 
# Predictions:
# 1. ESPN: Lakers win (85% confidence) - "Strong home court advantage"
# 2. CBS: Lakers win (70% confidence) - "Better recent form"
# 3. SI: Warriors win (60% confidence) - "Road team motivation"
# 4. BR: Lakers win (75% confidence) - "Key player matchups favor Lakers"
# 5. Athletic: Lakers win (80% confidence) - "Statistical analysis"
# 
# Generate consensus with explanation and risk assessment.
# ```
#
# ⚠️ COST OPTIMIZATION STRATEGIES:
# - Use cheaper models (GPT-3.5) for simple extractions
# - Batch multiple predictions in single API call
# - Cache results to avoid duplicate processing
# - Use local models for high-volume, low-complexity tasks
# - Implement smart retry logic to avoid wasted tokens
#
# 🔍 DEBUGGING AI RESPONSES:
# - Log all prompts and responses for analysis
# - Track token usage and costs
# - Monitor response quality and consistency
# - A/B test different prompt strategies
# - Validate structured outputs with Pydantic
#
# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================
#
# import asyncio
# from typing import List, Dict, Optional, Union
# from openai import AsyncOpenAI
# from anthropic import AsyncAnthropic
# from pydantic import BaseModel, Field
# import json
# import logging
# from tenacity import retry, stop_after_attempt, wait_exponential
#
# class PredictionExtraction(BaseModel):
#     """Structured prediction data extracted by AI"""
#     predicted_winner: str = Field(description="Team predicted to win")
#     confidence: float = Field(ge=0, le=1, description="Confidence score 0-1")
#     reasoning: str = Field(description="Key factors for prediction")
#     sentiment: float = Field(ge=-1, le=1, description="Sentiment score -1 to 1")
#
# class ConsensusRecommendation(BaseModel):
#     """AI-generated consensus recommendation"""
#     predicted_winner: str
#     confidence: float
#     consensus_percentage: float
#     recommendation: str  # "bet", "avoid", "monitor"
#     risk_level: str  # "low", "medium", "high"
#     explanation: str
#     key_factors: List[str]
#
# class AIAnalysisService:
#     def __init__(self):
#         self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
#         self.anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
#         self.logger = logging.getLogger(__name__)
#
#     @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
#     async def extract_prediction(self, raw_text: str, source: str) -> Optional[PredictionExtraction]:
#         """Extract structured prediction from raw scraped text"""
#         prompt = f"""
#         You are an expert sports analyst. Extract the betting prediction from this text.
#         
#         Source: {source}
#         Text: {raw_text}
#         
#         Extract:
#         - Which team is predicted to win
#         - Confidence level (0.0 to 1.0)
#         - Key reasoning factors
#         - Overall sentiment (-1.0 to 1.0)
#         
#         If no clear prediction exists, return null values.
#         Respond in valid JSON matching this schema:
#         {{
#             "predicted_winner": "team name or null",
#             "confidence": 0.75,
#             "reasoning": "key factors mentioned",
#             "sentiment": 0.5
#         }}
#         """
#         
#         try:
#             response = await self.openai_client.chat.completions.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.3,
#                 max_tokens=500
#             )
#             
#             result = json.loads(response.choices[0].message.content)
#             return PredictionExtraction(**result)
#             
#         except Exception as e:
#             self.logger.error(f"Prediction extraction failed: {e}")
#             return None
#
#     async def generate_consensus(self, predictions: List[PredictionExtraction]) -> ConsensusRecommendation:
#         """Generate consensus recommendation from multiple predictions"""
#         if not predictions:
#             raise ValueError("No predictions provided for consensus")
#         
#         # Calculate basic consensus metrics
#         team_votes = {}
#         total_confidence = 0
#         
#         for pred in predictions:
#             if pred.predicted_winner:
#                 team_votes[pred.predicted_winner] = team_votes.get(pred.predicted_winner, 0) + 1
#                 total_confidence += pred.confidence
#         
#         # Find winner and calculate metrics
#         winner = max(team_votes, key=team_votes.get) if team_votes else "Unknown"
#         consensus_pct = (team_votes.get(winner, 0) / len(predictions)) * 100
#         avg_confidence = total_confidence / len(predictions)
#         
#         # Generate AI explanation
#         prompt = f"""
#         Generate a consensus betting recommendation based on these predictions:
#         
#         Predictions: {[pred.dict() for pred in predictions]}
#         
#         Consensus: {winner} ({consensus_pct:.1f}% agreement)
#         Average Confidence: {avg_confidence:.2f}
#         
#         Provide:
#         - Recommendation (bet/avoid/monitor)
#         - Risk level (low/medium/high)
#         - Clear explanation
#         - Key factors supporting the consensus
#         """
#         
#         # Use AI to generate explanation and recommendation
#         response = await self.openai_client.chat.completions.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.4,
#             max_tokens=800
#         )
#         
#         # Parse AI response and create recommendation
#         return ConsensusRecommendation(
#             predicted_winner=winner,
#             confidence=avg_confidence,
#             consensus_percentage=consensus_pct,
#             recommendation="bet" if consensus_pct >= 70 and avg_confidence >= 0.7 else "monitor",
#             risk_level="low" if consensus_pct >= 80 else "medium",
#             explanation=response.choices[0].message.content,
#             key_factors=[pred.reasoning for pred in predictions if pred.reasoning]
#         )
#
# ============================================================================

# ============================================================================
# 💻 YOUR CODE GOES HERE - TRY TO IMPLEMENT FIRST!
# ============================================================================
#
# 🎯 YOUR TASK: Create an AIAnalysisService class that uses LLMs to analyze predictions
#
# 📋 STEP-BY-STEP IMPLEMENTATION:
#
# 1. Import required libraries:
#    - openai (for GPT-4 API)
#    - anthropic (for Claude API)
#    - pydantic (for data models)
#    - typing (for type hints)
#    - json (for parsing responses)
#
# 2. Create Pydantic models for:
#    - PredictionExtraction (winner, confidence, reasoning, sentiment)
#    - ConsensusRecommendation (final recommendation with explanation)
#
# 3. Create AIAnalysisService class with:
#    - __init__ method to set up API clients
#    - extract_prediction method (analyze raw text)
#    - calculate_consensus method (combine multiple predictions)
#    - generate_recommendation method (final betting advice)
#
# 🔍 EXAMPLE: Here's how to start your data models:
#
# from pydantic import BaseModel, Field
# from typing import List, Optional
#
# class PredictionExtraction(BaseModel):
#     predicted_winner: Optional[str] = None
#     confidence: float = Field(ge=0, le=1)
#     reasoning: str
#     sentiment: float = Field(ge=-1, le=1)
#
# class AIAnalysisService:
#     def __init__(self):
#         # TODO: Initialize OpenAI and Anthropic clients
#         # TODO: Set up logger
#         pass
#
#     async def extract_prediction(self, raw_text: str, source: str):
#         # TODO: Create prompt for LLM
#         # TODO: Call OpenAI API with retry logic
#         # TODO: Parse JSON response into PredictionExtraction
#         # TODO: Handle errors and fallback to Anthropic
#         pass
#
# 💡 HINTS:
# - Use structured prompts with clear JSON schema
# - Set temperature=0.3 for consistent results
# - Always validate LLM responses with Pydantic
# - Implement fallback from OpenAI to Anthropic
# - Use retry logic with exponential backoff
#
# 🧪 TEST YOUR CODE:
# ai_service = AIAnalysisService()
# result = await ai_service.extract_prediction("Lakers are favored by 5 points", "ESPN")
# print(result.predicted_winner, result.confidence)

# ============================================================================
# 🎯 DETAILED STEP-BY-STEP IMPLEMENTATION GUIDE
# ============================================================================

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES - WHAT EACH ONE DOES
# ============================================================================
#
# **WHAT TO DO:** Import all the Python libraries needed for AI/LLM integration
# **WHY YOU NEED IT:** Each library handles a specific part of AI analysis
# **WHEN TO USE:** Always at the top of your Python files
# **HOW IT WORKS:** Python's import system loads external functionality
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **from openai import AsyncOpenAI**: OpenAI GPT-4 integration
#    - WHAT IT DOES: Connects to OpenAI's API to use GPT-4 for text analysis
#    - WHY YOU NEED IT: GPT-4 is excellent at extracting structured data from unstructured text
#    - REAL EXAMPLE: ChatGPT uses the same API to understand and respond to user messages
#    - HOW IT WORKS: client = AsyncOpenAI(); response = await client.chat.completions.create()
#
# 🔹 **from anthropic import AsyncAnthropic**: Claude AI integration
#    - WHAT IT DOES: Provides fallback AI provider in case OpenAI fails or is rate-limited
#    - WHY YOU NEED IT: Production systems need redundancy - never rely on single provider
#    - REAL EXAMPLE: Netflix uses multiple CDNs, if one fails, traffic routes to another
#    - HOW IT WORKS: client = AsyncAnthropic(); response = await client.messages.create()
#
# 🔹 **from pydantic import BaseModel**: Data validation and structure
#    - WHAT IT DOES: Defines the exact structure of data that AI should return
#    - WHY YOU NEED IT: AI responses are unpredictable - you need to validate and structure them
#    - REAL EXAMPLE: Banking APIs use similar validation to ensure transaction data is correct
#    - HOW IT WORKS: class PredictionExtraction(BaseModel): predicted_winner: str; confidence: float
#
# **YOUR CODE HERE:**
# import asyncio
# import json
# import logging
# from typing import List, Dict, Optional
# from datetime import datetime
# from pydantic import BaseModel, Field
# from openai import AsyncOpenAI
# from anthropic import AsyncAnthropic

# ============================================================================
# STEP 2: CREATE PYDANTIC MODELS - DATA STRUCTURE DEFINITIONS
# ============================================================================
#
# **WHAT TO DO:** Define the exact structure of data your AI analysis will produce
# **WHY YOU NEED IT:** AI responses are unpredictable - you need consistent data structure
# **WHEN TO USE:** Before implementing AI logic - define what you want to extract
# **HOW IT WORKS:** Pydantic validates AI responses match your expected structure
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **class PredictionExtraction(BaseModel)**: Single prediction data structure
#    - WHAT IT DOES: Defines what data to extract from each betting site's text
#    - WHY YOU NEED IT: Converts messy text like "Lakers look strong tonight" into structured data
#    - REAL EXAMPLE: Sentiment analysis APIs return structured scores instead of raw text
#    - HOW IT WORKS: AI returns JSON that gets validated against this model
#
# 🔹 **predicted_winner: Optional[str]**: Team prediction field
#    - WHAT IT DOES: Stores which team is predicted to win (or None if unclear)
#    - WHY Optional: Some articles discuss games without making clear predictions
#    - REAL EXAMPLE: "This will be a close game" → predicted_winner = None
#    - HOW IT WORKS: Field(None, description="Team predicted to win")
#
# 🔹 **confidence: float**: Confidence score field
#    - WHAT IT DOES: Measures how confident the prediction is (0.0 to 1.0)
#    - WHY YOU NEED IT: "Lakers will definitely win" = 0.9, "Lakers might win" = 0.6
#    - REAL EXAMPLE: Weather forecasts show confidence: "80% chance of rain"
#    - HOW IT WORKS: Field(ge=0, le=1, description="Confidence score 0-1")
#
# **YOUR CODE HERE:**
# class PredictionExtraction(BaseModel):
#     """Structured prediction data extracted from raw text"""
#     predicted_winner: Optional[str] = Field(None, description="Team predicted to win")
#     confidence: float = Field(ge=0, le=1, description="Confidence score 0-1")
#     reasoning: str = Field(description="Key factors for prediction")
#     sentiment: float = Field(ge=-1, le=1, description="Sentiment score -1 to 1")

# ============================================================================
# STEP 3: CREATE AI ANALYSIS SERVICE CLASS
# ============================================================================
#
# **WHAT TO DO:** Create the main class that handles AI analysis of scraped text
# **WHY YOU NEED IT:** Centralizes all AI logic and manages multiple AI providers
# **WHEN TO USE:** Called by prediction service to analyze scraped betting predictions
# **HOW IT WORKS:** Takes raw text, sends to AI, returns structured predictions
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **class AIAnalysisService**: Main AI analysis class
#    - WHAT IT DOES: Manages AI clients and provides methods for text analysis
#    - WHY YOU NEED IT: Encapsulates AI complexity behind simple interface
#    - REAL EXAMPLE: Google Translate API hides complex ML models behind simple translate() method
#    - HOW IT WORKS: ai_service = AIAnalysisService(); result = await ai_service.extract_prediction()
#
# 🔹 **self.openai_client = AsyncOpenAI()**: Primary AI provider
#    - WHAT IT DOES: Creates connection to OpenAI's GPT-4 API
#    - WHY PRIMARY: GPT-4 is currently best at structured data extraction
#    - REAL EXAMPLE: Most AI startups use OpenAI as primary provider
#    - HOW IT WORKS: Uses API key from environment variables for authentication
#
# 🔹 **self.anthropic_client = AsyncAnthropic()**: Fallback AI provider
#    - WHAT IT DOES: Backup AI provider in case OpenAI fails or is rate-limited
#    - WHY FALLBACK: Production systems need redundancy for reliability
#    - REAL EXAMPLE: AWS uses multiple availability zones - if one fails, others continue
#    - HOW IT WORKS: Try OpenAI first, if it fails, automatically try Anthropic
#
# **YOUR CODE HERE:**
# class AIAnalysisService:
#     def __init__(self):
#         self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
#         self.anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
#         self.logger = logging.getLogger(__name__)

# YOUR IMPLEMENTATION HERE:
# (Write your AIAnalysisService class and models below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

# import asyncio
# import json
# import logging
# from typing import List, Dict, Optional
# from datetime import datetime
# from pydantic import BaseModel, Field, ValidationError
# from openai import AsyncOpenAI
# from anthropic import AsyncAnthropic
# from tenacity import retry, stop_after_attempt, wait_exponential
#
# # Pydantic models for structured data
# class PredictionExtraction(BaseModel):
#     """Structured prediction data extracted from raw text"""
#     predicted_winner: Optional[str] = Field(None, description="Team predicted to win")
#     confidence: float = Field(ge=0, le=1, description="Confidence score 0-1")
#     reasoning: str = Field(description="Key factors for prediction")
#     sentiment: float = Field(ge=-1, le=1, description="Sentiment score -1 to 1")
#
# class ConsensusRecommendation(BaseModel):
#     """AI-generated consensus recommendation"""
#     predicted_winner: str
#     confidence: float
#     consensus_percentage: float
#     recommendation: str  # "bet", "avoid", "monitor"
#     risk_level: str  # "low", "medium", "high"
#     explanation: str
#     key_factors: List[str]
#
# class AIAnalysisService:
#     def __init__(self):
#         # Initialize API clients
#         self.openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
#         self.anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
#         self.logger = logging.getLogger(__name__)
#
#     @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
#     async def extract_prediction(self, raw_text: str, source: str) -> Optional[PredictionExtraction]:
#         """Extract structured prediction from raw scraped text"""
#         prompt = f"""
#         You are an expert sports analyst. Extract the betting prediction from this text.
#
#         Source: {source}
#         Text: {raw_text}
#
#         Extract:
#         - Which team is predicted to win (or null if unclear)
#         - Confidence level (0.0 to 1.0, where 1.0 is completely certain)
#         - Key reasoning factors mentioned
#         - Overall sentiment (-1.0 negative to 1.0 positive)
#
#         If no clear prediction exists, return null for predicted_winner.
#         Respond in valid JSON matching this exact schema:
#         {{
#             "predicted_winner": "team name or null",
#             "confidence": 0.75,
#             "reasoning": "key factors mentioned in the text",
#             "sentiment": 0.5
#         }}
#         """
#
#         try:
#             # Try OpenAI first
#             response = await self.openai_client.chat.completions.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.3,
#                 max_tokens=500
#             )
#
#             json_text = response.choices[0].message.content.strip()
#             prediction_data = json.loads(json_text)
#
#             # Validate with Pydantic
#             prediction = PredictionExtraction(**prediction_data)
#             self.logger.info(f"✅ OpenAI extracted prediction from {source}")
#             return prediction
#
#         except Exception as e:
#             self.logger.warning(f"OpenAI extraction failed for {source}: {e}")
#
#             # Fallback to Anthropic
#             try:
#                 response = await self.anthropic_client.messages.create(
#                     model="claude-3-sonnet-20240229",
#                     max_tokens=500,
#                     temperature=0.3,
#                     messages=[{"role": "user", "content": prompt}]
#                 )
#
#                 json_text = response.content[0].text.strip()
#                 prediction_data = json.loads(json_text)
#                 prediction = PredictionExtraction(**prediction_data)
#
#                 self.logger.info(f"✅ Anthropic extracted prediction from {source}")
#                 return prediction
#
#             except Exception as e2:
#                 self.logger.error(f"Both AI providers failed for {source}: {e2}")
#                 return None
#
#     async def calculate_consensus(self, predictions: List[PredictionExtraction],
#                                 game_query: str) -> ConsensusRecommendation:
#         """Calculate consensus recommendation from multiple predictions"""
#         if not predictions:
#             raise ValueError("No predictions provided for consensus calculation")
#
#         # Count predictions by team
#         team_votes = {}
#         total_confidence = 0
#         valid_predictions = [p for p in predictions if p.predicted_winner]
#
#         for prediction in valid_predictions:
#             team = prediction.predicted_winner
#             if team not in team_votes:
#                 team_votes[team] = {'count': 0, 'confidence_sum': 0}
#
#             team_votes[team]['count'] += 1
#             team_votes[team]['confidence_sum'] += prediction.confidence
#             total_confidence += prediction.confidence
#
#         if not team_votes:
#             raise ValueError("No valid predictions found")
#
#         # Find consensus winner
#         consensus_team = max(team_votes.keys(), key=lambda t: team_votes[t]['count'])
#         consensus_count = team_votes[consensus_team]['count']
#         consensus_percentage = (consensus_count / len(valid_predictions)) * 100
#
#         # Calculate average confidence
#         avg_confidence = team_votes[consensus_team]['confidence_sum'] / consensus_count
#
#         # Determine recommendation and risk level
#         if consensus_percentage >= 80 and avg_confidence >= 0.7:
#             recommendation = "bet"
#             risk_level = "low"
#         elif consensus_percentage >= 60 and avg_confidence >= 0.6:
#             recommendation = "bet"
#             risk_level = "medium"
#         elif consensus_percentage >= 40:
#             recommendation = "monitor"
#             risk_level = "high"
#         else:
#             recommendation = "avoid"
#             risk_level = "high"
#
#         # Generate explanation
#         explanation = f"Consensus analysis: {consensus_count}/{len(valid_predictions)} sources predict {consensus_team} to win ({consensus_percentage:.1f}% agreement) with average confidence of {avg_confidence:.2f}."
#
#         # Extract key factors
#         key_factors = []
#         for prediction in valid_predictions:
#             if prediction.predicted_winner == consensus_team:
#                 factors = prediction.reasoning.split('. ')[:2]  # Take first 2 sentences
#                 key_factors.extend(factors)
#
#         return ConsensusRecommendation(
#             predicted_winner=consensus_team,
#             confidence=avg_confidence,
#             consensus_percentage=consensus_percentage,
#             recommendation=recommendation,
#             risk_level=risk_level,
#             explanation=explanation,
#             key_factors=key_factors[:5]  # Limit to top 5 factors
#         )
#
#     async def analyze_all_predictions(self, scraped_data: List[Dict],
#                                     game_query: str) -> ConsensusRecommendation:
#         """Complete analysis pipeline: extract predictions and calculate consensus"""
#         extraction_tasks = []
#
#         for data in scraped_data:
#             if data and 'raw_text' in data:
#                 task = self.extract_prediction(data['raw_text'], data['source'])
#                 extraction_tasks.append(task)
#
#         # Extract predictions concurrently
#         predictions = await asyncio.gather(*extraction_tasks, return_exceptions=True)
#         valid_predictions = [p for p in predictions if isinstance(p, PredictionExtraction)]
#
#         if not valid_predictions:
#             raise ValueError("No valid predictions could be extracted from scraped data")
#
#         # Calculate consensus
#         consensus = await self.calculate_consensus(valid_predictions, game_query)
#
#         self.logger.info(f"✅ Consensus calculated: {consensus.predicted_winner} ({consensus.consensus_percentage:.1f}%)")
#         return consensus

# ============================================================================
