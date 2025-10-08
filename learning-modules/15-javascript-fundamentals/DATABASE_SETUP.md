# 🏴‍☠️ ONE PIECE TRADING PLATFORM - DATABASE SETUP

## 🎯 **STOP USING HARDCODED DATA! USE YOUR EXISTING MYSQL DATABASE!**

This guide will help you use YOUR **EXISTING MySQL database** (schema.sql + sample_data.sql) with actual One Piece character data for your learning modules.

**🔥 YOU ALREADY HAVE THE DATABASE FILES! WE'RE USING THEM NOW! 🔥**

---

## 📋 **PREREQUISITES**

### 1. Install MySQL (if not already installed)

#### **Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql
sudo mysql_secure_installation
```

#### **macOS:**
```bash
brew install mysql
brew services start mysql
```

#### **Windows:**
Download from: https://dev.mysql.com/downloads/mysql/

### 2. Install Node.js Dependencies
```bash
cd learning-modules/15-javascript-fundamentals
npm install
```

---

## 🗄️ **DATABASE SETUP (Using YOUR Existing Files)**

### Step 1: Use YOUR Existing Database Files
**🔥 YOU ALREADY HAVE THESE FILES! 🔥**
- `database/schema.sql` - Creates the onepiece_market database and tables
- `database/sample_data.sql` - Inserts all the One Piece character data

### Step 2: Set Up MySQL Database
```bash
# Connect to MySQL as root
mysql -u root -p

# Run YOUR existing schema file
source /path/to/your/project/database/schema.sql

# Run YOUR existing sample data file
source /path/to/your/project/database/sample_data.sql

# Verify the setup
USE onepiece_market;
SHOW TABLES;
SELECT COUNT(*) FROM characters;
\q
```

### Step 3: Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with YOUR MySQL credentials
nano .env
```

Update your `.env` file:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=onepiece_market
DB_USER=root
DB_PASSWORD=your_mysql_password
```

### Step 4: Run Database Setup Script (Uses YOUR Files)
```bash
# This will use YOUR existing schema.sql and sample_data.sql files
npm run setup
```

### Step 5: Test Database Connection
```bash
# Verify everything is working with YOUR data
npm test
```

---

## 🏴‍☠️ **WHAT YOUR DATABASE CONTAINS**

### **📊 Characters Table (From YOUR sample_data.sql)**
- **25+ One Piece characters** with real bounties and prices
- **Straw Hat Pirates**: Luffy ($150), Zoro ($120), Nami ($95), Sanji ($110), etc.
- **Emperors**: Shanks ($220), Kaido ($200), Big Mom ($190), Blackbeard ($180)
- **Marines**: Akainu ($170), Kizaru ($155), Garp ($160)
- **Revolutionary Army**: Dragon ($210), Sabo ($130)
- **Sentiment Scores**: Each character has market sentiment (-1.0 to 1.0)
- **Weekly Changes**: Performance tracking for each character

### **👤 Users Table**
- **3 test users** with different balances
- **Secure password hashing** with bcrypt
- **Account security features** (lockout, failed attempts)

### **💼 Portfolios Table**
- **Sample portfolio data** showing character ownership
- **Real-time value calculations** based on current prices
- **Investment tracking** with average prices

### **💰 Transactions Table**
- **Complete trading history** for all users
- **Buy/sell records** with timestamps
- **Portfolio impact tracking**

---

## 🚀 **RUNNING THE LEARNING MODULE**

Once your database is set up:

```bash
# Run the JavaScript fundamentals module with REAL data
node 01-js-mastery-coding-lab.js
```

**You'll see:**
- ✅ **Real database queries** instead of hardcoded data
- ✅ **Actual PostgreSQL connections** with connection pooling
- ✅ **Professional error handling** and logging
- ✅ **Real character data** from your database
- ✅ **Portfolio calculations** based on actual holdings

---

## 🔧 **TROUBLESHOOTING**

### **Connection Refused Error**
```bash
# Start PostgreSQL service
sudo systemctl start postgresql

# Check if it's running
sudo systemctl status postgresql
```

### **Authentication Failed**
- Check your password in the `.env` file
- Make sure the user has proper permissions

### **Database Does Not Exist**
```bash
# Recreate the database
sudo -u postgres createdb onepiece_trading
```

### **Tables Don't Exist**
```bash
# Run the setup script again
npm run setup
```

---

## 📊 **DATABASE SCHEMA**

### **Characters Table**
```sql
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    crew VARCHAR(100) NOT NULL,
    bounty BIGINT NOT NULL,
    current_price DECIMAL(10,2) NOT NULL,
    previous_price DECIMAL(10,2) NOT NULL,
    daily_change DECIMAL(5,2) NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    image_url VARCHAR(255),
    description TEXT
);
```

### **Users Table**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    balance DECIMAL(12,2) DEFAULT 10000.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Portfolios Table**
```sql
CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    character_id INTEGER REFERENCES characters(id),
    quantity INTEGER NOT NULL DEFAULT 0,
    average_price DECIMAL(10,2) NOT NULL,
    total_invested DECIMAL(12,2) NOT NULL,
    UNIQUE(user_id, character_id)
);
```

---

## 🎯 **NEXT STEPS**

1. **✅ Set up your database** using this guide
2. **✅ Run the learning modules** with real data
3. **✅ Build your React frontend** to connect to this database
4. **✅ Add authentication** and user management
5. **✅ Deploy to production** with proper security

---

## 🏴‍☠️ **WHY THIS MATTERS**

**❌ Hardcoded Data Problems:**
- Not realistic for learning
- Doesn't teach database skills
- Can't practice real queries
- No error handling experience

**✅ Real Database Benefits:**
- **Professional experience** with PostgreSQL
- **Real query optimization** and performance
- **Proper error handling** and connection management
- **Production-ready patterns** you'll use at work
- **Portfolio-worthy projects** to show employers

**Companies use real databases, not hardcoded arrays!** 🚀

---

**🏴‍☠️ Ready to become a legendary database developer? ⚔️**
