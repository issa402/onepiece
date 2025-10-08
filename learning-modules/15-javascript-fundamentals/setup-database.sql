-- 🏴‍☠️ ONE PIECE TRADING PLATFORM DATABASE SETUP
-- This script creates the real database tables and data for your learning modules

-- Create database (run this first)
-- CREATE DATABASE onepiece_trading;
-- CREATE USER onepiece_user WITH PASSWORD 'your_password';
-- GRANT ALL PRIVILEGES ON DATABASE onepiece_trading TO onepiece_user;

-- Connect to the database and run the rest:
-- \c onepiece_trading;

-- ============================================================================
-- 📊 CHARACTERS TABLE - Store all One Piece character data
-- ============================================================================

CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    crew VARCHAR(100) NOT NULL,
    bounty BIGINT NOT NULL,
    current_price DECIMAL(10,2) NOT NULL,
    previous_price DECIMAL(10,2) NOT NULL,
    daily_change DECIMAL(5,2) NOT NULL, -- Percentage change
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    image_url VARCHAR(255),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 👤 USERS TABLE - Store user accounts and balances
-- ============================================================================

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    balance DECIMAL(12,2) DEFAULT 10000.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
    failed_login_attempts INTEGER DEFAULT 0,
    locked_until TIMESTAMP
);

-- ============================================================================
-- 💼 PORTFOLIOS TABLE - Store user's character holdings
-- ============================================================================

CREATE TABLE IF NOT EXISTS portfolios (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    character_id INTEGER REFERENCES characters(id) ON DELETE CASCADE,
    quantity INTEGER NOT NULL DEFAULT 0,
    average_price DECIMAL(10,2) NOT NULL,
    total_invested DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, character_id)
);

-- ============================================================================
-- 💰 TRANSACTIONS TABLE - Store all trading history
-- ============================================================================

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    character_id INTEGER REFERENCES characters(id) ON DELETE CASCADE,
    action VARCHAR(10) NOT NULL CHECK (action IN ('buy', 'sell')),
    quantity INTEGER NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    total_cost DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 📋 AUDIT LOGS TABLE - Store security and activity logs
-- ============================================================================

CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    details JSONB,
    ip_address INET,
    user_agent TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 🔄 USER SESSIONS TABLE - Track active user sessions
-- ============================================================================

CREATE TABLE IF NOT EXISTS user_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    session_token VARCHAR(255) UNIQUE NOT NULL,
    last_activity TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- 📊 INSERT REAL ONE PIECE CHARACTER DATA
-- ============================================================================

INSERT INTO characters (name, crew, bounty, current_price, previous_price, daily_change, image_url, description) VALUES
('Monkey D. Luffy', 'Straw Hat Pirates', 3000000000, 150.50, 145.25, 3.61, '/images/luffy.jpg', 'Captain of the Straw Hat Pirates and future Pirate King'),
('Roronoa Zoro', 'Straw Hat Pirates', 1111000000, 89.25, 92.10, -3.09, '/images/zoro.jpg', 'Swordsman of the Straw Hat Pirates, aiming to be the world''s greatest swordsman'),
('Nami', 'Straw Hat Pirates', 366000000, 45.75, 44.20, 3.51, '/images/nami.jpg', 'Navigator of the Straw Hat Pirates and master thief'),
('Usopp', 'Straw Hat Pirates', 500000000, 62.30, 59.85, 4.09, '/images/usopp.jpg', 'Sniper of the Straw Hat Pirates and brave warrior of the sea'),
('Sanji', 'Straw Hat Pirates', 1032000000, 78.90, 81.45, -3.13, '/images/sanji.jpg', 'Cook of the Straw Hat Pirates and master of Black Leg Style'),
('Tony Tony Chopper', 'Straw Hat Pirates', 1000, 12.50, 11.80, 5.93, '/images/chopper.jpg', 'Doctor of the Straw Hat Pirates and reindeer who ate the Human-Human Fruit'),
('Nico Robin', 'Straw Hat Pirates', 930000000, 71.20, 69.55, 2.37, '/images/robin.jpg', 'Archaeologist of the Straw Hat Pirates and survivor of Ohara'),
('Franky', 'Straw Hat Pirates', 394000000, 48.65, 50.20, -3.09, '/images/franky.jpg', 'Shipwright of the Straw Hat Pirates and cyborg'),
('Brook', 'Straw Hat Pirates', 383000000, 47.80, 46.15, 3.58, '/images/brook.jpg', 'Musician of the Straw Hat Pirates and living skeleton'),
('Jinbe', 'Straw Hat Pirates', 1100000000, 85.40, 83.75, 1.97, '/images/jinbe.jpg', 'Helmsman of the Straw Hat Pirates and former Warlord'),

-- Emperors and Top Pirates
('Kaido', 'Beast Pirates', 4611100000, 245.80, 240.15, 2.35, '/images/kaido.jpg', 'Former Emperor of the Sea and strongest creature in the world'),
('Charlotte Linlin (Big Mom)', 'Big Mom Pirates', 4388000000, 238.90, 242.30, -1.40, '/images/bigmom.jpg', 'Former Emperor of the Sea and captain of Big Mom Pirates'),
('Shanks', 'Red Hair Pirates', 4048900000, 220.75, 218.40, 1.08, '/images/shanks.jpg', 'Emperor of the Sea and captain of Red Hair Pirates'),
('Marshall D. Teach (Blackbeard)', 'Blackbeard Pirates', 3996000000, 215.60, 220.85, -2.38, '/images/blackbeard.jpg', 'Emperor of the Sea with two Devil Fruit powers'),

-- Marine Admirals
('Sakazuki (Akainu)', 'Marines', 0, 180.25, 175.90, 2.47, '/images/akainu.jpg', 'Fleet Admiral of the Marines with Magma-Magma Fruit'),
('Borsalino (Kizaru)', 'Marines', 0, 165.40, 168.75, -1.98, '/images/kizaru.jpg', 'Admiral of the Marines with Light-Light Fruit'),
('Issho (Fujitora)', 'Marines', 0, 155.80, 152.30, 2.30, '/images/fujitora.jpg', 'Admiral of the Marines with Gravity-Gravity Fruit'),

-- Revolutionary Army
('Monkey D. Dragon', 'Revolutionary Army', 0, 195.50, 192.80, 1.40, '/images/dragon.jpg', 'Leader of the Revolutionary Army and most wanted man'),
('Sabo', 'Revolutionary Army', 602000000, 68.90, 66.45, 3.69, '/images/sabo.jpg', 'Chief of Staff of Revolutionary Army and Luffy''s sworn brother'),

-- Other Notable Pirates
('Trafalgar D. Water Law', 'Heart Pirates', 3000000000, 148.75, 151.20, -1.62, '/images/law.jpg', 'Captain of Heart Pirates and surgeon of death'),
('Eustass Kid', 'Kid Pirates', 3000000000, 147.30, 144.85, 1.69, '/images/kid.jpg', 'Captain of Kid Pirates with magnetic powers');

-- ============================================================================
-- 👤 INSERT TEST USER DATA
-- ============================================================================

INSERT INTO users (username, email, password_hash, balance) VALUES
('luffy_fan', 'luffy@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.Gm.F5e', 15000.00), -- password: 'strawhat123'
('zoro_master', 'zoro@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.Gm.F5e', 12500.00), -- password: 'swords123'
('nami_navigator', 'nami@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj3bp.Gm.F5e', 20000.00); -- password: 'treasure123'

-- ============================================================================
-- 💼 INSERT SAMPLE PORTFOLIO DATA
-- ============================================================================

INSERT INTO portfolios (user_id, character_id, quantity, average_price, total_invested) VALUES
(1, 1, 10, 145.00, 1450.00), -- luffy_fan owns 10 Luffy shares
(1, 2, 5, 85.50, 427.50),    -- luffy_fan owns 5 Zoro shares
(1, 3, 8, 42.25, 338.00),    -- luffy_fan owns 8 Nami shares
(2, 2, 15, 88.75, 1331.25),  -- zoro_master owns 15 Zoro shares
(2, 11, 2, 240.00, 480.00),  -- zoro_master owns 2 Kaido shares
(3, 3, 25, 43.80, 1095.00),  -- nami_navigator owns 25 Nami shares
(3, 1, 3, 148.50, 445.50);   -- nami_navigator owns 3 Luffy shares

-- ============================================================================
-- 💰 INSERT SAMPLE TRANSACTION HISTORY
-- ============================================================================

INSERT INTO transactions (user_id, character_id, action, quantity, price, total_cost) VALUES
(1, 1, 'buy', 10, 145.00, 1450.00),
(1, 2, 'buy', 5, 85.50, 427.50),
(1, 3, 'buy', 8, 42.25, 338.00),
(2, 2, 'buy', 15, 88.75, 1331.25),
(2, 11, 'buy', 2, 240.00, 480.00),
(3, 3, 'buy', 25, 43.80, 1095.00),
(3, 1, 'buy', 3, 148.50, 445.50),
(1, 3, 'sell', 2, 45.75, 91.50),
(2, 2, 'buy', 3, 89.25, 267.75);

-- ============================================================================
-- 📊 CREATE INDEXES FOR PERFORMANCE
-- ============================================================================

CREATE INDEX IF NOT EXISTS idx_characters_name ON characters(name);
CREATE INDEX IF NOT EXISTS idx_characters_crew ON characters(crew);
CREATE INDEX IF NOT EXISTS idx_characters_current_price ON characters(current_price);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_portfolios_user_id ON portfolios(user_id);
CREATE INDEX IF NOT EXISTS idx_portfolios_character_id ON portfolios(character_id);
CREATE INDEX IF NOT EXISTS idx_transactions_user_id ON transactions(user_id);
CREATE INDEX IF NOT EXISTS idx_transactions_character_id ON transactions(character_id);
CREATE INDEX IF NOT EXISTS idx_transactions_created_at ON transactions(created_at);
CREATE INDEX IF NOT EXISTS idx_audit_logs_user_id ON audit_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_audit_logs_timestamp ON audit_logs(timestamp);

-- ============================================================================
-- 🔄 CREATE FUNCTIONS FOR AUTOMATIC UPDATES
-- ============================================================================

-- Function to update portfolio when transactions occur
CREATE OR REPLACE FUNCTION update_portfolio_on_transaction()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.action = 'buy' THEN
        INSERT INTO portfolios (user_id, character_id, quantity, average_price, total_invested)
        VALUES (NEW.user_id, NEW.character_id, NEW.quantity, NEW.price, NEW.total_cost)
        ON CONFLICT (user_id, character_id)
        DO UPDATE SET
            quantity = portfolios.quantity + NEW.quantity,
            average_price = (portfolios.total_invested + NEW.total_cost) / (portfolios.quantity + NEW.quantity),
            total_invested = portfolios.total_invested + NEW.total_cost,
            updated_at = CURRENT_TIMESTAMP;
    ELSIF NEW.action = 'sell' THEN
        UPDATE portfolios
        SET quantity = quantity - NEW.quantity,
            updated_at = CURRENT_TIMESTAMP
        WHERE user_id = NEW.user_id AND character_id = NEW.character_id;
        
        -- Remove portfolio entry if quantity becomes 0
        DELETE FROM portfolios
        WHERE user_id = NEW.user_id AND character_id = NEW.character_id AND quantity <= 0;
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger for automatic portfolio updates
CREATE TRIGGER trigger_update_portfolio
    AFTER INSERT ON transactions
    FOR EACH ROW
    EXECUTE FUNCTION update_portfolio_on_transaction();

-- Function to update character prices (simulate market movement)
CREATE OR REPLACE FUNCTION simulate_price_movement()
RETURNS void AS $$
BEGIN
    UPDATE characters
    SET 
        previous_price = current_price,
        current_price = current_price * (1 + (RANDOM() - 0.5) * 0.1), -- ±5% random change
        daily_change = ((current_price * (1 + (RANDOM() - 0.5) * 0.1)) - current_price) / current_price * 100,
        last_updated = CURRENT_TIMESTAMP;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- ✅ VERIFICATION QUERIES
-- ============================================================================

-- Check if everything was created successfully
SELECT 'Characters created: ' || COUNT(*) FROM characters;
SELECT 'Users created: ' || COUNT(*) FROM users;
SELECT 'Portfolios created: ' || COUNT(*) FROM portfolios;
SELECT 'Transactions created: ' || COUNT(*) FROM transactions;

-- Show sample data
SELECT 
    c.name,
    c.crew,
    c.current_price,
    c.daily_change
FROM characters c
ORDER BY c.current_price DESC
LIMIT 5;

COMMIT;
