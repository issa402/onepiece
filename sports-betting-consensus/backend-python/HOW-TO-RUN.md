# 🏴‍☠️ **HOW TO RUN YOUR FASTAPI APPLICATION**

## **📋 COMPLETE STEP-BY-STEP GUIDE**

### **🎯 PROBLEM: "externally-managed-environment" Error**

When you try `pip install`, you get this error because Ubuntu 24.04+ protects system Python packages.

### **✅ SOLUTION: Use Virtual Environment**

## **STEP 1: NAVIGATE TO YOUR PROJECT**
```bash
cd ~/onepiece/sports-betting-consensus/backend-python
```

## **STEP 2: CREATE VIRTUAL ENVIRONMENT**
```bash
python3 -m venv venv
```
**What this does:** Creates isolated Python environment in `venv/` folder

## **STEP 3: ACTIVATE VIRTUAL ENVIRONMENT**
```bash
source venv/bin/activate
```
**What this does:** Switches to isolated environment (you'll see `(venv)` in terminal)

## **STEP 4: INSTALL DEPENDENCIES**
```bash
pip install fastapi uvicorn python-multipart
```
**What this does:** Installs FastAPI and web server in virtual environment only

## **STEP 5: FIX CODE ISSUES (IF ANY)**

### **Fix CORS Middleware:**
In `app/main.py`, change:
```python
# WRONG:
app.add_middleware(
    CORSMiddleware(
        allow_origins=["http://localhost:3000"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
)

# CORRECT:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"]
)
```

### **Fix Response Model:**
Change:
```python
# WRONG:
@app.post("/api/v1/predictions/consensus", response model = PredictionResponse)

# CORRECT:
@app.post("/api/v1/predictions/consensus", response_model=PredictionResponse)
```

## **STEP 6: RUN THE SERVER**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Command breakdown:**
- `uvicorn` = ASGI web server
- `app.main:app` = Points to `app` variable in `main.py`
- `--reload` = Auto-restart when code changes
- `--host 0.0.0.0` = Accept connections from any IP
- `--port 8000` = Run on port 8000

## **STEP 7: TEST YOUR API**

### **Health Check:**
```bash
curl http://localhost:8000/health
```

### **Interactive Docs:**
Open browser to: `http://localhost:8000/docs`

### **Alternative Docs:**
Open browser to: `http://localhost:8000/redoc`

## **🔧 TROUBLESHOOTING**

### **If you get import errors:**
Comment out problematic imports temporarily:
```python
# from app.services.prediction_service import PredictionService
```

### **If you get "setup_logging" error:**
Comment out:
```python
# setup_logging()
# logger = logging.getLogger(__name__)
```

### **If you get lifespan errors:**
Comment out the lifespan function and its usage.

## **🎯 COMPLETE WORKING COMMANDS**

```bash
# 1. Navigate to project
cd ~/onepiece/sports-betting-consensus/backend-python

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
source venv/bin/activate

# 4. Install dependencies
pip install fastapi uvicorn python-multipart

# 5. Run server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 6. Test (in another terminal)
curl http://localhost:8000/health
```

## **🚀 SUCCESS INDICATORS**

You'll see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [XXXXX] using StatReload
INFO:     Started server process [XXXXX]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## **⚡ QUICK REFERENCE**

### **Start Development:**
```bash
cd ~/onepiece/sports-betting-consensus/backend-python
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

### **Stop Server:**
Press `Ctrl+C` in terminal

### **Deactivate Virtual Environment:**
```bash
deactivate
```

## **🎯 EXPECTED RESULTS**

### **Health Check Response:**
```json
{
  "status": "healthy",
  "service": "sports-betting-api", 
  "timestamp": "2025-11-03T19:23:40.115318",
  "version": "1.0.0"
}
```

### **Available Endpoints:**
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation
- `GET /redoc` - Alternative API documentation
- `POST /api/v1/predictions/consensus` - Main prediction endpoint (if implemented)

## **📁 PROJECT STRUCTURE AFTER SETUP**
```
sports-betting-consensus/backend-python/
├── venv/                    # Virtual environment (created by you)
├── app/
│   ├── main.py             # Your FastAPI app
│   └── services/
│       ├── __init__.py
│       ├── scraper_service.py
│       ├── ai_analysis_service.py
│       └── prediction_service.py
└── HOW-TO-RUN.md           # This file
```

**NOW YOU CAN RUN YOUR FASTAPI APP YOURSELF!** 🏴‍☠️
