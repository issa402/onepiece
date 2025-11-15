# ============================================================================
# 📚 LEARNING GUIDE: Web Scraping Service (services/scraper_service.py)
# ============================================================================
#
# 🎯 PURPOSE:
# This service handles automated web scraping of sports betting prediction websites.
# It's the core data collection engine that:
# - Scrapes multiple betting sites simultaneously
# - Extracts predictions from unstructured HTML/text
# - Handles anti-bot measures and rate limiting
# - Stores raw data for AI analysis
# - Manages scraping schedules and retries
#
# 🔧 TECHNOLOGIES USED:
# - BeautifulSoup4: HTML parsing and data extraction
# - Playwright: Browser automation for JavaScript-heavy sites
# - Requests/HTTPX: HTTP client for simple scraping
# - Selenium: Alternative browser automation (backup)
# - Pandas: Data processing and cleaning
# - Asyncio: Concurrent scraping for performance
# - Tenacity: Retry logic with exponential backoff
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Web Scraping Fundamentals:**
# Web scraping extracts data from websites by:
# 1. Making HTTP requests to target URLs
# 2. Parsing HTML content with CSS selectors
# 3. Extracting specific data points (predictions, odds, analysis)
# 4. Handling dynamic content loaded by JavaScript
# 5. Managing rate limits and anti-bot measures
#
# **Scraping Strategy Hierarchy:**
# 1. **Static Content**: Use requests + BeautifulSoup (fastest)
# 2. **JavaScript Content**: Use Playwright (headless browser)
# 3. **Complex Sites**: Use Selenium with full browser (slowest)
#
# **Anti-Bot Countermeasures:**
# - Rotate User-Agent headers
# - Use proxy rotation (optional)
# - Implement random delays between requests
# - Respect robots.txt (ethical scraping)
# - Handle CAPTCHA detection
# - Use session management for login-required sites
#
# **Data Extraction Patterns:**
# - CSS Selectors: `.prediction-text`, `#winner-pick`
# - XPath: `//div[@class='prediction']//text()`
# - Regex: Extract odds, percentages, team names
# - Natural Language Processing: Extract sentiment and confidence
#
# **Concurrent Scraping:**
# - Use asyncio for I/O-bound operations
# - Semaphore to limit concurrent requests
# - Queue-based processing for large datasets
# - Error isolation (one failed site doesn't break others)
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 34 (TypeScript/Node.js): Lines 600-700 - Async/await patterns
# - Module 36 (AI/LLM Integration): Lines 300-400 - Data processing pipelines
# - Python asyncio documentation for concurrent programming
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Create ScraperService class with async methods
# [ ] Implement site-specific scraping strategies
# [ ] Add retry logic with exponential backoff
# [ ] Handle different content types (static vs dynamic)
# [ ] Implement rate limiting and delays
# [ ] Add data validation and cleaning
# [ ] Create error handling for failed scrapes
# [ ] Add logging for monitoring and debugging
# [ ] Implement concurrent scraping with semaphores
# [ ] Store raw data for AI analysis
# [ ] Add health checks for scraping targets
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - HTML structure and CSS selectors
# - HTTP headers and session management
# - Async programming patterns in Python
# - Browser automation with Playwright
# - Regular expressions for text extraction
# - Error handling and retry strategies
# - Rate limiting and ethical scraping
# - Data validation and cleaning techniques
#
# 🚀 REAL-WORLD EXAMPLES:
# - Google: Web crawling for search indexing
# - Price comparison sites: Product data scraping
# - Financial services: Market data aggregation
# - News aggregators: Article collection
#
# 🔍 COMMON SCRAPING TARGETS:
# - ESPN.com: Sports predictions and analysis
# - CBS Sports: Expert picks and odds
# - Bleacher Report: Fan predictions and sentiment
# - The Athletic: Premium analysis content
# - Sports Illustrated: Historical prediction accuracy
#
# ⚠️ LEGAL AND ETHICAL CONSIDERATIONS:
# - Always check robots.txt before scraping
# - Respect rate limits and don't overload servers
# - Only scrape publicly available information
# - Consider API alternatives when available
# - Be transparent about data usage
#
# 🛠️ DEBUGGING TIPS:
# - Use browser dev tools to inspect HTML structure
# - Test CSS selectors in browser console
# - Log HTTP response codes and headers
# - Save HTML snapshots for offline testing
# - Use proxy tools to inspect network traffic
#
# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================
#
# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from playwright.async_api import async_playwright
# from typing import List, Dict, Optional
# import logging
# from tenacity import retry, stop_after_attempt, wait_exponential
# 
# class ScraperService:
#     def __init__(self):
#         self.session = None
#         self.semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests
#         self.logger = logging.getLogger(__name__)
#     
#     async def scrape_all_sources(self, game_query: str, game_date: datetime) -> List[Dict]:
#         """Scrape all configured betting sites for predictions"""
#         tasks = []
#         for site in settings.BETTING_SITES:
#             task = self.scrape_site(site, game_query, game_date)
#             tasks.append(task)
#         
#         results = await asyncio.gather(*tasks, return_exceptions=True)
#         return [r for r in results if not isinstance(r, Exception)]
#     
#     @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
#     async def scrape_site(self, site: str, game_query: str, game_date: datetime) -> Dict:
#         """Scrape a specific site with retry logic"""
#         async with self.semaphore:
#             if site == "espn.com":
#                 return await self.scrape_espn(game_query, game_date)
#             elif site == "cbssports.com":
#                 return await self.scrape_cbs_sports(game_query, game_date)
#             # Add more site-specific scrapers
#     
#     async def scrape_espn(self, game_query: str, game_date: datetime) -> Dict:
#         """ESPN-specific scraping logic"""
#         url = f"https://www.espn.com/nba/game/_/gameId/{game_query}"
#         
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, headers=self.get_headers()) as response:
#                 html = await response.text()
#                 soup = BeautifulSoup(html, 'html.parser')
#                 
#                 # Extract prediction data using CSS selectors
#                 prediction_element = soup.select_one('.prediction-text')
#                 if prediction_element:
#                     return {
#                         'source': 'ESPN',
#                         'prediction': prediction_element.text.strip(),
#                         'confidence': self.extract_confidence(prediction_element.text),
#                         'url': url,
#                         'scraped_at': datetime.utcnow()
#                     }
#         
#         return None
#
# ============================================================================

# ============================================================================
# 💻 YOUR CODE GOES HERE - TRY TO IMPLEMENT FIRST!
# ============================================================================
#
# 🎯 YOUR TASK: Create a ScraperService class that can scrape betting sites
#
# 📋 STEP-BY-STEP IMPLEMENTATION:
#
# 1. Import required libraries:
#    - asyncio (for concurrent scraping)
#    - aiohttp (for HTTP requests)
#    - BeautifulSoup (for HTML parsing)
#    - typing (for type hints)
#    - logging (for debugging)
#
# 2. Create ScraperService class with:
#    - __init__ method to set up session and semaphore
#    - scrape_all_sources method (main entry point)
#    - scrape_site method (handles individual sites)
#    - Site-specific methods (scrape_espn, scrape_cbs, etc.)
#
# 3. Key concepts to implement:
#    - Async/await for concurrent operations
#    - Semaphore to limit concurrent requests (max 5)
#    - Retry logic with exponential backoff
#    - CSS selectors to extract data from HTML
#    - Error handling for failed requests
#
# 🔍 EXAMPLE: Here's how to start your ScraperService class:
#
# class ScraperService:
#     def __init__(self):
#         # TODO: Initialize session, semaphore, logger
#         pass
#
#     async def scrape_all_sources(self, game_query: str, game_date) -> List[Dict]:
#         # TODO: Create tasks for each betting site
#         # TODO: Use asyncio.gather to run concurrently
#         # TODO: Filter out exceptions and return valid results
#         pass
#
# 💡 HINTS:
# - Use asyncio.Semaphore(5) to limit concurrent requests
# - Use aiohttp.ClientSession() for HTTP requests
# - Use BeautifulSoup(html, 'html.parser') to parse HTML
# - Use CSS selectors like soup.select_one('.prediction-text')
# - Always handle exceptions gracefully
#
# 🧪 TEST YOUR CODE:
# After implementing, test with:
# scraper = ScraperService()
# results = await scraper.scrape_all_sources("Lakers vs Warriors", datetime.now())
# print(results)

# ============================================================================
# 🎯 DETAILED STEP-BY-STEP IMPLEMENTATION GUIDE
# ============================================================================

# ============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES - WHAT EACH ONE DOES
# ============================================================================
#
# **WHAT TO DO:** Import all the Python libraries needed for web scraping
# **WHY YOU NEED IT:** Each library handles a specific part of web scraping
# **WHEN TO USE:** Always at the top of your Python files
# **HOW IT WORKS:** Python's import system loads external functionality
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **import asyncio**: Asynchronous programming
#    - WHAT IT DOES: Allows scraping multiple websites simultaneously instead of one-by-one
#    - WHY YOU NEED IT: Scraping 5 sites sequentially takes 50 seconds, concurrently takes 10 seconds
#    - REAL EXAMPLE: Google scrapes millions of websites concurrently using similar techniques
#    - HOW IT WORKS: Creates "tasks" that run in parallel without blocking each other
#
# 🔹 **import aiohttp**: Async HTTP client
#    - WHAT IT DOES: Makes HTTP requests (like visiting websites) asynchronously
#    - WHY YOU NEED IT: Regular requests library blocks - aiohttp doesn't
#    - REAL EXAMPLE: Netflix uses aiohttp to fetch movie data from multiple APIs simultaneously
#    - HOW IT WORKS: async with aiohttp.ClientSession() as session: await session.get(url)
#
# 🔹 **from bs4 import BeautifulSoup**: HTML parsing
#    - WHAT IT DOES: Converts messy HTML into searchable Python objects
#    - WHY YOU NEED IT: Websites return HTML, you need to extract specific data from it
#    - REAL EXAMPLE: Amazon uses similar tools to extract product info from supplier websites
#    - HOW IT WORKS: soup = BeautifulSoup(html); prediction = soup.find('div', class_='prediction')
#
# **YOUR CODE HERE:**
# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from typing import List, Dict, Optional
# import logging
# from datetime import datetime
# import random

# ============================================================================
# STEP 2: CREATE SCRAPERSERVICE CLASS - WHAT EACH PART DOES
# ============================================================================
#
# **WHAT TO DO:** Create the main class that handles all web scraping
# **WHY YOU NEED IT:** Organizes all scraping logic in one place with shared configuration
# **WHEN TO USE:** This is your main scraping interface that other services will use
# **HOW IT WORKS:** Class encapsulates state (config, rate limits) and behavior (scraping methods)
#
# **DETAILED BREAKDOWN:**
#
# 🔹 **class ScraperService**: Main scraping class
#    - WHAT IT DOES: Contains all scraping methods and shared configuration
#    - WHY YOU NEED IT: Organizes code and allows sharing rate limits, user agents, etc.
#    - REAL EXAMPLE: Scrapy framework uses similar class-based architecture
#    - HOW IT WORKS: scraper = ScraperService(); results = await scraper.scrape_all_sources()
#
# 🔹 **self.semaphore = asyncio.Semaphore(5)**: Rate limiting
#    - WHAT IT DOES: Limits to maximum 5 concurrent requests to avoid overwhelming servers
#    - WHY YOU NEED IT: Sending 100 requests simultaneously will get you blocked
#    - REAL EXAMPLE: Movie theaters limit tickets per person, APIs limit requests per second
#    - HOW IT WORKS: async with self.semaphore: # Only 5 requests can run at once
#
# **YOUR CODE HERE:**
class ScraperService:
    def __init__(self):
        self.semaphore = None  # Will implement later
        self.logger = None     # Will implement later

    async def scrape_betting_sites(self, game_query):
        """Mock scraper service for testing"""
        return {
            "sites_scraped": ["draftkings", "fanduel", "betmgm"],
            "predictions": [
                {"site": "draftkings", "prediction": "Team A", "confidence": 0.75},
                {"site": "fanduel", "prediction": "Team A", "confidence": 0.80},
                {"site": "betmgm", "prediction": "Team B", "confidence": 0.65}
            ]
        }

# class ScraperService:
#     def __init__(self):
#         self.semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests
#         self.logger = logging.getLogger(__name__)
#         self.user_agents = [
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
#         ]

# YOUR IMPLEMENTATION HERE:
# (Write your ScraperService class below)

# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================

# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup
# from playwright.async_api import async_playwright
# from typing import List, Dict, Optional
# import logging
# from tenacity import retry, stop_after_attempt, wait_exponential
# from datetime import datetime
# import random
#
# class ScraperService:
#     def __init__(self):
#         self.session = None
#         self.semaphore = asyncio.Semaphore(5)  # Max 5 concurrent requests
#         self.logger = logging.getLogger(__name__)
#         self.user_agents = [
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
#             "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
#         ]
#
#     async def scrape_all_sources(self, game_query: str, game_date: datetime) -> List[Dict]:
#         """Scrape all configured betting sites for predictions"""
#         sites = ["espn.com", "cbssports.com", "theathletic.com", "bleacherreport.com"]
#         tasks = []
#
#         for site in sites:
#             task = self.scrape_site(site, game_query, game_date)
#             tasks.append(task)
#
#         results = await asyncio.gather(*tasks, return_exceptions=True)
#         valid_results = [r for r in results if not isinstance(r, Exception)]
#
#         self.logger.info(f"✅ Scraped {len(valid_results)}/{len(sites)} sites successfully")
#         return valid_results
#
#     @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
#     async def scrape_site(self, site: str, game_query: str, game_date: datetime) -> Dict:
#         """Scrape a specific site with retry logic"""
#         async with self.semaphore:
#             await asyncio.sleep(random.uniform(1, 3))  # Random delay
#
#             if site == "espn.com":
#                 return await self.scrape_espn(game_query, game_date)
#             elif site == "cbssports.com":
#                 return await self.scrape_cbs_sports(game_query, game_date)
#             elif site == "theathletic.com":
#                 return await self.scrape_athletic(game_query, game_date)
#             elif site == "bleacherreport.com":
#                 return await self.scrape_bleacher_report(game_query, game_date)
#             else:
#                 return None
#
#     async def scrape_espn(self, game_query: str, game_date: datetime) -> Dict:
#         """ESPN-specific scraping logic"""
#         url = f"https://www.espn.com/nba/game/_/gameId/{game_query.replace(' vs ', '-')}"
#
#         try:
#             async with aiohttp.ClientSession() as session:
#                 headers = {"User-Agent": random.choice(self.user_agents)}
#                 async with session.get(url, headers=headers, timeout=30) as response:
#                     if response.status == 200:
#                         html = await response.text()
#                         soup = BeautifulSoup(html, 'html.parser')
#
#                         # Extract prediction data using CSS selectors
#                         prediction_element = soup.select_one('.prediction-text, .expert-pick, .game-prediction')
#
#                         if prediction_element:
#                             prediction_text = prediction_element.get_text(strip=True)
#                             return {
#                                 'source': 'ESPN',
#                                 'raw_text': prediction_text,
#                                 'url': url,
#                                 'scraped_at': datetime.utcnow(),
#                                 'confidence_raw': self.extract_confidence_indicators(prediction_text)
#                             }
#         except Exception as e:
#             self.logger.error(f"ESPN scraping failed: {e}")
#             return None
#
#     async def scrape_cbs_sports(self, game_query: str, game_date: datetime) -> Dict:
#         """CBS Sports-specific scraping logic"""
#         # Mock implementation - replace with real scraping logic
#         return {
#             'source': 'CBS Sports',
#             'raw_text': f"CBS Sports predicts a close game for {game_query}. Home team advantage expected.",
#             'url': f"https://cbssports.com/nba/predictions/{game_query}",
#             'scraped_at': datetime.utcnow(),
#             'confidence_raw': ['close game', 'home advantage']
#         }
#
#     async def scrape_athletic(self, game_query: str, game_date: datetime) -> Dict:
#         """The Athletic-specific scraping logic"""
#         # Mock implementation - replace with real scraping logic
#         return {
#             'source': 'The Athletic',
#             'raw_text': f"The Athletic's expert analysis for {game_query} suggests road team upset potential.",
#             'url': f"https://theathletic.com/nba/predictions/{game_query}",
#             'scraped_at': datetime.utcnow(),
#             'confidence_raw': ['expert analysis', 'upset potential']
#         }
#
#     async def scrape_bleacher_report(self, game_query: str, game_date: datetime) -> Dict:
#         """Bleacher Report-specific scraping logic"""
#         # Mock implementation - replace with real scraping logic
#         return {
#             'source': 'Bleacher Report',
#             'raw_text': f"Bleacher Report statistical model favors home team in {game_query}.",
#             'url': f"https://bleacherreport.com/nba/predictions/{game_query}",
#             'scraped_at': datetime.utcnow(),
#             'confidence_raw': ['statistical model', 'favors home team']
#         }
#
#     def extract_confidence_indicators(self, text: str) -> List[str]:
#         """Extract confidence indicators from prediction text"""
#         indicators = []
#         confidence_words = ['confident', 'likely', 'probable', 'expected', 'favored', 'strong']
#
#         for word in confidence_words:
#             if word.lower() in text.lower():
#                 indicators.append(word)
#
#         return indicators
#
#     def get_headers(self) -> Dict[str, str]:
#         """Get randomized headers for requests"""
#         return {
#             "User-Agent": random.choice(self.user_agents),
#             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#             "Accept-Language": "en-US,en;q=0.5",
#             "Accept-Encoding": "gzip, deflate",
#             "Connection": "keep-alive",
#         }

# ============================================================================
