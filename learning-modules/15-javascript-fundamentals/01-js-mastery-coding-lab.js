/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - JAVASCRIPT FUNDAMENTALS + OOP MASTERY
===============================================================================

🎯 WHAT YOU'LL LEARN IN THIS LAB (FROM ABSOLUTE SCRATCH):

📚 PART 1: JAVASCRIPT FUNDAMENTALS FROM ZERO
   - What variables are and why we need different types (const, let, var)
   - How functions work and why they're essential for reusable code
   - Objects and arrays for organizing complex data
   - Template literals for clean string formatting
   - Why we don't hardcode data and how to connect to databases

⚡ PART 2: ASYNCHRONOUS PROGRAMMING (THE HARD STUFF EXPLAINED)
   - What callbacks are and why they exist (functions that run later)
   - The callback hell problem and why it's terrible for maintenance
   - Promises as the solution to callback hell
   - Async/await as the modern, clean approach
   - Real database connections instead of YOUR real MySQL database

🏗️ PART 3: OBJECT-ORIENTED PROGRAMMING (PROFESSIONAL CODE)
   - Classes as blueprints for creating objects
   - Encapsulation to keep data private and secure
   - Inheritance to reuse and extend functionality
   - Polymorphism for flexible, maintainable code
   - Design patterns used in real companies

🗄️ PART 4: DATABASE INTEGRATION (USING YOUR REAL DATABASE)
   - MySQL with mysql2 library (YOUR onepiece_market database)
   - Connection pooling for performance and scalability
   - Real queries to YOUR schema.sql and sample_data.sql files
   - Why professional apps never hardcode data - always use databases

💰 SALARY IMPACT: ?0K → ?20K+ (Junior to Staff Engineer)
🏢 COMPANIES: Google, Meta, Netflix, Stripe, Goldman Sachs

===============================================================================
*/

console.log('🏴‍☠️ ONE PIECE TRADING PLATFORM - JAVASCRIPT MASTERY LAB');
console.log('===============================================================================');

// ============================================================================
// 📚 SECTION 1: JAVASCRIPT FUNDAMENTALS FROM ABSOLUTE SCRATCH
// ============================================================================

console.log('\n📚 SECTION 1: JAVASCRIPT FUNDAMENTALS FROM ABSOLUTE SCRATCH');
console.log('----------------------------------------------------------');

/*
🤔 WHAT IS JAVASCRIPT?
JavaScript is the programming language that runs in web browsers. It's the ONLY
language that can run directly in browsers, making it essential for web development.

🤔 WHY LEARN JAVASCRIPT?
- 95% of websites use JavaScript
- It's required for React, Node.js, and modern web development
- High-paying jobs ($80K-?00K+) require JavaScript skills
- You can build full-stack applications with just JavaScript

🤔 HOW DOES THIS CONNECT TO YOUR ONE PIECE PROJECT?
- Your CharacterList.tsx uses JavaScript (TypeScript is JavaScript with types)
- Your Flask backend will be replaced with Node.js (JavaScript on the server)
- Real-time price updates need JavaScript WebSockets
- Trading algorithms will be written in JavaScript
*/

// 🔥 Variables: Storing and Managing Data
console.log('\n🔥 1.1 Variables - How to Store Data:');

/*
🤔 WHAT ARE VARIABLES?
Variables are containers that store data values. Think of them like labeled boxes
where you can put different types of information.

🤔 WHY DO WE NEED DIFFERENT VARIABLE TYPES?
- const: For values that never change (like PI = 3.14159, API URLs)
- let: For values that can change (like a user's current score, character health)
- var: Old way, avoid using it (has confusing scoping rules that cause bugs)

🤔 REAL-WORLD EXAMPLE:
In your trading platform, character bounties change over time (let), but the
character's name never changes (const).
*/

// ❌ OLD WAY (var - confusing and error-prone)
console.log('❌ OLD WAY (var - causes bugs):');
var oldCharacterName = 'Luffy';
var oldCharacterName = 'Zoro'; // This overwrites without warning! Bug-prone!
console.log('Old var way:', oldCharacterName);

// ✅ MODERN WAY (const for constants, let for variables)
console.log('\n✅ MODERN WAY (const/let - safe and clear):');
const PIRATE_KING_BOUNTY = 5000000000; // This can NEVER change
let currentCharacterBounty = 3000000000; // This CAN change

console.log('Constant Pirate King bounty:', PIRATE_KING_BOUNTY);
console.log('Current character bounty:', currentCharacterBounty);

// You can change let variables
currentCharacterBounty = 3500000000; // Bounty increased!
console.log('Updated bounty:', currentCharacterBounty);

// But you CANNOT change const variables (this would cause an error):
// PIRATE_KING_BOUNTY = 6000000000; // ❌ This would crash the program!

// 🔥 Data Types: Different Kinds of Information
console.log('\n🔥 1.2 Data Types - Different Kinds of Information:');

/*
🤔 WHAT ARE DATA TYPES?
Data types tell JavaScript what kind of information you're storing.
Different types have different capabilities and uses.

🤔 WHY DO DATA TYPES MATTER?
- String: For text (character names, crew names)
- Number: For numeric calculations (bounties, ages, prices)
- Boolean: For true/false decisions (is character alive? is user logged in?)
- Array: For lists of items (crew members, trading history)
- Object: For complex data with multiple properties (character profile)
*/

// String: Text data
const characterName = 'Monkey D. Luffy'; // Text in quotes
console.log('String (text):', characterName, '- Type:', typeof characterName);

// Number: Numeric data
const bountyAmount = 3000000000; // Numbers without quotes
console.log('Number:', bountyAmount, '- Type:', typeof bountyAmount);

// Boolean: True/false data
const isStrawHat = true; // true or false
console.log('Boolean:', isStrawHat, '- Type:', typeof isStrawHat);

// Array: List of items
const crewMembers = ['Luffy', 'Zoro', 'Nami', 'Usopp', 'Sanji'];
console.log('Array (list):', crewMembers, '- Length:', crewMembers.length);

// Object: Complex data with properties
const character = {
    name: 'Monkey D. Luffy',
    age: 19,
    crew: 'Straw Hat Pirates',
    bounty: 3000000000,
    devilFruit: 'Gomu Gomu no Mi',
    isAlive: true,
    abilities: ['Gear Second', 'Gear Third', 'Gear Fourth']
};
console.log('Object (complex data):', character);

// 🔥 Template Literals: Modern String Formatting
console.log('\n🔥 1.3 Template Literals - Clean String Formatting:');

/*
🤔 WHAT ARE TEMPLATE LITERALS?
Template literals are a modern way to create strings that can include variables
and expressions. They use backticks (`) instead of quotes.

🤔 WHY USE TEMPLATE LITERALS?
- Cleaner than string concatenation (no more + + + everywhere)
- Can span multiple lines (great for HTML or formatted text)
- Can include expressions and calculations
- More readable and maintainable
- Used everywhere in modern JavaScript

🤔 REAL-WORLD EXAMPLE:
In your trading platform, you'll create user notifications, character profiles,
trading summaries - all use template literals for clean formatting.
*/

// ❌ OLD WAY (string concatenation - messy and error-prone)
console.log('❌ OLD WAY (string concatenation - messy):');
const oldMessage = 'Character: ' + character.name + 
                  ', Bounty: ' + character.bounty + 
                  ', Crew: ' + character.crew;
console.log(oldMessage);

// ✅ MODERN WAY (template literals - clean and readable)
console.log('\n✅ MODERN WAY (template literals - clean):');
const modernMessage = `
🏴‍☠️ CHARACTER PROFILE:
   Name: ${character.name}
   Age: ${character.age} years old
   Crew: ${character.crew}
   Bounty: ¥${character.bounty.toLocaleString()}
   Devil Fruit: ${character.devilFruit}
   Status: ${character.isAlive ? 'Alive' : 'Dead'}
   Bounty Category: ${character.bounty > 1000000000 ? 'Super High' : 'High'}
   Abilities: ${character.abilities.join(', ')}
`;
console.log(modernMessage);

// 🔥 Functions: Reusable Blocks of Code
console.log('\n🔥 1.4 Functions - Reusable Code Blocks:');

/*
🤔 WHAT ARE FUNCTIONS?
Functions are reusable blocks of code that perform specific tasks.
Think of them like recipes - you write the recipe once, then use it many times.

🤔 WHY USE FUNCTIONS?
- Avoid repeating code (DRY principle: Don't Repeat Yourself)
- Make code more organized and readable
- Easier to test and debug
- Can be reused throughout your application
- Essential for professional development

🤔 REAL-WORLD EXAMPLE:
In your trading platform, you'll have functions for:
- Calculating bounty increases
- Formatting currency displays
- Validating user input
- Processing trading transactions
*/

// ❌ WITHOUT FUNCTIONS (repetitive and hard to maintain)
console.log('❌ WITHOUT FUNCTIONS (repetitive code):');
let luffyBounty = 3000000000;
let luffyFormattedBounty = '¥' + luffyBounty.toLocaleString();
console.log('Luffy bounty:', luffyFormattedBounty);

let zoroBounty = 1111000000;
let zoroFormattedBounty = '¥' + zoroBounty.toLocaleString();
console.log('Zoro bounty:', zoroFormattedBounty);
// Imagine doing this for 100+ characters... nightmare!

// ✅ WITH FUNCTIONS (reusable and maintainable)
console.log('\n✅ WITH FUNCTIONS (reusable code):');

// Function declaration (traditional way)
function formatBounty(bountyAmount) {
    return '¥' + bountyAmount.toLocaleString();
}

// Arrow function (modern way - more concise)
const calculateNewBounty = (currentBounty, multiplier) => {
    return currentBounty * multiplier;
};

// Using the functions (much cleaner!)
console.log('Luffy bounty:', formatBounty(3000000000));
console.log('Zoro bounty:', formatBounty(1111000000));
console.log('Luffy new bounty:', formatBounty(calculateNewBounty(3000000000, 1.5)));

// Functions with multiple parameters and complex logic
const createCharacterProfile = (name, crew, bounty, devilFruit = 'None') => {
    const profile = {
        name: name,
        crew: crew,
        bounty: bounty,
        devilFruit: devilFruit,
        formattedBounty: formatBounty(bounty),
        threatLevel: bounty > 1000000000 ? 'Extremely Dangerous' : 
                    bounty > 500000000 ? 'Very Dangerous' : 
                    bounty > 100000000 ? 'Dangerous' : 'Low Threat',
        canDefeatMarines: bounty > 500000000,
        estimatedStrength: Math.floor(bounty / 100000000)
    };
    
    return profile;
};

// Using the complex function
const luffyProfile = createCharacterProfile('Monkey D. Luffy', 'Straw Hat Pirates', 3000000000, 'Gomu Gomu no Mi');
const namiProfile = createCharacterProfile('Nami', 'Straw Hat Pirates', 366000000); // No devil fruit

console.log('\n🏴‍☠️ Character Profiles Created with Functions:');
console.log(luffyProfile);
console.log(namiProfile);

// ============================================================================
// ⚡ SECTION 2: ASYNCHRONOUS PROGRAMMING (THE HARD STUFF EXPLAINED)
// ============================================================================

console.log('\n\n⚡ SECTION 2: ASYNCHRONOUS PROGRAMMING (THE HARD STUFF EXPLAINED)');
console.log('----------------------------------------------------------------');

/*
🤔 WHAT IS ASYNCHRONOUS PROGRAMMING?
Asynchronous programming is a way to handle operations that take time (like
fetching data from a database or API) without freezing your entire application.

🤔 WHY IS THIS IMPORTANT?
- Web applications need to handle multiple users simultaneously
- Database queries take time - you can't freeze the app while waiting
- API calls to other services take time
- File operations take time
- User interactions happen at unpredictable times

🤔 REAL-WORLD EXAMPLE:
When a user clicks "Buy Character Stock" in your trading platform:
1. Check user's balance (database query - takes time)
2. Verify character exists (API call - takes time)
3. Process payment (external service - takes time)
4. Update portfolio (database update - takes time)
5. Send confirmation email (email service - takes time)

Without async programming, your app would freeze for several seconds!

🤔 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
- Your CharacterList.tsx already uses async/await for API calls
- Your Flask backend will be replaced with Node.js using async patterns
- Real-time price updates need WebSocket connections (async)
- Database operations are all asynchronous
*/

// 🔥 Understanding Callbacks (The Foundation)
console.log('\n🔥 2.1 Callbacks - Functions That Run Later:');

/*
🤔 WHAT IS A CALLBACK?
A callback is a function that gets passed to another function to be executed
later, usually after some operation completes.

🤔 WHY DO CALLBACKS EXIST?
JavaScript is single-threaded, meaning it can only do one thing at a time.
But it can start an operation (like a database query) and then do other things
while waiting for it to complete. When it completes, the callback runs.

🤔 REAL-WORLD ANALOGY:
It's like ordering food at a restaurant:
1. You place your order (start async operation)
2. You get a number (callback function)
3. You sit down and do other things (JavaScript continues running)
4. When food is ready, they call your number (callback executes)
*/

// 🗄️ REAL DATABASE CONNECTION (Using YOUR actual MySQL database!)
//
// 🤔 WHY WE USE A DATABASE INSTEAD OF HARDCODED DATA:
// - Real applications NEVER hardcode data in the source code
// - Data needs to persist between server restarts
// - Multiple users need to access the same data
// - Data needs to be updated in real-time (stock prices, user portfolios)
// - Professional companies expect database integration skills
//
// 🤔 WHY WE USE CONNECTION POOLING:
// - Creating a new database connection for every query is SLOW and expensive
// - Connection pools maintain a set of reusable connections
// - Much faster performance under load (essential for production)
// - Prevents "too many connections" errors
// - Industry standard practice at all major tech companies
//
// 🤔 YOUR DATABASE SETUP:
// - Database name: onepiece_market (from YOUR schema.sql)
// - Tables: characters, users, portfolios, trades (from YOUR schema.sql)
// - Sample data: 25+ One Piece characters (from YOUR sample_data.sql)
// - Real bounties, prices, sentiment scores from the anime/manga
const mysql = require('mysql2/promise');


// Database connection pool (connects to YOUR ACTUAL onepiece_market database)
// This uses YOUR existing database files: database/schema.sql + database/sample_data.sql


const pool = mysql.createPool({
    host: process.env.DB_HOST || 'localhost',        // MySQL server location
    user: process.env.DB_USER || 'root',             // MySQL username
    password: process.env.DB_PASSWORD || 'your_mysql_password', // MySQL password
    database: process.env.DB_NAME || 'onepiece_market', // YOUR actual database name from schema.sql
    port: process.env.DB_PORT || 3306,               // MySQL default port
    waitForConnections: true,    // Wait for available connection instead of failing
    connectionLimit: 20,         // Maximum 20 concurrent connections (production-ready)
    queueLimit: 0,              // No limit on queued connection requests
    acquireTimeout: 60000,      // 60 seconds to get a connection before timeout
    timeout: 60000,             // 60 seconds for query execution timeout
    reconnect: true             // Automatically reconnect if connection is lost
});

// ✅ REAL DATABASE FUNCTION (Professional callback approach)
//
// 🤔 WHAT THIS FUNCTION DOES:
// - Takes a character ID and a callback function as parameters
// - Executes a REAL MySQL query against YOUR onepiece_market database
// - Uses YOUR actual schema.sql table structure and sample_data.sql data
// - Returns character data through the callback (error-first pattern)
// - Demonstrates professional database integration patterns
//
// 🤔 WHY WE USE CALLBACKS HERE:
// - Database queries are asynchronous (they take time to complete)
// - JavaScript doesn't wait - it continues executing other code
// - When the query finishes, it calls our callback function with the result
// - This is the foundation pattern before Promises and async/await
//
// 🤔 ERROR-FIRST CALLBACK PATTERN:
// - callback(error, data) - if error exists, data is null
// - callback(null, data) - if successful, error is null
// - This is the Node.js standard pattern used everywhere
function fetchCharacterFromDatabase(characterId, callback) {
    console.log(`🔍 Starting REAL MySQL query for character ${characterId} from YOUR onepiece_market database...`);

    // REAL MySQL query using YOUR ACTUAL schema columns from database/schema.sql
    //
    // 🤔 WHAT THIS QUERY DOES:
    // - Selects character data from YOUR characters table (schema.sql)
    // - LEFT JOINs with portfolios to get user ownership data
    // - Uses COALESCE to handle NULL values (returns 0 if user owns nothing)
    // - Calculates portfolio_value in real-time (current_price * quantity)
    // - Only returns active characters (is_active = TRUE)
    // - Uses parameterized queries (?) to prevent SQL injection attacks
    const query = `
        SELECT
            c.id,                    -- Character ID from YOUR schema.sql
            c.name,                  -- Character name (e.g., "Monkey D. Luffy")
            c.crew,                  -- Crew name (e.g., "Straw Hat Pirates")
            c.bounty,                -- Bounty amount (e.g., 3000000000 for Luffy)
            c.current_price,         -- Current stock price (e.g., 150.00 for Luffy)
            c.market_cap,            -- Market capitalization (calculated field)
            c.sentiment_score,       -- Market sentiment (-1.0 to 1.0, e.g., 0.85 for Luffy)
            c.weekly_change,         -- Weekly price change percentage
            c.description,           -- Character description
            c.image_url,             -- Character image URL
            c.is_active,             -- Whether character is actively traded
            c.created_at,            -- When character was added to database
            c.updated_at,            -- Last update timestamp
            COALESCE(p.quantity, 0) as owned_quantity,        -- How many shares user owns (0 if none)
            COALESCE(p.average_price, 0) as average_price,    -- Average price user paid
            COALESCE(p.total_invested, 0) as total_invested,  -- Total amount user invested
            (c.current_price * COALESCE(p.quantity, 0)) as portfolio_value  -- Current value of holdings
        FROM characters c
        LEFT JOIN portfolios p ON c.id = p.character_id AND p.user_id = ?  -- Join with user's portfolio
        WHERE c.id = ? AND c.is_active = TRUE  -- Only get the requested active character
    `;

    // Execute query using YOUR actual MySQL database connection pool
    //
    // 🤔 WHAT pool.execute() DOES:
    // - Gets a connection from the pool (reuses existing connections for performance)
    // - Executes the SQL query with the provided parameters [1, characterId]
    // - Returns a Promise that resolves with [rows, fields] when query completes
    // - Automatically releases the connection back to the pool when done
    // - Uses prepared statements to prevent SQL injection attacks
    //
    // 🤔 PARAMETER BINDING:
    // - [1, characterId] maps to the two ? placeholders in the query
    // - First ? gets user_id = 1 (demo user from YOUR sample_data.sql)
    // - Second ? gets the characterId parameter passed to this function
    // - This prevents SQL injection and improves performance
    
    
    pool.execute(query, [1, characterId]) // user_id = 1 for demo, characterId from function parameter
        .then(([rows, fields]) => {
            // 🤔 DESTRUCTURING ASSIGNMENT:
            // - MySQL returns [rows, fields] array
            // - rows = actual data from YOUR database
            // - fields = metadata about columns (we don't need it here)
            // - [rows, fields] extracts both into separate variables

            // Check if character exists in YOUR database
            if (rows.length === 0) {
                console.log(`❌ Character ${characterId} not found in YOUR onepiece_market database`);
                console.log('💡 Available character IDs in YOUR sample_data.sql: 1-25+');
                return callback(new Error('Character not found'), null);
            }

            // Get the first (and only) character from results
            const character = rows[0];

            // Display all the data from YOUR database with detailed explanations
            console.log(`✅ Found character from YOUR REAL MySQL database: ${character.name}`);
            console.log(`🏴‍☠️ Crew: ${character.crew} (from YOUR sample_data.sql)`);
            console.log(`💰 Current price: $${character.current_price} (stock trading price)`);
            console.log(`🏆 Bounty: ¥${character.bounty.toLocaleString()} (from One Piece anime/manga)`);
            console.log(`📊 Market cap: $${character.market_cap.toLocaleString()} (calculated: price * 1M shares)`);
            console.log(`😊 Sentiment: ${character.sentiment_score} (${character.sentiment_score > 0 ? 'Bullish 📈' : 'Bearish 📉'}) (market sentiment -1.0 to 1.0)`);
            console.log(`📈 Weekly change: ${character.weekly_change}% (price change over last week)`);
            console.log(`👤 You own: ${character.owned_quantity} shares (from portfolios table)`);
            console.log(`💎 Portfolio value: $${character.portfolio_value} (current_price * owned_quantity)`);
            console.log(`💸 Total invested: $${character.total_invested} (how much you spent buying)`);
            console.log(`📊 Average price: $${character.average_price} (average price you paid per share)`);

            // Call the callback with success (error = null, data = character)
            // This is the standard Node.js error-first callback pattern
            callback(null, character);
        })
        
        .catch(error => {
            // Handle any database errors
            console.error('❌ MySQL query error:', error.message);
            console.error('💡 TROUBLESHOOTING STEPS:');
            console.error('   1. Make sure MySQL is running: sudo systemctl start mysql');
            console.error('   2. Create YOUR database: mysql -u root -p < database/schema.sql');
            console.error('   3. Insert YOUR data: mysql -u root -p < database/sample_data.sql');
            console.error('   4. Test connection: mysql -u root -p onepiece_market');
            console.error('   5. Check .env file has correct MySQL password');

            // Call the callback with error (error = error object, data = null)
            callback(error, null);
        });
}

// Using the callback (this is how your CharacterList.tsx COULD work)
console.log('📱 User clicked on Monkey D. Luffy (character ID 1)...');
fetchCharacterFromDatabase(1, (error, character) => {
    if (error) {
        console.error('❌ Failed to fetch character:', error.message);
        console.error('💡 Make sure you ran: mysql -u root -p < database/schema.sql');
        console.error('💡 And then: mysql -u root -p < database/sample_data.sql');
        return;
    }

    console.log('✅ Character loaded successfully from YOUR database!');
    console.log(`   Name: ${character.name} (should be "Monkey D. Luffy")`);
    console.log(`   Crew: ${character.crew} (should be "Straw Hat Pirates")`);
    console.log(`   Price: $${character.current_price} (should be ?50.00)`);
    console.log(`   Bounty: ¥${character.bounty.toLocaleString()} (should be ¥3,000,000,000)`);
    console.log(`   Sentiment: ${character.sentiment_score} (should be 0.85 - very bullish!)`);
    console.log(`   You own: ${character.owned_quantity} shares`);
});

console.log('🔄 JavaScript continues running while waiting for database...');

// ✅ ASYNC/AWAIT VERSION (Modern professional approach using YOUR MySQL database)
//
// 🤔 WHAT ASYNC/AWAIT DOES:
// - async keyword makes a function return a Promise automatically
// - await keyword pauses execution until the Promise resolves
// - Much cleaner and easier to read than callbacks or .then() chains
// - This is the MODERN way to handle asynchronous operations
// - Used in all major companies: Google, Meta, Netflix, etc.
//
// 🤔 WHY ASYNC/AWAIT IS BETTER THAN CALLBACKS:
// - No callback hell - code reads top to bottom like synchronous code
// - Better error handling with try/catch blocks
// - Easier to debug and maintain
// - Industry standard for modern JavaScript development
// - Your React components already use this pattern
async function fetchCharacterFromDatabaseAsync(characterId) {
    console.log(`🔍 Starting REAL async MySQL query for character ${characterId} from YOUR onepiece_market database...`);


    try {
        // REAL MySQL query to YOUR actual database (using YOUR schema.sql structure)
        //
        // 🤔 WHY WE DON'T NEED pool.getConnection() WITH mysql2:
        // - mysql2 handles connection pooling automatically
        // - pool.execute() gets a connection, runs query, releases connection
        // - Much simpler than manual connection management
        // - Better performance and resource management
        const query = `
            SELECT
                c.id,
                c.name,
                c.crew,
                c.bounty,
                c.current_price,         -- Current stock price from YOUR sample_data.sql
                c.market_cap,            -- Market capitalization (calculated field)
                c.sentiment_score,       -- Market sentiment (-1.0 to 1.0)
                c.weekly_change,         -- Weekly price change percentage
                c.description,           -- Character description
                c.image_url,             -- Character image URL
                c.is_active,             -- Whether character is actively traded
                c.created_at,            -- When character was added to database
                c.updated_at,            -- Last update timestamp
                COALESCE(p.quantity, 0) as owned_quantity,        -- How many shares user owns
                COALESCE(p.average_price, 0) as average_price,    -- Average price user paid
                COALESCE(p.total_invested, 0) as total_invested,  -- Total amount user invested
                (c.current_price * COALESCE(p.quantity, 0)) as portfolio_value  -- Current value of holdings
            FROM characters c
            LEFT JOIN portfolios p ON c.id = p.character_id AND p.user_id = ?  -- MySQL parameter syntax
            WHERE c.id = ? AND c.is_active = TRUE  -- MySQL parameter syntax
        `;

        // Execute query using YOUR actual MySQL database connection pool
        // 🤔 DESTRUCTURING WITH ASYNC/AWAIT:
        // - await pauses execution until Promise resolves
        // - [rows] extracts just the rows from [rows, fields] result
        // - Much cleaner than .then() chains
        const [rows] = await pool.execute(query, [1, characterId]); // user_id = 1, characterId

        if (rows.length === 0) {
            console.log(`❌ Character ${characterId} not found in YOUR onepiece_market database`);
            throw new Error('Character not found in your database');
        }

        const character = rows[0];

        console.log(`✅ Found character from YOUR REAL MySQL database: ${character.name}`);
        console.log(`🏴‍☠️ Crew: ${character.crew}`);
        console.log(`💰 Current price: $${character.current_price}`);
        console.log(`🏆 Bounty: ¥${character.bounty.toLocaleString()}`);
        console.log(`📊 Market cap: $${character.market_cap.toLocaleString()}`);
        console.log(`😊 Sentiment: ${character.sentiment_score} (${character.sentiment_score > 0 ? 'Bullish 📈' : 'Bearish 📉'})`);
        console.log(`📈 Weekly change: ${character.weekly_change}%`);
        console.log(`👤 You own: ${character.owned_quantity} shares`);
        console.log(`💎 Portfolio value: $${character.portfolio_value}`);
        console.log(`📊 Profit/Loss: ${character.profit_loss_percentage}%`);

        return character;

    } catch (error) {
        console.error('❌ MySQL async query error:', error.message);
        console.error('💡 TROUBLESHOOTING:');
        console.error('   1. Make sure MySQL is running: sudo systemctl start mysql');
        console.error('   2. Create database: mysql -u root -p < database/schema.sql');
        console.error('   3. Insert data: mysql -u root -p < database/sample_data.sql');
        console.error('   4. Check connection: mysql -u root -p onepiece_market');
        throw error;
    }
    // 🤔 NO FINALLY BLOCK NEEDED:
    // - mysql2 automatically handles connection pooling
    // - No need to manually release connections like with MySQL
    // - Connection is automatically returned to pool after query completes
}

// Using async/await (MODERN approach for your React components)
console.log('\n📱 Modern async/await approach:');


(async () => {
    try {
        const character = await fetchCharacterFromDatabaseAsync(1); // Luffy from YOUR database
        console.log('✅ Character loaded with async/await from YOUR onepiece_market database!');
        console.log(`📊 Character: ${character.name} from ${character.crew}`);
        console.log(`   Expected: "Monkey D. Luffy" from "Straw Hat Pirates"`);
        console.log(`💰 Current Price: $${character.current_price} (should be ?50.00)`);
        console.log(`🏴‍☠️ Bounty: ¥${character.bounty.toLocaleString()} (should be ¥3,000,000,000)`);
        console.log(`� Sentiment: ${character.sentiment_score} (should be 0.85 - very bullish!)`);
        console.log(`📈 Weekly change: ${character.weekly_change}%`);
        console.log(`�👤 Owned: ${character.owned_quantity} shares`);
        console.log(`💎 Portfolio value: $${character.portfolio_value}`);
        // In React, you'd update the state: setCharacter(character)
    } catch (error) {
        console.error('❌ Error loading character:', error.message);
        console.error('💡 Make sure MySQL is running and database is set up');
        // In React, you'd show an error message to the user
    }
})();

// 🔥 The Problem with Callbacks (Callback Hell)
console.log('\n🔥 2.2 Callback Hell - Why Callbacks Become Nightmares:');

/*
🤔 WHAT IS CALLBACK HELL?
When you need to do multiple async operations in sequence, callbacks become
nested inside other callbacks, creating deeply nested, hard-to-read code.

🤔 WHY IS CALLBACK HELL BAD?
- Code becomes unreadable and hard to maintain
- Error handling becomes complex and repetitive
- Debugging becomes extremely difficult
- Adding new features becomes a nightmare
- New developers can't understand the code

🤔 REAL-WORLD EXAMPLE:
In your trading platform, buying a character stock requires:
1. Fetch character data
2. Check user's account balance
3. Verify character is available for trading
4. Process the transaction
5. Update user's portfolio
6. Send confirmation notification

With callbacks, this becomes nested hell...
*/

// Example of callback hell (DON'T DO THIS!)
function buyCharacterStock(userId, characterId, quantity) {
    console.log('\n😵 CALLBACK HELL EXAMPLE (DON\'T DO THIS!):');

    // Step 1: Fetch character data
    fetchCharacterFromDatabase(characterId, (err1, character) => {
        if (err1) return console.error('Failed to fetch character:', err1);

        // Step 2: Check user balance (nested callback)
        fetchUserBalance(userId, (err2, balance) => {
            if (err2) return console.error('Failed to fetch balance:', err2);

            const totalCost = character.currentPrice * quantity;
            if (balance < totalCost) {
                return console.error('Insufficient funds');
            }

            // Step 3: Process transaction (more nesting)
            processTransaction(userId, characterId, quantity, totalCost, (err3, transaction) => {
                if (err3) return console.error('Transaction failed:', err3);

                // Step 4: Update portfolio (even more nesting)
                updateUserPortfolio(userId, characterId, quantity, (err4, portfolio) => {
                    if (err4) return console.error('Portfolio update failed:', err4);

                    // Step 5: Send notification (maximum nesting!)
                    sendNotification(userId, `Successfully bought ${quantity} shares of ${character.name}`, (err5) => {
                        if (err5) return console.error('Notification failed:', err5);

                        console.log('✅ Transaction completed successfully!');
                        // This is 6 levels deep! Impossible to maintain!
                    });
                });
            });
        });
    });
}

// Helper functions to simulate the callback hell


function fetchUserBalance(userId, callback) {
    setTimeout(() => callback(null, 10000), 500); // ?0,000 balance
}

function processTransaction(userId, characterId, quantity, cost, callback) {
    setTimeout(() => callback(null, { id: 'txn_123', cost, quantity }), 800);
}

function updateUserPortfolio(userId, characterId, quantity, callback) {
    setTimeout(() => callback(null, { characterId, quantity, totalShares: quantity }), 600);
}

function sendNotification(userId, message, callback) {
    setTimeout(() => callback(null), 300);
}

// This creates callback hell!
// buyCharacterStock(1, 1, 10); // Uncomment to see the nightmare

// 🔥 Promises: The Solution to Callback Hell
console.log('\n🔥 2.3 Promises - The Solution to Callback Hell:');

/*
🤔 WHAT IS A PROMISE?
A Promise is an object that represents the eventual completion (or failure) of
an asynchronous operation. It's like a "promise" that you'll get a result later.

🤔 WHY ARE PROMISES BETTER THAN CALLBACKS?
- No more nested callback hell
- Better error handling with .catch()
- Can chain operations with .then()
- More readable and maintainable code
- Can handle multiple async operations easily

🤔 PROMISE STATES:
- Pending: The operation is still running
- Fulfilled: The operation completed successfully
- Rejected: The operation failed

🤔 REAL-WORLD ANALOGY:
A promise is like ordering something online:
- Pending: Your order is being processed
- Fulfilled: Your package arrives (you get the data)
- Rejected: Order cancelled (you get an error)
*/

// Converting our callback function to use Promises
function fetchCharacterPromise(characterId) {
    return new Promise((resolve, reject) => {
        console.log(`🔍 Promise: Fetching character ${characterId}...`);

        setTimeout(() => {
            const databaseCharacters = {
                1: {
                    id: 1,
                    name: 'Monkey D. Luffy',
                    crew: 'Straw Hat Pirates',
                    bounty: 3000000000,
                    currentPrice: 150.50,
                    lastUpdated: new Date()
                },
                2: {
                    id: 2,
                    name: 'Roronoa Zoro',
                    crew: 'Straw Hat Pirates',
                    bounty: 1111000000,
                    currentPrice: 89.25,
                    lastUpdated: new Date()
                }
            };

            const character = databaseCharacters[characterId];
            if (character) {
                resolve(character); // Success - fulfill the promise
            } else {
                reject(new Error('Character not found')); // Failure - reject the promise
            }
        }, 1000);
    });
}

// Using Promises with .then() and .catch() (much cleaner than callbacks!)
console.log('📱 User clicked on character 2 (using Promises)...');
fetchCharacterPromise(2)
    .then(character => {
        console.log('✅ Promise resolved - character loaded:');
        console.log(`   Name: ${character.name}`);
        console.log(`   Stock Price: $${character.currentPrice}`);

        // You can return a value to chain another .then()
        return character.currentPrice * 1.1; // Calculate 10% price increase
    })
    .then(newPrice => {
        console.log(`💰 Predicted new price: $${newPrice.toFixed(2)}`);

        // You can return another Promise to chain async operations
        return new Promise(resolve => {
            setTimeout(() => {
                resolve(`Price updated to $${newPrice.toFixed(2)}`);
            }, 500);
        });
    })
    .then(updateMessage => {
        console.log('📈', updateMessage);
    })
    .catch(error => {
        console.error('❌ Promise rejected:', error.message);
    });

// 🔥 Async/Await: The Modern, Clean Way
console.log('\n🔥 2.4 Async/Await - The Modern, Clean Way:');

/*
🤔 WHAT IS ASYNC/AWAIT?
Async/await is syntactic sugar over Promises that makes asynchronous code
look and behave more like synchronous code. It's the modern standard.

🤔 WHY USE ASYNC/AWAIT?
- Code looks like regular, synchronous code (easier to read)
- Error handling with try/catch (familiar pattern)
- No more .then() chains
- Easier to debug
- Industry standard for modern JavaScript

🤔 HOW IT WORKS:
- async: Makes a function return a Promise
- await: Pauses execution until the Promise resolves
- try/catch: Handles errors cleanly

🤔 REAL-WORLD USAGE:
This is how your CharacterList.tsx SHOULD be written, and how all modern
JavaScript applications handle async operations.
*/

// Converting our Promise function to use async/await
async function fetchCharacterModern(characterId) {
    try {
        console.log(`🔍 Async/Await: Fetching character ${characterId}...`);

        // This looks synchronous but is actually asynchronous!
        const character = await new Promise((resolve, reject) => {
            setTimeout(() => {
                const databaseCharacters = {
                    1: {
                        id: 1,
                        name: 'Monkey D. Luffy',
                        crew: 'Straw Hat Pirates',
                        bounty: 3000000000,
                        currentPrice: 150.50,
                        marketCap: 3000000000 / 1000000, // ?B market cap
                        dailyChange: +5.2
                    },
                    2: {
                        id: 2,
                        name: 'Roronoa Zoro',
                        crew: 'Straw Hat Pirates',
                        bounty: 1111000000,
                        currentPrice: 89.25,
                        marketCap: 1111000000 / 1000000, // ?.1B market cap
                        dailyChange: -2.1
                    },
                    3: {
                        id: 3,
                        name: 'Nami',
                        crew: 'Straw Hat Pirates',
                        bounty: 366000000,
                        currentPrice: 45.75,
                        marketCap: 366000000 / 1000000, // ?66M market cap
                        dailyChange: +8.7
                    }
                };

                const char = databaseCharacters[characterId];
                if (char) {
                    resolve(char);
                } else {
                    reject(new Error('Character not found'));
                }
            }, 1200);
        });

        console.log('✅ Async/Await success:');
        console.log(`   ${character.name} - $${character.currentPrice}`);
        console.log(`   Market Cap: $${character.marketCap.toFixed(1)}M`);
        console.log(`   Daily Change: ${character.dailyChange > 0 ? '+' : ''}${character.dailyChange}%`);

        return character;

    } catch (error) {
        console.error('❌ Async/Await error:', error.message);
        throw error; // Re-throw for caller to handle
    }
}

// Using async/await (this is how modern JavaScript looks!)
async function demonstrateModernAsync() {
    try {
        console.log('📱 Loading multiple characters with async/await...');

        // Sequential loading (one after another)
        const luffy = await fetchCharacterModern(1);
        const zoro = await fetchCharacterModern(2);

        console.log(`🏴‍☠️ Loaded ${luffy.name} and ${zoro.name} sequentially`);

        // Parallel loading (all at once - much faster!)
        console.log('\n⚡ Loading characters in parallel...');
        const [nami, usopp, sanji] = await Promise.all([
            fetchCharacterModern(3),
            fetchCharacterPromise(1), // Mix different async functions
            new Promise(resolve => setTimeout(() => resolve({
                name: 'Sanji',
                currentPrice: 67.80,
                dailyChange: +3.4
            }), 800))
        ]);

        console.log('✅ All characters loaded in parallel:');
        console.log(`   ${nami.name}: $${nami.currentPrice} (${nami.dailyChange > 0 ? '+' : ''}${nami.dailyChange}%)`);
        console.log(`   ${usopp.name}: $${usopp.currentPrice}`);
        console.log(`   ${sanji.name}: $${sanji.currentPrice} (${sanji.dailyChange > 0 ? '+' : ''}${sanji.dailyChange}%)`);

    } catch (error) {
        console.log('⚠️ Some operations failed, but we handled it gracefully:', error.message);
    }
}

// Execute the modern async demo
demonstrateModernAsync();

// ============================================================================
// 🗄️ SECTION 3: DATABASE INTEGRATION (WHY WE DON'T HARDCODE DATA)
// ============================================================================

console.log('\n\n🗄️ SECTION 3: DATABASE INTEGRATION (WHY WE DON\'T HARDCODE DATA)');
console.log('--------------------------------------------------------------------');

/*
🤔 WHY DON'T WE HARDCODE DATA?
In the examples above, we database-driven character data inside our functions.
This is TERRIBLE for real applications because:

❌ PROBLEMS WITH HARDCODED DATA:
- Data can't change without redeploying code
- No way to add new characters without coding
- Can't handle user-generated content
- No data persistence between sessions
- Can't scale to millions of users
- No way to backup or restore data

✅ BENEFITS OF DATABASES:
- Data persists even if server restarts
- Can handle millions of records efficiently
- Multiple users can access same data
- Data can be updated without code changes
- Backup and recovery capabilities
- Advanced querying and filtering

🤔 WHAT DATABASES DOES JAVASCRIPT USE?

🐘 POSTGRESQL (SQL Database):
- Structured data with relationships
- ACID compliance (data integrity)
- Complex queries with SQL
- Used by: Instagram, Spotify, Netflix
- JavaScript library: node-mysql (mysql2)

🍃 MONGODB (NoSQL Database):
- Flexible, document-based storage
- JSON-like documents
- Horizontal scaling
- Used by: Facebook, Google, Adobe
- JavaScript library: Mongoose

⚡ REDIS (In-Memory Cache):
- Lightning-fast data access
- Session storage and caching
- Real-time features
- Used by: Twitter, GitHub, Stack Overflow
- JavaScript library: redis

🤔 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
- Character data stored in MySQL
- User sessions cached in Redis
- Trading history in MongoDB
- Real-time prices cached in Redis
*/

// 🔥 MySQL Integration (SQL Database)
console.log('\n🔥 3.1 MySQL Integration - Structured Data:');

/*
🤔 WHAT IS POSTGRESQL?
MySQL is a powerful, open-source SQL database that stores data in tables
with rows and columns. It's perfect for structured data with relationships.

🤔 WHY USE POSTGRESQL FOR YOUR TRADING PLATFORM?
- Character data has clear structure (name, crew, bounty, etc.)
- User accounts need relationships (user -> portfolio -> trades)
- ACID compliance ensures trading data integrity
- Complex queries for trading analytics
- Proven at scale (used by major companies)

🤔 JAVASCRIPT LIBRARY: node-mysql (mysql2)
This is the most popular MySQL client for Node.js
*/

const mysql = require('mysql2/promise');

const pool = mysql.createPool({
    host : 'localhost',
    user : 'onepiece_user',
    
})
// Example: How to connect to MySQL in JavaScript
const mysqlExample = `
// Install: npm install mysql2
const { Pool } = require('mysql2');

// Database connection configuration
const pool = mysql.createPool({
    user: 'onepiece_user',
    host: 'localhost',
    database: 'onepiece_market',
    password: 'your_secure_password',
    port: 3306,
    max: 20, // Maximum number of connections
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
});

// Function to fetch characters from MySQL (NOT database-driven!)
async function getCharactersFromMySQL() {
    const client = await pool.getConnection();
    try {
        const query = \`
            SELECT
                id,
                name,
                crew,
                bounty,
                current_price,
                weekly_change,
                market_cap,
                created_at,
                updated_at
            FROM characters
            WHERE is_active = true
            ORDER BY bounty DESC
            LIMIT 10
        \`;

        const result = await connection.execute(query);
        return rows;
    } catch (error) {
        console.error('Database query failed:', error);
        throw error;
    } finally {
        client.release(); // Always release the connection!
    }
}

// Function to buy character stock (with database transaction)
async function buyCharacterStock(userId, characterId, quantity) {
    const client = await pool.getConnection();
    try {
        // Start database transaction (all-or-nothing)
        await connection.execute('BEGIN');

        // 1. Check user balance
        const balanceResult = await connection.execute(
            'SELECT balance FROM users WHERE id = ?',
            [userId]
        );

        // 2. Get character price
        const priceResult = await connection.execute(
            'SELECT current_price FROM characters WHERE id = ?',
            [characterId]
        );

        const balance = balanceResult.rows[0].balance;
        const price = priceResult.rows[0].current_price;
        const totalCost = price * quantity;

        if (balance < totalCost) {
            throw new Error('Insufficient funds');
        }

        // 3. Update user balance
        await connection.execute(
            'UPDATE users SET balance = balance - ? WHERE id = ?',
            [totalCost, userId]
        );

        // 4. Add to user portfolio
        await connection.execute(\`
            INSERT INTO user_portfolio (user_id, character_id, quantity, purchase_price)
            VALUES (?, ?, ?, ?)
            ON CONFLICT (user_id, character_id)
            DO UPDATE SET quantity = user_portfolio.quantity + ?
        \`, [userId, characterId, quantity, price]);

        // 5. Record transaction
        await connection.execute(\`
            INSERT INTO transactions (user_id, character_id, type, quantity, price, total_cost)
            VALUES (?, ?, 'BUY', ?, ?, ?)
        \`, [userId, characterId, quantity, price, totalCost]);

        // Commit transaction (make all changes permanent)
        await connection.execute('COMMIT');

        return {
            success: true,
            transactionId: 'txn_' + Date.now(),
            totalCost,
            newBalance: balance - totalCost
        };

    } catch (error) {
        // Rollback transaction (undo all changes)
        await connection.execute('ROLLBACK');
        throw error;
    } finally {
        client.release();
    }
}
`;

console.log('📚 MySQL Example Code:');
console.log(mysqlExample);

// 🔥 MongoDB Integration (NoSQL Database)
console.log('\n🔥 3.2 MongoDB Integration - Flexible Documents:');

/*
🤔 WHAT IS MONGODB?
MongoDB is a NoSQL database that stores data as JSON-like documents.
It's perfect for flexible data that doesn't fit rigid table structures.

🤔 WHY USE MONGODB FOR YOUR TRADING PLATFORM?
- User preferences and settings (flexible structure)
- Trading logs and analytics (varying data fields)
- Real-time chat messages
- Notification history
- A/B testing data

🤔 JAVASCRIPT LIBRARY: Mongoose
Mongoose is an Object Document Mapper (ODM) that makes MongoDB easier to use
*/

const mongoExample = `
// Install: npm install mongoose
const mongoose = require('mongoose');

// Connect to MongoDB
await mongoose.connect('mongodb://localhost:27017/onepiece_market');

// Define character schema (structure for documents)
const characterSchema = new mongoose.Schema({
    name: { type: String, required: true, unique: true },
    crew: { type: String, required: true },
    bounty: { type: Number, required: true },
    devilFruit: { type: String, default: null },
    abilities: [String],
    currentPrice: { type: Number, required: true },
    priceHistory: [{
        price: Number,
        timestamp: { type: Date, default: Date.now }
    }],
    metadata: {
        firstAppearance: String,
        voiceActor: String,
        popularity: Number
    }
}, {
    timestamps: true // Automatically add createdAt and updatedAt
});

// Create model (like a class for creating documents)
const Character = mongoose.model('Character', characterSchema);

// Function to create a new character
async function createCharacter(characterData) {
    try {
        const character = new Character(characterData);
        await character.save();
        return character;
    } catch (error) {
        console.error('Failed to create character:', error);
        throw error;
    }
}

// Function to find characters with flexible queries
async function findCharacters(filters = {}) {
    try {
        const characters = await Character.find(filters)
            .sort({ bounty: -1 }) // Sort by bounty descending
            .limit(20)
            .select('name crew bounty currentPrice') // Only return specific fields
            .lean(); // Return plain JavaScript objects (faster)

        return characters;
    } catch (error) {
        console.error('Failed to find characters:', error);
        throw error;
    }
}

// Function to update character price with history
async function updateCharacterPrice(characterId, newPrice) {
    try {
        const character = await Character.findById(characterId);

        // Add current price to history
        character.priceHistory.push({
            price: character.currentPrice,
            timestamp: new Date()
        });

        // Update current price
        character.currentPrice = newPrice;

        // Keep only last 100 price points
        if (character.priceHistory.length > 100) {
            character.priceHistory = character.priceHistory.slice(-100);
        }

        await character.save();
        return character;
    } catch (error) {
        console.error('Failed to update price:', error);
        throw error;
    }
}
`;

console.log('📚 MongoDB Example Code:');
console.log(mongoExample);

// 🔥 Redis Integration (In-Memory Cache)
console.log('\n🔥 3.3 Redis Integration - Lightning-Fast Cache:');

/*
🤔 WHAT IS REDIS?
Redis is an in-memory data store that's extremely fast because it keeps
all data in RAM. It's perfect for caching and real-time features.

🤔 WHY USE REDIS FOR YOUR TRADING PLATFORM?
- Cache frequently accessed character data (millisecond response times)
- Store user sessions (login state, shopping cart)
- Real-time price updates (pub/sub messaging)
- Rate limiting (prevent API abuse)
- Leaderboards and rankings

🤔 JAVASCRIPT LIBRARY: redis
The official Redis client for Node.js
*/

const redisExample = `
// Install: npm install redis
const redis = require('redis');

// Create Redis client
const client = redis.createClient({
    host: 'localhost',
    port: 6379,
    password: 'your_redis_password', // If Redis has auth enabled
    db: 0 // Redis database number (0-15)
});

// Connect to Redis
await client.connect();

// Function to cache character data
async function cacheCharacterData(characterId, characterData) {
    try {
        const key = \`character:\${characterId}\`;
        const value = JSON.stringify(characterData);

        // Cache for 1 hour (3600 seconds)
        await client.setEx(key, 3600, value);

        console.log(\`Cached character \${characterId}\`);
    } catch (error) {
        console.error('Failed to cache character:', error);
    }
}

// Function to get cached character data
async function getCachedCharacter(characterId) {
    try {
        const key = \`character:\${characterId}\`;
        const cachedData = await client.get(key);

        if (cachedData) {
            return JSON.parse(cachedData);
        }

        return null; // Not in cache
    } catch (error) {
        console.error('Failed to get cached character:', error);
        return null;
    }
}

// Function to implement caching strategy
async function getCharacterWithCache(characterId) {
    // 1. Try to get from cache first (fast)
    let character = await getCachedCharacter(characterId);

    if (character) {
        console.log('✅ Character loaded from cache (fast!)');
        return character;
    }

    // 2. If not in cache, get from database (slower)
    console.log('⏳ Character not in cache, loading from database...');
    character = await getCharactersFromMySQL(); // Your database function

    // 3. Cache the result for next time
    await cacheCharacterData(characterId, character);

    return character;
}

// Function for real-time price updates using Redis Pub/Sub
async function setupRealTimePrices() {
    // Publisher (sends price updates)
    const publisher = redis.createClient();
    await publisher.connect();

    // Subscriber (receives price updates)
    const subscriber = redis.createClient();
    await subscriber.connect();

    // Subscribe to price updates
    await subscriber.subscribe('price-updates', (message) => {
        const priceUpdate = JSON.parse(message);
        console.log(\`📈 Price Update: \${priceUpdate.character} = $\${priceUpdate.price}\`);

        // In your React app, you'd update the UI here
        // updateCharacterPrice(priceUpdate.characterId, priceUpdate.price);
    });

    // Simulate publishing price updates
    setInterval(async () => {
        const priceUpdate = {
            characterId: 1,
            character: 'Luffy',
            price: (Math.random() * 200 + 100).toFixed(2),
            timestamp: new Date().toISOString()
        };

        await publisher.publish('price-updates', JSON.stringify(priceUpdate));
    }, 5000); // Update every 5 seconds
}
`;

console.log('📚 Redis Example Code:');
console.log(redisExample);

// ============================================================================
// 🎯 SECTION 4: PUTTING IT ALL TOGETHER - YOUR ONE PIECE PROJECT
// ============================================================================

console.log('\n\n🎯 SECTION 4: PUTTING IT ALL TOGETHER - YOUR ONE PIECE PROJECT');
console.log('----------------------------------------------------------------');

/*
🤔 HOW TO APPLY THIS TO YOUR CHARACTERLIST.TSX:

Your current CharacterList.tsx probably looks like this:

❌ CURRENT (basic but functional):
```typescript
const [characters, setCharacters] = useState([]);
useEffect(() => {
    fetch('http://localhost:5000/api/characters')
        .then(response => response.json())
        .then(data => setCharacters(data));
}, []);
```

✅ AFTER THIS MODULE (professional implementation):
```typescript
import { CharacterService } from '../services/CharacterService';

const CharacterList: React.FC = () => {
    const [characters, setCharacters] = useState<Character[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const loadCharacters = async () => {
            try {
                setLoading(true);
                const characterService = CharacterService.getInstance();
                const data = await characterService.fetchCharacters();
                setCharacters(data);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Failed to load characters');
            } finally {
                setLoading(false);
            }
        };

        loadCharacters();
    }, []);

    if (loading) return <div>Loading characters...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            {characters.map(character => (
                <CharacterCard key={character.id} character={character} />
            ))}
        </div>
    );
};
```

🤔 WHAT YOU'LL BUILD NEXT:
1. Replace your Flask backend with Node.js + Express
2. Connect to MySQL for character data
3. Add Redis caching for performance
4. Implement real-time price updates with WebSockets
5. Add user authentication and portfolio management
6. Build trading algorithms with OOP patterns
*/

console.log('\n🏆 CONGRATULATIONS! YOU\'VE COMPLETED JAVASCRIPT FUNDAMENTALS!');
console.log('================================================================');

console.log(`
🎯 WHAT YOU'VE LEARNED:
✅ JavaScript fundamentals (variables, functions, objects, arrays)
✅ Template literals for clean string formatting
✅ Asynchronous programming (callbacks, promises, async/await)
✅ Why callback hell is bad and how to avoid it
✅ Database integration (MySQL, MongoDB, Redis)
✅ Why we don't hardcode data in real applications
✅ Professional patterns used in ?00K+ engineering roles

💰 YOUR NEW SKILLS ARE WORTH:
📚 JavaScript Fundamentals: $60K-$90K (Junior Developer)
⚡ Async Programming: $90K-?30K (Mid-Level Developer)
🗄️ Database Integration: ?30K-?80K (Senior Developer)
🏗️ Professional Patterns: ?80K-?50K+ (Staff Engineer)

🚀 NEXT STEPS:
1. Apply these patterns to your CharacterList.tsx
2. Move to Module 16: Node.js Backend Development
3. Replace your Flask app.py with Express.js
4. Connect to real databases instead of YOUR real MySQL database
5. Build the complete One Piece trading platform

🏴‍☠️ YOU'RE ON YOUR WAY TO BECOMING A LEGENDARY ENGINEER!
`);

// ============================================================================
// 📚 COMPLETE REFERENCE SOLUTIONS
// ============================================================================

console.log('\n\n📚 COMPLETE REFERENCE SOLUTIONS');
console.log('================================');

/*
🎯 COMPLETE CHARACTER SERVICE CLASS (Professional Implementation)

This is how a senior engineer would implement the CharacterService for your
One Piece trading platform. Study this code and use it as reference!
*/

const completeCharacterService = `
// CharacterService.js - Professional implementation
class CharacterService {
    // Singleton pattern - only one instance exists
    static instance = null;

    constructor() {
        this.cache = new Map();
        this.subscribers = new Set();
        this.isConnected = false;
    }

    static getInstance() {
        if (!CharacterService.instance) {
            CharacterService.instance = new CharacterService();
        }
        return CharacterService.instance;
    }

    // Connect to databases
    async connect() {
        if (this.isConnected) return;

        try {
            // Connect to MySQL
            this.mysql2Pool = mysql.createPool({
                user: 'onepiece_user',
                host: 'localhost',
                database: 'onepiece_market',
                password: process.env.DB_PASSWORD,
                port: 3306,
            });

            // Connect to Redis
            this.redisClient = redis.createClient();
            await this.redisClient.connect();

            this.isConnected = true;
            console.log('✅ Connected to databases');
        } catch (error) {
            console.error('❌ Database connection failed:', error);
            throw error;
        }
    }

    // Fetch characters with caching
    async fetchCharacters() {
        await this.connect();

        try {
            // 1. Try cache first
            const cached = await this.redisClient.get('characters:all');
            if (cached) {
                console.log('📦 Loaded from cache');
                return JSON.parse(cached);
            }

            // 2. Query database
            const client = await this.mysql2Pool.connect();
            const result = await connection.execute(\`
                SELECT id, name, crew, bounty, current_price, weekly_change
                FROM characters
                WHERE is_active = true
                ORDER BY bounty DESC
            \`);
            client.release();

            const characters = rows;

            // 3. Cache for 5 minutes
            await this.redisClient.setEx('characters:all', 300, JSON.stringify(characters));

            console.log(\`📊 Loaded \${characters.length} characters from database\`);
            return characters;

        } catch (error) {
            console.error('❌ Failed to fetch characters:', error);
            throw new Error('Unable to load characters');
        }
    }

    // Buy character stock with transaction
    async buyCharacterStock(userId, characterId, quantity) {
        await this.connect();
        const client = await this.mysql2Pool.connect();

        try {
            await connection.execute('BEGIN');

            // Check balance and get price
            const [balanceResult, priceResult] = await Promise.all([
                connection.execute('SELECT balance FROM users WHERE id = ?', [userId]),
                connection.execute('SELECT current_price FROM characters WHERE id = ?', [characterId])
            ]);

            const balance = balanceResult.rows[0]?.balance;
            const price = priceResult.rows[0]?.current_price;

            if (!balance || !price) {
                throw new Error('User or character not found');
            }

            const totalCost = price * quantity;
            if (balance < totalCost) {
                throw new Error('Insufficient funds');
            }

            // Execute transaction
            await Promise.all([
                connection.execute('UPDATE users SET balance = balance - ? WHERE id = ?', [totalCost, userId]),
                connection.execute(\`
                    INSERT INTO user_portfolio (user_id, character_id, quantity, purchase_price)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT (user_id, character_id)
                    DO UPDATE SET quantity = user_portfolio.quantity + ?
                \`, [userId, characterId, quantity, price]),
                connection.execute(\`
                    INSERT INTO transactions (user_id, character_id, type, quantity, price, total_cost)
                    VALUES (?, ?, 'BUY', ?, ?, ?)
                \`, [userId, characterId, quantity, price, totalCost])
            ]);

            await connection.execute('COMMIT');

            // Invalidate cache
            await this.redisClient.del('characters:all');

            // Notify subscribers
            this.notifySubscribers('STOCK_PURCHASED', {
                userId, characterId, quantity, totalCost
            });

            return {
                success: true,
                transactionId: \`txn_\${Date.now()}\`,
                totalCost,
                newBalance: balance - totalCost
            };

        } catch (error) {
            await connection.execute('ROLLBACK');
            throw error;
        } finally {
            client.release();
        }
    }

    // Observer pattern for real-time updates
    subscribe(callback) {
        this.subscribers.add(callback);
        return () => this.subscribers.delete(callback);
    }

    notifySubscribers(event, data) {
        this.subscribers.forEach(callback => {
            try {
                callback(event, data);
            } catch (error) {
                console.error('Subscriber error:', error);
            }
        });
    }

    // Cleanup
    async disconnect() {
        if (this.mysql2Pool) await this.mysql2Pool.end();
        if (this.redisClient) await this.redisClient.quit();
        this.isConnected = false;
    }
}

// Export for use in your React components
module.exports = CharacterService;
`;

console.log('📚 Complete CharacterService Implementation:');
console.log(completeCharacterService);

console.log('\n🎯 HOW TO USE THIS IN YOUR REACT COMPONENT:');
console.log(`
// In your CharacterList.tsx
import { useEffect, useState } from 'react';
import CharacterService from '../services/CharacterService';

const CharacterList = () => {
    const [characters, setCharacters] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const service = CharacterService.getInstance();

        // Load initial data
        service.fetchCharacters()
            .then(setCharacters)
            .catch(console.error)
            .finally(() => setLoading(false));

        // Subscribe to real-time updates
        const unsubscribe = service.subscribe((event, data) => {
            if (event === 'PRICE_UPDATE') {
                setCharacters(prev => prev.map(char =>
                    char.id === data.characterId
                        ? { ...char, current_price: data.newPrice }
                        : char
                ));
            }
        });

        return unsubscribe; // Cleanup on unmount
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <div>
            {characters.map(character => (
                <div key={character.id}>
                    <h3>{character.name}</h3>
                    <p>Price: \${character.current_price}</p>
                    <button onClick={() => buyStock(character.id, 1)}>
                        Buy 1 Share
                    </button>
                </div>
            ))}
        </div>
    );
};
`);

console.log('\n═══════════════════════════════════════════════════════════════════════════════');
console.log('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!');
console.log('═══════════════════════════════════════════════════════════════════════════════');

console.log('\n🚀 STEP 1: UPDATE YOUR REACT COMPONENTS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📁 Files to update:');
console.log('• frontend/src/components/Characters/CharacterList.tsx');
console.log('• frontend/src/components/Characters/CharacterCard.tsx');
console.log('• frontend/src/services/CharacterService.ts');
console.log('');
console.log('🎯 WHAT TO DO:');
console.log('1. Replace basic fetch() calls with async/await patterns');
console.log('2. Add proper error handling with try/catch blocks');
console.log('3. Implement loading states and error messages');
console.log('4. Use the CharacterService class pattern from above');
console.log('');
console.log('📚 REFERENCE: Use the complete CharacterService implementation above');

console.log('\n🚀 STEP 2: CREATE PROFESSIONAL SERVICE CLASSES');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/services/CharacterService.ts');
console.log('');
console.log('✅ Features to implement:');
console.log('• Singleton pattern for single instance');
console.log('• Async/await for all API calls');
console.log('• Error handling with meaningful messages');
console.log('• Caching for better performance');
console.log('• Observer pattern for real-time updates');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- Complete CharacterService class (lines 1474-1647)');
console.log('- Async/await patterns (lines 1393-1407)');
console.log('- Error handling examples (lines 1549-1552)');

console.log('\n🚀 STEP 3: CONNECT TO YOUR API GATEWAY');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🌐 YOUR API CALLS WILL GO TO:');
console.log('• http://localhost:5000/api/characters (GET all characters)');
console.log('• http://localhost:5000/api/characters/:id (GET single character)');
console.log('• http://localhost:5000/api/characters/:id/buy (POST buy character stock)');
console.log('• http://localhost:5000/api/auth/login (POST user authentication)');
console.log('');
console.log('🔧 MAKE SURE YOUR REACT APP:');
console.log('1. Uses async/await for all API calls');
console.log('2. Handles loading states properly');
console.log('3. Shows meaningful error messages');
console.log('4. Updates UI in real-time when data changes');

console.log('\n🚀 STEP 4: TEST YOUR IMPLEMENTATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🧪 TESTING STEPS:');
console.log('');
console.log('1. Start your React frontend:');
console.log('   cd frontend');
console.log('   npm start');
console.log('');
console.log('2. Open browser console (F12)');
console.log('3. Check for JavaScript errors');
console.log('4. Verify async/await patterns work');
console.log('5. Test error handling by disconnecting internet');
console.log('');
console.log('✅ SUCCESS CRITERIA:');
console.log('- No JavaScript errors in console');
console.log('- Loading states show properly');
console.log('- Error messages display when API fails');
console.log('- Character data loads and displays correctly');

console.log('\n═══════════════════════════════════════════════════════════════════════════════');
console.log('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES');
console.log('═══════════════════════════════════════════════════════════════════════════════');

console.log('\n🧩 MODULE CONNECTIONS:');
console.log('');
console.log('📚 Module 16 (Node.js) → Your API Gateway will use these JavaScript patterns');
console.log('📚 Module 18 (TypeScript) → Add type safety to your JavaScript code');
console.log('📚 Module 19 (React) → Use async/await in React hooks and components');
console.log('📚 Module 3 (Database) → Your JavaScript will query MySQL and Redis');
console.log('📚 Module 7 (Security) → Add JWT authentication to your JavaScript services');

console.log('\n🎯 NEXT MODULES TO COMPLETE:');
console.log('1. Module 16: Build Node.js API Gateway using these JavaScript skills');
console.log('2. Module 18: Add TypeScript types to your JavaScript code');
console.log('3. Module 19: Complete React components with async/await patterns');

console.log('\n🏴‍☠️ READY FOR THE NEXT MODULE? LET\'S BUILD YOUR NODE.JS BACKEND! ⚔️');
console.log('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!');
