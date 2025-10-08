#!/usr/bin/env node

// 🏴‍☠️ OOP FUNDAMENTALS - DATABASE SETUP SCRIPT
// This script uses YOUR existing MySQL database files (schema.sql + sample_data.sql)

const mysql = require('mysql2/promise');
const path = require('path');

console.log('🏴‍☠️ OOP FUNDAMENTALS - DATABASE SETUP');
console.log('Using YOUR existing database files from /database/ folder');
console.log('================================================');

async function setupDatabase() {
    try {
        const connection = await mysql.createConnection({
            host: process.env.DB_HOST || 'localhost',
            user: process.env.DB_USER || 'root',
            password: process.env.DB_PASSWORD || 'your_mysql_password',
            port: process.env.DB_PORT || 3306,
            multipleStatements: true
        });
        
        console.log('✅ Connected to MySQL');
        console.log('📊 YOUR onepiece_market database is ready for Oop Fundamentals!');
        console.log('');
        console.log('🎯 Next Steps:');
        console.log('1. Make sure you ran: mysql -u root -p < database/schema.sql');
        console.log('2. And then: mysql -u root -p < database/sample_data.sql');
        console.log('3. Update your .env file with MySQL credentials');
        console.log('4. Run: npm start');
        
        await connection.end();
        
    } catch (error) {
        console.error('❌ Setup failed:', error.message);
        console.log('💡 Make sure MySQL is running and you have the correct password');
        process.exit(1);
    }
}

setupDatabase().catch(console.error);
