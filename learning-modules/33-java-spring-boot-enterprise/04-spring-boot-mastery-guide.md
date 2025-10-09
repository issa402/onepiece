# 🏴‍☠️ SPRING BOOT MASTERY - Complete FAANG-Level Guide

## **Integrated with Your One Piece Trading Platform**

---

# **🔥 1. Spring Boot Core Internals**

## **✅ Core Topics (Netflix/Amazon Level)**

### **🔹 Spring Boot Architecture & Auto-Configuration**
- **How @EnableAutoConfiguration Works** - Conditional beans, classpath scanning, auto-config classes
- **Spring Boot Starter Internals** - Dependency management, transitive dependencies, version alignment
- **ApplicationContext Initialization** - Bean factory, post-processors, lifecycle callbacks
- **Embedded Server Integration** - Tomcat, Jetty, Undertow performance comparison

### **🔹 Bean Lifecycle & Dependency Injection**
- **Bean Scopes Deep Dive** - Singleton, prototype, request, session, application
- **Lifecycle Callbacks** - @PostConstruct, @PreDestroy, InitializingBean, DisposableBean
- **Circular Dependency Resolution** - Constructor injection, setter injection, @Lazy
- **Conditional Bean Creation** - @ConditionalOnProperty, @ConditionalOnClass, custom conditions

### **🔹 Configuration & Profiles**
- **External Configuration** - application.yml, environment variables, command line args
- **Profile Management** - Development, testing, production configurations
- **Property Binding** - @ConfigurationProperties, @Value, SpEL expressions
- **Configuration Precedence** - Property source ordering, override mechanisms

---

## **🎯 ONE PIECE PROJECT INTEGRATION:**

### **🏴‍☠️ Character Service Auto-Configuration**
```java
// Custom Auto-Configuration for One Piece Character Service
@Configuration
@ConditionalOnClass(CharacterService.class)
@ConditionalOnProperty(name = "onepiece.character.enabled", havingValue = "true", matchIfMissing = true)
@EnableConfigurationProperties(CharacterProperties.class)
public class CharacterAutoConfiguration {
    
    @Bean
    @ConditionalOnMissingBean
    public CharacterService characterService(CharacterRepository repository, 
                                           CharacterProperties properties) {
        return new CharacterServiceImpl(repository, properties);
    }
    
    @Bean
    @ConditionalOnProperty(name = "onepiece.character.caching.enabled", havingValue = "true")
    public CacheManager characterCacheManager() {
        return new RedisCacheManager();
    }
}

@ConfigurationProperties(prefix = "onepiece.character")
@Data
public class CharacterProperties {
    private boolean enabled = true;
    private int maxBounty = 5000000000L;
    private String defaultCrew = "Straw Hat Pirates";
    private CachingProperties caching = new CachingProperties();
    
    @Data
    public static class CachingProperties {
        private boolean enabled = true;
        private Duration ttl = Duration.ofMinutes(30);
        private int maxSize = 1000;
    }
}
```

### **🚀 Practice Questions & Answers:**

**1️⃣ How does Spring Boot Auto-Configuration work internally?**
```java
// In your One Piece project, this is how auto-config works:
@SpringBootApplication
public class OnePieceTradingApplication {
    // @EnableAutoConfiguration (included in @SpringBootApplication) triggers:
    // 1. Classpath scanning for META-INF/spring.factories
    // 2. Loading auto-configuration classes
    // 3. Evaluating @Conditional annotations
    // 4. Creating beans based on conditions
}

// Example: CharacterService auto-configuration
// spring.factories entry:
// org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
// com.onepiece.trading.autoconfigure.CharacterAutoConfiguration
```

**2️⃣ Difference between @Component, @Service, and @Repository?**
```java
// In One Piece project context:

@Repository  // Data access layer - adds exception translation
public class CharacterRepository {
    // Handles database operations for characters
    // Spring translates SQLException to DataAccessException
}

@Service     // Business logic layer - semantic annotation
public class TradingService {
    // Contains business rules for character trading
    // Typically @Transactional methods
}

@Component   // Generic Spring-managed component
public class PriceCalculator {
    // Utility component for price calculations
    // Can be injected anywhere
}

@Controller  // Web layer - handles HTTP requests
public class CharacterController {
    // REST endpoints for character operations
}
```

---

# **🔥 2. Spring Boot REST API & Web Layer**

## **✅ Advanced Web Layer Integration**

### **🔹 Request Processing Deep Dive**
- **DispatcherServlet Internals** - Request mapping, handler resolution, view resolution
- **Handler Mapping** - @RequestMapping, path variables, request parameters
- **Message Converters** - JSON, XML, custom converters, content negotiation
- **Exception Handling** - @ExceptionHandler, @ControllerAdvice, global error handling

### **🎯 ONE PIECE API IMPLEMENTATION:**

```java
// Enterprise-level Character Trading API
@RestController
@RequestMapping("/api/v1/characters")
@Validated
@Slf4j
public class CharacterController {
    
    private final CharacterService characterService;
    private final TradingService tradingService;
    
    // Constructor injection (best practice)
    public CharacterController(CharacterService characterService, 
                             TradingService tradingService) {
        this.characterService = characterService;
        this.tradingService = tradingService;
    }
    
    @GetMapping
    @Cacheable(value = "characters", unless = "#result.isEmpty()")
    public ResponseEntity<PagedResponse<CharacterDto>> getAllCharacters(
            @RequestParam(defaultValue = "0") @Min(0) int page,
            @RequestParam(defaultValue = "20") @Min(1) @Max(100) int size,
            @RequestParam(required = false) String crew,
            @RequestParam(required = false) @Min(0) Long minBounty) {
        
        log.info("Fetching characters - page: {}, size: {}, crew: {}, minBounty: {}", 
                page, size, crew, minBounty);
        
        CharacterSearchCriteria criteria = CharacterSearchCriteria.builder()
            .crew(crew)
            .minBounty(minBounty)
            .build();
            
        Pageable pageable = PageRequest.of(page, size, Sort.by("bounty").descending());
        Page<Character> characters = characterService.findAll(criteria, pageable);
        
        PagedResponse<CharacterDto> response = PagedResponse.<CharacterDto>builder()
            .content(characters.getContent().stream()
                .map(this::toDto)
                .collect(Collectors.toList()))
            .page(characters.getNumber())
            .size(characters.getSize())
            .totalElements(characters.getTotalElements())
            .totalPages(characters.getTotalPages())
            .build();
            
        return ResponseEntity.ok(response);
    }
    
    @PostMapping("/{characterId}/trade")
    @PreAuthorize("hasRole('TRADER')")
    public ResponseEntity<TradeResult> tradeCharacter(
            @PathVariable @Positive Long characterId,
            @Valid @RequestBody TradeRequest request,
            Authentication authentication) {
        
        log.info("Trade request for character {} by user {}", characterId, authentication.getName());
        
        TradeResult result = tradingService.executeTrade(characterId, request, authentication.getName());
        
        return ResponseEntity.ok(result);
    }
}

// Global Exception Handler
@ControllerAdvice
@Slf4j
public class GlobalExceptionHandler {
    
    @ExceptionHandler(CharacterNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleCharacterNotFound(CharacterNotFoundException ex) {
        log.warn("Character not found: {}", ex.getMessage());
        
        ErrorResponse error = ErrorResponse.builder()
            .message("Character not found")
            .details(ex.getMessage())
            .timestamp(Instant.now())
            .status(HttpStatus.NOT_FOUND.value())
            .path("/api/v1/characters")
            .build();
            
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
    }
    
    @ExceptionHandler(InsufficientFundsException.class)
    public ResponseEntity<ErrorResponse> handleInsufficientFunds(InsufficientFundsException ex) {
        log.warn("Insufficient funds for trade: {}", ex.getMessage());
        
        ErrorResponse error = ErrorResponse.builder()
            .message("Insufficient funds for this trade")
            .details(ex.getMessage())
            .timestamp(Instant.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .build();
            
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }
    
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ErrorResponse> handleValidationErrors(MethodArgumentNotValidException ex) {
        List<String> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> error.getField() + ": " + error.getDefaultMessage())
            .collect(Collectors.toList());
            
        ErrorResponse error = ErrorResponse.builder()
            .message("Validation failed")
            .details(String.join(", ", errors))
            .timestamp(Instant.now())
            .status(HttpStatus.BAD_REQUEST.value())
            .build();
            
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
    }
}
```

### **🔹 Spring Boot Actuator Integration**
```java
// Custom Health Check for One Piece Services
@Component
public class TradingSystemHealthIndicator implements HealthIndicator {
    
    private final CharacterService characterService;
    private final TradingService tradingService;
    
    @Override
    public Health health() {
        try {
            // Check if character service is responsive
            long characterCount = characterService.getTotalCount();
            
            // Check if trading service is functional
            boolean tradingEnabled = tradingService.isTradingEnabled();
            
            if (characterCount > 0 && tradingEnabled) {
                return Health.up()
                    .withDetail("characters", characterCount)
                    .withDetail("trading", "enabled")
                    .withDetail("status", "All systems operational")
                    .build();
            } else {
                return Health.down()
                    .withDetail("characters", characterCount)
                    .withDetail("trading", tradingEnabled ? "enabled" : "disabled")
                    .withDetail("status", "System degraded")
                    .build();
            }
        } catch (Exception e) {
            return Health.down()
                .withDetail("error", e.getMessage())
                .withDetail("status", "System failure")
                .build();
        }
    }
}

// Custom Metrics for Trading Platform
@Component
public class TradingMetrics {
    
    private final MeterRegistry meterRegistry;
    private final Counter tradeCounter;
    private final Timer tradeExecutionTimer;
    private final Gauge activeTraders;
    
    public TradingMetrics(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        this.tradeCounter = Counter.builder("onepiece.trades.total")
            .description("Total number of character trades")
            .register(meterRegistry);
        this.tradeExecutionTimer = Timer.builder("onepiece.trades.execution.time")
            .description("Time taken to execute trades")
            .register(meterRegistry);
        this.activeTraders = Gauge.builder("onepiece.traders.active")
            .description("Number of active traders")
            .register(meterRegistry, this, TradingMetrics::getActiveTraderCount);
    }
    
    public void recordTrade(TradeType type, BigDecimal amount) {
        tradeCounter.increment(
            Tags.of(
                Tag.of("type", type.name()),
                Tag.of("amount_range", getAmountRange(amount))
            )
        );
    }
    
    public Timer.Sample startTradeTimer() {
        return Timer.start(meterRegistry);
    }
    
    public void recordTradeExecution(Timer.Sample sample, boolean successful) {
        sample.stop(Timer.builder("onepiece.trades.execution.time")
            .tag("status", successful ? "success" : "failure")
            .register(meterRegistry));
    }
    
    private double getActiveTraderCount() {
        // Implementation to get active trader count
        return 0.0; // Placeholder
    }
    
    private String getAmountRange(BigDecimal amount) {
        if (amount.compareTo(BigDecimal.valueOf(1000000)) < 0) return "small";
        if (amount.compareTo(BigDecimal.valueOf(100000000)) < 0) return "medium";
        return "large";
    }
}
```

---

## **🚀 Practice Questions & Implementation:**

**1️⃣ How does Spring handle request-response mapping internally?**
```java
// In your One Piece project:
// 1. DispatcherServlet receives HTTP request
// 2. HandlerMapping finds matching @RequestMapping
// 3. HandlerAdapter invokes controller method
// 4. MessageConverter serializes response to JSON
// 5. Response sent back to client

@RequestMapping("/api/v1/characters/{id}")
public ResponseEntity<CharacterDto> getCharacter(@PathVariable Long id) {
    // Spring automatically:
    // - Converts path variable to Long
    // - Calls method with converted parameter
    // - Converts return value to JSON using Jackson
    // - Sets appropriate HTTP headers
}
```

**2️⃣ Difference between @RequestBody and @ResponseBody?**
```java
// @RequestBody - Deserializes HTTP request body to Java object
@PostMapping("/characters")
public ResponseEntity<Character> createCharacter(@RequestBody @Valid CreateCharacterRequest request) {
    // Spring converts JSON request body to CreateCharacterRequest object
    Character character = characterService.create(request);
    return ResponseEntity.status(HttpStatus.CREATED).body(character);
}

// @ResponseBody - Serializes Java object to HTTP response body
// (Implicit with @RestController)
@GetMapping("/characters/{id}")
public CharacterDto getCharacter(@PathVariable Long id) {
    // Spring converts CharacterDto object to JSON response body
    return characterService.findById(id);
}
```

---

---

# **🔥 3. Spring Boot Database & Persistence Layer**

## **✅ JPA/Hibernate Deep Dive with One Piece Trading**

### **🔹 Entity Relationships & Performance**
- **Entity Lifecycle** - Transient, persistent, detached, removed states
- **Fetch Strategies** - LAZY vs EAGER, N+1 problem solutions
- **Hibernate Caching** - First-level, second-level, query cache
- **Transaction Management** - @Transactional, isolation levels, propagation

### **🎯 ONE PIECE ENTITY DESIGN:**

```java
// Character Entity with Advanced JPA Features
@Entity
@Table(name = "characters", indexes = {
    @Index(name = "idx_character_crew", columnList = "crew"),
    @Index(name = "idx_character_bounty", columnList = "bounty")
})
@EntityListeners(AuditingEntityListener.class)
@NamedEntityGraph(
    name = "Character.withCrewAndAbilities",
    attributeNodes = {
        @NamedAttributeNode("crew"),
        @NamedAttributeNode(value = "abilities", subgraph = "abilities-subgraph")
    },
    subgraphs = {
        @NamedSubgraph(name = "abilities-subgraph", attributeNodes = @NamedAttributeNode("type"))
    }
)
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Character {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    @Size(min = 2, max = 100)
    private String name;

    @Column(nullable = false)
    @Min(0)
    private BigDecimal bounty;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private CharacterType type; // PIRATE, MARINE, REVOLUTIONARY, etc.

    // Many-to-One with Crew (Optimized fetch)
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "crew_id")
    @JsonIgnoreProperties({"characters"}) // Prevent circular reference
    private Crew crew;

    // One-to-Many with Abilities (Batch fetch optimization)
    @OneToMany(mappedBy = "character", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @BatchSize(size = 20) // Hibernate optimization
    @OrderBy("powerLevel DESC")
    private List<Ability> abilities = new ArrayList<>();

    // Many-to-Many with Trading History
    @ManyToMany(mappedBy = "characters", fetch = FetchType.LAZY)
    @JsonIgnore
    private Set<Trade> trades = new HashSet<>();

    // Optimistic Locking
    @Version
    private Long version;

    // Audit Fields
    @CreatedDate
    @Column(nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @LastModifiedDate
    @Column(nullable = false)
    private LocalDateTime updatedAt;

    @CreatedBy
    @Column(updatable = false)
    private String createdBy;

    @LastModifiedBy
    private String lastModifiedBy;

    // Calculated field (not persisted)
    @Transient
    private BigDecimal marketValue;

    // Custom lifecycle callbacks
    @PrePersist
    protected void onCreate() {
        if (bounty == null) {
            bounty = BigDecimal.ZERO;
        }
    }

    @PostLoad
    protected void onLoad() {
        // Calculate market value based on bounty and abilities
        this.marketValue = calculateMarketValue();
    }

    private BigDecimal calculateMarketValue() {
        BigDecimal base = bounty;
        if (abilities != null && !abilities.isEmpty()) {
            int abilityBonus = abilities.size() * 10;
            base = base.multiply(BigDecimal.valueOf(1 + abilityBonus / 100.0));
        }
        return base;
    }
}

// Advanced Repository with Custom Queries
@Repository
public interface CharacterRepository extends JpaRepository<Character, Long>,
                                           JpaSpecificationExecutor<Character> {

    // Query Methods with Fetch Joins (Solves N+1 Problem)
    @Query("SELECT c FROM Character c " +
           "LEFT JOIN FETCH c.crew " +
           "LEFT JOIN FETCH c.abilities " +
           "WHERE c.bounty >= :minBounty")
    List<Character> findByBountyGreaterThanEqualWithDetails(@Param("minBounty") BigDecimal minBounty);

    // Named Entity Graph Usage
    @EntityGraph("Character.withCrewAndAbilities")
    @Query("SELECT c FROM Character c WHERE c.crew.name = :crewName")
    List<Character> findByCrewNameWithDetails(@Param("crewName") String crewName);

    // Native Query for Complex Operations
    @Query(value = "SELECT c.*, " +
                   "RANK() OVER (ORDER BY c.bounty DESC) as bounty_rank " +
                   "FROM characters c " +
                   "WHERE c.type = :type", nativeQuery = true)
    List<Object[]> findCharactersWithBountyRank(@Param("type") String type);

    // Projection for Performance
    @Query("SELECT new com.onepiece.trading.dto.CharacterSummaryDto(" +
           "c.id, c.name, c.bounty, c.crew.name) " +
           "FROM Character c " +
           "WHERE c.bounty BETWEEN :minBounty AND :maxBounty")
    List<CharacterSummaryDto> findCharacterSummaries(@Param("minBounty") BigDecimal minBounty,
                                                    @Param("maxBounty") BigDecimal maxBounty);

    // Batch Operations
    @Modifying
    @Query("UPDATE Character c SET c.bounty = c.bounty * :multiplier WHERE c.crew.id = :crewId")
    int updateBountyForCrew(@Param("crewId") Long crewId, @Param("multiplier") BigDecimal multiplier);

    // Specification for Dynamic Queries
    static Specification<Character> hasMinBounty(BigDecimal minBounty) {
        return (root, query, criteriaBuilder) ->
            minBounty == null ? null : criteriaBuilder.greaterThanOrEqualTo(root.get("bounty"), minBounty);
    }

    static Specification<Character> belongsToCrew(String crewName) {
        return (root, query, criteriaBuilder) ->
            crewName == null ? null : criteriaBuilder.equal(root.get("crew").get("name"), crewName);
    }
}

// Service Layer with Transaction Management
@Service
@Transactional(readOnly = true)
@Slf4j
public class CharacterService {

    private final CharacterRepository characterRepository;
    private final CrewRepository crewRepository;
    private final CacheManager cacheManager;

    public CharacterService(CharacterRepository characterRepository,
                          CrewRepository crewRepository,
                          CacheManager cacheManager) {
        this.characterRepository = characterRepository;
        this.crewRepository = crewRepository;
        this.cacheManager = cacheManager;
    }

    // Read-only transaction for queries
    @Cacheable(value = "characters", key = "#id")
    public Optional<Character> findById(Long id) {
        log.debug("Finding character by id: {}", id);
        return characterRepository.findById(id);
    }

    // Write transaction with proper isolation
    @Transactional(isolation = Isolation.READ_COMMITTED, propagation = Propagation.REQUIRED)
    @CacheEvict(value = "characters", key = "#result.id")
    public Character save(Character character) {
        log.info("Saving character: {}", character.getName());

        // Validate business rules
        validateCharacter(character);

        // Save with optimistic locking
        try {
            Character saved = characterRepository.save(character);
            log.info("Character saved successfully: {}", saved.getId());
            return saved;
        } catch (OptimisticLockingFailureException e) {
            log.warn("Optimistic locking failure for character: {}", character.getId());
            throw new ConcurrentModificationException("Character was modified by another user");
        }
    }

    // Batch operation with custom transaction
    @Transactional(propagation = Propagation.REQUIRES_NEW, timeout = 30)
    public void updateCrewBounties(Long crewId, BigDecimal multiplier) {
        log.info("Updating bounties for crew {} with multiplier {}", crewId, multiplier);

        int updatedCount = characterRepository.updateBountyForCrew(crewId, multiplier);
        log.info("Updated {} character bounties", updatedCount);

        // Clear cache for affected characters
        cacheManager.getCache("characters").clear();
    }

    // Complex query with Specifications
    public Page<Character> findCharacters(CharacterSearchCriteria criteria, Pageable pageable) {
        Specification<Character> spec = Specification.where(null);

        if (criteria.getMinBounty() != null) {
            spec = spec.and(CharacterRepository.hasMinBounty(criteria.getMinBounty()));
        }

        if (criteria.getCrewName() != null) {
            spec = spec.and(CharacterRepository.belongsToCrew(criteria.getCrewName()));
        }

        return characterRepository.findAll(spec, pageable);
    }

    private void validateCharacter(Character character) {
        if (character.getBounty().compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Bounty cannot be negative");
        }

        if (character.getName() == null || character.getName().trim().isEmpty()) {
            throw new IllegalArgumentException("Character name is required");
        }
    }
}
```

### **🚀 Practice Questions & Solutions:**

**1️⃣ What's the difference between FetchType.LAZY and FetchType.EAGER?**
```java
// In One Piece context:

// LAZY (Default for @OneToMany, @ManyToMany) - Loads data on demand
@OneToMany(fetch = FetchType.LAZY)
private List<Ability> abilities; // Not loaded until accessed

// EAGER (Default for @ManyToOne, @OneToOne) - Loads data immediately
@ManyToOne(fetch = FetchType.EAGER)
private Crew crew; // Always loaded with Character

// Best Practice: Use LAZY + Entity Graphs for performance
@EntityGraph("Character.withCrewAndAbilities")
List<Character> findByCrewName(String crewName);
```

**2️⃣ How does Hibernate's 1st and 2nd Level Cache work?**
```java
// First Level Cache (Session Cache) - Automatic
@Transactional
public void demonstrateFirstLevelCache() {
    Character luffy1 = characterRepository.findById(1L).orElse(null); // DB query
    Character luffy2 = characterRepository.findById(1L).orElse(null); // From cache (same session)
    // luffy1 == luffy2 (same object reference)
}

// Second Level Cache (SessionFactory Cache) - Configured
@Entity
@Cache(usage = CacheConcurrencyStrategy.READ_WRITE)
public class Character {
    // Cached across sessions
}

// Configuration in application.yml:
spring:
  jpa:
    properties:
      hibernate:
        cache:
          use_second_level_cache: true
          region:
            factory_class: org.hibernate.cache.jcache.JCacheRegionFactory
```

**3️⃣ Solving N+1 Query Problem:**
```java
// Problem: Loading characters with their abilities
List<Character> characters = characterRepository.findAll(); // 1 query
for (Character character : characters) {
    character.getAbilities().size(); // N queries (one per character)
}

// Solution 1: Fetch Join
@Query("SELECT DISTINCT c FROM Character c LEFT JOIN FETCH c.abilities")
List<Character> findAllWithAbilities();

// Solution 2: Entity Graph
@EntityGraph(attributePaths = {"abilities", "crew"})
List<Character> findAll();

// Solution 3: Batch Fetching
@OneToMany(fetch = FetchType.LAZY)
@BatchSize(size = 25)
private List<Ability> abilities;
```

---

# **🔥 4. Spring Boot Security & JWT Authentication**

## **✅ Enterprise Security for One Piece Trading**

### **🎯 COMPLETE SECURITY IMPLEMENTATION:**

```java
// JWT Security Configuration
@Configuration
@EnableWebSecurity
@EnableMethodSecurity(prePostEnabled = true)
public class SecurityConfig {

    private final JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    private final JwtRequestFilter jwtRequestFilter;
    private final UserDetailsService userDetailsService;

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder(12); // Strong hashing
    }

    @Bean
    public AuthenticationManager authenticationManager(
            AuthenticationConfiguration authConfig) throws Exception {
        return authConfig.getAuthenticationManager();
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf(csrf -> csrf.disable())
            .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(authz -> authz
                .requestMatchers("/api/v1/auth/**").permitAll()
                .requestMatchers("/api/v1/characters").hasAnyRole("USER", "TRADER", "ADMIN")
                .requestMatchers(HttpMethod.POST, "/api/v1/characters/*/trade").hasRole("TRADER")
                .requestMatchers(HttpMethod.POST, "/api/v1/characters").hasRole("ADMIN")
                .requestMatchers("/actuator/health").permitAll()
                .requestMatchers("/actuator/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .exceptionHandling(ex -> ex.authenticationEntryPoint(jwtAuthenticationEntryPoint))
            .addFilterBefore(jwtRequestFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}

// JWT Token Utility
@Component
public class JwtTokenUtil {

    private static final String SECRET = "onePieceSecretKey";
    private static final int JWT_TOKEN_VALIDITY = 5 * 60 * 60; // 5 hours

    public String getUsernameFromToken(String token) {
        return getClaimFromToken(token, Claims::getSubject);
    }

    public Date getExpirationDateFromToken(String token) {
        return getClaimFromToken(token, Claims::getExpiration);
    }

    public <T> T getClaimFromToken(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = getAllClaimsFromToken(token);
        return claimsResolver.apply(claims);
    }

    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();

        // Add custom claims
        if (userDetails instanceof OnePieceUserDetails) {
            OnePieceUserDetails opUser = (OnePieceUserDetails) userDetails;
            claims.put("userId", opUser.getUserId());
            claims.put("crew", opUser.getCrew());
            claims.put("bounty", opUser.getBounty());
        }

        return createToken(claims, userDetails.getUsername());
    }

    private String createToken(Map<String, Object> claims, String subject) {
        return Jwts.builder()
            .setClaims(claims)
            .setSubject(subject)
            .setIssuedAt(new Date(System.currentTimeMillis()))
            .setExpiration(new Date(System.currentTimeMillis() + JWT_TOKEN_VALIDITY * 1000))
            .signWith(SignatureAlgorithm.HS512, SECRET)
            .compact();
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = getUsernameFromToken(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
}

// Custom UserDetails Implementation
public class OnePieceUserDetails implements UserDetails {

    private final User user;

    public OnePieceUserDetails(User user) {
        this.user = user;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return user.getRoles().stream()
            .map(role -> new SimpleGrantedAuthority("ROLE_" + role.getName()))
            .collect(Collectors.toList());
    }

    @Override
    public String getPassword() {
        return user.getPassword();
    }

    @Override
    public String getUsername() {
        return user.getEmail();
    }

    // Custom getters for JWT claims
    public Long getUserId() {
        return user.getId();
    }

    public String getCrew() {
        return user.getCrew() != null ? user.getCrew().getName() : null;
    }

    public BigDecimal getBounty() {
        return user.getBounty();
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        return !user.isLocked();
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return user.isActive();
    }
}
```

---

# **🔥 5. Spring Boot Kafka & Event-Driven Architecture**

## **✅ Real-Time Trading Events with Kafka**

### **🎯 ONE PIECE TRADING EVENT SYSTEM:**

```java
// Kafka Configuration for Trading Events
@Configuration
@EnableKafka
public class KafkaConfig {

    @Value("${spring.kafka.bootstrap-servers}")
    private String bootstrapServers;

    // Producer Configuration
    @Bean
    public ProducerFactory<String, Object> producerFactory() {
        Map<String, Object> configProps = new HashMap<>();
        configProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        configProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        configProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
        configProps.put(ProducerConfig.ACKS_CONFIG, "all"); // Ensure durability
        configProps.put(ProducerConfig.RETRIES_CONFIG, 3);
        configProps.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true); // Exactly-once semantics
        return new DefaultKafkaProducerFactory<>(configProps);
    }

    @Bean
    public KafkaTemplate<String, Object> kafkaTemplate() {
        return new KafkaTemplate<>(producerFactory());
    }

    // Consumer Configuration
    @Bean
    public ConsumerFactory<String, Object> consumerFactory() {
        Map<String, Object> props = new HashMap<>();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "onepiece-trading-group");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class);
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, JsonDeserializer.class);
        props.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        props.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false); // Manual commit for reliability
        props.put(JsonDeserializer.TRUSTED_PACKAGES, "com.onepiece.trading.events");
        return new DefaultKafkaConsumerFactory<>(props);
    }

    @Bean
    public ConcurrentKafkaListenerContainerFactory<String, Object> kafkaListenerContainerFactory() {
        ConcurrentKafkaListenerContainerFactory<String, Object> factory = new ConcurrentKafkaListenerContainerFactory<>();
        factory.setConsumerFactory(consumerFactory());
        factory.getContainerProperties().setAckMode(ContainerProperties.AckMode.MANUAL_IMMEDIATE);
        return factory;
    }
}

// Trading Event Publisher
@Service
@Slf4j
public class TradingEventPublisher {

    private final KafkaTemplate<String, Object> kafkaTemplate;

    public TradingEventPublisher(KafkaTemplate<String, Object> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void publishTradeExecuted(TradeExecutedEvent event) {
        log.info("Publishing trade executed event: {}", event);

        kafkaTemplate.send("trade-executed", event.getTradeId().toString(), event)
            .addCallback(
                result -> log.info("Trade event sent successfully: {}", event.getTradeId()),
                failure -> log.error("Failed to send trade event: {}", event.getTradeId(), failure)
            );
    }

    public void publishCharacterPriceUpdated(CharacterPriceUpdatedEvent event) {
        log.info("Publishing character price update: {}", event);

        kafkaTemplate.send("character-price-updated", event.getCharacterId().toString(), event);
    }

    public void publishUserRegistered(UserRegisteredEvent event) {
        log.info("Publishing user registration event: {}", event);

        kafkaTemplate.send("user-registered", event.getUserId().toString(), event);
    }
}

// Event Consumer for Real-time Processing
@Component
@Slf4j
public class TradingEventConsumer {

    private final NotificationService notificationService;
    private final AnalyticsService analyticsService;
    private final CacheManager cacheManager;

    public TradingEventConsumer(NotificationService notificationService,
                              AnalyticsService analyticsService,
                              CacheManager cacheManager) {
        this.notificationService = notificationService;
        this.analyticsService = analyticsService;
        this.cacheManager = cacheManager;
    }

    @KafkaListener(topics = "trade-executed", groupId = "notification-service")
    public void handleTradeExecuted(TradeExecutedEvent event, Acknowledgment ack) {
        try {
            log.info("Processing trade executed event: {}", event);

            // Send notifications to involved parties
            notificationService.notifyTradeParticipants(event);

            // Update real-time analytics
            analyticsService.recordTrade(event);

            // Invalidate relevant caches
            cacheManager.getCache("character-prices").evict(event.getCharacterId());

            ack.acknowledge(); // Manual acknowledgment for reliability
            log.info("Successfully processed trade event: {}", event.getTradeId());

        } catch (Exception e) {
            log.error("Error processing trade event: {}", event.getTradeId(), e);
            // Don't acknowledge - message will be retried
        }
    }

    @KafkaListener(topics = "character-price-updated", groupId = "price-alert-service")
    public void handleCharacterPriceUpdated(CharacterPriceUpdatedEvent event, Acknowledgment ack) {
        try {
            log.info("Processing character price update: {}", event);

            // Check for price alerts
            notificationService.checkPriceAlerts(event.getCharacterId(), event.getNewPrice());

            // Update market data
            analyticsService.updateMarketData(event);

            ack.acknowledge();

        } catch (Exception e) {
            log.error("Error processing price update event: {}", event.getCharacterId(), e);
        }
    }

    @KafkaListener(topics = "user-registered", groupId = "welcome-service")
    public void handleUserRegistered(UserRegisteredEvent event, Acknowledgment ack) {
        try {
            log.info("Processing user registration: {}", event);

            // Send welcome email
            notificationService.sendWelcomeEmail(event.getUserId());

            // Initialize user preferences
            analyticsService.initializeUserProfile(event);

            ack.acknowledge();

        } catch (Exception e) {
            log.error("Error processing user registration: {}", event.getUserId(), e);
        }
    }
}

// Event Models
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class TradeExecutedEvent {
    private Long tradeId;
    private Long buyerId;
    private Long sellerId;
    private Long characterId;
    private BigDecimal price;
    private LocalDateTime executedAt;
    private TradeType type;
}

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class CharacterPriceUpdatedEvent {
    private Long characterId;
    private String characterName;
    private BigDecimal oldPrice;
    private BigDecimal newPrice;
    private BigDecimal changePercentage;
    private LocalDateTime updatedAt;
}
```

---

# **🔥 6. Spring Boot Microservices & Distributed Systems**

## **✅ Enterprise Microservices Architecture**

### **🎯 ONE PIECE MICROSERVICES ECOSYSTEM:**

```java
// Service Discovery with Eureka
@SpringBootApplication
@EnableEurekaClient
@EnableCircuitBreaker
@EnableFeignClients
public class CharacterServiceApplication {
    public static void main(String[] args) {
        SpringApplication.run(CharacterServiceApplication.class, args);
    }
}

// Feign Client for Inter-Service Communication
@FeignClient(name = "user-service", fallback = UserServiceFallback.class)
public interface UserServiceClient {

    @GetMapping("/api/v1/users/{userId}")
    UserDto getUser(@PathVariable("userId") Long userId);

    @PostMapping("/api/v1/users/{userId}/balance/deduct")
    BalanceResponse deductBalance(@PathVariable("userId") Long userId,
                                @RequestBody DeductBalanceRequest request);

    @GetMapping("/api/v1/users/{userId}/trading-limits")
    TradingLimitsDto getTradingLimits(@PathVariable("userId") Long userId);
}

// Circuit Breaker Implementation
@Component
@Slf4j
public class UserServiceFallback implements UserServiceClient {

    @Override
    public UserDto getUser(Long userId) {
        log.warn("User service unavailable, returning fallback for user: {}", userId);
        return UserDto.builder()
            .id(userId)
            .name("Unknown User")
            .status("UNAVAILABLE")
            .build();
    }

    @Override
    public BalanceResponse deductBalance(Long userId, DeductBalanceRequest request) {
        log.error("User service unavailable, cannot deduct balance for user: {}", userId);
        throw new ServiceUnavailableException("User service is currently unavailable");
    }

    @Override
    public TradingLimitsDto getTradingLimits(Long userId) {
        log.warn("User service unavailable, returning default limits for user: {}", userId);
        return TradingLimitsDto.builder()
            .dailyLimit(BigDecimal.valueOf(1000000))
            .transactionLimit(BigDecimal.valueOf(100000))
            .build();
    }
}

// Resilience4j Circuit Breaker Configuration
@Configuration
public class ResilienceConfig {

    @Bean
    public CircuitBreaker tradingCircuitBreaker() {
        return CircuitBreaker.ofDefaults("trading-service");
    }

    @Bean
    public RetryTemplate retryTemplate() {
        RetryTemplate retryTemplate = new RetryTemplate();

        FixedBackOffPolicy backOffPolicy = new FixedBackOffPolicy();
        backOffPolicy.setBackOffPeriod(2000); // 2 seconds
        retryTemplate.setBackOffPolicy(backOffPolicy);

        SimpleRetryPolicy retryPolicy = new SimpleRetryPolicy();
        retryPolicy.setMaxAttempts(3);
        retryTemplate.setRetryPolicy(retryPolicy);

        return retryTemplate;
    }
}

// Distributed Trading Service
@Service
@Slf4j
public class DistributedTradingService {

    private final UserServiceClient userServiceClient;
    private final CharacterRepository characterRepository;
    private final TradingEventPublisher eventPublisher;
    private final CircuitBreaker circuitBreaker;
    private final RetryTemplate retryTemplate;

    @CircuitBreaker(name = "trading-service", fallbackMethod = "fallbackExecuteTrade")
    @Retry(name = "trading-service")
    @TimeLimiter(name = "trading-service")
    @Transactional
    public CompletableFuture<TradeResult> executeTrade(TradeRequest request) {
        return CompletableFuture.supplyAsync(() -> {
            log.info("Executing trade: {}", request);

            // 1. Validate character exists and is available
            Character character = characterRepository.findById(request.getCharacterId())
                .orElseThrow(() -> new CharacterNotFoundException("Character not found"));

            // 2. Check user balance (external service call)
            UserDto buyer = userServiceClient.getUser(request.getBuyerId());
            if (buyer.getBalance().compareTo(request.getPrice()) < 0) {
                throw new InsufficientFundsException("Insufficient balance");
            }

            // 3. Check trading limits (external service call)
            TradingLimitsDto limits = userServiceClient.getTradingLimits(request.getBuyerId());
            if (request.getPrice().compareTo(limits.getTransactionLimit()) > 0) {
                throw new TradingLimitExceededException("Transaction exceeds daily limit");
            }

            // 4. Deduct balance (external service call)
            DeductBalanceRequest deductRequest = DeductBalanceRequest.builder()
                .amount(request.getPrice())
                .reason("Character purchase: " + character.getName())
                .build();

            BalanceResponse balanceResponse = userServiceClient.deductBalance(request.getBuyerId(), deductRequest);

            // 5. Create trade record
            Trade trade = Trade.builder()
                .buyerId(request.getBuyerId())
                .sellerId(character.getOwnerId())
                .characterId(character.getId())
                .price(request.getPrice())
                .status(TradeStatus.COMPLETED)
                .executedAt(LocalDateTime.now())
                .build();

            // 6. Update character ownership
            character.setOwnerId(request.getBuyerId());
            characterRepository.save(character);

            // 7. Publish trade event
            TradeExecutedEvent event = TradeExecutedEvent.builder()
                .tradeId(trade.getId())
                .buyerId(request.getBuyerId())
                .sellerId(character.getOwnerId())
                .characterId(character.getId())
                .price(request.getPrice())
                .executedAt(LocalDateTime.now())
                .type(TradeType.PURCHASE)
                .build();

            eventPublisher.publishTradeExecuted(event);

            return TradeResult.builder()
                .tradeId(trade.getId())
                .status("SUCCESS")
                .message("Trade executed successfully")
                .newBalance(balanceResponse.getNewBalance())
                .build();
        });
    }

    // Fallback method for circuit breaker
    public CompletableFuture<TradeResult> fallbackExecuteTrade(TradeRequest request, Exception ex) {
        log.error("Trade execution failed, using fallback: {}", ex.getMessage());

        return CompletableFuture.completedFuture(
            TradeResult.builder()
                .status("FAILED")
                .message("Trading service is temporarily unavailable. Please try again later.")
                .build()
        );
    }
}
```

---

# **🔥 7. Spring Boot Performance Optimization**

## **✅ High-Performance Trading System**

### **🎯 PERFORMANCE OPTIMIZATION TECHNIQUES:**

```java
// Async Processing for High Throughput
@Service
@Slf4j
public class AsyncTradingService {

    @Async("tradingExecutor")
    @Retryable(value = {Exception.class}, maxAttempts = 3, backoff = @Backoff(delay = 1000))
    public CompletableFuture<Void> processTradeAsync(TradeRequest request) {
        log.info("Processing trade asynchronously: {}", request.getTradeId());

        try {
            // Simulate complex trade processing
            Thread.sleep(2000);

            // Process trade logic here
            log.info("Trade processed successfully: {}", request.getTradeId());

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException("Trade processing interrupted", e);
        }

        return CompletableFuture.completedFuture(null);
    }

    @Async("tradingExecutor")
    public CompletableFuture<List<CharacterDto>> getCharactersAsync(List<Long> characterIds) {
        return CompletableFuture.supplyAsync(() -> {
            // Batch fetch characters for better performance
            return characterRepository.findAllById(characterIds)
                .stream()
                .map(this::toDto)
                .collect(Collectors.toList());
        });
    }
}

// Caching Strategy for High-Performance Reads
@Service
@CacheConfig(cacheNames = "characters")
@Slf4j
public class CachedCharacterService {

    private final CharacterRepository characterRepository;
    private final RedisTemplate<String, Object> redisTemplate;

    @Cacheable(key = "#id", unless = "#result == null")
    public Optional<Character> findById(Long id) {
        log.debug("Fetching character from database: {}", id);
        return characterRepository.findById(id);
    }

    @Cacheable(key = "'top-characters:' + #limit")
    public List<Character> getTopCharactersByBounty(int limit) {
        log.debug("Fetching top {} characters by bounty", limit);
        return characterRepository.findTopByBounty(PageRequest.of(0, limit));
    }

    @CacheEvict(key = "#character.id")
    public Character save(Character character) {
        log.debug("Saving character and evicting cache: {}", character.getId());
        return characterRepository.save(character);
    }

    @CacheEvict(allEntries = true)
    public void clearAllCache() {
        log.info("Clearing all character cache");
    }

    // Custom cache implementation with Redis
    public List<Character> getPopularCharacters() {
        String cacheKey = "popular-characters";

        // Try to get from Redis cache first
        List<Character> cached = (List<Character>) redisTemplate.opsForValue().get(cacheKey);
        if (cached != null) {
            log.debug("Returning popular characters from Redis cache");
            return cached;
        }

        // Fetch from database if not in cache
        List<Character> characters = characterRepository.findPopularCharacters();

        // Cache for 1 hour
        redisTemplate.opsForValue().set(cacheKey, characters, Duration.ofHours(1));

        log.debug("Cached popular characters in Redis");
        return characters;
    }
}

// Database Connection Pool Optimization
@Configuration
public class DatabaseConfig {

    @Bean
    @ConfigurationProperties("spring.datasource.hikari")
    public HikariConfig hikariConfig() {
        HikariConfig config = new HikariConfig();

        // Performance optimizations
        config.setMaximumPoolSize(20);
        config.setMinimumIdle(5);
        config.setConnectionTimeout(30000);
        config.setIdleTimeout(600000);
        config.setMaxLifetime(1800000);
        config.setLeakDetectionThreshold(60000);

        // Connection pool monitoring
        config.setRegisterMbeans(true);

        return config;
    }

    @Bean
    public DataSource dataSource() {
        return new HikariDataSource(hikariConfig());
    }
}

// JVM Performance Monitoring
@Component
@Slf4j
public class PerformanceMonitor {

    private final MeterRegistry meterRegistry;
    private final MemoryMXBean memoryBean;
    private final List<GarbageCollectorMXBean> gcBeans;

    public PerformanceMonitor(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        this.memoryBean = ManagementFactory.getMemoryMXBean();
        this.gcBeans = ManagementFactory.getGarbageCollectorMXBeans();

        // Register custom metrics
        registerMemoryMetrics();
        registerGCMetrics();
    }

    private void registerMemoryMetrics() {
        Gauge.builder("jvm.memory.heap.used")
            .description("Used heap memory")
            .register(meterRegistry, this, monitor -> monitor.memoryBean.getHeapMemoryUsage().getUsed());

        Gauge.builder("jvm.memory.heap.max")
            .description("Max heap memory")
            .register(meterRegistry, this, monitor -> monitor.memoryBean.getHeapMemoryUsage().getMax());
    }

    private void registerGCMetrics() {
        for (GarbageCollectorMXBean gcBean : gcBeans) {
            Gauge.builder("jvm.gc.collections")
                .tag("gc", gcBean.getName())
                .description("GC collections")
                .register(meterRegistry, gcBean, GarbageCollectorMXBean::getCollectionCount);

            Gauge.builder("jvm.gc.time")
                .tag("gc", gcBean.getName())
                .description("GC time")
                .register(meterRegistry, gcBean, GarbageCollectorMXBean::getCollectionTime);
        }
    }

    @EventListener
    public void handleTradeEvent(TradeExecutedEvent event) {
        // Record trade metrics
        Timer.Sample sample = Timer.start(meterRegistry);
        sample.stop(Timer.builder("onepiece.trade.execution.time")
            .tag("type", event.getType().name())
            .register(meterRegistry));
    }
}
```

---

# **🔥 8. High-Performance Networking & Reactive Systems**

## **✅ Netty & WebFlux for Ultra-High Performance**

### **🎯 REACTIVE ONE PIECE TRADING API:**

```java
// Reactive Character Controller with WebFlux
@RestController
@RequestMapping("/api/v2/characters")
@Slf4j
public class ReactiveCharacterController {

    private final ReactiveCharacterService characterService;

    public ReactiveCharacterController(ReactiveCharacterService characterService) {
        this.characterService = characterService;
    }

    @GetMapping(produces = MediaType.APPLICATION_NDJSON_VALUE)
    public Flux<CharacterDto> streamCharacters() {
        return characterService.findAllCharacters()
            .delayElements(Duration.ofMillis(100)) // Simulate real-time streaming
            .doOnNext(character -> log.debug("Streaming character: {}", character.getName()));
    }

    @GetMapping("/{id}")
    public Mono<ResponseEntity<CharacterDto>> getCharacter(@PathVariable Long id) {
        return characterService.findById(id)
            .map(character -> ResponseEntity.ok(toDto(character)))
            .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @PostMapping
    public Mono<ResponseEntity<CharacterDto>> createCharacter(@Valid @RequestBody CreateCharacterRequest request) {
        return characterService.create(request)
            .map(character -> ResponseEntity.status(HttpStatus.CREATED).body(toDto(character)))
            .onErrorResume(ValidationException.class,
                ex -> Mono.just(ResponseEntity.badRequest().build()));
    }

    @GetMapping("/search")
    public Flux<CharacterDto> searchCharacters(@RequestParam String query) {
        return characterService.searchCharacters(query)
            .map(this::toDto)
            .onErrorResume(ex -> {
                log.error("Error searching characters", ex);
                return Flux.empty();
            });
    }
}

// Reactive Service Layer
@Service
@Slf4j
public class ReactiveCharacterService {

    private final ReactiveCharacterRepository characterRepository;
    private final WebClient userServiceClient;

    public ReactiveCharacterService(ReactiveCharacterRepository characterRepository,
                                  WebClient.Builder webClientBuilder) {
        this.characterRepository = characterRepository;
        this.userServiceClient = webClientBuilder
            .baseUrl("http://user-service")
            .build();
    }

    public Flux<Character> findAllCharacters() {
        return characterRepository.findAll()
            .doOnSubscribe(subscription -> log.info("Starting character stream"))
            .doOnComplete(() -> log.info("Character stream completed"));
    }

    public Mono<Character> findById(Long id) {
        return characterRepository.findById(id)
            .doOnNext(character -> log.debug("Found character: {}", character.getName()))
            .doOnError(ex -> log.error("Error finding character: {}", id, ex));
    }

    public Mono<Character> create(CreateCharacterRequest request) {
        return Mono.fromCallable(() -> {
            Character character = Character.builder()
                .name(request.getName())
                .bounty(request.getBounty())
                .type(request.getType())
                .build();
            return character;
        })
        .flatMap(characterRepository::save)
        .doOnSuccess(character -> log.info("Created character: {}", character.getName()));
    }

    public Flux<Character> searchCharacters(String query) {
        return characterRepository.findByNameContainingIgnoreCase(query)
            .timeout(Duration.ofSeconds(5))
            .onErrorResume(TimeoutException.class,
                ex -> Flux.error(new SearchTimeoutException("Search timed out")));
    }

    // Reactive external service call
    public Mono<UserDto> getUserReactive(Long userId) {
        return userServiceClient
            .get()
            .uri("/api/v1/users/{userId}", userId)
            .retrieve()
            .bodyToMono(UserDto.class)
            .timeout(Duration.ofSeconds(3))
            .retry(2)
            .onErrorResume(ex -> {
                log.warn("Failed to get user {}: {}", userId, ex.getMessage());
                return Mono.just(UserDto.builder().id(userId).name("Unknown").build());
            });
    }
}

// WebClient Configuration for Reactive HTTP Calls
@Configuration
public class WebClientConfig {

    @Bean
    public WebClient.Builder webClientBuilder() {
        return WebClient.builder()
            .clientConnector(new ReactorClientHttpConnector(
                HttpClient.create()
                    .option(ChannelOption.CONNECT_TIMEOUT_MILLIS, 3000)
                    .responseTimeout(Duration.ofSeconds(3))
                    .doOnConnected(conn ->
                        conn.addHandlerLast(new ReadTimeoutHandler(3))
                            .addHandlerLast(new WriteTimeoutHandler(3)))
            ))
            .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
            .defaultHeader(HttpHeaders.USER_AGENT, "OnePiece-Trading-Service/1.0");
    }

    @Bean
    @LoadBalanced
    public WebClient.Builder loadBalancedWebClientBuilder() {
        return webClientBuilder();
    }
}
```

---

## **💰 COMPLETE SPRING BOOT MASTERY IMPACT:**

### **🔥 SALARY PROGRESSION:**
- **Basic Spring Boot**: $75K-$95K (REST APIs, basic features)
- **Advanced Spring Boot**: $105K-$145K (Security, JPA, caching)
- **Enterprise Spring Boot**: $145K-$195K (Microservices, Kafka, performance)
- **Reactive Spring Boot**: $195K-$300K (WebFlux, Netty, high-performance)
- **Spring Boot Architect**: $300K-$600K+ (Platform design, team leadership)

### **🏢 COMPANIES HIRING SPRING BOOT EXPERTS:**
- **Netflix**: $200K-$400K (Microservices, reactive systems)
- **Amazon**: $180K-$350K (High-scale backend systems)
- **Google**: $220K-$450K (Enterprise platforms, performance)
- **LinkedIn**: $190K-$380K (Social platform backend)
- **Uber**: $200K-$400K (Real-time systems, high throughput)

---

## **🎯 QUICK START WITH YOUR ONE PIECE PROJECT:**

```bash
# 1. Start your Spring Boot service
cd learning-modules/33-java-spring-boot-enterprise
./start-java-service.sh start

# 2. Test the reactive endpoints
curl http://localhost:8080/api/v2/characters

# 3. Stream characters in real-time
curl -N http://localhost:8080/api/v2/characters

# 4. Check performance metrics
curl http://localhost:8080/actuator/metrics

# 5. Monitor health
curl http://localhost:8080/actuator/health
```

**🏴‍☠️ CONGRATULATIONS! YOU NOW HAVE COMPLETE SPRING BOOT MASTERY!**

**🚀 FROM BASIC CRUD TO REACTIVE MICROSERVICES - YOU'VE MASTERED IT ALL!**

**⚔️ READY TO BUILD THE NEXT NETFLIX OR AMAZON WITH SPRING BOOT!** 🎉
