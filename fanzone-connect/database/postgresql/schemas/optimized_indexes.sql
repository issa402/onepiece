-- 🏆 FANZONE CONNECT - DATABASE OPTIMIZATION
-- Module 03: Database Optimization - Advanced PostgreSQL Performance
-- World Cup 2026 Fan Platform - High-Performance Database Schema

-- =====================================================
-- FANZONE CONNECT DATABASE OPTIMIZATION SCHEMA
-- Designed for 5M+ concurrent users during World Cup
-- =====================================================

-- Enable required extensions for advanced features
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "btree_gin";
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";
CREATE EXTENSION IF NOT EXISTS "postgis";

-- =====================================================
-- USERS TABLE WITH OPTIMIZED INDEXES
-- =====================================================

-- Primary users table with partitioning by registration date
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    country_code CHAR(2),
    preferred_language CHAR(2) DEFAULT 'en',
    phone_number VARCHAR(20),
    date_of_birth DATE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_login TIMESTAMP WITH TIME ZONE,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    fan_level VARCHAR(20) DEFAULT 'standard' -- standard, premium, vip
) PARTITION BY RANGE (created_at);

-- Create monthly partitions for users (optimized for World Cup timeline)
CREATE TABLE users_2024 PARTITION OF users
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
CREATE TABLE users_2025 PARTITION OF users
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
CREATE TABLE users_2026 PARTITION OF users
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- High-performance indexes for users
CREATE INDEX CONCURRENTLY idx_users_email_hash ON users USING hash (email);
CREATE INDEX CONCURRENTLY idx_users_username_trgm ON users USING gin (username gin_trgm_ops);
CREATE INDEX CONCURRENTLY idx_users_country_active ON users (country_code, is_active) WHERE is_active = TRUE;
CREATE INDEX CONCURRENTLY idx_users_fan_level ON users (fan_level) WHERE fan_level IN ('premium', 'vip');
CREATE INDEX CONCURRENTLY idx_users_last_login ON users (last_login DESC) WHERE last_login IS NOT NULL;

-- =====================================================
-- EVENTS TABLE WITH GIS OPTIMIZATION
-- =====================================================

CREATE TABLE events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_type VARCHAR(50) NOT NULL, -- match, fan_fest, watch_party, cultural
    venue_id UUID NOT NULL,
    location GEOGRAPHY(POINT, 4326), -- PostGIS for geospatial queries
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    capacity INTEGER,
    current_attendees INTEGER DEFAULT 0,
    ticket_price DECIMAL(10,2),
    is_official BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (start_time);

-- Partition events by World Cup phases
CREATE TABLE events_group_stage PARTITION OF events
    FOR VALUES FROM ('2026-06-11') TO ('2026-06-27');
CREATE TABLE events_knockout PARTITION OF events
    FOR VALUES FROM ('2026-06-27') TO ('2026-07-19');

-- Geospatial and performance indexes for events
CREATE INDEX CONCURRENTLY idx_events_location_gist ON events USING gist (location);
CREATE INDEX CONCURRENTLY idx_events_time_range ON events (start_time, end_time);
CREATE INDEX CONCURRENTLY idx_events_type_official ON events (event_type, is_official);
CREATE INDEX CONCURRENTLY idx_events_venue_time ON events (venue_id, start_time);
CREATE INDEX CONCURRENTLY idx_events_capacity_ratio ON events ((current_attendees::float / capacity)) WHERE capacity > 0;

-- =====================================================
-- ACCOMMODATIONS WITH FULL-TEXT SEARCH
-- =====================================================

CREATE TABLE accommodations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    host_id UUID NOT NULL REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    accommodation_type VARCHAR(50) NOT NULL, -- hotel, airbnb, hostel, fan_house
    address TEXT NOT NULL,
    location GEOGRAPHY(POINT, 4326),
    city VARCHAR(100) NOT NULL,
    country_code CHAR(2) NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL,
    max_guests INTEGER NOT NULL,
    amenities JSONB,
    availability_calendar JSONB, -- Optimized JSON storage for calendar
    rating DECIMAL(3,2) DEFAULT 0.00,
    review_count INTEGER DEFAULT 0,
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    search_vector TSVECTOR -- Full-text search optimization
);

-- Full-text search and geospatial indexes
CREATE INDEX CONCURRENTLY idx_accommodations_search ON accommodations USING gin (search_vector);
CREATE INDEX CONCURRENTLY idx_accommodations_location ON accommodations USING gist (location);
CREATE INDEX CONCURRENTLY idx_accommodations_city_type ON accommodations (city, accommodation_type);
CREATE INDEX CONCURRENTLY idx_accommodations_price_range ON accommodations (price_per_night) WHERE price_per_night BETWEEN 50 AND 500;
CREATE INDEX CONCURRENTLY idx_accommodations_rating ON accommodations (rating DESC, review_count DESC);
CREATE INDEX CONCURRENTLY idx_accommodations_amenities ON accommodations USING gin (amenities);

-- Trigger to update search vector
CREATE OR REPLACE FUNCTION update_accommodation_search_vector()
RETURNS TRIGGER AS $$
BEGIN
    NEW.search_vector := to_tsvector('english', 
        COALESCE(NEW.title, '') || ' ' || 
        COALESCE(NEW.description, '') || ' ' || 
        COALESCE(NEW.city, '') || ' ' ||
        COALESCE(NEW.amenities::text, '')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER accommodation_search_vector_update
    BEFORE INSERT OR UPDATE ON accommodations
    FOR EACH ROW EXECUTE FUNCTION update_accommodation_search_vector();

-- =====================================================
-- BOOKINGS WITH OPTIMIZED QUERIES
-- =====================================================

CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id),
    accommodation_id UUID REFERENCES accommodations(id),
    event_id UUID REFERENCES events(id),
    booking_type VARCHAR(20) NOT NULL, -- accommodation, event, transport
    check_in_date DATE,
    check_out_date DATE,
    guests_count INTEGER NOT NULL DEFAULT 1,
    total_amount DECIMAL(10,2) NOT NULL,
    booking_status VARCHAR(20) DEFAULT 'pending', -- pending, confirmed, cancelled, completed
    payment_status VARCHAR(20) DEFAULT 'pending', -- pending, paid, refunded, failed
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
) PARTITION BY RANGE (created_at);

-- Partition bookings by month for World Cup period
CREATE TABLE bookings_2026_q2 PARTITION OF bookings
    FOR VALUES FROM ('2026-04-01') TO ('2026-07-01');
CREATE TABLE bookings_2026_q3 PARTITION OF bookings
    FOR VALUES FROM ('2026-07-01') TO ('2026-10-01');

-- Performance indexes for bookings
CREATE INDEX CONCURRENTLY idx_bookings_user_status ON bookings (user_id, booking_status);
CREATE INDEX CONCURRENTLY idx_bookings_accommodation_dates ON bookings (accommodation_id, check_in_date, check_out_date);
CREATE INDEX CONCURRENTLY idx_bookings_payment_status ON bookings (payment_status) WHERE payment_status = 'pending';
CREATE INDEX CONCURRENTLY idx_bookings_date_range ON bookings (check_in_date, check_out_date);

-- =====================================================
-- ANALYTICS MATERIALIZED VIEWS
-- =====================================================

-- Real-time analytics for World Cup dashboard
CREATE MATERIALIZED VIEW fan_analytics_summary AS
SELECT 
    DATE_TRUNC('hour', created_at) as hour,
    country_code,
    fan_level,
    COUNT(*) as user_count,
    COUNT(*) FILTER (WHERE is_active = TRUE) as active_users,
    COUNT(*) FILTER (WHERE last_login > NOW() - INTERVAL '24 hours') as daily_active
FROM users 
WHERE created_at >= '2026-01-01'
GROUP BY DATE_TRUNC('hour', created_at), country_code, fan_level;

CREATE UNIQUE INDEX ON fan_analytics_summary (hour, country_code, fan_level);

-- Booking revenue analytics
CREATE MATERIALIZED VIEW booking_revenue_summary AS
SELECT 
    DATE_TRUNC('day', created_at) as day,
    booking_type,
    booking_status,
    COUNT(*) as booking_count,
    SUM(total_amount) as total_revenue,
    AVG(total_amount) as avg_booking_value
FROM bookings 
WHERE created_at >= '2026-01-01'
GROUP BY DATE_TRUNC('day', created_at), booking_type, booking_status;

CREATE UNIQUE INDEX ON booking_revenue_summary (day, booking_type, booking_status);

-- =====================================================
-- PERFORMANCE MONITORING
-- =====================================================

-- Function to refresh materialized views
CREATE OR REPLACE FUNCTION refresh_analytics_views()
RETURNS void AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY fan_analytics_summary;
    REFRESH MATERIALIZED VIEW CONCURRENTLY booking_revenue_summary;
END;
$$ LANGUAGE plpgsql;

-- Schedule analytics refresh every 15 minutes during World Cup
-- (This would be handled by a cron job or scheduler in production)
