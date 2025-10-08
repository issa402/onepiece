"""
🏴‍☠️ DATABASE SETUP SCRIPT - MYSQL CONNECTION & INITIALIZATION
Your mission: Create a script to set up your MySQL database and populate it with One Piece data

WHAT YOU'RE BUILDING:
- MySQL database connection
- Table creation and schema setup
- Sample data insertion
- Database health checks
- Error handling for database operations

LEARNING OBJECTIVES:
- MySQL database operations
- Python database connectivity
- SQL execution from Python
- Transaction management
- Error handling in database operations
"""

# TODO 1: IMPORT STATEMENTS
# You need these libraries:
# - pymysql (MySQL connector)
# - os (environment variables)
# - sys (system operations)
# - logging (error tracking)
# - dotenv (load_dotenv)


# WRITE YOUR IMPORTS HERE:
import os
import pymysql
import sys 
import logging

from dotenv import load_dotenv

# TODO 2: LOAD ENVIRONMENT VARIABLES
# Load database credentials from .env file
load_dotenv()

# TODO 3: DATABASE CONFIGURATION
# Set up your database connection parameters:
# DB_HOST = os.getenv('DB_HOST', 'localhost')
# DB_PORT = int(os.getenv('DB_PORT', 3306))
# DB_USER = os.getenv('DB_USER', 'root')
# DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
# DB_NAME = os.getenv('DB_NAME', 'onepiece_market')

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 3306))
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'onepiece123' )
DB_NAME = os.getenv('DB_NAME', 'onepiece_market')


# TODO 4: CREATE DATABASE CONNECTION FUNCTION
# def create_connection():
#     """Create and return MySQL database connection"""
#     try:
#         # Create connection to MySQL server (without specifying database)
#         # Use pymysql.connect() with host, port, user, password
#         # Return the connection object
#     except Exception as e:
#         # Log error and return None
def create_connection(db=DB_NAME):
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=db,
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.MySQLError as e:
        logging.error(f"Failed to connect to MySQL: {e}", exc_info=True)
        return None
        

# TODO 5: CREATE DATABASE FUNCTION
# def create_database(connection):
#     """Create the onepiece_market database if it doesn't exist"""
#     try:
#         # Create cursor from connection
#         # Execute SQL: CREATE DATABASE IF NOT EXISTS onepiece_market
#         # Commit the transaction
#         # Close cursor
#     except Exception as e:
#         # Handle errors and rollback if needed
def create_database(connection):
    """
    Connects to MySQL server (no specific DB), creates onepiece_market if it doesn't exist.
    """
    # 1. Connect to MySQL server without selecting a database
    conn = create_connection(db=None)
    if conn is None:
        sys.exit("❌ Could not connect to MySQL server. Aborting database creation.")

    try:
        with conn.cursor() as cur:
            # 2. Create the database if it doesn't already exist
            cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            logging.info(f"✅ Database `{DB_NAME}` is ready (created or already existed).")

        # 3. Commit the CREATE DATABASE
        conn.commit()

    except pymysql.MySQLError as e:
        logging.error(f"❌ Failed to create database `{DB_NAME}`: {e}", exc_info=True)
        # Roll back in case CREATE DATABASE partially applied (rare, but safe)
        conn.rollback()

    finally:
        # 4. Ensure the connection is closed
        conn.close()  


# TODO 6: EXECUTE SQL FILE FUNCTION
# def execute_sql_file(connection, file_path):
#     """Execute SQL commands from a file"""
#     try:
#         # Read the SQL file
#         # Split into individual statements
#         # Execute each statement
#         # Commit changes
#     except Exception as e:
#         # Handle errors and rollback
def execute_sql_file(connection, file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip() and not stmt.strip().startswith('--')]

        with connection.cursor() as cursor:
            for stmt in statements:
                cursor.execute(stmt)

        connection.commit()
        logging.info(f"Successfully executed SQL file: {file_path}")

    except pymysql.MySQLError as e:
        logging.error(f"Error executing sql file '{file_path}': {e}", exc_info=True)
        connection.rollback()
        raise

    except FileNotFoundError:
        logging.error(f"SQL file not found: {file_path}", exc_info=True)
        raise

    except Exception as e:
        logging.error(f"Unexpected error during SQL execution: {e}", exc_info=True)
        connection.rollback()
        raise



# TODO 7: CHECK TABLE EXISTS FUNCTION
# def check_table_exists(connection, table_name):
#     """Check if a table exists in the database"""
#     try:
#         # Create cursor
#         # Execute: SHOW TABLES LIKE 'table_name'
#         # Return True if table exists, False otherwise
#     except Exception as e:
#         # Handle errors
def check_table_exists(connection, table_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES LIKE %s", (table_name,))
            result = cursor.fetchone()
            return result is not None
    except pymysql.MySQLError as e:
        logging.error(f"Error checking table '{table_name}': {e}", exc_info=True)
        return False


# TODO 8: GET TABLE COUNT FUNCTION
# def get_table_count(connection, table_name):
#     """Get the number of records in a table"""
#     try:
#         # Create cursor
#         # Execute: SELECT COUNT(*) FROM table_name
#         # Return the count
#     except Exception as e:
#         # Handle errors and return 0
def get_table_count(connection, table_name):
    if not check_table_exists(connection, table_name):
        logging.warning(f"Table '{table_name}' does not exist")
        return None

    try:
        with connection.cursor() as cursor:
            sql = f"SELECT COUNT(*) AS cnt FROM `{table_name}`;"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row["cnt"] if row and "cnt" in row else 0
    except pymysql.MySQLError as e:
        logging.error(f"No count was found in table '{table_name}': {e}", exc_info=True)
        return None


# TODO 9: MAIN SETUP FUNCTION
# def setup_database():
#     """Main function to set up the entire database"""
#     print("🏴‍☠️ Starting One Piece Database Setup...")
#     
#     # Step 1: Create connection to MySQL server
#     # Step 2: Create the database
#     # Step 3: Connect to the specific database
#     # Step 4: Execute schema.sql to create tables
#     # Step 5: Execute sample_data.sql to insert data
#     # Step 6: Verify setup by checking table counts
#     # Step 7: Close connections
def setup_database():
    print("🏴‍☠️ Starting One Piece Database Setup...")
    conn_server = create_connection(db=None)
    if conn_server is None:
        sys.exit("Could not connect")
    
    create_database(conn_server)
    conn_server.close()

    conn = create_connection(db=DB_NAME)
    if conn is None:
        sys.exit("Could not connect")

    try:
        execute_sql_file(conn, "../../database/schema.sql")

        execute_sql_file(conn, "../../database/sample_data.sql")

        table_to_check = [
             "characters",
            "users",
            "portfolios",
            "trades",
            "sentiment_data",
            "price_history",
            "market_events"

        ]
        for tbl in table_to_check:
            count = get_table_count(conn, tbl)
            print(f"Table '{tbl}' has {count} rows")

    finally:
        conn.close()
        print("Database setup complete")

    


# TODO 10: DATABASE HEALTH CHECK FUNCTION
# def health_check():
#     """Check if database is properly set up and accessible"""
#     try:
#         # Connect to database
#         # Check if all required tables exist
#         # Check if tables have data
#         # Return health status
#     except Exception as e:
#         # Return unhealthy status
# TODO 10: HEALTH CHECK ENDPOINT
# List all tables your script creates or relies on
REQUIRED_TABLES = [
    "characters",
    "users",
    "portfolios",
    "trades",
    "sentiment_data",
    "price_history",
    "market_events",
]

def health_check():
    """
    Returns (True, {...}) if all tables exist and are accessible.
    Otherwise returns (False, {table: 'missing' or 'empty', ...}).
    """
    conn = create_connection()           # uses DB_NAME by default
    if conn is None:
        return False, {"connection": "failed"}

    problems = {}
    for table in REQUIRED_TABLES:
        if not check_table_exists(conn, table):
            problems[table] = "missing"
            continue

        count = get_table_count(conn, table)
        # You could treat count==0 as a warning instead. Adjust as you like.
        if count is None:
            problems[table] = "error_checking_count"
        elif count == 0:
            problems[table] = "empty"

    conn.close()

    if problems:
        return False, problems
    else:
        return True, {t: "ok" for t in REQUIRED_TABLES}



# TODO 11: RESET DATABASE FUNCTION
# def reset_database():
#     """Drop and recreate the database (for development)"""
#     # WARNING: This will delete all data!
#     try:
#         # Connect to MySQL server
#         # Drop database if exists
#         # Recreate database
#         # Run setup again
#     except Exception as e:
#         # Handle errors
def reset_database():
    """
    Drop and recreate the onepiece_market database (development only).
    WARNING: This will delete all data!
    """
    # 1. Connect to MySQL server without specifying a database
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.MySQLError as e:
        logging.error(f"❌ Cannot connect to MySQL server for reset: {e}", exc_info=True)
        sys.exit(1)

    # 2. Drop and recreate the database
    try:
        with conn.cursor() as cur:
            cur.execute(f"DROP DATABASE IF EXISTS `{DB_NAME}`;")
            logging.info(f"🗑️ Dropped database `{DB_NAME}` (if existed).")

            cur.execute(
                f"CREATE DATABASE `{DB_NAME}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
            )
            logging.info(f"✅ Recreated database `{DB_NAME}`.")
        conn.commit()
    except pymysql.MySQLError as e:
        logging.error(f"❌ Error during reset: {e}", exc_info=True)
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()

    # 3. Re-run entire setup (schema + sample data)
    logging.info("🔄 Running full database setup...")
    setup_database()
    logging.info("🎉 Reset and setup complete.")



# TODO 12: MAIN EXECUTION BLOCK
# if __name__ == '__main__':
#     # Parse command line arguments
#     # if 'reset' argument: call reset_database()
#     # elif 'health' argument: call health_check()
#     # else: call setup_database()
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="OnePiece DB Utility: setup, reset, or health check"
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Drop & rebuild the database (DESTRUCTIVE!)'
    )
    parser.add_argument(
        '--health',
        action='store_true',
        help='Run a script-level database health check'
    )
    args = parser.parse_args()

    if args.reset:
        # Drop & recreate, then seed schema + data
        reset_database()
        sys.exit(0)

    if args.health:
        # Returns (bool, details)
        healthy, details = health_check()
        if healthy:
            print("✅ Database is healthy:", details)
            sys.exit(0)
        else:
            print("❌ Database health check failed:", details)
            sys.exit(1)

    # Default: setup (create DB, tables, seed data)
    setup_database()
    sys.exit(0)


"""
🎯 WHAT EACH FUNCTION DOES:

create_connection(): Connects to MySQL server
create_database(): Creates the onepiece_market database
execute_sql_file(): Runs SQL commands from schema.sql and sample_data.sql
check_table_exists(): Verifies tables were created
get_table_count(): Counts records in tables
setup_database(): Main orchestrator function
health_check(): Verifies everything is working
reset_database(): Cleans and rebuilds database

🚀 PYMYSQL CONCEPTS YOU'LL LEARN:

1. pymysql.connect() - Create database connection
2. connection.cursor() - Create cursor for executing SQL
3. cursor.execute() - Run SQL commands
4. connection.commit() - Save changes to database
5. connection.rollback() - Undo changes on error
6. cursor.fetchone() - Get single result
7. cursor.fetchall() - Get all results

📚 SQL CONCEPTS:

1. CREATE DATABASE - Create new database
2. USE database - Switch to database
3. SHOW TABLES - List all tables
4. SELECT COUNT(*) - Count records
5. Transaction management (commit/rollback)

🔧 ERROR HANDLING:

1. try/except blocks for database operations
2. Connection error handling
3. SQL execution error handling
4. Proper resource cleanup (close cursors/connections)

USAGE EXAMPLES:
python database_setup.py          # Normal setup
python database_setup.py reset    # Reset database
python database_setup.py health   # Check database health

NEXT FILE AFTER THIS: Create .env configuration file! 🚀
"""
