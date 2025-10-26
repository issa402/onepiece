// ============================================================================
// CHARACTER.JAVA - TEMPLATE FOR YOUR FIRST JPA ENTITY
// ============================================================================
//
// 🎯 PURPOSE: This file is a template to help you create your first Spring Boot
//             JPA entity. It contains ONLY comments and guidance - NO actual code.
//             Your job is to implement the code based on these instructions.
//
// 📚 WHAT YOU'LL LEARN:
//    - What JPA entities are and why we use them
//    - How Spring Boot maps Java classes to database tables
//    - What annotations do and why they're needed
//    - How to design a proper entity class
//
// 🏴‍☠️ WHAT THIS ENTITY REPRESENTS:
//    A One Piece character (Luffy, Zoro, Nami, etc.) that users can trade
//    like stocks in a stock market.
//
// ⚠️ PREREQUISITES - YOU MUST COMPLETE THESE FIRST:
//    1. Create Spring Boot project using Spring Initializr
//    2. Add dependencies: Spring Web, Spring Data JPA, PostgreSQL, Lombok
//    3. Create PostgreSQL database: onepiece_characters
//    4. Configure application.properties with database connection
//    5. Create package structure: com.onepiece.character.model
//
// 📁 FILE LOCATION:
//    This file MUST be created at:
//    character-service/src/main/java/com/onepiece/character/model/Character.java
//
//    DO NOT create this file in the repository root!
//    DO NOT create this as a standalone Java file!
//
// ============================================================================

// ----------------------------------------------------------------------------
// STEP 1: PACKAGE DECLARATION
// ----------------------------------------------------------------------------
// TODO: Declare the package name
//
// SYNTAX:
// package com.onepiece.character.model;
//
// WHY?
// - Packages organize your code into logical groups
// - All entity classes should be in a "model" or "entity" package
// - This MUST match your directory structure
//
// DIRECTORY STRUCTURE:
// src/main/java/
// └── com/
//     └── onepiece/
//         └── character/
//             └── model/
//                 └── Character.java  ← You are here!
//
// If your package declaration doesn't match the directory structure,
// Java will give you a compilation error!


// ----------------------------------------------------------------------------
// STEP 2: IMPORT STATEMENTS
// ----------------------------------------------------------------------------
// TODO: Import the necessary classes from JPA and Lombok
//
// ⚠️ IMPORTANT: Spring Boot 3+ uses jakarta.persistence, NOT javax.persistence!
//
// Check your Spring Boot version:
// - Spring Boot 2.x → use javax.persistence.*
// - Spring Boot 3.x → use jakarta.persistence.*
//
// To check your version, look at pom.xml:
// <parent>
//     <groupId>org.springframework.boot</groupId>
//     <artifactId>spring-boot-starter-parent</artifactId>
//     <version>3.2.0</version>  ← If 3.x, use jakarta
// </parent>
//
// ----------------------------------------------------------------------------
// JPA IMPORTS (choose based on Spring Boot version):
// ----------------------------------------------------------------------------
//
// FOR SPRING BOOT 3.x (RECOMMENDED):
// import jakarta.persistence.Entity;
// import jakarta.persistence.Table;
// import jakarta.persistence.Id;
// import jakarta.persistence.GeneratedValue;
// import jakarta.persistence.GenerationType;
// import jakarta.persistence.Column;
//
// FOR SPRING BOOT 2.x (OLDER):
// import javax.persistence.Entity;
// import javax.persistence.Table;
// import javax.persistence.Id;
// import javax.persistence.GeneratedValue;
// import javax.persistence.GenerationType;
// import javax.persistence.Column;
//
// ----------------------------------------------------------------------------
// LOMBOK IMPORTS (same for all Spring Boot versions):
// ----------------------------------------------------------------------------
//
// import lombok.Data;
// import lombok.NoArgsConstructor;
// import lombok.AllArgsConstructor;
//
// ----------------------------------------------------------------------------
// WHAT EACH IMPORT DOES:
// ----------------------------------------------------------------------------
//
// @Entity - Marks this class as a JPA entity (database table)
// @Table - Specifies the table name in the database
// @Id - Marks a field as the primary key
// @GeneratedValue - Auto-generates ID values
// @GenerationType - Strategy for generating IDs (IDENTITY, SEQUENCE, AUTO)
// @Column - Customizes column properties (name, nullable, length)
//
// @Data - Generates getters, setters, toString(), equals(), hashCode()
// @NoArgsConstructor - Generates no-argument constructor
// @AllArgsConstructor - Generates constructor with all fields
//
// ----------------------------------------------------------------------------
// WHY LOMBOK?
// ----------------------------------------------------------------------------
//
// WITHOUT Lombok, you'd need to write:
// - 8 getter methods (getId(), getName(), getType(), etc.)
// - 8 setter methods (setId(), setName(), setType(), etc.)
// - toString() method (50+ lines)
// - equals() method (30+ lines)
// - hashCode() method (20+ lines)
// - 2 constructors
// TOTAL: ~200 lines of boilerplate code!
//
// WITH Lombok:
// - Just add @Data, @NoArgsConstructor, @AllArgsConstructor
// - Lombok generates everything at compile time
// TOTAL: 3 annotations!
//
// ----------------------------------------------------------------------------
// MAVEN DEPENDENCY CHECK:
// ----------------------------------------------------------------------------
//
// Make sure pom.xml has Lombok dependency:
// <dependency>
//     <groupId>org.projectlombok</groupId>
//     <artifactId>lombok</artifactId>
//     <optional>true</optional>
// </dependency>
//
// If missing, add it and run: mvn clean install


// ----------------------------------------------------------------------------
// STEP 3: CLASS-LEVEL ANNOTATIONS
// ----------------------------------------------------------------------------
// TODO: Add annotations to the class
//
// ANNOTATION 1: @Entity
// - WHAT IT IS: Tells Spring Boot this class represents a database table
// - WHY IT EXISTS: JPA needs to know which classes should be mapped to tables
// - HOW IT WORKS: Spring Boot scans for @Entity classes and creates tables
//
// ANNOTATION 2: @Table(name = "characters")
// - WHAT IT IS: Specifies the exact table name in the database
// - WHY IT EXISTS: By default, JPA uses the class name as table name.
//                  This lets you customize it.
// - HOW IT WORKS: When Hibernate creates the table, it uses this name
// - NOTE: Without this, the table would be named "Character" (class name)
//
// ANNOTATION 3: @Data (Lombok)
// - WHAT IT IS: Generates getters, setters, toString(), equals(), hashCode()
// - WHY IT EXISTS: Saves you from writing 100+ lines of boilerplate code
// - HOW IT WORKS: Lombok processes this at compile time and adds methods
//
// ANNOTATION 4: @NoArgsConstructor (Lombok)
// - WHAT IT IS: Generates a constructor with no parameters
// - WHY IT EXISTS: JPA requires a no-arg constructor to create instances
// - HOW IT WORKS: Creates: public Character() {}
//
// ANNOTATION 5: @AllArgsConstructor (Lombok)
// - WHAT IT IS: Generates a constructor with all fields as parameters
// - WHY IT EXISTS: Convenient for creating objects with all values at once
// - HOW IT WORKS: Creates: public Character(Long id, String name, ...)
//
// SYNTAX:
// @Entity
// @Table(name = "characters")
// @Data
// @NoArgsConstructor
// @AllArgsConstructor
// public class Character {
//     // fields go here
// }


// ----------------------------------------------------------------------------
// STEP 4: PRIMARY KEY FIELD (ID)
// ----------------------------------------------------------------------------
// TODO: Create the primary key field
//
// FIELD: id
// - TYPE: Long (not long - use the wrapper class!)
// - WHY Long? Can be null, and supports large numbers
//
// ANNOTATION 1: @Id
// - WHAT IT IS: Marks this field as the primary key
// - WHY IT EXISTS: Every database table needs a unique identifier
// - HOW IT WORKS: JPA uses this field to identify unique rows
//
// ANNOTATION 2: @GeneratedValue(strategy = GenerationType.IDENTITY)
// - WHAT IT IS: Tells the database to auto-generate ID values
// - WHY IT EXISTS: You don't want to manually assign IDs (1, 2, 3...)
// - HOW IT WORKS: Database auto-increments: 1, 2, 3, 4, 5...
// - STRATEGY OPTIONS:
//   * IDENTITY - Database auto-increment (PostgreSQL, MySQL)
//   * SEQUENCE - Database sequence (Oracle, PostgreSQL)
//   * AUTO - Let JPA choose the best strategy
//   * TABLE - Use a separate table to generate IDs (rarely used)
//
// ANNOTATION 3: @Column(name = "id")
// - WHAT IT IS: Maps this field to a database column
// - WHY IT EXISTS: Lets you customize column properties
// - HOW IT WORKS: Creates a column named "id" in the database
// - NOTE: This is optional if field name matches column name
//
// SYNTAX:
// @Id
// @GeneratedValue(strategy = GenerationType.IDENTITY)
// @Column(name = "id")
// private Long id;


// ----------------------------------------------------------------------------
// STEP 5: CHARACTER NAME FIELD
// ----------------------------------------------------------------------------
// TODO: Create the name field
//
// FIELD: name
// - TYPE: String
// - PURPOSE: Store character's name (e.g., "Monkey D. Luffy")
//
// ANNOTATION: @Column(name = "name", nullable = false, length = 100)
// - name = "name" → Column name in database
// - nullable = false → This field is REQUIRED (cannot be null)
// - length = 100 → Maximum 100 characters
//
// WHY nullable = false?
// - Every character MUST have a name
// - Database will reject INSERT if name is missing
// - This is a business rule: "A character without a name doesn't make sense"
//
// WHY length = 100?
// - Limits the column size in the database
// - Prevents someone from inserting a 10,000 character name
// - Saves database space
//
// SYNTAX:
// @Column(name = "name", nullable = false, length = 100)
// private String name;


// ----------------------------------------------------------------------------
// STEP 6: CHARACTER TYPE FIELD
// ----------------------------------------------------------------------------
// TODO: Create the type field
//
// FIELD: type
// - TYPE: String
// - PURPOSE: Character type (e.g., "Pirate", "Marine", "Revolutionary")
// - EXAMPLES: "Pirate", "Marine", "Warlord", "Revolutionary", "Civilian"
//
// ANNOTATION: @Column(name = "type", nullable = false, length = 50)
//
// ALTERNATIVE (Advanced): You could use an Enum instead of String
// - Create enum: public enum CharacterType { PIRATE, MARINE, WARLORD }
// - Use @Enumerated(EnumType.STRING) annotation
// - BENEFIT: Type safety - can't accidentally set type to "Pizza"
// - For now, String is fine for learning
//
// SYNTAX:
// @Column(name = "type", nullable = false, length = 50)
// private String type;


// ----------------------------------------------------------------------------
// STEP 7: BOUNTY FIELD (PRICE)
// ----------------------------------------------------------------------------
// TODO: Create the bounty field
//
// FIELD: bounty
// - TYPE: Long
// - PURPOSE: Character's bounty in Berries (One Piece currency)
// - EXAMPLES: Luffy = 3,000,000,000, Zoro = 1,111,000,000
// - NOTE: This is also the "price" users pay to buy this character
//
// ANNOTATION: @Column(name = "bounty", nullable = false)
//
// WHY Long instead of Integer?
// - Integer max value: 2,147,483,647 (2.1 billion)
// - Luffy's bounty: 3,000,000,000 (3 billion) - TOO BIG for Integer!
// - Long max value: 9,223,372,036,854,775,807 (plenty of room)
//
// WHY nullable = false?
// - Every character must have a bounty/price
// - Even if bounty is 0 (unknown characters), it should be explicitly 0
//
// SYNTAX:
// @Column(name = "bounty", nullable = false)
// private Long bounty;


// ----------------------------------------------------------------------------
// STEP 8: DEVIL FRUIT FIELD
// ----------------------------------------------------------------------------
// TODO: Create the devilFruit field
//
// FIELD: devilFruit
// - TYPE: String
// - PURPOSE: Name of the Devil Fruit the character ate
// - EXAMPLES: "Gomu Gomu no Mi", "Mera Mera no Mi", null (if no fruit)
//
// ANNOTATION: @Column(name = "devil_fruit", nullable = true, length = 100)
//
// WHY nullable = true?
// - NOT all characters have Devil Fruits (e.g., Zoro, Sanji)
// - This field is OPTIONAL
// - Database allows NULL values
//
// NOTE: Column name is "devil_fruit" (snake_case) but field name is
//       "devilFruit" (camelCase). This is a common Java convention:
//       - Java uses camelCase for variables
//       - Databases use snake_case for columns
//       - JPA handles the mapping automatically
//
// SYNTAX:
// @Column(name = "devil_fruit", nullable = true, length = 100)
// private String devilFruit;


// ----------------------------------------------------------------------------
// STEP 9: CREW FIELD
// ----------------------------------------------------------------------------
// TODO: Create the crew field
//
// FIELD: crew
// - TYPE: String
// - PURPOSE: Name of the crew/organization the character belongs to
// - EXAMPLES: "Straw Hat Pirates", "Marines", "Red Hair Pirates"
//
// ANNOTATION: @Column(name = "crew", nullable = true, length = 100)
//
// WHY nullable = true?
// - Some characters don't belong to any crew
// - This is optional information
//
// SYNTAX:
// @Column(name = "crew", nullable = true, length = 100)
// private String crew;


// ----------------------------------------------------------------------------
// STEP 10: IMAGE URL FIELD
// ----------------------------------------------------------------------------
// TODO: Create the imageUrl field
//
// FIELD: imageUrl
// - TYPE: String
// - PURPOSE: URL to character's image (for frontend display)
// - EXAMPLE: "https://example.com/images/luffy.png"
//
// ANNOTATION: @Column(name = "image_url", nullable = true, length = 500)
//
// WHY length = 500?
// - URLs can be long, especially with query parameters
// - 500 characters should be enough for most URLs
//
// WHY nullable = true?
// - Image is optional (nice to have, but not required)
// - App should work even without images
//
// SYNTAX:
// @Column(name = "image_url", nullable = true, length = 500)
// private String imageUrl;


// ----------------------------------------------------------------------------
// STEP 11: DESCRIPTION FIELD
// ----------------------------------------------------------------------------
// TODO: Create the description field
//
// FIELD: description
// - TYPE: String
// - PURPOSE: Brief description of the character
// - EXAMPLE: "Captain of the Straw Hat Pirates, aims to become Pirate King"
//
// ANNOTATION: @Column(name = "description", nullable = true, length = 1000)
//
// WHY length = 1000?
// - Descriptions can be longer than names
// - 1000 characters allows for detailed descriptions
//
// ALTERNATIVE: Use @Column(columnDefinition = "TEXT")
// - TEXT type in database (unlimited length)
// - Use this if you need very long descriptions
//
// SYNTAX:
// @Column(name = "description", nullable = true, length = 1000)
// private String description;


// ----------------------------------------------------------------------------
// STEP 12: PUTTING IT ALL TOGETHER
// ----------------------------------------------------------------------------
// TODO: Now write the complete class with all fields
//
// Your final class should look like this structure:
//
// ============================================================================
// COMPLETE EXAMPLE (for reference - implement this yourself!)
// ============================================================================
//
// package com.onepiece.character.model;
//
// import jakarta.persistence.*;  // For Spring Boot 3.x
// // OR
// // import javax.persistence.*;  // For Spring Boot 2.x
//
// import lombok.Data;
// import lombok.NoArgsConstructor;
// import lombok.AllArgsConstructor;
//
// @Entity
// @Table(name = "characters")
// @Data
// @NoArgsConstructor
// @AllArgsConstructor
// public class Character {
//
//     @Id
//     @GeneratedValue(strategy = GenerationType.IDENTITY)
//     @Column(name = "id")
//     private Long id;
//
//     @Column(name = "name", nullable = false, length = 100)
//     private String name;
//
//     @Column(name = "type", nullable = false, length = 50)
//     private String type;
//
//     @Column(name = "bounty", nullable = false)
//     private Long bounty;
//
//     @Column(name = "devil_fruit", nullable = true, length = 100)
//     private String devilFruit;
//
//     @Column(name = "crew", nullable = true, length = 100)
//     private String crew;
//
//     @Column(name = "image_url", nullable = true, length = 500)
//     private String imageUrl;
//
//     @Column(name = "description", nullable = true, length = 1000)
//     private String description;
// }
//
// ============================================================================


// ----------------------------------------------------------------------------
// STEP 13: UNDERSTANDING WHAT HAPPENS WHEN YOU RUN THIS
// ----------------------------------------------------------------------------
//
// When you run your Spring Boot application with this entity:
//
// 1. SPRING BOOT STARTUP:
//    - Spring Boot scans for @Entity classes
//    - Finds your Character class
//    - Passes it to Hibernate (JPA implementation)
//
// 2. HIBERNATE CREATES THE TABLE:
//    - Reads all @Column annotations
//    - Generates SQL CREATE TABLE statement:
//
//    CREATE TABLE characters (
//        id BIGSERIAL PRIMARY KEY,
//        name VARCHAR(100) NOT NULL,
//        type VARCHAR(50) NOT NULL,
//        bounty BIGINT NOT NULL,
//        devil_fruit VARCHAR(100),
//        crew VARCHAR(100),
//        image_url VARCHAR(500),
//        description VARCHAR(1000)
//    );
//
// 3. YOU CAN NOW USE THIS ENTITY:
//    - Save characters to database
//    - Query characters from database
//    - Update character data
//    - Delete characters
//
// 4. EXAMPLE USAGE (in a Service class):
//
//    Character luffy = new Character();
//    luffy.setName("Monkey D. Luffy");
//    luffy.setType("Pirate");
//    luffy.setBounty(3000000000L);
//    luffy.setDevilFruit("Gomu Gomu no Mi");
//    luffy.setCrew("Straw Hat Pirates");
//    
//    characterRepository.save(luffy);  // Saves to database!


// ----------------------------------------------------------------------------
// STEP 14: COMMON MISTAKES TO AVOID
// ----------------------------------------------------------------------------
//
// ❌ MISTAKE 1: Using primitive types (int, long) instead of wrapper classes
//    - WRONG: private long id;
//    - RIGHT: private Long id;
//    - WHY? Primitives can't be null, but database IDs can be null before saving
//
// ❌ MISTAKE 2: Forgetting @Entity annotation
//    - Spring Boot won't recognize this as a database entity
//    - No table will be created
//
// ❌ MISTAKE 3: Forgetting @Id annotation
//    - JPA requires every entity to have a primary key
//    - You'll get an error: "No identifier specified for entity"
//
// ❌ MISTAKE 4: Using wrong GenerationType
//    - IDENTITY works for PostgreSQL, MySQL
//    - SEQUENCE works for Oracle, PostgreSQL
//    - Use AUTO if unsure (JPA will choose)
//
// ❌ MISTAKE 5: Making required fields nullable
//    - If a field is essential (like name), use nullable = false
//    - This enforces data integrity at the database level
//
// ❌ MISTAKE 6: Not setting length for String fields
//    - Default is VARCHAR(255)
//    - Be explicit about your requirements


// ----------------------------------------------------------------------------
// STEP 15: TESTING YOUR ENTITY
// ----------------------------------------------------------------------------
//
// After creating this entity, test it by:
//
// 1. Run your Spring Boot application
// 2. Check the console for Hibernate SQL statements
// 3. Connect to PostgreSQL and verify the table was created:
//    - psql -U postgres -d onepiece_characters
//    - \dt (list tables)
//    - \d characters (describe characters table)
//
// 4. Create a simple test in CharacterController:
//    @PostMapping("/test")
//    public Character test() {
//        Character luffy = new Character();
//        luffy.setName("Luffy");
//        luffy.setType("Pirate");
//        luffy.setBounty(3000000000L);
//        return characterRepository.save(luffy);
//    }
//
// 5. Call the endpoint with Postman:
//    POST http://localhost:8081/api/characters/test
//
// 6. Check the database:
//    SELECT * FROM characters;


// ----------------------------------------------------------------------------
// STEP 16: MAVEN DEPENDENCIES REQUIRED
// ----------------------------------------------------------------------------
//
// Make sure your pom.xml contains these dependencies:
//
// ============================================================================
// REQUIRED DEPENDENCIES IN pom.xml
// ============================================================================
//
// <?xml version="1.0" encoding="UTF-8"?>
// <project xmlns="http://maven.apache.org/POM/4.0.0"
//          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
//          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
//          https://maven.apache.org/xsd/maven-4.0.0.xsd">
//     <modelVersion>4.0.0</modelVersion>
//
//     <parent>
//         <groupId>org.springframework.boot</groupId>
//         <artifactId>spring-boot-starter-parent</artifactId>
//         <version>3.2.0</version>  <!-- Or latest stable version -->
//         <relativePath/>
//     </parent>
//
//     <groupId>com.onepiece</groupId>
//     <artifactId>character-service</artifactId>
//     <version>0.0.1-SNAPSHOT</version>
//     <name>character-service</name>
//     <description>One Piece Character Trading Service</description>
//
//     <properties>
//         <java.version>17</java.version>
//     </properties>
//
//     <dependencies>
//         <!-- Spring Boot Web - For REST APIs -->
//         <dependency>
//             <groupId>org.springframework.boot</groupId>
//             <artifactId>spring-boot-starter-web</artifactId>
//         </dependency>
//
//         <!-- Spring Data JPA - For database operations -->
//         <dependency>
//             <groupId>org.springframework.boot</groupId>
//             <artifactId>spring-boot-starter-data-jpa</artifactId>
//         </dependency>
//
//         <!-- PostgreSQL Driver - To connect to PostgreSQL -->
//         <dependency>
//             <groupId>org.postgresql</groupId>
//             <artifactId>postgresql</artifactId>
//             <scope>runtime</scope>
//         </dependency>
//
//         <!-- Lombok - Reduces boilerplate code -->
//         <dependency>
//             <groupId>org.projectlombok</groupId>
//             <artifactId>lombok</artifactId>
//             <optional>true</optional>
//         </dependency>
//
//         <!-- Spring Boot DevTools - Hot reload (optional) -->
//         <dependency>
//             <groupId>org.springframework.boot</groupId>
//             <artifactId>spring-boot-devtools</artifactId>
//             <scope>runtime</scope>
//             <optional>true</optional>
//         </dependency>
//
//         <!-- Spring Boot Test - For testing -->
//         <dependency>
//             <groupId>org.springframework.boot</groupId>
//             <artifactId>spring-boot-starter-test</artifactId>
//             <scope>test</scope>
//         </dependency>
//     </dependencies>
//
//     <build>
//         <plugins>
//             <plugin>
//                 <groupId>org.springframework.boot</groupId>
//                 <artifactId>spring-boot-maven-plugin</artifactId>
//                 <configuration>
//                     <excludes>
//                         <exclude>
//                             <groupId>org.projectlombok</groupId>
//                             <artifactId>lombok</artifactId>
//                         </exclude>
//                     </excludes>
//                 </configuration>
//             </plugin>
//         </plugins>
//     </build>
// </project>
//
// ============================================================================
// HOW TO VERIFY DEPENDENCIES ARE INSTALLED:
// ============================================================================
//
// 1. Open terminal in project root (where pom.xml is)
// 2. Run: mvn dependency:tree
// 3. You should see all dependencies listed
// 4. If any are missing, run: mvn clean install
//
// ============================================================================

// ----------------------------------------------------------------------------
// STEP 17: APPLICATION.PROPERTIES CONFIGURATION
// ----------------------------------------------------------------------------
//
// Make sure src/main/resources/application.properties contains:
//
// ============================================================================
// REQUIRED CONFIGURATION IN application.properties
// ============================================================================
//
// # Server Configuration
// server.port=8081
//
// # Database Configuration
// spring.datasource.url=jdbc:postgresql://localhost:5432/onepiece_characters
// spring.datasource.username=postgres
// spring.datasource.password=postgres
// spring.datasource.driver-class-name=org.postgresql.Driver
//
// # JPA/Hibernate Configuration
// spring.jpa.hibernate.ddl-auto=update
// spring.jpa.show-sql=true
// spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.PostgreSQLDialect
// spring.jpa.properties.hibernate.format_sql=true
//
// # Logging (for debugging)
// logging.level.org.hibernate.SQL=DEBUG
// logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE
//
// ============================================================================
// WHAT THESE SETTINGS MEAN:
// ============================================================================
//
// server.port=8081
//   → Your service will run on http://localhost:8081
//
// spring.datasource.url=jdbc:postgresql://localhost:5432/onepiece_characters
//   → Connect to PostgreSQL database named "onepiece_characters"
//   → Database is running on localhost:5432
//
// spring.datasource.username=postgres
// spring.datasource.password=postgres
//   → Database credentials (change if yours are different)
//
// spring.jpa.hibernate.ddl-auto=update
//   → Automatically create/update database tables
//   → Options: create, create-drop, update, validate, none
//   → Use "update" for development (keeps existing data)
//   → Use "validate" for production (doesn't modify schema)
//
// spring.jpa.show-sql=true
//   → Print SQL queries to console (great for learning!)
//   → You'll see: INSERT INTO characters (...) VALUES (...)
//
// ============================================================================

// ----------------------------------------------------------------------------
// STEP 18: NEXT STEPS AFTER CHARACTER.JAVA
// ----------------------------------------------------------------------------
//
// After completing this Character entity, you'll create:
//
// 1. CharacterRepository.java
//    - Location: src/main/java/com/onepiece/character/repository/
//    - Interface that extends JpaRepository<Character, Long>
//    - Provides CRUD operations automatically (save, findById, findAll, delete)
//    - Add custom query methods (findByType, findByNameContaining)
//    - No implementation needed - Spring Data JPA generates it!
//
// 2. CharacterService.java
//    - Location: src/main/java/com/onepiece/character/service/
//    - Business logic layer
//    - Uses CharacterRepository to access database
//    - Handles exceptions, validation, business rules
//    - Methods: getAllCharacters(), getCharacterById(), createCharacter(), etc.
//
// 3. CharacterController.java
//    - Location: src/main/java/com/onepiece/character/controller/
//    - REST API endpoints
//    - Receives HTTP requests from frontend/Postman
//    - Calls CharacterService
//    - Returns JSON responses
//    - Endpoints: GET /api/characters, POST /api/characters, etc.
//
// 4. Exception Handling
//    - Create custom exceptions (CharacterNotFoundException)
//    - Create GlobalExceptionHandler with @ControllerAdvice
//    - Return proper HTTP status codes (404, 400, 500)
//
// 5. Validation
//    - Add @Valid, @NotNull, @NotBlank annotations
//    - Validate input before saving to database
//    - Return validation errors to client
//
// 6. Testing
//    - Write unit tests for CharacterService
//    - Write integration tests for CharacterController
//    - Use JUnit 5 and Mockito
//
// ============================================================================
// FINAL CHECKLIST BEFORE CREATING CHARACTER.JAVA:
// ============================================================================
//
// [ ] Java JDK 17+ installed (java -version)
// [ ] Maven installed (mvn -version)
// [ ] PostgreSQL installed and running
// [ ] Spring Boot project created using Spring Initializr
// [ ] pom.xml contains all required dependencies
// [ ] PostgreSQL database "onepiece_characters" created
// [ ] application.properties configured with database connection
// [ ] Package structure created: com.onepiece.character.model
// [ ] IDE (IntelliJ IDEA) opened with project loaded
// [ ] Dependencies downloaded (mvn clean install)
//
// If ALL checkboxes are checked, you're ready to create Character.java!
//
// Good luck! Ask me questions if you get stuck on any Spring Boot concepts!
//
// ============================================================================

