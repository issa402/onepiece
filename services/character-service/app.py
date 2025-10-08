"""
🏴‍☠️ ONE PIECE CHARACTER SERVICE - FLASK REST API BLUEPRINT
Your mission: Build a REST API to manage One Piece characters and their stock data

WHAT YOU'RE BUILDING:
- A Flask web server that handles HTTP requests
- Database models for characters
- REST API endpoints (GET, POST, PUT, DELETE)
- Data validation and error handling
- JSON responses for frontend consumption

LEARNING OBJECTIVES:
- Flask framework basics
- SQLAlchemy ORM (Object Relational Mapping)
- REST API design principles
- HTTP status codes and methods
- Database operations (CRUD)
- JSON serialization
- Error handling and logging
"""

# TODO 1: IMPORT STATEMENTS
# You need to import these Python libraries:
# Copy and paste this EXACT code block:

import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from dotenv import load_dotenv
from datetime import datetime
from flask import abort
import pymysql

# SYNTAX EXPLANATION:
# import os                    - Built-in module for environment variables
# from flask import Flask      - Import specific classes from modules
# from dotenv import load_dotenv - Third-party library for .env files
#
# LEARNING RESOURCES:
# Flask Tutorial: https://flask.palletsprojects.com/en/2.3.x/tutorial/
# SQLAlchemy Guide: https://docs.sqlalchemy.org/en/20/tutorial/


# TODO 2: LOAD ENVIRONMENT VARIABLES
# Copy this EXACT code:
load_dotenv()

# SYNTAX EXPLANATION:
# load_dotenv() - Loads variables from .env file into os.environ
# Now you can use os.getenv('VARIABLE_NAME') to access them

# TODO 3: INITIALIZE FLASK APP
# Copy this EXACT code:
app = Flask(__name__)

# SYNTAX EXPLANATION:
# Flask(__name__) - Creates Flask app instance
# __name__ - Python built-in variable with current module name

# TODO 4: FLASK CONFIGURATION
# Copy this EXACT code block:
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'luffy-will-be-pirate-king-secret-2024')
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER', 'root')}:"
    f"{os.getenv('DB_PASSWORD', 'password')}@"
    f"{os.getenv('DB_HOST', 'localhost')}:"
    f"{os.getenv('DB_PORT', '3306')}/"
    f"{os.getenv('DB_NAME', 'onepiece_market')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SYNTAX EXPLANATION:
# app.config['KEY'] = value - Sets Flask configuration
# os.getenv('VAR', 'default') - Gets environment variable with fallback
# f"string {variable}" - F-string formatting (Python 3.6+)
#
# LEARNING TIP:
# The connection string format: mysql+pymysql://user:password@host:port/database


# TODO 5: INITIALIZE EXTENSIONS
# Initialize SQLAlchemy: db = SQLAlchemy(app)
# Initialize CORS: CORS(app, origins=...)
db = SQLAlchemy(app)
CORS : CORS(app, origins = "*")

# TODO 6: CONFIGURE LOGGING
# Set up logging to track what your API is doing
logging.basicConfig(
    level = logging.INFO, 
    format = "%(asctime)s [%(levelname)s] %(message)s"
)
logging.info("API started")



# TODO 7: CREATE CHARACTER MODEL
# This is your database table structure as a Python class
#
# class Character(db.Model):
#     __tablename__ = 'characters'
#
#     # Define these columns using db.Column():
#     # - id (Integer, primary key, auto increment)
#     # - name (String 100, required, unique)
#     # - crew (String 100, optional)
#     # - bounty (BigInteger, default 0)
#     # - current_price (Numeric 10,2, required, default 100.00)
#     # - sentiment_score (Numeric 3,2, default 0.00)
#     # - weekly_change (Numeric 5,2, default 0.00)
#     # - description (Text, optional)
#     # - image_url (String 255, optional)
#     # - is_active (Boolean, default True)
#     # - created_at (DateTime, default now)
#     # - updated_at (DateTime, default now, update on change)
#
#     def to_dict(self):
#         # Convert database object to Python dictionary for JSON response
#         # Return all character fields as a dictionary
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    crew = db.Column(db.String(100), nullable=True)
    bounty = db.Column(db.BigInteger, default=0)
    current_price = db.Column(db.Numeric(10, 2), nullable=False, default=100.00)
    sentiment_score = db.Column(db.Numeric(3, 2), default=0.00)
    weekly_change = db.Column(db.Numeric(5, 2), default=0.00)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        """Convert database object to Python dictionary for JSON response"""
        return {
            'id': self.id,
            'name': self.name,
            'crew': self.crew,
            'bounty': self.bounty,
            'current_price': float(self.current_price) if self.current_price else 0.0,
            'market_cap': float(self.current_price * 1000000) if self.current_price else 0.0,
            'sentiment_score': float(self.sentiment_score) if self.sentiment_score else 0.0,
            'weekly_change': float(self.weekly_change) if self.weekly_change else 0.0,
            'description': self.description,
            'image_url': self.image_url,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }




# TODO 8: CREATE VALIDATION SCHEMA
# Use Marshmallow to validate incoming data
#
# class CharacterSchema(Schema):
#     # Define validation rules for each field
#     # - name: required string, not empty
#     # - bounty: optional integer, >= 0
#     # - current_price: decimal, > 0
#     # - sentiment_score: decimal, between -1.0 and 1.0
#     # etc.
class CharacterSchema(Schema):
    name = fields.String(required=True)
    crew = fields.String()
    bounty = fields.Integer(validate=lambda x: x >= 0)
    current_price = fields.Decimal(required=True, as_string=True)
    sentiment_score = fields.Decimal(validate=lambda x: -1.0 <= float(x) <= 1.0)
    weekly_change = fields.Decimal()
    description = fields.String()
    image_url = fields.String()
    is_active = fields.Boolean()

character_schema = CharacterSchema() # for single id charcater
characters_schema = CharacterSchema(many=True) # for all list ids

# TODO 9: ERROR HANDLERS
@app.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": e.messages}), 400

@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def handle_500(e):
    return jsonify({"error": "Internal server error"}), 500

# TODO 10: HEALTH CHECK ENDPOINT
@app.route('/health', methods=['GET'])
def health_check():
    try:
        from sqlalchemy import text
        db.session.execute(text('SELECT 1'))
        return jsonify({
            "status": "healthy",
            "service": "character-service",
            "timestamp": datetime.now().isoformat(),
            "database": "connected"
        }), 200
    except Exception as e:
        logging.error(f"Health check failed: {e}")
        return jsonify({"status": "error", "details": str(e)}), 500

# TODO 11: GET ALL CHARACTERS ENDPOINT
@app.route('/api/characters', methods=['GET'])
def get_characters():
    query = Character.query

    # Filters
    crew = request.args.get('crew')
    is_active = request.args.get('is_active')
    sort_by = request.args.get('sort_by', 'id')
    sort_order = request.args.get('sort_order', 'asc')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    if crew:
        query = query.filter_by(crew=crew)
    if is_active is not None:
        query = query.filter_by(is_active=is_active.lower() == 'true')

    # Sorting
    if sort_order == 'desc':
        query = query.order_by(db.desc(getattr(Character, sort_by)))
    else:
        query = query.order_by(getattr(Character, sort_by))

    # Pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    characters = [char.to_dict() for char in pagination.items]

    return jsonify({
        "characters": characters,
        "total": pagination.total,
        "page": pagination.page,
        "pages": pagination.pages
    })




# TODO 12: GET SINGLE CHARACTER ENDPOINT
# @app.route('/api/characters/<int:character_id>', methods=['GET'])
# def get_character(character_id):
#     # Find character by ID or return 404
#     # Return character as JSON
@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    char = Character.query.get(character_id)
    if not char:
        abort(404)
    return jsonify(character_schema.dump(char)),200

# TODO 13: CREATE CHARACTER ENDPOINT
# @app.route('/api/characters', methods=['POST'])
# def create_character():
#     # Get JSON data from request
#     # Validate data using schema
#     # Check if character name already exists
#     # Create new character in database
#     # Return created character as JSON
@app.route('/api/characters', methods=['POST'])
def create_character():
    try:
        payload = request.get_json()
        if payload is None:
            return jsonify({'error': 'MISSING Json'}),400
    except Exception:
        return jsonify({'error', 'Invalid JSON'}),400
    
    try:
        data = character_schema.load(payload)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    if Character.query.filter_by(name = data["name"]).first():
        return jsonify({"error": "fCharacter '{data['name']}' already exists"}), 409
    
    new_char = Character(**data)
    db.session.add(new_char)
    db.session.commit()

    return jsonify(character_schema.dump(new_char)),201
    



# TODO 14: UPDATE CHARACTER ENDPOINT
# @app.route('/api/characters/<int:character_id>', methods=['PUT'])
# def update_character(character_id):
#     # Find existing character
#     # Validate incoming data
#     # Check for name conflicts
#     # Update character fields
#     # Save to database
#     # Return updated character
@app.route('/api/characters/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    # 1. Fetch existing character or return 404
    character = Character.query.get_or_404(character_id)

    # 2. Validate incoming JSON (partial=True allows updating any subset of fields)
    try:
        data = character_schema.load(request.get_json(), partial=True)
    except ValidationError as err:
        return jsonify(error=err.messages), 400

    # 3. If name is changing, ensure uniqueness across other records
    if "name" in data:
        conflict = (
            Character.query
            .filter(Character.name == data["name"], Character.id != character_id)
            .first()
        )
        if conflict:
            return jsonify(error={"name": ["Name already in use"]}), 409

    # 4. Apply updates dynamically
    for field, value in data.items():
        setattr(character, field, value)

    # 5. Persist changes
    db.session.commit()

    # 6. Return the updated resource
    return jsonify(character_schema.dump(character)), 200



# TODO 15: DELETE CHARACTER ENDPOINT (SOFT DELETE)
# @app.route('/api/characters/<int:character_id>', methods=['DELETE'])
# def delete_character(character_id):
#     # Find character
#     # Set is_active = False (soft delete)
#     # Save to database
#     # Return success message
@app.route('/api/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get_or_404(character_id)
    
    character.is_active = False
    db.session.commit()

    return jsonify({
        "message": f"Character '{character.name}' has been deactivated",
        "id" : character.id,
        "is_active" : character.is_active
    }), 200


# TODO 16: GET CHARACTER PRICE ENDPOINT
# @app.route('/api/characters/<int:character_id>/price', methods=['GET'])
# def get_character_price(character_id):
#     # Get character price info
#     # Calculate market cap
#     # Return price data as JSON
@app.route('/api/characters/<int:character_id>/price', methods = ['GET'])
def get_character_price(character_id):
    char = Character.query.get_or_404(character_id)

    current_price = float(char.current_price)
    bounty = char.bounty

    market_cap = current_price * bounty

    return jsonify({
        "id" : char.id,
        "name" : char.name,
        "current_price" : current_price,
        "bounty" : bounty,
        "market_cap" : market_cap
    }),200

# TODO 17: UPDATE CHARACTER PRICE ENDPOINT
# @app.route('/api/characters/<int:character_id>/price', methods=['POST'])
# def update_character_price(character_id):
#     # Get new price from request
#     # Calculate weekly change percentage
#     # Update character price
#     # Return updated price info
@app.route('/api/characters/<int:character_id>/price', methods = ['POST'])
def update_character_price(character_id):
    char = Character.query.get_or_404(character_id)

    try:
        payload = request.get_json()
        if payload is None:
            return jsonify({"error": "Missing JSON format"}),400
    except Exception:
        return jsonify({"error" : "Invalid JSON format"}), 400
    # 3. Validate the 'current_price' field exists and is a positive number
    if "current_price" not in payload:
        return jsonify({"error": "Field 'current_price' is required"}), 400

    try:
        new_price = float(payload["current_price"])
        if new_price <= 0:
            return jsonify({"error": "'current_price' must be greater than 0"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "'current_price' must be a number"}), 400

    # 4. Calculate weekly change percentage
    old_price = float(char.current_price)
    if old_price != 0:
        weekly_change = ((new_price - old_price) / old_price) * 100
    else:
        weekly_change = 0.0  # avoid division by zero

    # 5. Update the character's price and weekly change
    char.current_price = new_price
    char.weekly_change = round(weekly_change, 2)  # round to 2 decimal places

    # 6. Save the changes
    db.session.commit()

    # 7. Return updated price info
    return jsonify({
        "id": char.id,
        "name": char.name,
        "current_price": float(char.current_price),
        "weekly_change": char.weekly_change
    }), 200           

# TODO 18: MAIN EXECUTION BLOCK
# if __name__ == '__main__':
#     # Create database tables
#     # Get port and host from environment
#     # Run the Flask app
if __name__ == '__main__':
    # TEMPORARY FIX: Skip database creation for now
    # with app.app_context():
    #     db.create_all()

    # 2. Get host and port from environment variables with safe defaults
    import os
    host = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))

    # 3. Optional: Enable debug mode via environment variable
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 'yes')

    print(f"🏴‍☠️ Starting One Piece Character Service on {host}:{port}")

    # 4. Run the app
    app.run(host=host, port=port, debug=debug_mode)
"""
🎯 WHAT EACH PART DOES:

IMPORTS: Bring in the tools you need (Flask, database, validation, etc.)
CONFIG: Tell Flask how to connect to database and set security keys
MODEL: Define what a "character" looks like in the database
SCHEMA: Rules for validating data that comes from users
ENDPOINTS: Functions that handle different HTTP requests (GET, POST, etc.)
ERROR HANDLERS: What to do when things go wrong

🚀 FLASK CONCEPTS YOU'LL LEARN:

1. @app.route() - Decorator that maps URLs to functions
2. request.get_json() - Get JSON data from HTTP request
3. jsonify() - Convert Python dict to JSON response
4. db.session - Database transaction management
5. query.filter() - Database filtering
6. HTTP status codes (200, 201, 400, 404, 500)

📚 SQLALCHEMY CONCEPTS:

1. db.Model - Base class for database tables
2. db.Column() - Define table columns
3. db.Integer, db.String, db.Numeric - Data types
4. primary_key=True - Primary key column
5. nullable=False - Required field
6. default= - Default values

🔧 MARSHMALLOW CONCEPTS:

1. Schema - Data validation rules
2. fields.Str() - String validation
3. fields.Int() - Integer validation
4. required=True - Required fields
5. validate= - Custom validation functions

NEXT STEPS AFTER CODING:
1. Create .env file with your database credentials
2. Install dependencies: pip install -r requirements.txt
3. Set up MySQL database
4. Test your API endpoints

START CODING BRO! 🚀 Fill in each TODO section step by step!
"""

"""
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR COMPLETE IMPLEMENTATION CHAIN AFTER CHARACTER SERVICE
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You've completed the Character Service app.py file!

📚 WHAT YOU JUST BUILT:
✅ Flask REST API server
✅ SQLAlchemy database models
✅ Character CRUD endpoints
✅ Data validation with Marshmallow
✅ Error handling and logging
✅ CORS configuration
✅ Database connection setup
✅ JSON response formatting

🎯 YOUR NEXT IMPLEMENTATION STEPS (FOLLOW THIS EXACT ORDER):

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 1: CREATE CHARACTER MODEL (REQUIRED)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/character-service/models/character.py
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Create detailed Character database model

WHAT YOU'LL CREATE:
• Character class with all attributes
• Database relationships
• Validation methods
• Serialization methods
• Character statistics calculations

AFTER COMPLETING character.py, THAT FILE WILL TELL YOU:
→ Next file: services/character-service/models/crew.py

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 2: CREATE CREW MODEL (AFTER STEP 1)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/character-service/models/crew.py (after character.py)
⏱️ TIME: 20-30 minutes
🎯 PURPOSE: Create Crew model for character relationships

WHAT YOU'LL CREATE:
• Crew class with crew information
• One-to-many relationship with characters
• Crew statistics and aggregations
• Crew validation methods

AFTER COMPLETING crew.py, THAT FILE WILL TELL YOU:
→ Next file: services/character-service/services/character_service.py

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 3: CREATE BUSINESS LOGIC SERVICE (AFTER STEP 2)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/character-service/services/character_service.py (after crew.py)
⏱️ TIME: 45-60 minutes
🎯 PURPOSE: Create business logic layer

WHAT YOU'LL CREATE:
• Character business logic
• Search and filtering algorithms
• Character statistics calculations
• Data transformation methods
• Caching logic

AFTER COMPLETING character_service.py, THAT FILE WILL TELL YOU:
→ Next file: services/character-service/utils/database.py

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 4: CREATE DATABASE UTILITIES (AFTER STEP 3)
═══════════════════════════════════════════════════════════════════════════════

🔥 NEXT FILE: services/character-service/utils/database.py (after character_service.py)
⏱️ TIME: 20-30 minutes
🎯 PURPOSE: Create database utility functions

WHAT YOU'LL CREATE:
• Database initialization
• Connection management
• Migration utilities
• Seed data functions

AFTER COMPLETING database.py, THAT FILE WILL TELL YOU:
→ Next step: Test Character Service OR connect to API Gateway

═══════════════════════════════════════════════════════════════════════════════
📍 STEP 5: CHOOSE YOUR NEXT PATH (AFTER STEP 4)
═══════════════════════════════════════════════════════════════════════════════

🎯 OPTION A: TEST CHARACTER SERVICE (RECOMMENDED)
🔥 NEXT STEP: Test your Character Service endpoints
⏱️ TIME: 30-45 minutes
🎯 PURPOSE: Verify your Character Service works independently

🎯 OPTION B: CONNECT TO API GATEWAY
🔥 NEXT STEP: Update API Gateway to connect to Character Service
⏱️ TIME: 15-30 minutes
🎯 PURPOSE: Enable end-to-end communication

🎯 OPTION C: BUILD TRADING SERVICE
🔥 NEXT FILE: services/trading-service/Program.cs
⏱️ TIME: 3-4 hours
🎯 PURPOSE: Create C# Trading Service for high-performance trading

🎯 OPTION D: OPTIMIZE DATABASE
🔥 NEXT LEARNING MODULE: Module 3 - Database Optimization
📁 NEXT FILE: learning-modules/03-database-optimization/01-postgresql-redis-coding-lab.py
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Add caching and optimize database performance

═══════════════════════════════════════════════════════════════════════════════
🎯 RECOMMENDED IMPLEMENTATION ORDER:
═══════════════════════════════════════════════════════════════════════════════

1. ✅ services/character-service/app.py (COMPLETED)
2. 🔥 services/character-service/models/character.py (NEXT)
3. 👥 services/character-service/models/crew.py
4. 🧠 services/character-service/services/character_service.py
5. 🗄️ services/character-service/utils/database.py
6. 🧪 Test Character Service endpoints
7. 🔗 Connect to API Gateway
8. 🗄️ Database optimization (Module 3)

═══════════════════════════════════════════════════════════════════════════════
🧪 TESTS YOU SHOULD RUN FIRST:
═══════════════════════════════════════════════════════════════════════════════

□ python app.py (Start Character Service)
□ curl http://localhost:5001/api/characters (Test character list)
□ curl http://localhost:5001/api/characters/1 (Test single character)
□ curl -X POST http://localhost:5001/api/characters -d '{"name":"Test"}' (Test create)

If these work, proceed to create the model files!

═══════════════════════════════════════════════════════════════════════════════
🏴‍☠️ READY FOR THE NEXT STEP?
═══════════════════════════════════════════════════════════════════════════════

🔥 CREATE THIS FILE NEXT: services/character-service/models/character.py

This file doesn't exist yet - you need to create it! The character.py file will contain the Character database model and will tell you what to do after completing it.

🚀 Keep building your legendary One Piece trading platform! ⚔️
"""