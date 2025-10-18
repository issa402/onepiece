# Quick Start Guide - Java Enterprise Tutorial

## 🚀 Run All Tutorials at Once

To run all 8 topic demos in sequence, compile and run the comprehensive demo:

```bash
# Navigate to the directory
cd learning-modules/33-java-spring-boot-enterprise

# Compile the Java file
javac 01-java-spring-boot-enterprise-coding-lab.java

# Run the comprehensive demo
java ComprehensiveTutorialDemo
```

This will execute all 8 topic demos and show you the complete output!

---

## 📋 Run Individual Topic Demos

If you want to run specific topics, you can execute individual demo classes:

### Topic 1: Exception Handling
```java
java ExceptionHandlingDemo
```

### Topic 2: Generics
```java
java GenericsDemo
```

### Topic 3: Lambda Expressions and Stream API
```java
java LambdaStreamDemo
```

### Topic 4: Multithreading and Concurrency
```java
java MultithreadingDemo
```

### Topic 5: File I/O and Serialization
```java
java FileIODemo
```

### Topic 6: Design Patterns
```java
java DesignPatternsDemo
```

### Topic 7: Spring Framework
```java
java SpringFrameworkDemo
```

### Topic 8: Database Integration
```java
java DatabaseIntegrationDemo
```

---

## 🏗️ Building a Real Spring Boot Application

The Spring Framework and Database Integration topics show you the structure, but to actually run a Spring Boot application with cloud database:

### Step 1: Create Spring Boot Project

Visit [Spring Initializr](https://start.spring.io/) and configure:
- **Project**: Maven
- **Language**: Java
- **Spring Boot**: 3.2.x (latest stable)
- **Dependencies**: 
  - Spring Web
  - Spring Data JPA
  - PostgreSQL Driver
  - Validation

### Step 2: Project Structure
```
onepiece-trading/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/onepiece/trading/
│   │   │       ├── OnePieceTradingApplication.java
│   │   │       ├── entity/
│   │   │       │   ├── DevilFruitEntity.java
│   │   │       │   ├── UserEntity.java
│   │   │       │   └── TradeEntity.java
│   │   │       ├── repository/
│   │   │       │   ├── DevilFruitRepository.java
│   │   │       │   └── UserRepository.java
│   │   │       ├── service/
│   │   │       │   ├── DevilFruitService.java
│   │   │       │   └── TradeService.java
│   │   │       ├── controller/
│   │   │       │   ├── DevilFruitController.java
│   │   │       │   └── TradeController.java
│   │   │       └── dto/
│   │   │           ├── DevilFruitDTO.java
│   │   │           └── ApiResponseDTO.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
└── pom.xml
```

### Step 3: Configure Database (application.properties)

**For PostgreSQL on Heroku (Free Tier):**
```properties
spring.datasource.url=${DATABASE_URL}
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

**For PostgreSQL on AWS RDS:**
```properties
spring.datasource.url=jdbc:postgresql://your-db.rds.amazonaws.com:5432/onepiece
spring.datasource.username=${DB_USERNAME}
spring.datasource.password=${DB_PASSWORD}
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=update
```

**For Local PostgreSQL (Development):**
```properties
spring.datasource.url=jdbc:postgresql://localhost:5432/onepiece
spring.datasource.username=postgres
spring.datasource.password=yourpassword
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
```

### Step 4: Run the Application
```bash
# Using Maven
./mvnw spring-boot:run

# Or using Gradle
./gradlew bootRun
```

Your API will be available at: `http://localhost:8080`

---

## 🌐 Setting Up Cloud Database

### Option 1: Heroku PostgreSQL (Easiest - Free Tier)

```bash
# Install Heroku CLI
# Then:
heroku login
heroku create onepiece-trading
heroku addons:create heroku-postgresql:hobby-dev
heroku config:get DATABASE_URL
```

The DATABASE_URL is automatically set as an environment variable!

### Option 2: AWS RDS PostgreSQL

1. Go to AWS Console → RDS
2. Click "Create database"
3. Choose PostgreSQL
4. Select "Free tier" template
5. Set database name: `onepiece`
6. Set master username and password
7. Configure security group to allow your IP
8. Click "Create database"
9. Copy the endpoint URL
10. Update application.properties

### Option 3: Google Cloud SQL

```bash
# Install gcloud CLI
gcloud sql instances create onepiece-db \
    --database-version=POSTGRES_14 \
    --tier=db-f1-micro \
    --region=us-central1

gcloud sql databases create onepiece --instance=onepiece-db
```

---

## 🧪 Testing Your API

### Using cURL:

**Create a Devil Fruit:**
```bash
curl -X POST http://localhost:8080/api/fruits \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gomu Gomu no Mi",
    "type": "Paramecia",
    "price": 1000000
  }'
```

**Get All Fruits:**
```bash
curl http://localhost:8080/api/fruits
```

**Get Fruit by ID:**
```bash
curl http://localhost:8080/api/fruits/1
```

**Update Fruit:**
```bash
curl -X PUT http://localhost:8080/api/fruits/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gomu Gomu no Mi",
    "type": "Paramecia",
    "price": 1500000
  }'
```

**Delete Fruit:**
```bash
curl -X DELETE http://localhost:8080/api/fruits/1
```

### Using Postman:

1. Download Postman
2. Create a new collection "One Piece Trading"
3. Add requests for each endpoint
4. Test your API!

---

## 📦 Dependencies (pom.xml)

```xml
<dependencies>
    <!-- Spring Boot Starter Web -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- Spring Boot Starter Data JPA -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    
    <!-- PostgreSQL Driver -->
    <dependency>
        <groupId>org.postgresql</groupId>
        <artifactId>postgresql</artifactId>
        <scope>runtime</scope>
    </dependency>
    
    <!-- Validation -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-validation</artifactId>
    </dependency>
    
    <!-- Lombok (Optional - reduces boilerplate) -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    
    <!-- Spring Boot Starter Test -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

---

## 🎯 Learning Path

1. **Week 1**: Topics 1-3 (Exception Handling, Generics, Lambdas)
2. **Week 2**: Topics 4-5 (Multithreading, File I/O)
3. **Week 3**: Topic 6 (Design Patterns)
4. **Week 4**: Topics 7-8 (Spring Framework, Database Integration)
5. **Week 5**: Build your own complete application
6. **Week 6**: Deploy to cloud and add advanced features

---

## 💡 Tips for Success

1. **Run the code** - Don't just read, execute and experiment!
2. **Modify examples** - Change values, add features, break things and fix them
3. **Build projects** - Apply what you learn to real projects
4. **Read documentation** - Spring Boot docs are excellent
5. **Join communities** - Stack Overflow, Reddit r/java, Spring community
6. **Practice daily** - Consistency is key

---

## 🆘 Troubleshooting

### "Class not found" error
Make sure you compiled the file first:
```bash
javac 01-java-spring-boot-enterprise-coding-lab.java
```

### Database connection error
- Check your database is running
- Verify connection URL, username, password
- Check firewall/security group settings
- Ensure database driver is in classpath

### Port 8080 already in use
Change the port in application.properties:
```properties
server.port=8081
```

---

## 📞 Need Help?

- Check the TUTORIAL_GUIDE.md for detailed explanations
- Review the code comments - they explain everything
- Search Stack Overflow for specific errors
- Join Spring Boot communities

---

**You're all set! Start with the comprehensive demo and work through each topic. Happy coding! 🚀**

