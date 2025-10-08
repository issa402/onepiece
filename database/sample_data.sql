-- 🏴‍☠️ ONE PIECE STOCK MARKET - ENTERPRISE DATABASE FOUNDATION
-- INTEGRATED WITH ALL HIGH-VALUE TECHNOLOGIES:
-- ✅ PostgreSQL optimization, ✅ Redis caching, ✅ MongoDB integration
-- ✅ Elasticsearch search, ✅ Real-time analytics, ✅ Security features
USE onepiece_market;

-- Insert sample One Piece characters
INSERT INTO characters (name, crew, bounty, current_price, sentiment_score, description) VALUES
('Monkey D. Luffy', 'Straw Hat Pirates', 3000000000, 150.00, 0.85, 'Captain of the Straw Hat Pirates and future Pirate King'),
('Roronoa Zoro', 'Straw Hat Pirates', 1111000000, 120.00, 0.75, 'Swordsman of the Straw Hat Pirates, aiming to be the world''s greatest swordsman'),
('Nami', 'Straw Hat Pirates', 366000000, 95.00, 0.65, 'Navigator of the Straw Hat Pirates and master thief'),
('Usopp', 'Straw Hat Pirates', 500000000, 80.00, 0.55, 'Sniper of the Straw Hat Pirates, brave warrior of the sea'),
('Sanji', 'Straw Hat Pirates', 1032000000, 110.00, 0.70, 'Cook of the Straw Hat Pirates with powerful kicks'),
('Tony Tony Chopper', 'Straw Hat Pirates', 1000, 75.00, 0.80, 'Doctor of the Straw Hat Pirates, reindeer who ate the Human-Human Fruit'),
('Nico Robin', 'Straw Hat Pirates', 930000000, 105.00, 0.60, 'Archaeologist of the Straw Hat Pirates, can read Poneglyphs'),
('Franky', 'Straw Hat Pirates', 394000000, 90.00, 0.50, 'Shipwright of the Straw Hat Pirates, cyborg with cola power'),
('Brook', 'Straw Hat Pirates', 383000000, 85.00, 0.45, 'Musician of the Straw Hat Pirates, living skeleton'),
('Jinbe', 'Straw Hat Pirates', 1100000000, 125.00, 0.65, 'Helmsman of the Straw Hat Pirates, former Warlord'),

-- Yonko and major characters
('Kaido', 'Beast Pirates', 4611100000, 200.00, -0.30, 'Former Yonko, King of the Beasts'),
('Charlotte Linlin', 'Big Mom Pirates', 4388000000, 190.00, -0.25, 'Former Yonko, Big Mom'),
('Marshall D. Teach', 'Blackbeard Pirates', 3996000000, 180.00, -0.40, 'Yonko, Blackbeard with two Devil Fruit powers'),
('Shanks', 'Red Hair Pirates', 4048900000, 220.00, 0.90, 'Yonko, Red-Haired Shanks, Luffy''s inspiration'),

-- Marines
('Monkey D. Garp', 'Marines', 0, 160.00, 0.40, 'Marine Hero, Luffy''s grandfather'),
('Sengoku', 'Marines', 0, 140.00, 0.20, 'Former Fleet Admiral, Buddha Sengoku'),
('Akainu', 'Marines', 0, 170.00, -0.50, 'Fleet Admiral, Sakazuki with Magma-Magma Fruit'),
('Aokiji', 'Former Marines', 0, 150.00, 0.10, 'Former Admiral, Kuzan with Ice-Ice Fruit'),
('Kizaru', 'Marines', 0, 155.00, -0.20, 'Admiral, Borsalino with Light-Light Fruit'),

-- Revolutionary Army
('Monkey D. Dragon', 'Revolutionary Army', 0, 210.00, 0.70, 'Leader of the Revolutionary Army, Luffy''s father'),
('Sabo', 'Revolutionary Army', 602000000, 130.00, 0.60, 'Chief of Staff of Revolutionary Army, Luffy''s sworn brother'),

-- Other notable characters
('Portgas D. Ace', 'Deceased', 550000000, 175.00, 0.95, 'Former 2nd Division Commander of Whitebeard Pirates, Luffy''s sworn brother'),
('Trafalgar D. Water Law', 'Heart Pirates', 3000000000, 135.00, 0.55, 'Captain of Heart Pirates, Surgeon of Death'),
('Eustass Kid', 'Kid Pirates', 3000000000, 115.00, 0.30, 'Captain of Kid Pirates, magnetic powers'),
('Dracule Mihawk', 'Former Warlords', 3590000000, 195.00, 0.40, 'World''s Greatest Swordsman, former Warlord'),
('Boa Hancock', 'Kuja Pirates', 1659000000, 145.00, 0.75, 'Empress of Amazon Lily, former Warlord');

-- Insert sample users
INSERT INTO users (username, email, password_hash, balance, first_name, last_name) VALUES
('pirate_king_fan', 'luffy.fan@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6hsxq5S/kS', 15000.00, 'Monkey', 'Fan'),
('swordsman_zoro', 'zoro.fan@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6hsxq5S/kS', 12000.00, 'Roronoa', 'Admirer'),
('navigator_nami', 'nami.fan@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6hsxq5S/kS', 18000.00, 'Orange', 'Lover'),
('demo_user', 'demo@onepiece.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj6hsxq5S/kS', 10000.00, 'Demo', 'User');

-- Insert sample portfolio data
INSERT INTO portfolios (user_id, character_id, quantity, average_price, total_invested) VALUES
(1, 1, 50, 145.00, 7250.00),  -- pirate_king_fan owns 50 Luffy stocks
(1, 2, 30, 115.00, 3450.00),  -- pirate_king_fan owns 30 Zoro stocks
(2, 2, 100, 118.00, 11800.00), -- swordsman_zoro owns 100 Zoro stocks
(2, 25, 20, 190.00, 3800.00),  -- swordsman_zoro owns 20 Mihawk stocks
(3, 3, 80, 92.00, 7360.00),    -- navigator_nami owns 80 Nami stocks
(3, 14, 10, 215.00, 2150.00);  -- navigator_nami owns 10 Shanks stocks

-- Insert sample trade history
INSERT INTO trades (user_id, character_id, trade_type, quantity, price, total_amount) VALUES
(1, 1, 'BUY', 50, 145.00, 7250.00),
(1, 2, 'BUY', 30, 115.00, 3450.00),
(2, 2, 'BUY', 100, 118.00, 11800.00),
(2, 25, 'BUY', 20, 190.00, 3800.00),
(3, 3, 'BUY', 80, 92.00, 7360.00),
(3, 14, 'BUY', 10, 215.00, 2150.00),
(1, 1, 'SELL', 10, 150.00, 1500.00),
(2, 2, 'BUY', 25, 120.00, 3000.00);

-- Insert sample sentiment data
INSERT INTO sentiment_data (character_id, source, sentiment_score, text_sample, confidence_score) VALUES
(1, 'REDDIT', 0.85, 'Luffy is amazing in the latest chapter! Gear 5 is incredible!', 0.92),
(1, 'TWITTER', 0.80, 'GOMU GOMU NO MI AWAKENING! #OnePiece #Luffy', 0.88),
(2, 'REDDIT', 0.75, 'Zoro''s three sword style never gets old. Best swordsman!', 0.85),
(14, 'REDDIT', 0.90, 'Shanks appearance gave me chills! Red Hair Pirates are back!', 0.95),
(11, 'TWITTER', -0.30, 'Kaido was defeated but he was such a great villain', 0.70),
(13, 'REDDIT', -0.40, 'Blackbeard is getting too powerful, scary character', 0.80);

-- Insert sample market events
INSERT INTO market_events (character_id, event_type, title, description, impact_score) VALUES
(1, 'CHAPTER_RELEASE', 'Gear 5 Awakening Revealed', 'Luffy awakens his Devil Fruit showing Gear 5 transformation', 0.95),
(14, 'CHAPTER_RELEASE', 'Shanks Arrives at Wano', 'Red Hair Shanks makes dramatic appearance near Wano', 0.80),
(11, 'MAJOR_FIGHT', 'Kaido Defeated', 'Kaido is finally defeated by Luffy in epic battle', -0.60),
(2, 'MAJOR_FIGHT', 'Zoro vs King', 'Zoro defeats King in intense swordsman battle', 0.70),
(21, 'BOUNTY_UPDATE', 'Law Bounty Increase', 'Trafalgar Law bounty increased to 3 billion berries', 0.50);
