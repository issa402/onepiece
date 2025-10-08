# 🏴‍☠️ One Piece Character Service API

A REST API for managing One Piece characters and their stock market data.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up environment
cp .env.example .env
# Edit .env with your database credentials

# 3. Set up database
python database_setup.py

# 4. Run the application
python app.py
```

## 📋 API Endpoints

### Health Check
```http
GET /health
```
Returns the health status of the API service.

**Response:**
```json
{
  "status": "healthy",
  "service": "character-service",
  "timestamp": "2024-01-01T12:00:00Z",
  "database": "connected"
}
```

### Characters

#### Get All Characters
```http
GET /api/characters
```

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `per_page` (int): Items per page (default: 20, max: 100)
- `crew` (string): Filter by crew name
- `is_active` (boolean): Filter by active status
- `sort_by` (string): Sort field (name, bounty, current_price)
- `sort_order` (string): Sort direction (asc, desc)

**Response:**
```json
{
  "characters": [
    {
      "id": 1,
      "name": "Monkey D. Luffy",
      "crew": "Straw Hat Pirates",
      "bounty": 3000000000,
      "current_price": 150.00,
      "market_cap": 150000000.00,
      "sentiment_score": 0.85,
      "weekly_change": 5.25,
      "description": "Captain of the Straw Hat Pirates",
      "image_url": null,
      "is_active": true,
      "created_at": "2024-01-01T12:00:00Z",
      "updated_at": "2024-01-01T12:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 25,
    "pages": 2,
    "has_next": true,
    "has_prev": false
  }
}
```

#### Get Single Character
```http
GET /api/characters/{id}
```

**Response:**
```json
{
  "id": 1,
  "name": "Monkey D. Luffy",
  "crew": "Straw Hat Pirates",
  "bounty": 3000000000,
  "current_price": 150.00,
  "market_cap": 150000000.00,
  "sentiment_score": 0.85,
  "weekly_change": 5.25,
  "description": "Captain of the Straw Hat Pirates",
  "image_url": null,
  "is_active": true,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

#### Create Character
```http
POST /api/characters
```

**Request Body:**
```json
{
  "name": "New Character",
  "crew": "New Crew",
  "bounty": 1000000,
  "current_price": 100.00,
  "sentiment_score": 0.5,
  "description": "A new One Piece character"
}
```

**Response:** `201 Created`
```json
{
  "id": 26,
  "name": "New Character",
  "crew": "New Crew",
  "bounty": 1000000,
  "current_price": 100.00,
  "market_cap": 100000000.00,
  "sentiment_score": 0.5,
  "weekly_change": 0.0,
  "description": "A new One Piece character",
  "image_url": null,
  "is_active": true,
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T12:00:00Z"
}
```

#### Update Character
```http
PUT /api/characters/{id}
```

**Request Body:**
```json
{
  "bounty": 2000000,
  "current_price": 120.00,
  "sentiment_score": 0.75
}
```

**Response:** `200 OK`

#### Delete Character (Soft Delete)
```http
DELETE /api/characters/{id}
```

**Response:** `200 OK`
```json
{
  "message": "Character deleted successfully"
}
```

### Character Prices

#### Get Character Price
```http
GET /api/characters/{id}/price
```

**Response:**
```json
{
  "character_id": 1,
  "character_name": "Monkey D. Luffy",
  "current_price": 150.00,
  "market_cap": 150000000.00,
  "weekly_change": 5.25,
  "sentiment_score": 0.85,
  "last_updated": "2024-01-01T12:00:00Z"
}
```

#### Update Character Price
```http
POST /api/characters/{id}/price
```

**Request Body:**
```json
{
  "price": 160.00
}
```

**Response:**
```json
{
  "character_id": 1,
  "character_name": "Monkey D. Luffy",
  "old_price": 150.00,
  "new_price": 160.00,
  "weekly_change": 6.67,
  "updated_at": "2024-01-01T12:00:00Z"
}
```

## 🔧 Error Responses

### 400 Bad Request
```json
{
  "error": "Validation error",
  "messages": {
    "name": ["This field is required."],
    "current_price": ["Must be greater than 0."]
  }
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 409 Conflict
```json
{
  "error": "Character with this name already exists"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

## 🗄️ Database Schema

### Characters Table
| Column | Type | Description |
|--------|------|-------------|
| id | INT | Primary key |
| name | VARCHAR(100) | Character name (unique) |
| crew | VARCHAR(100) | Crew name |
| bounty | BIGINT | Bounty amount |
| current_price | DECIMAL(10,2) | Current stock price |
| sentiment_score | DECIMAL(3,2) | Sentiment score (-1.0 to 1.0) |
| weekly_change | DECIMAL(5,2) | Weekly price change percentage |
| description | TEXT | Character description |
| image_url | VARCHAR(255) | Character image URL |
| is_active | BOOLEAN | Active status |
| created_at | DATETIME | Creation timestamp |
| updated_at | DATETIME | Last update timestamp |

## 🧪 Testing

```bash
# Run unit tests
python test_unit.py

# Run API tests
python test_api.py

# Run specific test
python test_api.py health

# Run with coverage
python -m coverage run test_unit.py
python -m coverage report
```

## 🐳 Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# Build image only
docker build -t onepiece-character-service .

# Run container
docker run -p 5001:5001 onepiece-character-service
```

## 🔒 Security Features

- Input validation with Marshmallow
- SQL injection prevention with SQLAlchemy ORM
- CORS configuration for cross-origin requests
- Environment variable configuration
- Error handling without sensitive data exposure

## 📊 Monitoring

- Health check endpoint for monitoring
- Structured logging
- Error tracking and reporting
- Performance metrics (future)

## 🚀 Deployment

### Development
```bash
python run.py start --mode dev
```

### Production
```bash
python run.py start --mode prod
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Ensure all tests pass
5. Submit a pull request

## 📝 License

This project is part of the One Piece Character Stock Market learning project.

---

**Next Service:** Trading Service (C# .NET Core) 🚀
