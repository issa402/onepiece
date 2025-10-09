/*
🏴‍☠️ MODULE 33: FAANG-LEVEL JAVA ENTERPRISE MASTERY
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
ENTERPRISE-LEVEL Java Spring Boot backend like Netflix, Amazon, Google, LinkedIn!
This is the EXACT Java stack that powers the world's biggest tech companies!

📚 COMPREHENSIVE LEARNING OBJECTIVES:

🔥 JAVA FUNDAMENTALS (FAANG LEVEL):
- Advanced OOP, memory management, JVM internals
- Collections framework, multithreading, performance optimization
- Generics, lambdas, streams, modern Java features (17+)
- Design patterns, reflection, annotations

⚡ MAVEN BUILD MASTERY:
- Multi-module projects, dependency management, BOM patterns
- Profiles, plugins, release management, CI/CD integration
- Performance optimization, security scanning, quality gates
- Enterprise patterns, corporate standards

🗄️ SPRING CORE DEEP DIVE:
- IoC container, dependency injection, bean lifecycle
- AOP (Aspect-Oriented Programming), pointcuts, advice
- Configuration approaches (XML, annotations, Java config)
- Testing strategies, profiles, conditional configuration

🚀 SPRING BOOT ENTERPRISE:
- Auto-configuration, starters, actuator, profiles
- RESTful APIs, validation, exception handling
- JPA/Hibernate, transactions, connection pooling
- Security, JWT, OAuth2, method-level security

🔗 INTEGRATES WITH YOUR ONE PIECE PROJECT:
- REPLACES: Your Node.js services with Java equivalents
- SCALES: To enterprise level like Netflix/Amazon
- CONNECTS: To your existing PostgreSQL database and frontend
- DEMONSTRATES: Why big tech chooses Java for core services

💰 CAREER IMPACT: +$50K-$150K (Complete Java enterprise stack!)

🎯 BIG TECH COMPANIES USING THIS COMPLETE STACK:
- Netflix: Core streaming services, billing, user management
- Amazon: E-commerce backend, AWS services, internal tools
- Google: Enterprise services, internal platforms
- LinkedIn: Social platform backend, messaging, data processing
- Uber: Core services, enterprise features, microservices
- Twitter: Backend services, API layer, real-time processing
- PayPal: Payment processing, fraud detection, enterprise systems
- Airbnb: Booking services, pricing engine, data platforms
*/

// TODO 1: MAVEN PROJECT STRUCTURE (ENTERPRISE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Set up enterprise Maven multi-module project

ENTERPRISE MAVEN STRUCTURE:
onepiece-trading-platform/
├── pom.xml (parent POM)
├── onepiece-common/
├── onepiece-character-service/
├── onepiece-trading-service/
├── onepiece-user-service/
└── onepiece-api-gateway/

PARENT POM.XML EXAMPLE:
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.onepiece.trading</groupId>
    <artifactId>onepiece-parent</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <spring-boot.version>3.2.0</spring-boot.version>
        <spring-cloud.version>2023.0.0</spring-cloud.version>
    </properties>

    <modules>
        <module>onepiece-common</module>
        <module>onepiece-character-service</module>
        <module>onepiece-trading-service</module>
        <module>onepiece-user-service</module>
        <module>onepiece-api-gateway</module>
    </modules>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>

CHILD MODULE POM.XML EXAMPLE (character-service):
<project>
    <parent>
        <groupId>com.onepiece.trading</groupId>
        <artifactId>onepiece-parent</artifactId>
        <version>1.0.0-SNAPSHOT</version>
    </parent>

    <artifactId>onepiece-character-service</artifactId>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>com.onepiece.trading</groupId>
            <artifactId>onepiece-common</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>
</project>
*/

// TODO 2: SPRING CORE CONFIGURATION (FAANG PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create enterprise Spring Core configuration

SPRING CORE FUNDAMENTALS:
- IoC Container and Dependency Injection
- Bean lifecycle and scopes
- AOP for cross-cutting concerns
- Configuration approaches (Java config preferred)
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
        System.out.println("📚 Comprehensive Java + Maven + Spring Core Implementation");
    }
}

// TODO 1.5: SPRING CORE CONFIGURATION (ENTERPRISE PATTERN)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create enterprise Spring Core configuration

SPRING CORE FUNDAMENTALS IMPLEMENTATION:
- IoC Container and Dependency Injection
- Bean lifecycle and scopes
- AOP for cross-cutting concerns
- Configuration approaches (Java config preferred)
*/

package com.onepiece.trading.config;

import org.springframework.context.annotation.*;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.cache.CacheManager;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.transaction.annotation.EnableTransactionManagement;
import org.springframework.aop.framework.ProxyFactoryBean;
import org.springframework.aop.support.NameMatchMethodPointcut;

import java.util.concurrent.Executor;

/**
 * 🏴‍☠️ Enterprise Spring Core Configuration
 *
 * This demonstrates FAANG-level Spring Core patterns:
 * - Advanced bean configuration and lifecycle management
 * - Conditional bean creation based on properties/profiles
 * - Multiple bean instances with qualifiers
 * - Custom scopes and proxy configurations
 */
@Configuration
@EnableCaching
@EnableAsync
@EnableTransactionManagement
@Profile("!test")
public class CoreConfiguration {

    // Bean with custom lifecycle callbacks
    @Bean(initMethod = "initialize", destroyMethod = "cleanup")
    @Scope("singleton")
    public PriceCalculationEngine priceCalculationEngine() {
        PriceCalculationEngine engine = new PriceCalculationEngine();
        engine.setAlgorithm("ADVANCED_VOLATILITY");
        return engine;
    }

    // Conditional bean creation (Netflix pattern)
    @Bean
    @ConditionalOnProperty(name = "onepiece.caching.enabled", havingValue = "true", matchIfMissing = true)
    public CacheManager redisCacheManager() {
        return new RedisCacheManager();
    }

    // Primary bean when multiple candidates exist
    @Bean
    @Primary
    public NotificationService primaryNotificationService() {
        return new EmailNotificationService();
    }

    // Qualified bean for specific use cases
    @Bean
    @Qualifier("sms")
    public NotificationService smsNotificationService() {
        return new SmsNotificationService();
    }

    // Qualified bean for push notifications
    @Bean
    @Qualifier("push")
    public NotificationService pushNotificationService() {
        return new PushNotificationService();
    }

    // Custom thread pool for async operations (Uber pattern)
    @Bean("tradingExecutor")
    public Executor tradingTaskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(20);
        executor.setQueueCapacity(100);
        executor.setThreadNamePrefix("Trading-");
        executor.setWaitForTasksToCompleteOnShutdown(true);
        executor.setAwaitTerminationSeconds(30);
        return executor;
    }

    // Profile-specific configuration
    @Bean
    @Profile("development")
    public DatabaseInitializer devDatabaseInitializer() {
        return new DevDatabaseInitializer();
    }

    @Bean
    @Profile("production")
    public DatabaseInitializer prodDatabaseInitializer() {
        return new ProdDatabaseInitializer();
    }
}

// ASPECT-ORIENTED PROGRAMMING (AOP) IMPLEMENTATION
@Aspect
@Component
public class TradingAspect {

    private static final Logger logger = LoggerFactory.getLogger(TradingAspect.class);

    // Before advice - executed before method (LinkedIn pattern)
    @Before("execution(* com.onepiece.trading.service.TradingService.executeTrade(..))")
    public void beforeTrade(JoinPoint joinPoint) {
        Object[] args = joinPoint.getArgs();
        logger.info("🏴‍☠️ Starting trade execution: {} with args: {}",
                   joinPoint.getSignature().getName(), args);
    }

    // Around advice - complete method interception (Netflix monitoring pattern)
    @Around("@annotation(com.onepiece.trading.annotation.Monitored)")
    public Object monitorPerformance(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        String methodName = joinPoint.getSignature().getName();

        try {
            logger.debug("⚡ Starting method: {}", methodName);
            Object result = joinPoint.proceed();
            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;

            logger.info("✅ Method {} executed successfully in {}ms", methodName, executionTime);

            // Record metrics (Prometheus/Micrometer integration)
            recordMethodMetrics(methodName, executionTime, "SUCCESS");

            return result;
        } catch (Exception e) {
            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;

            logger.error("❌ Method {} failed after {}ms: {}", methodName, executionTime, e.getMessage());
            recordMethodMetrics(methodName, executionTime, "ERROR");
            throw e;
        }
    }

    // After returning advice - executed after successful method completion
    @AfterReturning(pointcut = "execution(* com.onepiece.trading.service.*.*(..))", returning = "result")
    public void afterSuccessfulExecution(JoinPoint joinPoint, Object result) {
        logger.debug("🎉 Method {} completed with result: {}",
                    joinPoint.getSignature().getName(), result);
    }

    // After throwing advice - exception handling (Google error tracking pattern)
    @AfterThrowing(pointcut = "execution(* com.onepiece.trading.service.*.*(..))", throwing = "exception")
    public void afterThrowingException(JoinPoint joinPoint, Exception exception) {
        logger.error("💥 Method {} threw exception: {}",
                    joinPoint.getSignature().getName(), exception.getMessage(), exception);

        // Send to error tracking service (Sentry, Rollbar, etc.)
        sendToErrorTracking(joinPoint, exception);
    }

    private void recordMethodMetrics(String methodName, long executionTime, String status) {
        // Implementation for metrics recording
        // This would integrate with Micrometer/Prometheus
    }

    private void sendToErrorTracking(JoinPoint joinPoint, Exception exception) {
        // Implementation for error tracking
        // This would integrate with Sentry, Rollbar, or similar
    }
}

// TODO 3: SPRING BOOT ENTERPRISE FEATURES (COMPLETE IMPLEMENTATION)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement complete Spring Boot enterprise features

SPRING BOOT ENTERPRISE STACK:
- Auto-configuration and starters
- Actuator for monitoring and management
- Security with JWT authentication
- JPA/Hibernate with advanced features
- Kafka for event-driven architecture
- Microservices with service discovery
- Performance optimization and caching
- Reactive programming with WebFlux
*/

package com.onepiece.trading.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpStatus;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.validation.annotation.Validated;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Sort;

import javax.validation.Valid;
import javax.validation.constraints.Min;
import javax.validation.constraints.Max;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 🏴‍☠️ Enterprise Character Trading Controller
 *
 * This demonstrates complete Spring Boot enterprise patterns:
 * - RESTful API design with proper HTTP methods
 * - Validation and error handling
 * - Security with role-based access control
 * - Caching for performance optimization
 * - Pagination and sorting for large datasets
 * - Comprehensive logging and monitoring
 */
@RestController
@RequestMapping("/api/v1/characters")
@Validated
@Slf4j
@CrossOrigin(origins = "http://localhost:3000") // React frontend
public class CharacterController {

    private final CharacterService characterService;
    private final TradingService tradingService;
    private final NotificationService notificationService;

    // Constructor injection (Spring Boot best practice)
    public CharacterController(CharacterService characterService,
                             TradingService tradingService,
                             NotificationService notificationService) {
        this.characterService = characterService;
        this.tradingService = tradingService;
        this.notificationService = notificationService;
    }

    /**
     * Get all characters with pagination, sorting, and filtering
     * Demonstrates: Pagination, caching, validation, query parameters
     */
    @GetMapping
    @Cacheable(value = "characters", key = "'page:' + #page + ':size:' + #size + ':crew:' + #crew",
               unless = "#result.isEmpty()")
    public ResponseEntity<PagedResponse<CharacterDto>> getAllCharacters(
            @RequestParam(defaultValue = "0") @Min(0) int page,
            @RequestParam(defaultValue = "20") @Min(1) @Max(100) int size,
            @RequestParam(required = false) String crew,
            @RequestParam(required = false) @Min(0) Long minBounty,
            @RequestParam(defaultValue = "bounty") String sortBy,
            @RequestParam(defaultValue = "desc") String sortDir) {

        log.info("🔍 Fetching characters - page: {}, size: {}, crew: {}, minBounty: {}",
                page, size, crew, minBounty);

        // Create search criteria
        CharacterSearchCriteria criteria = CharacterSearchCriteria.builder()
            .crew(crew)
            .minBounty(minBounty)
            .build();

        // Create pageable with sorting
        Sort sort = Sort.by(sortDir.equalsIgnoreCase("desc") ?
                           Sort.Direction.DESC : Sort.Direction.ASC, sortBy);
        Pageable pageable = PageRequest.of(page, size, sort);

        // Fetch characters
        Page<Character> charactersPage = characterService.findAll(criteria, pageable);

        // Convert to DTOs
        List<CharacterDto> characterDtos = charactersPage.getContent().stream()
            .map(this::convertToDto)
            .collect(Collectors.toList());

        // Build response
        PagedResponse<CharacterDto> response = PagedResponse.<CharacterDto>builder()
            .content(characterDtos)
            .page(charactersPage.getNumber())
            .size(charactersPage.getSize())
            .totalElements(charactersPage.getTotalElements())
            .totalPages(charactersPage.getTotalPages())
            .first(charactersPage.isFirst())
            .last(charactersPage.isLast())
            .build();

        log.info("✅ Retrieved {} characters out of {} total",
                characterDtos.size(), charactersPage.getTotalElements());

        return ResponseEntity.ok(response);
    }

    /**
     * Get character by ID
     * Demonstrates: Path variables, caching, error handling
     */
    @GetMapping("/{id}")
    @Cacheable(value = "character", key = "#id")
    public ResponseEntity<CharacterDto> getCharacter(@PathVariable @Min(1) Long id) {
        log.info("🔍 Fetching character with id: {}", id);

        Optional<Character> character = characterService.findById(id);

        if (character.isPresent()) {
            CharacterDto dto = convertToDto(character.get());
            log.info("✅ Found character: {}", dto.getName());
            return ResponseEntity.ok(dto);
        } else {
            log.warn("❌ Character not found with id: {}", id);
            return ResponseEntity.notFound().build();
        }
    }

    /**
     * Create new character
     * Demonstrates: POST method, validation, security, cache eviction
     */
    @PostMapping
    @PreAuthorize("hasRole('ADMIN')")
    @CacheEvict(value = "characters", allEntries = true)
    public ResponseEntity<CharacterDto> createCharacter(
            @Valid @RequestBody CreateCharacterRequest request,
            Authentication authentication) {

        log.info("🆕 Creating new character: {} by user: {}",
                request.getName(), authentication.getName());

        try {
            Character character = Character.builder()
                .name(request.getName())
                .bounty(request.getBounty())
                .type(request.getType())
                .crew(request.getCrewId() != null ?
                      crewService.findById(request.getCrewId()).orElse(null) : null)
                .createdBy(authentication.getName())
                .build();

            Character savedCharacter = characterService.save(character);
            CharacterDto dto = convertToDto(savedCharacter);

            // Send notification
            notificationService.notifyCharacterCreated(savedCharacter);

            log.info("✅ Character created successfully: {} with id: {}",
                    dto.getName(), dto.getId());

            return ResponseEntity.status(HttpStatus.CREATED).body(dto);

        } catch (ValidationException e) {
            log.error("❌ Validation error creating character: {}", e.getMessage());
            return ResponseEntity.badRequest().build();
        } catch (Exception e) {
            log.error("❌ Error creating character: {}", e.getMessage(), e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    /**
     * Execute character trade
     * Demonstrates: Complex business logic, transactions, security, async processing
     */
    @PostMapping("/{characterId}/trade")
    @PreAuthorize("hasRole('TRADER')")
    public ResponseEntity<TradeResult> tradeCharacter(
            @PathVariable @Min(1) Long characterId,
            @Valid @RequestBody TradeRequest request,
            Authentication authentication) {

        log.info("💰 Trade request for character {} by user {} - Price: {}",
                characterId, authentication.getName(), request.getPrice());

        try {
            // Validate character exists
            Character character = characterService.findById(characterId)
                .orElseThrow(() -> new CharacterNotFoundException("Character not found: " + characterId));

            // Execute trade
            TradeResult result = tradingService.executeTrade(
                characterId,
                request,
                authentication.getName()
            );

            if (result.isSuccessful()) {
                log.info("✅ Trade executed successfully: {} - New balance: {}",
                        result.getTradeId(), result.getNewBalance());

                // Clear relevant caches
                cacheManager.getCache("character").evict(characterId);
                cacheManager.getCache("characters").clear();

                return ResponseEntity.ok(result);
            } else {
                log.warn("❌ Trade failed: {}", result.getMessage());
                return ResponseEntity.badRequest().body(result);
            }

        } catch (CharacterNotFoundException e) {
            log.error("❌ Character not found for trade: {}", characterId);
            return ResponseEntity.notFound().build();
        } catch (InsufficientFundsException e) {
            log.warn("❌ Insufficient funds for trade: {}", e.getMessage());
            TradeResult errorResult = TradeResult.builder()
                .status("FAILED")
                .message("Insufficient funds for this trade")
                .build();
            return ResponseEntity.badRequest().body(errorResult);
        } catch (Exception e) {
            log.error("❌ Unexpected error during trade: {}", e.getMessage(), e);
            TradeResult errorResult = TradeResult.builder()
                .status("ERROR")
                .message("An unexpected error occurred. Please try again.")
                .build();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResult);
        }
    }

    /**
     * Get character trading history
     * Demonstrates: Complex queries, pagination, security
     */
    @GetMapping("/{characterId}/trades")
    @PreAuthorize("hasRole('USER')")
    public ResponseEntity<PagedResponse<TradeDto>> getCharacterTrades(
            @PathVariable @Min(1) Long characterId,
            @RequestParam(defaultValue = "0") @Min(0) int page,
            @RequestParam(defaultValue = "10") @Min(1) @Max(50) int size) {

        log.info("📊 Fetching trade history for character: {}", characterId);

        Pageable pageable = PageRequest.of(page, size, Sort.by("executedAt").descending());
        Page<Trade> tradesPage = tradingService.getCharacterTrades(characterId, pageable);

        List<TradeDto> tradeDtos = tradesPage.getContent().stream()
            .map(this::convertToTradeDto)
            .collect(Collectors.toList());

        PagedResponse<TradeDto> response = PagedResponse.<TradeDto>builder()
            .content(tradeDtos)
            .page(tradesPage.getNumber())
            .size(tradesPage.getSize())
            .totalElements(tradesPage.getTotalElements())
            .totalPages(tradesPage.getTotalPages())
            .build();

        log.info("✅ Retrieved {} trades for character {}", tradeDtos.size(), characterId);

        return ResponseEntity.ok(response);
    }

    // Helper methods for DTO conversion
    private CharacterDto convertToDto(Character character) {
        return CharacterDto.builder()
            .id(character.getId())
            .name(character.getName())
            .bounty(character.getBounty())
            .type(character.getType())
            .crewName(character.getCrew() != null ? character.getCrew().getName() : null)
            .marketValue(character.getMarketValue())
            .createdAt(character.getCreatedAt())
            .updatedAt(character.getUpdatedAt())
            .build();
    }

    private TradeDto convertToTradeDto(Trade trade) {
        return TradeDto.builder()
            .id(trade.getId())
            .buyerId(trade.getBuyerId())
            .sellerId(trade.getSellerId())
            .characterId(trade.getCharacterId())
            .price(trade.getPrice())
            .status(trade.getStatus())
            .executedAt(trade.getExecutedAt())
            .build();
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
