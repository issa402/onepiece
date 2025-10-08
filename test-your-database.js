#!/usr/bin/env node

// 🔥 TEST YOUR REAL DATABASE CONNECTION AND DATA
// This script tests YOUR actual onepiece_market MySQL database

require('dotenv').config();
const mysql = require('mysql2/promise');

console.log('🔥 TESTING YOUR REAL ONEPIECE_MARKET DATABASE');
console.log('==============================================');
console.log('🎯 Using YOUR existing database files:');
console.log('   📁 database/schema.sql');
console.log('   📁 database/sample_data.sql');
console.log('');

// Database configuration (using YOUR MySQL setup)
const dbConfig = {
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || 'your_mysql_password',
    database: process.env.DB_NAME || 'onepiece_market',
    port: process.env.DB_PORT || 3306,
};

async function testYourDatabase() {
    let connection;
    
    try {
        console.log('🔍 Connecting to YOUR MySQL database...');
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
            SELECT 
                id,
                name, 
                crew, 
                bounty,
                current_price, 
                market_cap,
                sentiment_score, 
                weekly_change,
                is_active
            FROM characters 
            WHERE is_active = TRUE
            ORDER BY current_price DESC 
            LIMIT 10
        `);
        
        if (charactersResult.length > 0) {
            console.log(`✅ Found ${charactersResult.length} characters in YOUR database:`);
            console.log('');
            console.log('🏆 TOP 10 MOST VALUABLE CHARACTERS (from YOUR sample_data.sql):');
            charactersResult.forEach((char, index) => {
                const sentimentIcon = char.sentiment_score > 0 ? '📈' : '📉';
                const changeIcon = char.weekly_change >= 0 ? '⬆️' : '⬇️';
                console.log(`   ${index + 1}. ${sentimentIcon} ${char.name}`);
                console.log(`      Crew: ${char.crew}`);
                console.log(`      Price: $${char.current_price}`);
                console.log(`      Bounty: ¥${char.bounty.toLocaleString()}`);
                console.log(`      Market Cap: $${char.market_cap.toLocaleString()}`);
                console.log(`      Sentiment: ${char.sentiment_score} ${char.sentiment_score > 0 ? '(Bullish)' : '(Bearish)'}`);
                console.log(`      Weekly Change: ${changeIcon}${char.weekly_change}%`);
                console.log('');
            });
        } else {
            console.log('❌ No character data found. Run setup first:');
            console.log('   mysql -u root -p < database/schema.sql');
            console.log('   mysql -u root -p < database/sample_data.sql');
        }
        
        // Test users table
        console.log('👥 Testing users data from YOUR database...');
        const [usersResult] = await connection.query(`
            SELECT id, username, email, balance, first_name, last_name
            FROM users 
            LIMIT 5
        `);
        
        if (usersResult.length > 0) {
            console.log(`✅ Found ${usersResult.length} users in YOUR database:`);
            usersResult.forEach((user, index) => {
                console.log(`   ${index + 1}. ${user.username} (${user.first_name} ${user.last_name})`);
                console.log(`      Email: ${user.email}`);
                console.log(`      Balance: $${user.balance.toLocaleString()}`);
                console.log('');
            });
        } else {
            console.log('❌ No user data found.');
        }
        
        // Test specific characters that should exist in YOUR sample_data.sql
        console.log('🎯 Testing specific characters from YOUR sample_data.sql...');
        
        const expectedCharacters = [
            { id: 1, name: 'Monkey D. Luffy', price: 150.00, bounty: 3000000000 },
            { id: 2, name: 'Roronoa Zoro', price: 120.00, bounty: 1111000000 },
            { id: 3, name: 'Nami', price: 95.00, bounty: 366000000 },
            { id: 24, name: 'Shanks', price: 220.00, bounty: 4048900000 }
        ];
        
        for (const expected of expectedCharacters) {
            try {
                const [charResult] = await connection.query(
                    'SELECT * FROM characters WHERE id = ?', 
                    [expected.id]
                );
                
                if (charResult.length > 0) {
                    const char = charResult[0];
                    const priceMatch = Math.abs(char.current_price - expected.price) < 0.01;
                    const bountyMatch = char.bounty == expected.bounty;
                    
                    console.log(`   ${priceMatch && bountyMatch ? '✅' : '⚠️'} Character ${expected.id}:`);
                    console.log(`      Expected: ${expected.name} - $${expected.price} - ¥${expected.bounty.toLocaleString()}`);
                    console.log(`      Found: ${char.name} - $${char.current_price} - ¥${char.bounty.toLocaleString()}`);
                    
                    if (!priceMatch) {
                        console.log(`      ⚠️ Price mismatch: expected $${expected.price}, got $${char.current_price}`);
                    }
                    if (!bountyMatch) {
                        console.log(`      ⚠️ Bounty mismatch: expected ¥${expected.bounty.toLocaleString()}, got ¥${char.bounty.toLocaleString()}`);
                    }
                } else {
                    console.log(`   ❌ Character ${expected.id} (${expected.name}) not found`);
                }
            } catch (error) {
                console.log(`   ❌ Error checking character ${expected.id}: ${error.message}`);
            }
        }
        
        console.log('');
        console.log('🎉 DATABASE TEST COMPLETED!');
        console.log('');
        console.log('🎯 Next Steps:');
        console.log('1. If all tests passed, your database is ready!');
        console.log('2. Go to learning-modules/15-javascript-fundamentals/');
        console.log('3. Run: npm install');
        console.log('4. Run: node 01-js-mastery-coding-lab.js');
        console.log('5. You should see REAL data from YOUR database!');
        console.log('');
        console.log('🏴‍☠️ YOUR ONEPIECE_MARKET DATABASE IS READY FOR LEARNING! ⚔️');
        
    } catch (error) {
        console.error('❌ Database test failed:', error.message);
        console.log('');
        console.log('🔧 TROUBLESHOOTING:');
        
        if (error.code === 'ECONNREFUSED') {
            console.log('1. Make sure MySQL is running:');
            console.log('   sudo systemctl start mysql');
            console.log('   # or on macOS: brew services start mysql');
        } else if (error.code === 'ER_ACCESS_DENIED_ERROR') {
            console.log('1. Check your MySQL password:');
            console.log('   Update DB_PASSWORD in your .env file');
            console.log('   Or reset MySQL root password if needed');
        } else if (error.code === 'ER_BAD_DB_ERROR') {
            console.log('1. Database does not exist. Create it:');
            console.log('   mysql -u root -p < database/schema.sql');
            console.log('   mysql -u root -p < database/sample_data.sql');
        } else {
            console.log('1. Check your database configuration');
            console.log('2. Make sure MySQL is running');
            console.log('3. Verify your .env file settings');
        }
        
        console.log('');
        console.log('💡 Manual test:');
        console.log('   mysql -u root -p');
        console.log('   USE onepiece_market;');
        console.log('   SELECT COUNT(*) FROM characters;');
        console.log('   SELECT name, current_price FROM characters LIMIT 5;');
        
        process.exit(1);
    } finally {
        if (connection) {
            await connection.end();
        }
    }
}

// Run the test
testYourDatabase().catch(console.error);
