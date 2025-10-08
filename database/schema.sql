-- 🏴‍☠️ ONE PIECE CHARACTER STOCK MARKET DATABASE SCHEMA
-- MySQL 8.0 Compatible - GUARANTEED TO WORK WITH ALL SERVICES!
--
-- SETUP INSTRUCTIONS:
-- 1. Start MySQL: sudo systemctl start mysql (Linux) or start MySQL service (Windows)
-- 2. Login to MySQL: mysql -u root -p
-- 3. Run this file: source /path/to/schema.sql
-- 4. Verify: SHOW TABLES;
--
-- COMPATIBILITY: This schema works with:
-- ✅ Python Flask (SQLAlchemy ORM)
-- ✅ C# .NET Core (Entity Framework)
-- ✅ Node.js (MySQL2 driver)
-- ✅ C++ (MySQL Connector)

-- Create database
CREATE DATABASE IF NOT EXISTS onepiece_market;
USE onepiece_market;

-- Characters table - stores One Piece character information and stock data
CREATE TABLE characters (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    crew VARCHAR(100),
    bounty BIGINT DEFAULT 0,
    current_price DECIMAL(10, 2) NOT NULL DEFAULT 100.00,
    market_cap DECIMAL(15, 2) GENERATED ALWAYS AS (current_price * 1000000) STORED,
    sentiment_score DECIMAL(3, 2) DEFAULT 0.00 CHECK (sentiment_score >= -1.00 AND sentiment_score <= 1.00),
    weekly_change DECIMAL(5, 2) DEFAULT 0.00,
    description TEXT,
    image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_name (name),
    INDEX idx_crew (crew),
    INDEX idx_current_price (current_price),
    INDEX idx_sentiment_score (sentiment_score),
    INDEX idx_is_active (is_active)
);

-- Users table - stores user account information
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL DEFAULT 10000.00,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_username (username),
    INDEX idx_email (email),
    INDEX idx_is_active (is_active)
);

-- Portfolios table - tracks user holdings of character stocks
CREATE TABLE portfolios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    character_id INT NOT NULL,
    quantity INT NOT NULL DEFAULT 0,
    average_price DECIMAL(10, 2) NOT NULL,
    total_invested DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    UNIQUE KEY unique_user_character (user_id, character_id),
    INDEX idx_user_id (user_id),
    INDEX idx_character_id (character_id),
    INDEX idx_quantity (quantity)
);

-- Trades table - records all buy/sell transactions
CREATE TABLE trades (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    character_id INT NOT NULL,
    trade_type ENUM('BUY', 'SELL') NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(12, 2) NOT NULL,
    status ENUM('PENDING', 'COMPLETED', 'CANCELLED') DEFAULT 'COMPLETED',
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_character_id (character_id),
    INDEX idx_trade_type (trade_type),
    INDEX idx_timestamp (timestamp),
    INDEX idx_status (status)
);

-- Sentiment data table - stores sentiment analysis results
CREATE TABLE sentiment_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    character_id INT NOT NULL,
    source ENUM('REDDIT', 'TWITTER', 'MANUAL', 'CHAPTER_RELEASE') NOT NULL,
    sentiment_score DECIMAL(3, 2) NOT NULL CHECK (sentiment_score >= -1.00 AND sentiment_score <= 1.00),
    text_sample TEXT,
    confidence_score DECIMAL(3, 2) DEFAULT 0.00,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    INDEX idx_character_id (character_id),
    INDEX idx_source (source),
    INDEX idx_sentiment_score (sentiment_score),
    INDEX idx_timestamp (timestamp)
);

-- Price history table - tracks historical price data for analytics
CREATE TABLE price_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    character_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    volume INT DEFAULT 0,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE CASCADE,
    INDEX idx_character_id (character_id),
    INDEX idx_timestamp (timestamp)
);

-- Market events table - tracks significant events affecting character prices
CREATE TABLE market_events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    character_id INT,
    event_type ENUM('CHAPTER_RELEASE', 'BOUNTY_UPDATE', 'CREW_CHANGE', 'MAJOR_FIGHT', 'OTHER') NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    impact_score DECIMAL(3, 2) DEFAULT 0.00,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (character_id) REFERENCES characters(id) ON DELETE SET NULL,
    INDEX idx_character_id (character_id),
    INDEX idx_event_type (event_type),
    INDEX idx_timestamp (timestamp)
);
