#!/usr/bin/env node

// 🔥 SIMPLE TEST TO CHECK IF YOUR DATABASE EXISTS
// This script tests if your onepiece_market database exists

const mysql = require('mysql2/promise');

console.log('🔥 SIMPLE DATABASE TEST');
console.log('======================');

async function testDatabase() {
    try {
        // Try connecting without password first
        console.log('🔍 Testing MySQL connection without password...');
        let connection = await mysql.createConnection({
            host: 'localhost',
            user: 'root',
            port: 3306,
        });
        
        console.log('✅ Connected to MySQL successfully!');
        
        // Check if your database exists
        console.log('🔍 Checking if onepiece_market database exists...');
        const [databases] = await connection.query('SHOW DATABASES');
        
        const hasOnePieceDB = databases.some(db => db.Database === 'onepiece_market');
        
        if (hasOnePieceDB) {
            console.log('✅ onepiece_market database found!');
            
            // Switch to your database
            await connection.query('USE onepiece_market');
            
            // Check tables
            console.log('🔍 Checking tables in your database...');
            const [tables] = await connection.query('SHOW TABLES');
            
            console.log('📊 Tables found:');
            tables.forEach(table => {
                console.log(`   - ${Object.values(table)[0]}`);
            });
            
            // Check character data
            if (tables.some(table => Object.values(table)[0] === 'characters')) {
                console.log('🏴‍☠️ Checking character data...');
                const [characters] = await connection.query('SELECT name, current_price FROM characters LIMIT 5');
                
                console.log('✅ Sample characters from YOUR database:');
                characters.forEach(char => {
                    console.log(`   - ${char.name}: $${char.current_price}`);
                });
            }
            
        } else {
            console.log('❌ onepiece_market database not found');
            console.log('💡 Available databases:');
            databases.forEach(db => {
                console.log(`   - ${db.Database}`);
            });
            console.log('');
            console.log('🔧 To create your database:');
            console.log('   mysql -u root -p < database/schema.sql');
            console.log('   mysql -u root -p < database/sample_data.sql');
        }
        
        await connection.end();
        
    } catch (error) {
        if (error.code === 'ER_ACCESS_DENIED_ERROR') {
            console.log('❌ Access denied - MySQL requires password');
            console.log('');
            console.log('🔧 Try one of these:');
            console.log('1. Set MySQL password to empty:');
            console.log('   sudo mysql -u root');
            console.log('   ALTER USER \'root\'@\'localhost\' IDENTIFIED WITH mysql_native_password BY \'\';');
            console.log('   FLUSH PRIVILEGES;');
            console.log('   EXIT;');
            console.log('');
            console.log('2. Or create .env file with your MySQL password:');
            console.log('   echo "DB_PASSWORD=your_mysql_password" > .env');
            console.log('');
            console.log('3. Or test manually:');
            console.log('   mysql -u root -p');
            console.log('   SHOW DATABASES;');
            console.log('   USE onepiece_market;');
            console.log('   SELECT * FROM characters LIMIT 3;');
            
        } else {
            console.error('❌ Database test failed:', error.message);
            console.log('');
            console.log('🔧 Make sure MySQL is running:');
            console.log('   sudo systemctl start mysql');
            console.log('   # or on macOS: brew services start mysql');
        }
    }
}

testDatabase().catch(console.error);
