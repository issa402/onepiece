#!/usr/bin/env node

// 🏴‍☠️ ONE PIECE TRADING PLATFORM - DATABASE CONNECTION TEST
// This script tests YOUR real MySQL database connection

require('dotenv').config();
const mysql = require('mysql2/promise');

console.log('🏴‍☠️ ONE PIECE TRADING PLATFORM - DATABASE TEST');
console.log('Testing YOUR existing onepiece_market MySQL database');
console.log('==============================================');

// Database configuration (using YOUR MySQL setup)
const dbConfig = {
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || 'your_mysql_password',
    database: process.env.DB_NAME || 'onepiece_market',
    port: process.env.DB_PORT || 3306,
};

async function testDatabaseConnection() {
    let connection;

    try {
        console.log('🔍 Testing MySQL connection...');
        console.log(`   Host: ${dbConfig.host}:${dbConfig.port}`);
        console.log(`   Database: ${dbConfig.database}`);
        console.log(`   User: ${dbConfig.user}`);
        console.log('');

        // Test basic connection
        connection = await mysql.createConnection(dbConfig);
        const [timeResult] = await connection.query('SELECT NOW() as current_time');
        console.log('✅ MySQL connection successful!');
        console.log(`   Current time: ${timeResult[0].current_time}`);
        console.log('');
        
        // Test character data from YOUR database
        console.log('🏴‍☠️ Testing character data from YOUR onepiece_market database...');
        const [charactersResult] = await connection.query(`
            SELECT name, crew, current_price, sentiment_score, weekly_change
            FROM characters
            WHERE is_active = TRUE
            ORDER BY current_price DESC
            LIMIT 3
        `);

        if (charactersResult.length > 0) {
            console.log('✅ Character data found in YOUR database:');
            charactersResult.forEach(char => {
                const sentimentIcon = char.sentiment_score > 0 ? '📈' : '📉';
                const changeIcon = char.weekly_change >= 0 ? '⬆️' : '⬇️';
                console.log(`   ${sentimentIcon} ${char.name} (${char.crew}): $${char.current_price} ${changeIcon}${char.weekly_change}%`);
            });
        } else {
            console.log('❌ No character data found. Run setup first: npm run setup');
        }
        console.log('');
        
        // Test user data
        console.log('👤 Testing user data...');
        const usersResult = await pool.execute('SELECT username, balance FROM users LIMIT 3');
        
        if (usersResult.rows.length > 0) {
            console.log('✅ User data found:');
            usersResult.rows.forEach(user => {
                console.log(`   💰 ${user.username}: $${user.balance}`);
            });
        } else {
            console.log('❌ No user data found. Run setup first: npm run setup');
        }
        console.log('');
        
        // Test portfolio data
        console.log('💼 Testing portfolio data...');
        const portfolioResult = await pool.execute(`
            SELECT 
                u.username,
                c.name as character_name,
                p.quantity,
                (p.quantity * c.current_price) as current_value
            FROM portfolios p
            JOIN users u ON p.user_id = u.id
            JOIN characters c ON p.character_id = c.id
            LIMIT 3
        `);
        
        if (portfolioResult.rows.length > 0) {
            console.log('✅ Portfolio data found:');
            portfolioResult.rows.forEach(portfolio => {
                console.log(`   📊 ${portfolio.username} owns ${portfolio.quantity} ${portfolio.character_name} shares (Value: $${portfolio.current_value})`);
            });
        } else {
            console.log('❌ No portfolio data found. Run setup first: npm run setup');
        }
        console.log('');
        
        // Test a real query like the learning module uses
        console.log('🔍 Testing learning module query...');
        const testQuery = `
            SELECT 
                c.id,
                c.name,
                c.crew,
                c.bounty,
                c.current_price,
                c.current_price,
                c.weekly_change,
                c.updated_at,
                COALESCE(p.quantity, 0) as owned_quantity,
                (c.current_price * COALESCE(p.quantity, 0)) as portfolio_value
            FROM characters c
            LEFT JOIN portfolios p ON c.id = p.character_id AND p.user_id = ?
            WHERE c.id = ?
        `;
        
        const testResult = await pool.execute(testQuery, [1, 1]); // user_id=1, character_id=1
        
        if (testResult.rows.length > 0) {
            const char = testResult.rows[0];
            console.log('✅ Learning module query successful:');
            console.log(`   📊 Character: ${char.name} from ${char.crew}`);
            console.log(`   💰 Current Price: $${char.current_price}`);
            console.log(`   🏴‍☠️ Bounty: ¥${char.bounty.toLocaleString()}`);
            console.log(`   👤 Owned: ${char.owned_quantity} shares`);
            console.log(`   💎 Portfolio value: $${char.portfolio_value}`);
        } else {
            console.log('❌ Learning module query failed. Check your data.');
        }
        console.log('');
        
        console.log('🎯 Database test completed successfully!');
        console.log('');
        console.log('✅ Your database is ready for the learning modules!');
        console.log('   Run: node 01-js-mastery-coding-lab.js');
        
    } catch (error) {
        console.error('❌ Database test failed:', error.message);
        
        if (error.code === 'ECONNREFUSED') {
            console.log('\n🔧 MySQL is not running. Start it with:');
            console.log('   sudo systemctl start mysqlql');
            console.log('   # or on macOS: brew services start mysqlql');
        } else if (error.code === '3D000') {
            console.log('\n🔧 Database does not exist. Run setup first:');
            console.log('   npm run setup');
        } else if (error.code === '28P01') {
            console.log('\n🔧 Authentication failed. Check your credentials in .env file');
        } else if (error.code === '42P01') {
            console.log('\n🔧 Tables do not exist. Run setup first:');
            console.log('   npm run setup');
        }
        
        process.exit(1);
    } finally {
        await pool.end();
    }
}

// Run the test
testDatabaseConnection().catch(console.error);
