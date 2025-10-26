# 🎯 AI-Powered Sports Betting Consensus Aggregator

## **PROJECT OVERVIEW**

A full-stack web application that aggregates sports betting predictions from multiple websites, uses AI to analyze consensus, and provides users with data-driven betting recommendations.

## **🏗️ ARCHITECTURE**

### **Microservices Design:**
- **Frontend Service** (React/Next.js) - Port 3000
- **Python Scraping Service** (FastAPI) - Port 8000
- **Java API Gateway** (Spring Boot) - Port 8080
- **AI Analysis Service** (Python/FastAPI) - Port 8001
- **MCP Server** - Port 3001
- **PostgreSQL Database** - Port 5432
- **Redis Cache** - Port 6379

### **Technology Stack:**
- **Frontend:** React, TypeScript, Next.js, Tailwind CSS, SWR
- **Backend Python:** FastAPI, SQLAlchemy, Celery, BeautifulSoup, Playwright
- **Backend Java:** Spring Boot, Spring Security, Spring Data JPA
- **AI/LLM:** OpenAI API, Anthropic Claude, LangChain
- **Database:** PostgreSQL, Redis
- **DevOps:** Docker, Docker Compose, GitHub Actions
- **MCP:** Custom MCP server for AI agent integration

## **🚀 QUICK START**

### **Prerequisites:**
- Python 3.11+
- Node.js 18+
- Java 17+
- Docker & Docker Compose
- PostgreSQL 15+
- Redis 7+

### **Local Development:**
```bash
# Clone the repository
git clone <your-repo-url>
cd sports-betting-consensus

# Start all services with Docker Compose
docker-compose up -d

# Or run services individually:

# 1. Start Python scraping service
cd backend-python
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# 2. Start React frontend
cd frontend
npm install
npm run dev

# 3. Start Java API gateway
cd backend-java
./mvnw spring-boot:run

# 4. Start MCP server
cd mcp-server
npm install
npm run dev
```

## **📊 FEATURES**

### **Core Functionality:**
- ✅ **Real-time Web Scraping** - Automated scraping of 5+ sports betting sites
- ✅ **AI-Powered Analysis** - LLM extraction of predictions from unstructured text
- ✅ **Consensus Algorithm** - Weighted scoring based on source reliability
- ✅ **User Authentication** - Secure login and personalized betting history
- ✅ **Performance Tracking** - Historical accuracy metrics and analytics
- ✅ **Multi-Sport Support** - NBA, NFL, MLB, Soccer, Tennis, etc.

### **Advanced Features:**
- 🔄 **Background Job Processing** - Celery-based scheduled scraping
- 📈 **Real-time Updates** - WebSocket connections for live predictions
- 🤖 **MCP Integration** - AI agents can query betting data programmatically
- 📊 **Analytics Dashboard** - Comprehensive performance metrics
- 🔐 **Enterprise Security** - JWT authentication, rate limiting, CORS
- 🐳 **Containerized Deployment** - Full Docker orchestration

## **🎯 USER FLOW**

1. **User Input:** Enter game details (e.g., "Lakers vs Warriors, Jan 25, 2025")
2. **Automated Scraping:** System scrapes 5+ betting prediction websites
3. **AI Analysis:** LLM extracts and analyzes predictions from scraped content
4. **Consensus Calculation:** Algorithm weighs predictions by source reliability
5. **Results Display:** User sees consensus prediction with confidence score
6. **Performance Tracking:** Historical accuracy and betting performance analytics

## **📁 PROJECT STRUCTURE**

```
sports-betting-consensus/
├── frontend/                 # React/Next.js application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── next.config.js
├── backend-python/           # FastAPI scraping & AI service
│   ├── app/
│   │   ├── api/             # API endpoints
│   │   ├── core/            # Configuration & utilities
│   │   ├── models/          # SQLAlchemy models
│   │   ├── services/        # Business logic
│   │   └── scrapers/        # Web scraping modules
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── backend-java/             # Spring Boot API gateway
│   ├── src/main/java/
│   ├── src/main/resources/
│   ├── pom.xml
│   └── Dockerfile
├── mcp-server/               # Custom MCP server
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── docs/                     # Documentation & diagrams
├── scripts/                  # Deployment & utility scripts
├── docker-compose.yml        # Local development orchestration
├── docker-compose.prod.yml   # Production deployment
└── README.md
```

## **🔧 DEVELOPMENT PHASES**

- [x] **Phase 1:** Python FastAPI Scraping Service ✅
- [ ] **Phase 2:** PostgreSQL Database & Data Models
- [ ] **Phase 3:** AI/LLM Prediction Analysis Service
- [ ] **Phase 4:** React/Next.js Frontend
- [ ] **Phase 5:** Java Spring Boot API Gateway
- [ ] **Phase 6:** Docker & Service Orchestration
- [ ] **Phase 7:** MCP Server Integration
- [ ] **Phase 8:** CI/CD & Cloud Deployment

## **💼 CAREER IMPACT**

### **Skills Demonstrated:**
- Full-stack development (React, TypeScript, Python, Java)
- Microservices architecture & API design
- AI/LLM integration & prompt engineering
- Web scraping & data engineering
- Enterprise patterns (API gateway, message queues)
- DevOps (Docker, CI/CD, monitoring)
- Real-world problem solving

### **Target Roles:**
- Full-Stack Engineer ($100K-$180K)
- Backend Engineer - Python/Java ($120K-$200K)
- AI/ML Engineer ($130K-$250K)
- Data Engineer ($110K-$190K)
- DevOps Engineer ($120K-$220K)

### **Companies:**
- **Sports Betting:** DraftKings, FanDuel, BetMGM
- **Fintech:** Robinhood, Coinbase, trading firms
- **AI Companies:** OpenAI, Anthropic, Scale AI
- **Enterprise:** JPMorgan Chase, Goldman Sachs

## **🚀 GETTING STARTED**

Ready to build your career-defining project? Let's start with Phase 1!

```bash
cd backend-python
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Visit http://localhost:8000/docs to see the interactive API documentation.

## **📞 SUPPORT**

- **Documentation:** See `/docs` folder for detailed guides
- **API Reference:** Visit `/docs` endpoint on each service
- **Issues:** Create GitHub issues for bugs or feature requests

---

**🏴‍☠️ Built with the power of the Grand Line development stack!** ⚔️
