/*
🏴‍☠️ MODULE 33: JAVA SPRING BOOT ENTERPRISE - BIG TECH BACKEND MASTERY
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
ENTERPRISE-LEVEL Java Spring Boot backend like Netflix, Amazon, Google, LinkedIn!
This is the EXACT Java stack that powers the world's biggest tech companies!

📚 LEARNING OBJECTIVES:
- Spring Boot fundamentals (Netflix/Amazon standard)
- RESTful API development (Enterprise patterns)
- JPA/Hibernate ORM (Database layer like Google)
- Spring Security (Authentication like LinkedIn)
- Microservices architecture (Netflix pattern)
- Enterprise design patterns (Big tech standards)
- Production deployment (Docker + Kubernetes)
- Testing strategies (Unit + Integration)

🔗 INTEGRATES WITH YOUR ONE PIECE PROJECT:
- REPLACES: Your Node.js services with Java equivalents
- SCALES: To enterprise level like Netflix/Amazon
- CONNECTS: To your existing database and frontend
- DEMONSTRATES: Why big tech chooses Java for core services

💰 CAREER IMPACT: +$50K-$100K (Java Spring Boot is highest paid backend skill!)

🎯 BIG TECH COMPANIES USING JAVA SPRING BOOT:
- Netflix: Core streaming services, billing, user management
- Amazon: E-commerce backend, AWS services
- Google: Enterprise services, internal tools
- LinkedIn: Social platform backend, messaging
- Uber: Some core services, enterprise features
- Twitter: Backend services, API layer
*/

// TODO 1: SPRING BOOT APPLICATION SETUP (NETFLIX PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create Spring Boot application like Netflix

NETFLIX'S JAVA ARCHITECTURE:
- Spring Boot for microservices
- Spring Cloud for service discovery
- Spring Data JPA for database access
- Spring Security for authentication
- Docker containers for deployment

YOUR ONE PIECE TRADING SERVICE IN JAVA:
*/

package com.onepiece.trading;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.EnableEurekaClient;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/**
 * 🏴‍☠️ One Piece Trading Platform - Java Spring Boot Version
 * 
 * This is how Netflix, Amazon, and Google structure their Java applications:
 * - @SpringBootApplication: Auto-configuration and component scanning
 * - @EnableEurekaClient: Service discovery (Netflix pattern)
 * - @EnableJpaRepositories: Database access layer
 * - @EnableTransactionManagement: ACID transactions for trading
 */
@SpringBootApplication
@EnableEurekaClient  // Netflix service discovery
@EnableJpaRepositories
@EnableTransactionManagement
public class OnePieceTradingApplication {
    
    public static void main(String[] args) {
        SpringApplication.run(OnePieceTradingApplication.class, args);
        System.out.println("🏴‍☠️ One Piece Trading Platform Started!");
        System.out.println("🚀 Enterprise Java Backend Running on Spring Boot");
    }
}

// TODO 2: ENTITY MODELS (JPA/HIBERNATE - GOOGLE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create JPA entities like Google's enterprise systems

GOOGLE'S DATA LAYER APPROACH:
- JPA entities for object-relational mapping
- Hibernate for database operations
- Validation annotations for data integrity
- Audit trails for enterprise compliance

CHARACTER ENTITY (MAPS TO YOUR DATABASE):
*/

package com.onepiece.trading.entity;

import javax.persistence.*;
import javax.validation.constraints.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.List;

/**
 * 🏴‍☠️ Character Entity - Enterprise JPA Model
 * 
 * This maps to your existing character table but with enterprise features:
 * - JPA annotations for ORM mapping
 * - Validation constraints for data integrity
 * - Audit fields for compliance
 * - Relationships for complex queries
 */
@Entity
@Table(name = "characters", indexes = {
    @Index(name = "idx_character_name", columnList = "name"),
    @Index(name = "idx_character_crew", columnList = "crew"),
    @Index(name = "idx_character_price", columnList = "current_price")
})
public class Character {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @NotBlank(message = "Character name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    @Column(nullable = false, unique = true)
    private String name;
    
    @NotBlank(message = "Crew is required")
    @Column(nullable = false)
    private String crew;
    
    @NotNull(message = "Current price is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    @Column(name = "current_price", precision = 10, scale = 2)
    private BigDecimal currentPrice;
    
    @Column(name = "devil_fruit")
    private String devilFruit;
    
    @Column(name = "bounty", precision = 15, scale = 0)
    private BigDecimal bounty;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private CharacterRarity rarity;
    
    @Column(name = "image_url")
    private String imageUrl;
    
    @Column(columnDefinition = "TEXT")
    private String description;
    
    // Audit fields (Enterprise requirement)
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
    
    @Column(name = "created_by")
    private String createdBy;
    
    // Relationships (Enterprise data modeling)
    @OneToMany(mappedBy = "character", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Trade> trades;
    
    @OneToMany(mappedBy = "character", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<PriceHistory> priceHistory;
    
    // Constructors
    public Character() {}
    
    public Character(String name, String crew, BigDecimal currentPrice, CharacterRarity rarity) {
        this.name = name;
        this.crew = crew;
        this.currentPrice = currentPrice;
        this.rarity = rarity;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }
    
    // JPA Lifecycle callbacks (Enterprise audit trail)
    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
    }
    
    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }
    
    // Getters and Setters (Enterprise bean pattern)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    
    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }
    
    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }
    
    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }
    
    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }
    
    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }
    
    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }
    
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getUpdatedAt() { return updatedAt; }
    
    public String getCreatedBy() { return createdBy; }
    public void setCreatedBy(String createdBy) { this.createdBy = createdBy; }
    
    public List<Trade> getTrades() { return trades; }
    public void setTrades(List<Trade> trades) { this.trades = trades; }
    
    public List<PriceHistory> getPriceHistory() { return priceHistory; }
    public void setPriceHistory(List<PriceHistory> priceHistory) { this.priceHistory = priceHistory; }
    
    // Enterprise toString method
    @Override
    public String toString() {
        return String.format("Character{id=%d, name='%s', crew='%s', price=%s, rarity=%s}", 
                           id, name, crew, currentPrice, rarity);
    }
}

// Character Rarity Enum (Enterprise type safety)
enum CharacterRarity {
    COMMON("Common", 1.0),
    UNCOMMON("Uncommon", 1.5),
    RARE("Rare", 2.0),
    EPIC("Epic", 3.0),
    LEGENDARY("Legendary", 5.0),
    MYTHICAL("Mythical", 10.0);
    
    private final String displayName;
    private final double multiplier;
    
    CharacterRarity(String displayName, double multiplier) {
        this.displayName = displayName;
        this.multiplier = multiplier;
    }
    
    public String getDisplayName() { return displayName; }
    public double getMultiplier() { return multiplier; }
}

// TODO 3: REPOSITORY LAYER (SPRING DATA JPA - AMAZON PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create repository layer like Amazon's data access

AMAZON'S REPOSITORY PATTERN:
- Spring Data JPA for automatic query generation
- Custom queries for complex business logic
- Pagination and sorting for large datasets
- Caching for performance optimization

CHARACTER REPOSITORY:
*/

package com.onepiece.trading.repository;

import com.onepiece.trading.entity.Character;
import com.onepiece.trading.entity.CharacterRarity;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Repository;

import java.math.BigDecimal;
import java.util.List;
import java.util.Optional;

/**
 * 🏴‍☠️ Character Repository - Enterprise Data Access Layer
 * 
 * This is how Amazon structures their data access:
 * - JpaRepository for CRUD operations
 * - Custom queries for business logic
 * - Caching for performance
 * - Pagination for large datasets
 */
@Repository
public interface CharacterRepository extends JpaRepository<Character, Long> {
    
    // Spring Data JPA automatic query generation
    Optional<Character> findByName(String name);
    
    List<Character> findByCrew(String crew);
    
    List<Character> findByRarity(CharacterRarity rarity);
    
    Page<Character> findByCrewContainingIgnoreCase(String crew, Pageable pageable);
    
    // Custom queries for complex business logic (Amazon pattern)
    @Query("SELECT c FROM Character c WHERE c.currentPrice BETWEEN :minPrice AND :maxPrice")
    List<Character> findByPriceRange(@Param("minPrice") BigDecimal minPrice, 
                                   @Param("maxPrice") BigDecimal maxPrice);
    
    @Query("SELECT c FROM Character c WHERE c.bounty > :minBounty ORDER BY c.bounty DESC")
    List<Character> findHighBountyCharacters(@Param("minBounty") BigDecimal minBounty);
    
    @Query("SELECT c FROM Character c WHERE c.devilFruit IS NOT NULL")
    List<Character> findDevilFruitUsers();
    
    // Native SQL for complex analytics (Enterprise reporting)
    @Query(value = "SELECT crew, COUNT(*) as character_count, AVG(current_price) as avg_price " +
                   "FROM characters GROUP BY crew ORDER BY character_count DESC", 
           nativeQuery = true)
    List<Object[]> getCrewStatistics();
    
    // Cached queries for performance (Netflix pattern)
    @Cacheable("popularCharacters")
    @Query("SELECT c FROM Character c JOIN c.trades t GROUP BY c ORDER BY COUNT(t) DESC")
    List<Character> findMostTradedCharacters(Pageable pageable);
    
    // Search functionality (Google-style search)
    @Query("SELECT c FROM Character c WHERE " +
           "LOWER(c.name) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(c.crew) LIKE LOWER(CONCAT('%', :searchTerm, '%')) OR " +
           "LOWER(c.devilFruit) LIKE LOWER(CONCAT('%', :searchTerm, '%'))")
    Page<Character> searchCharacters(@Param("searchTerm") String searchTerm, Pageable pageable);
    
    // Business logic queries
    @Query("SELECT COUNT(c) FROM Character c WHERE c.rarity = :rarity")
    long countByRarity(@Param("rarity") CharacterRarity rarity);
    
    @Query("SELECT c FROM Character c WHERE c.currentPrice = " +
           "(SELECT MAX(c2.currentPrice) FROM Character c2)")
    Optional<Character> findMostExpensiveCharacter();
    
    @Query("SELECT c FROM Character c WHERE c.bounty = " +
           "(SELECT MAX(c2.bounty) FROM Character c2 WHERE c2.bounty IS NOT NULL)")
    Optional<Character> findHighestBountyCharacter();
}

// TODO 4: SERVICE LAYER (BUSINESS LOGIC - LINKEDIN PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create service layer like LinkedIn's business logic

LINKEDIN'S SERVICE PATTERN:
- @Service annotation for business logic
- @Transactional for data consistency
- DTO pattern for data transfer
- Exception handling for error management
- Validation for business rules

CHARACTER SERVICE:
*/

package com.onepiece.trading.service;

import com.onepiece.trading.entity.Character;
import com.onepiece.trading.entity.CharacterRarity;
import com.onepiece.trading.repository.CharacterRepository;
import com.onepiece.trading.dto.CharacterDTO;
import com.onepiece.trading.dto.CharacterCreateDTO;
import com.onepiece.trading.dto.CharacterUpdateDTO;
import com.onepiece.trading.exception.CharacterNotFoundException;
import com.onepiece.trading.exception.DuplicateCharacterException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;

import java.math.BigDecimal;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 🏴‍☠️ Character Service - Enterprise Business Logic Layer
 * 
 * This is how LinkedIn structures their business logic:
 * - @Service for business operations
 * - @Transactional for data consistency
 * - DTO pattern for clean API contracts
 * - Exception handling for error management
 */
@Service
@Transactional
public class CharacterService {
    
    private final CharacterRepository characterRepository;
    
    @Autowired
    public CharacterService(CharacterRepository characterRepository) {
        this.characterRepository = characterRepository;
    }
    
    // READ OPERATIONS (with caching like Netflix)
    @Cacheable("characters")
    @Transactional(readOnly = true)
    public List<CharacterDTO> getAllCharacters() {
        return characterRepository.findAll()
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Cacheable("character")
    @Transactional(readOnly = true)
    public CharacterDTO getCharacterById(Long id) {
        Character character = characterRepository.findById(id)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with id: " + id));
        return convertToDTO(character);
    }
    
    @Transactional(readOnly = true)
    public CharacterDTO getCharacterByName(String name) {
        Character character = characterRepository.findByName(name)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with name: " + name));
        return convertToDTO(character);
    }
    
    @Transactional(readOnly = true)
    public Page<CharacterDTO> searchCharacters(String searchTerm, Pageable pageable) {
        return characterRepository.searchCharacters(searchTerm, pageable)
                .map(this::convertToDTO);
    }
    
    @Transactional(readOnly = true)
    public List<CharacterDTO> getCharactersByCrew(String crew) {
        return characterRepository.findByCrew(crew)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Transactional(readOnly = true)
    public List<CharacterDTO> getCharactersByPriceRange(BigDecimal minPrice, BigDecimal maxPrice) {
        return characterRepository.findByPriceRange(minPrice, maxPrice)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    // WRITE OPERATIONS (with cache invalidation)
    @CacheEvict(value = {"characters", "popularCharacters"}, allEntries = true)
    public CharacterDTO createCharacter(CharacterCreateDTO createDTO) {
        // Business validation
        if (characterRepository.findByName(createDTO.getName()).isPresent()) {
            throw new DuplicateCharacterException("Character already exists with name: " + createDTO.getName());
        }
        
        // Create entity from DTO
        Character character = new Character(
            createDTO.getName(),
            createDTO.getCrew(),
            createDTO.getCurrentPrice(),
            createDTO.getRarity()
        );
        
        character.setDevilFruit(createDTO.getDevilFruit());
        character.setBounty(createDTO.getBounty());
        character.setImageUrl(createDTO.getImageUrl());
        character.setDescription(createDTO.getDescription());
        character.setCreatedBy("SYSTEM"); // In real app, get from security context
        
        Character savedCharacter = characterRepository.save(character);
        return convertToDTO(savedCharacter);
    }
    
    @CacheEvict(value = {"character", "characters", "popularCharacters"}, allEntries = true)
    public CharacterDTO updateCharacter(Long id, CharacterUpdateDTO updateDTO) {
        Character character = characterRepository.findById(id)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found with id: " + id));
        
        // Update fields if provided
        if (updateDTO.getCurrentPrice() != null) {
            character.setCurrentPrice(updateDTO.getCurrentPrice());
        }
        if (updateDTO.getDevilFruit() != null) {
            character.setDevilFruit(updateDTO.getDevilFruit());
        }
        if (updateDTO.getBounty() != null) {
            character.setBounty(updateDTO.getBounty());
        }
        if (updateDTO.getImageUrl() != null) {
            character.setImageUrl(updateDTO.getImageUrl());
        }
        if (updateDTO.getDescription() != null) {
            character.setDescription(updateDTO.getDescription());
        }
        
        Character updatedCharacter = characterRepository.save(character);
        return convertToDTO(updatedCharacter);
    }
    
    @CacheEvict(value = {"character", "characters", "popularCharacters"}, allEntries = true)
    public void deleteCharacter(Long id) {
        if (!characterRepository.existsById(id)) {
            throw new CharacterNotFoundException("Character not found with id: " + id);
        }
        characterRepository.deleteById(id);
    }
    
    // BUSINESS LOGIC METHODS
    @Transactional(readOnly = true)
    public List<CharacterDTO> getMostTradedCharacters(int limit) {
        Pageable pageable = Pageable.ofSize(limit);
        return characterRepository.findMostTradedCharacters(pageable)
                .stream()
                .map(this::convertToDTO)
                .collect(Collectors.toList());
    }
    
    @Transactional(readOnly = true)
    public CharacterDTO getMostExpensiveCharacter() {
        Character character = characterRepository.findMostExpensiveCharacter()
                .orElseThrow(() -> new CharacterNotFoundException("No characters found"));
        return convertToDTO(character);
    }
    
    // DTO CONVERSION (Enterprise pattern)
    private CharacterDTO convertToDTO(Character character) {
        CharacterDTO dto = new CharacterDTO();
        dto.setId(character.getId());
        dto.setName(character.getName());
        dto.setCrew(character.getCrew());
        dto.setCurrentPrice(character.getCurrentPrice());
        dto.setDevilFruit(character.getDevilFruit());
        dto.setBounty(character.getBounty());
        dto.setRarity(character.getRarity());
        dto.setImageUrl(character.getImageUrl());
        dto.setDescription(character.getDescription());
        dto.setCreatedAt(character.getCreatedAt());
        dto.setUpdatedAt(character.getUpdatedAt());
        return dto;
    }
}

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR JAVA SPRING BOOT IMPLEMENTATION
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You now understand enterprise Java like big tech!

📚 WHAT YOU JUST LEARNED:
✅ Spring Boot application structure (Netflix pattern)
✅ JPA/Hibernate entity modeling (Google approach)
✅ Repository pattern with Spring Data (Amazon style)
✅ Service layer with business logic (LinkedIn pattern)
✅ Enterprise design patterns and best practices
✅ Caching strategies for performance
✅ Transaction management for data consistency
✅ Exception handling and validation

🎯 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
├── REPLACES: Your Node.js character service with Java
├── SCALES: To enterprise level like Netflix/Amazon
├── INTEGRATES: With your existing MySQL database
├── PROVIDES: Enterprise-grade features and patterns
└── DEMONSTRATES: Why big tech chooses Java for core services

🎯 BIG TECH ENTERPRISE FEATURES YOU NOW HAVE:
✅ JPA/Hibernate ORM (like Google's data layer)
✅ Spring Data repositories (like Amazon's data access)
✅ Service layer architecture (like LinkedIn's business logic)
✅ Caching with Spring Cache (like Netflix's performance)
✅ Transaction management (like enterprise banking systems)
✅ Validation and exception handling (like production systems)

🔥 NEXT STEPS:
1. Create the REST controller layer (API endpoints)
2. Add Spring Security (authentication/authorization)
3. Implement microservices communication
4. Add monitoring and metrics
5. Deploy with Docker and Kubernetes

🎯 CAREER IMPACT:
With these Java Spring Boot skills, you're now qualified for:
- Senior Java Developer: $120K - $180K
- Enterprise Architect: $150K - $220K
- Big Tech Backend Engineer: $180K - $300K

🚀 You now understand why Netflix, Amazon, and Google use Java! ⚔️
*/

// TODO 5: REST CONTROLLER LAYER (NETFLIX API PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create REST controllers like Netflix's API layer

NETFLIX'S REST API APPROACH:
- @RestController for RESTful endpoints
- @RequestMapping for URL routing
- @Valid for request validation
- ResponseEntity for HTTP responses
- Exception handling with @ControllerAdvice

CHARACTER REST CONTROLLER:
*/

package com.onepiece.trading.controller;

import com.onepiece.trading.dto.CharacterDTO;
import com.onepiece.trading.dto.CharacterCreateDTO;
import com.onepiece.trading.dto.CharacterUpdateDTO;
import com.onepiece.trading.service.CharacterService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.math.BigDecimal;
import java.util.List;

/**
 * 🏴‍☠️ Character REST Controller - Netflix-style API Layer
 *
 * This is how Netflix structures their REST APIs:
 * - RESTful endpoints with proper HTTP methods
 * - Request/Response DTOs for clean contracts
 * - Validation and error handling
 * - Pagination for large datasets
 */
@RestController
@RequestMapping("/api/v1/characters")
@CrossOrigin(origins = "*") // Allow frontend connections
public class CharacterController {

    private final CharacterService characterService;

    @Autowired
    public CharacterController(CharacterService characterService) {
        this.characterService = characterService;
    }

    // GET /api/v1/characters - Get all characters
    @GetMapping
    public ResponseEntity<List<CharacterDTO>> getAllCharacters() {
        List<CharacterDTO> characters = characterService.getAllCharacters();
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/{id} - Get character by ID
    @GetMapping("/{id}")
    public ResponseEntity<CharacterDTO> getCharacterById(@PathVariable Long id) {
        CharacterDTO character = characterService.getCharacterById(id);
        return ResponseEntity.ok(character);
    }

    // GET /api/v1/characters/name/{name} - Get character by name
    @GetMapping("/name/{name}")
    public ResponseEntity<CharacterDTO> getCharacterByName(@PathVariable String name) {
        CharacterDTO character = characterService.getCharacterByName(name);
        return ResponseEntity.ok(character);
    }

    // GET /api/v1/characters/search - Search characters
    @GetMapping("/search")
    public ResponseEntity<Page<CharacterDTO>> searchCharacters(
            @RequestParam String q,
            Pageable pageable) {
        Page<CharacterDTO> characters = characterService.searchCharacters(q, pageable);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/crew/{crew} - Get characters by crew
    @GetMapping("/crew/{crew}")
    public ResponseEntity<List<CharacterDTO>> getCharactersByCrew(@PathVariable String crew) {
        List<CharacterDTO> characters = characterService.getCharactersByCrew(crew);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/price-range - Get characters by price range
    @GetMapping("/price-range")
    public ResponseEntity<List<CharacterDTO>> getCharactersByPriceRange(
            @RequestParam BigDecimal minPrice,
            @RequestParam BigDecimal maxPrice) {
        List<CharacterDTO> characters = characterService.getCharactersByPriceRange(minPrice, maxPrice);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/most-traded - Get most traded characters
    @GetMapping("/most-traded")
    public ResponseEntity<List<CharacterDTO>> getMostTradedCharacters(
            @RequestParam(defaultValue = "10") int limit) {
        List<CharacterDTO> characters = characterService.getMostTradedCharacters(limit);
        return ResponseEntity.ok(characters);
    }

    // GET /api/v1/characters/most-expensive - Get most expensive character
    @GetMapping("/most-expensive")
    public ResponseEntity<CharacterDTO> getMostExpensiveCharacter() {
        CharacterDTO character = characterService.getMostExpensiveCharacter();
        return ResponseEntity.ok(character);
    }

    // POST /api/v1/characters - Create new character
    @PostMapping
    public ResponseEntity<CharacterDTO> createCharacter(@Valid @RequestBody CharacterCreateDTO createDTO) {
        CharacterDTO character = characterService.createCharacter(createDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(character);
    }

    // PUT /api/v1/characters/{id} - Update character
    @PutMapping("/{id}")
    public ResponseEntity<CharacterDTO> updateCharacter(
            @PathVariable Long id,
            @Valid @RequestBody CharacterUpdateDTO updateDTO) {
        CharacterDTO character = characterService.updateCharacter(id, updateDTO);
        return ResponseEntity.ok(character);
    }

    // DELETE /api/v1/characters/{id} - Delete character
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteCharacter(@PathVariable Long id) {
        characterService.deleteCharacter(id);
        return ResponseEntity.noContent().build();
    }
}

// TODO 6: DTO CLASSES (ENTERPRISE DATA TRANSFER PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create DTOs like enterprise applications

ENTERPRISE DTO PATTERN:
- Separate DTOs for different operations
- Validation annotations for data integrity
- Clean separation between API and domain models
- Immutable objects where possible

CHARACTER DTOs:
*/

package com.onepiece.trading.dto;

import com.onepiece.trading.entity.CharacterRarity;
import javax.validation.constraints.*;
import java.math.BigDecimal;
import java.time.LocalDateTime;

/**
 * 🏴‍☠️ Character DTO - Data Transfer Object for API responses
 */
public class CharacterDTO {
    private Long id;
    private String name;
    private String crew;
    private BigDecimal currentPrice;
    private String devilFruit;
    private BigDecimal bounty;
    private CharacterRarity rarity;
    private String imageUrl;
    private String description;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;

    // Constructors, getters, and setters
    public CharacterDTO() {}

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}

/**
 * 🏴‍☠️ Character Create DTO - For creating new characters
 */
class CharacterCreateDTO {
    @NotBlank(message = "Character name is required")
    @Size(min = 2, max = 100, message = "Name must be between 2 and 100 characters")
    private String name;

    @NotBlank(message = "Crew is required")
    private String crew;

    @NotNull(message = "Current price is required")
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    private BigDecimal currentPrice;

    @NotNull(message = "Rarity is required")
    private CharacterRarity rarity;

    private String devilFruit;
    private BigDecimal bounty;
    private String imageUrl;
    private String description;

    // Constructors, getters, and setters
    public CharacterCreateDTO() {}

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getCrew() { return crew; }
    public void setCrew(String crew) { this.crew = crew; }

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public CharacterRarity getRarity() { return rarity; }
    public void setRarity(CharacterRarity rarity) { this.rarity = rarity; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}

/**
 * 🏴‍☠️ Character Update DTO - For updating existing characters
 */
class CharacterUpdateDTO {
    @DecimalMin(value = "0.0", inclusive = false, message = "Price must be positive")
    private BigDecimal currentPrice;

    private String devilFruit;
    private BigDecimal bounty;
    private String imageUrl;
    private String description;

    // Constructors, getters, and setters
    public CharacterUpdateDTO() {}

    public BigDecimal getCurrentPrice() { return currentPrice; }
    public void setCurrentPrice(BigDecimal currentPrice) { this.currentPrice = currentPrice; }

    public String getDevilFruit() { return devilFruit; }
    public void setDevilFruit(String devilFruit) { this.devilFruit = devilFruit; }

    public BigDecimal getBounty() { return bounty; }
    public void setBounty(BigDecimal bounty) { this.bounty = bounty; }

    public String getImageUrl() { return imageUrl; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
}
