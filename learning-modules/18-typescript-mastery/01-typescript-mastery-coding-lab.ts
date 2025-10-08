/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - TYPESCRIPT MASTERY LAB
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL BUILD FOR YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ TYPE-SAFE CHARACTER TRADING API - Strongly typed interfaces
✅ ADVANCED TYPE SYSTEM - Generics, unions, intersections
✅ TYPESCRIPT OOP MASTERY - Classes with proper typing
✅ DECORATOR PATTERNS - Method decorators for logging/validation
✅ UTILITY TYPES - Pick, Omit, Partial for API responses
✅ TYPE GUARDS & ASSERTIONS - Runtime type checking
✅ MODULE SYSTEM - Proper imports/exports with types
✅ CONFIGURATION SYSTEM - Type-safe environment variables

💰 SALARY IMPACT: +$60K-?20K (TypeScript is MANDATORY in 2024)
🏢 COMPANIES: Microsoft, Google, Airbnb, Slack, Discord, Shopify

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 YOUR CURRENT CharacterList.tsx COMPONENT:
   - Has basic TypeScript → You'll add advanced type safety
   - Uses any types → You'll create proper interfaces
   - Basic error handling → You'll add type-safe error types
   - Simple props → You'll use generic components

🎯 YOUR CURRENT PROJECT STRUCTURE:
   - Mixed JS/TS files → You'll standardize on TypeScript
   - Basic types → You'll create comprehensive type system
   - No validation → You'll add runtime type checking
   - Simple interfaces → You'll use advanced type patterns

🎯 WHAT YOU'LL ADD TO YOUR PROJECT:
   - Complete type safety across frontend and backend
   - Advanced generic patterns for reusable components
   - Type-safe API client with proper error handling
   - Decorator-based validation and logging system
   - Utility types for database models and API responses

📚 TYPESCRIPT CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 TYPE SYSTEM MASTERY:
• Primitive types, interfaces, and type aliases
• Union and intersection types
• Generic types and constraints
• Conditional types and mapped types
• Template literal types

🏗️ ADVANCED OOP IN TYPESCRIPT:
• Classes with access modifiers
• Abstract classes and interfaces
• Decorators for methods and classes
• Mixins and composition patterns
• Method overloading and function signatures

⚡ UTILITY TYPES & TYPE MANIPULATION:
• Built-in utility types (Pick, Omit, Partial, Required)
• Custom utility types for your domain
• Type guards and type assertions
• Discriminated unions for state management
• Brand types for type safety

🔒 TYPE SAFETY PATTERNS:
• Strict null checks and optional chaining
• Error handling with Result types
• API response typing with generics
• Form validation with type-safe schemas
• Configuration management with const assertions

🔧 TYPESCRIPT SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. INTERFACES & TYPES:
   interface Character {
       readonly id: number;
       name: string;
       crew: string;
       bounty: number;
       devilFruit?: DevilFruit;
       hakiTypes: HakiType[];
   }
   
   type ApiResponse<T> = {
       data: T;
       status: 'success' | 'error';
       message?: string;
   };

2. GENERICS:
   class TradingService<T extends Character> {
       async trade<U extends TradeType>(
           character: T,
           tradeData: TradeRequest<U>
       ): Promise<TradeResult<T, U>> {
           // Type-safe trading logic
       }
   }

3. DECORATORS:
   class CharacterService {
       @log
       @validate
       async createCharacter(data: CreateCharacterRequest): Promise<Character> {
           // Decorated method with logging and validation
       }
   }

4. UTILITY TYPES:
   type CharacterUpdate = Partial<Pick<Character, 'name' | 'bounty'>>;
   type CharacterResponse = Omit<Character, 'createdAt'> & {
       marketCap: number;
   };
*/

// 🧪 HANDS-ON LAB 1: TYPE SYSTEM FUNDAMENTALS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 TYPESCRIPT TYPE SYSTEM EXPLAINED:
TypeScript adds static type checking to JavaScript, catching errors
at compile time instead of runtime. This is CRUCIAL for large applications
and professional development.

REAL-WORLD EXAMPLE:
Netflix uses TypeScript for their entire frontend, preventing bugs
that could crash the streaming service for millions of users.

IN ONE PIECE PROJECT:
Type-safe character data, trading operations, API responses, and
user interactions - preventing runtime errors in production.
*/

// TODO 1: BASIC TYPES & INTERFACES
// YOUR CODE HERE - Define character interfaces:


// TODO 2: UNION & INTERSECTION TYPES
// YOUR CODE HERE - Create flexible type combinations:


// TODO 3: GENERIC TYPES
// YOUR CODE HERE - Build reusable generic patterns:


// 🧪 HANDS-ON LAB 2: ADVANCED OOP WITH TYPESCRIPT
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 TYPESCRIPT OOP EXPLAINED:
TypeScript enhances JavaScript classes with access modifiers,
abstract classes, interfaces, and decorators. This provides
enterprise-level object-oriented programming capabilities.

REAL-WORLD EXAMPLE:
Angular framework is built entirely with TypeScript OOP patterns,
using decorators, dependency injection, and strict typing.

IN ONE PIECE PROJECT:
Character class hierarchies with proper encapsulation, abstract
battle systems, and decorator-based validation for trading operations.
*/

// TODO 4: CLASSES WITH ACCESS MODIFIERS
// YOUR CODE HERE - Create properly encapsulated classes:


// TODO 5: ABSTRACT CLASSES & INTERFACES
// YOUR CODE HERE - Build abstract patterns:


// TODO 6: DECORATORS
// YOUR CODE HERE - Implement method decorators:


// 🧪 HANDS-ON LAB 3: UTILITY TYPES & TYPE MANIPULATION
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 UTILITY TYPES EXPLAINED:
TypeScript provides powerful utility types that transform existing
types. These are essential for API design, form handling, and
maintaining type safety across complex applications.

REAL-WORLD EXAMPLE:
Shopify's admin interface uses utility types extensively to ensure
type safety between their GraphQL API and React components.

IN ONE PIECE PROJECT:
API response types, form validation schemas, database model
transformations, and component prop derivations.
*/

// TODO 7: BUILT-IN UTILITY TYPES
// YOUR CODE HERE - Use Pick, Omit, Partial, Required:


// TODO 8: CUSTOM UTILITY TYPES
// YOUR CODE HERE - Create domain-specific utilities:


// TODO 9: TYPE GUARDS & ASSERTIONS
// YOUR CODE HERE - Implement runtime type checking:


// 🧪 HANDS-ON LAB 4: API & ERROR HANDLING PATTERNS
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 TYPE-SAFE ERROR HANDLING EXPLAINED:
Professional TypeScript applications use Result types, discriminated
unions, and proper error boundaries to handle failures gracefully
while maintaining type safety.

REAL-WORLD EXAMPLE:
Discord's client uses TypeScript Result types to handle network
failures, API errors, and user input validation consistently.

IN ONE PIECE PROJECT:
Type-safe API client, error handling for trading operations,
form validation, and user feedback systems.
*/

// TODO 10: RESULT TYPES FOR ERROR HANDLING
// YOUR CODE HERE - Implement Result<T, E> pattern:


// TODO 11: API CLIENT WITH GENERICS
// YOUR CODE HERE - Build type-safe API client:


// TODO 12: FORM VALIDATION SCHEMAS
// YOUR CODE HERE - Create type-safe validation:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════
*/

// 🔥 COMPLETE TYPESCRIPT MASTERY IMPLEMENTATION

console.log('🏴‍☠️ TypeScript Mastery - One Piece Trading Platform');

// 1. TYPE SYSTEM FUNDAMENTALS SOLUTIONS

// Basic Types & Interfaces
interface Character {
    readonly id: number;
    name: string;
    crew: string;
    bounty: number;
    health: number;
    isAlive: boolean;
    devilFruit?: DevilFruit;
    hakiTypes: HakiType[];
    createdAt: Date;
    updatedAt: Date;
}

interface DevilFruit {
    readonly name: string;
    readonly type: 'Paramecia' | 'Zoan' | 'Logia';
    readonly awakened: boolean;
    power: string;
    weakness: string[];
}

type HakiType = 'Observation' | 'Armament' | "Conqueror's";

type CrewType = 'Pirate' | 'Marine' | 'Revolutionary' | 'Bounty Hunter';

// Union & Intersection Types
type CharacterStatus = 'Active' | 'Defeated' | 'Missing' | 'Retired';

type BattleResult = 'Victory' | 'Defeat' | 'Draw' | 'Interrupted';

// Intersection type for enhanced characters
type EnhancedCharacter = Character & {
    powerLevel: number;
    specialAbilities: string[];
    battleHistory: BattleRecord[];
};

interface BattleRecord {
    opponent: string;
    result: BattleResult;
    date: Date;
    location: string;
}

// Generic Types
interface ApiResponse<T> {
    data: T;
    status: 'success' | 'error';
    message?: string;
    timestamp: Date;
}

interface PaginatedResponse<T> extends ApiResponse<T[]> {
    pagination: {
        page: number;
        limit: number;
        total: number;
        totalPages: number;
    };
}

// Generic Repository Pattern
interface Repository<T, K = number> {
    findById(id: K): Promise<T | null>;
    findAll(): Promise<T[]>;
    create(entity: Omit<T, 'id' | 'createdAt' | 'updatedAt'>): Promise<T>;
    update(id: K, updates: Partial<T>): Promise<T>;
    delete(id: K): Promise<boolean>;
}

// 2. ADVANCED OOP WITH TYPESCRIPT SOLUTIONS

// Classes with Access Modifiers
abstract class BaseCharacter {
    protected readonly id: number;
    protected _name: string;
    protected _health: number = 100;
    private _secretTechniques: string[] = [];
    
    constructor(id: number, name: string) {
        this.id = id;
        this._name = name;
    }
    
    // Public getter
    public get name(): string {
        return this._name;
    }
    
    // Public setter with validation
    public set name(value: string) {
        if (value.length < 2) {
            throw new Error('Name must be at least 2 characters');
        }
        this._name = value;
    }
    
    // Protected method (accessible by subclasses)
    protected takeDamage(damage: number): void {
        this._health = Math.max(0, this._health - damage);
        if (this._health === 0) {
            console.log(`💀 ${this._name} has been defeated!`);
        }
    }
    
    // Private method (only accessible within this class)
    private learnSecretTechnique(technique: string): void {
        this._secretTechniques.push(technique);
        console.log(`🎯 ${this._name} learned secret technique: ${technique}`);
    }
    
    // Abstract method (must be implemented by subclasses)
    public abstract attack(target: BaseCharacter): AttackResult;
    
    // Abstract getter
    public abstract get characterType(): CrewType;
}

// Interface for combat behavior
interface Combatant {
    attack(target: Combatant): AttackResult;
    defend(): number;
    useSpecialAbility(): string;
}

// Interface for Devil Fruit users
interface DevilFruitUser {
    devilFruit: DevilFruit;
    useDevilFruitPower(): string;
    canSwim: false; // Devil Fruit users can't swim
}

// Concrete implementation
class Pirate extends BaseCharacter implements Combatant, DevilFruitUser {
    public readonly ship: string;
    public readonly position: string;
    public devilFruit?: DevilFruit;
    public readonly canSwim: false = false;
    
    constructor(
        id: number,
        name: string,
        ship: string,
        position: string = 'Crew Member'
    ) {
        super(id, name);
        this.ship = ship;
        this.position = position;
    }
    
    public get characterType(): CrewType {
        return 'Pirate';
    }
    
    public attack(target: BaseCharacter): AttackResult {
        const damage = Math.floor(Math.random() * 30) + 10;
        target.takeDamage(damage);
        
        return {
            attacker: this.name,
            target: target.name,
            damage,
            message: `⚔️ ${this.name} attacks ${target.name} for ${damage} damage!`,
            critical: damage > 25
        };
    }
    
    public defend(): number {
        return Math.floor(Math.random() * 15) + 5;
    }
    
    public useSpecialAbility(): string {
        if (this.devilFruit) {
            return this.useDevilFruitPower();
        }
        return `${this.name} uses a special sword technique!`;
    }
    
    public useDevilFruitPower(): string {
        if (!this.devilFruit) {
            throw new Error(`${this.name} doesn't have a Devil Fruit!`);
        }
        return `🔥 ${this.name} uses ${this.devilFruit.name} power: ${this.devilFruit.power}!`;
    }
    
    public eatDevilFruit(fruit: DevilFruit): void {
        if (this.devilFruit) {
            throw new Error(`${this.name} already has a Devil Fruit!`);
        }
        this.devilFruit = fruit;
        console.log(`🍎 ${this.name} ate the ${fruit.name}!`);
    }
}

interface AttackResult {
    attacker: string;
    target: string;
    damage: number;
    message: string;
    critical: boolean;
}

// Method Decorators
function log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        console.log(`📝 Calling ${propertyName} with args:`, args);
        const result = method.apply(this, args);
        console.log(`📝 ${propertyName} returned:`, result);
        return result;
    };
}

function validate(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        // Basic validation example
        if (args.some(arg => arg === null || arg === undefined)) {
            throw new Error(`${propertyName}: All arguments must be provided`);
        }
        return method.apply(this, args);
    };
}

function asyncErrorHandler(target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    
    descriptor.value = async function (...args: any[]) {
        try {
            return await method.apply(this, args);
        } catch (error) {
            console.error(`❌ Error in ${propertyName}:`, error);
            throw error;
        }
    };
}

// Service class with decorators
class CharacterService {
    private characters: Character[] = [];
    
    @log
    @validate
    public createCharacter(data: CreateCharacterRequest): Character {
        const character: Character = {
            id: this.characters.length + 1,
            ...data,
            health: 100,
            isAlive: true,
            hakiTypes: [],
            createdAt: new Date(),
            updatedAt: new Date()
        };
        
        this.characters.push(character);
        return character;
    }
    
    @log
    @asyncErrorHandler
    public async fetchCharacterById(id: number): Promise<Character | null> {
        // Simulate async operation
        await new Promise(resolve => setTimeout(resolve, 100));
        return this.characters.find(char => char.id === id) || null;
    }
    
    @log
    public updateCharacter(id: number, updates: CharacterUpdate): Character {
        const character = this.characters.find(char => char.id === id);
        if (!character) {
            throw new Error(`Character with id ${id} not found`);
        }
        
        Object.assign(character, updates, { updatedAt: new Date() });
        return character;
    }
}

// 3. UTILITY TYPES & TYPE MANIPULATION SOLUTIONS

// Built-in Utility Types
type CreateCharacterRequest = Omit<Character, 'id' | 'health' | 'isAlive' | 'hakiTypes' | 'createdAt' | 'updatedAt'>;

type CharacterUpdate = Partial<Pick<Character, 'name' | 'crew' | 'bounty'>>;

type CharacterResponse = Omit<Character, 'createdAt' | 'updatedAt'> & {
    marketCap: number;
    priceChange: number;
};

type RequiredCharacterFields = Required<Pick<Character, 'name' | 'crew'>>;

// Custom Utility Types
type DeepPartial<T> = {
    [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

type NonNullable<T> = T extends null | undefined ? never : T;

type ExtractArrayType<T> = T extends (infer U)[] ? U : never;

// Conditional Types
type IsArray<T> = T extends any[] ? true : false;

type GetReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

// Template Literal Types
type EventName<T extends string> = `on${Capitalize<T>}`;

type ApiEndpoint<T extends string> = `/api/${T}`;

// Mapped Types
type ReadonlyCharacter = {
    readonly [K in keyof Character]: Character[K];
};

type OptionalCharacter = {
    [K in keyof Character]?: Character[K];
};

// Type Guards
function isCharacter(obj: any): obj is Character {
    return (
        typeof obj === 'object' &&
        obj !== null &&
        typeof obj.id === 'number' &&
        typeof obj.name === 'string' &&
        typeof obj.crew === 'string' &&
        typeof obj.bounty === 'number'
    );
}

function isPirate(character: Character): character is Character & { characterType: 'Pirate' } {
    return character.crew.toLowerCase().includes('pirate');
}

function hasDevilFruit(character: Character): character is Character & { devilFruit: DevilFruit } {
    return character.devilFruit !== undefined;
}

// Discriminated Unions
type LoadingState = {
    status: 'loading';
};

type SuccessState<T> = {
    status: 'success';
    data: T;
};

type ErrorState = {
    status: 'error';
    error: string;
};

type AsyncState<T> = LoadingState | SuccessState<T> | ErrorState;

// 4. API & ERROR HANDLING PATTERNS SOLUTIONS

// Result Type for Error Handling
type Result<T, E = Error> = Success<T> | Failure<E>;

interface Success<T> {
    success: true;
    data: T;
}

interface Failure<E> {
    success: false;
    error: E;
}

// Result utility functions
const success = <T>(data: T): Success<T> => ({ success: true, data });

const failure = <E>(error: E): Failure<E> => ({ success: false, error });

// Type-safe API Client
class ApiClient {
    private baseUrl: string;
    
    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }
    
    async get<T>(endpoint: string): Promise<Result<T, string>> {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`);
            
            if (!response.ok) {
                return failure(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            return success(data);
        } catch (error) {
            return failure(error instanceof Error ? error.message : 'Unknown error');
        }
    }
    
    async post<T, U>(endpoint: string, body: U): Promise<Result<T, string>> {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(body),
            });
            
            if (!response.ok) {
                return failure(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const data = await response.json();
            return success(data);
        } catch (error) {
            return failure(error instanceof Error ? error.message : 'Unknown error');
        }
    }
}

// Generic Repository Implementation
class CharacterRepository implements Repository<Character> {
    private apiClient: ApiClient;
    
    constructor(apiClient: ApiClient) {
        this.apiClient = apiClient;
    }
    
    async findById(id: number): Promise<Character | null> {
        const result = await this.apiClient.get<Character>(`/characters/${id}`);
        
        if (result.success) {
            return isCharacter(result.data) ? result.data : null;
        }
        
        console.error('Failed to fetch character:', result.error);
        return null;
    }
    
    async findAll(): Promise<Character[]> {
        const result = await this.apiClient.get<Character[]>('/characters');
        
        if (result.success) {
            return result.data.filter(isCharacter);
        }
        
        console.error('Failed to fetch characters:', result.error);
        return [];
    }
    
    async create(data: CreateCharacterRequest): Promise<Character> {
        const result = await this.apiClient.post<Character, CreateCharacterRequest>('/characters', data);
        
        if (result.success && isCharacter(result.data)) {
            return result.data;
        }
        
        throw new Error(result.success ? 'Invalid character data' : result.error);
    }
    
    async update(id: number, updates: CharacterUpdate): Promise<Character> {
        const result = await this.apiClient.post<Character, CharacterUpdate>(`/characters/${id}`, updates);
        
        if (result.success && isCharacter(result.data)) {
            return result.data;
        }
        
        throw new Error(result.success ? 'Invalid character data' : result.error);
    }
    
    async delete(id: number): Promise<boolean> {
        const result = await this.apiClient.get<{ success: boolean }>(`/characters/${id}`);
        return result.success && result.data.success;
    }
}

// Form Validation Schema
interface ValidationRule<T> {
    validate: (value: T) => boolean;
    message: string;
}

type ValidationSchema<T> = {
    [K in keyof T]: ValidationRule<T[K]>[];
};

class FormValidator<T> {
    private schema: ValidationSchema<T>;
    
    constructor(schema: ValidationSchema<T>) {
        this.schema = schema;
    }
    
    validate(data: T): Result<T, Record<keyof T, string[]>> {
        const errors: Partial<Record<keyof T, string[]>> = {};
        
        for (const field in this.schema) {
            const rules = this.schema[field];
            const value = data[field];
            const fieldErrors: string[] = [];
            
            for (const rule of rules) {
                if (!rule.validate(value)) {
                    fieldErrors.push(rule.message);
                }
            }
            
            if (fieldErrors.length > 0) {
                errors[field] = fieldErrors;
            }
        }
        
        if (Object.keys(errors).length > 0) {
            return failure(errors as Record<keyof T, string[]>);
        }
        
        return success(data);
    }
}

// Example validation schema
const characterValidationSchema: ValidationSchema<CreateCharacterRequest> = {
    name: [
        { validate: (name) => name.length >= 2, message: 'Name must be at least 2 characters' },
        { validate: (name) => name.length <= 50, message: 'Name must be less than 50 characters' }
    ],
    crew: [
        { validate: (crew) => crew.length >= 2, message: 'Crew name must be at least 2 characters' }
    ],
    bounty: [
        { validate: (bounty) => bounty >= 0, message: 'Bounty must be non-negative' }
    ]
};

// DEMONSTRATION FUNCTION
async function demonstrateTypeScriptMastery(): Promise<void> {
    console.log('\n🏴‍☠️ TYPESCRIPT MASTERY DEMONSTRATION');
    console.log('=' * 50);
    
    // 1. TYPE-SAFE CHARACTER CREATION
    console.log('\n🔧 TYPE-SAFE CHARACTER CREATION:');
    const characterService = new CharacterService();
    
    const luffyData: CreateCharacterRequest = {
        name: 'Monkey D. Luffy',
        crew: 'Straw Hat Pirates',
        bounty: 3000000000
    };
    
    const luffy = characterService.createCharacter(luffyData);
    console.log(`✅ Created character: ${luffy.name}`);
    
    // 2. OOP WITH TYPESCRIPT
    console.log('\n🏗️ OOP WITH TYPESCRIPT:');
    const pirateLuffy = new Pirate(1, 'Monkey D. Luffy', 'Thousand Sunny', 'Captain');
    
    const gomuGomuFruit: DevilFruit = {
        name: 'Gomu Gomu no Mi',
        type: 'Paramecia',
        awakened: true,
        power: 'Rubber body manipulation',
        weakness: ['Sea water', 'Seastone']
    };
    
    pirateLuffy.eatDevilFruit(gomuGomuFruit);
    console.log(pirateLuffy.useSpecialAbility());
    
    // 3. TYPE GUARDS AND VALIDATION
    console.log('\n🛡️ TYPE GUARDS AND VALIDATION:');
    const validator = new FormValidator(characterValidationSchema);
    const validationResult = validator.validate(luffyData);
    
    if (validationResult.success) {
        console.log('✅ Character data is valid');
    } else {
        console.log('❌ Validation errors:', validationResult.error);
    }
    
    // 4. API CLIENT WITH ERROR HANDLING
    console.log('\n🌐 API CLIENT WITH ERROR HANDLING:');
    const apiClient = new ApiClient('http://localhost:5000/api');
    const repository = new CharacterRepository(apiClient);
    
    try {
        const characters = await repository.findAll();
        console.log(`✅ Fetched ${characters.length} characters`);
    } catch (error) {
        console.error('❌ Failed to fetch characters:', error);
    }
    
    console.log('\n🎉 ALL TYPESCRIPT PATTERNS DEMONSTRATED!');
}

// Run the demonstration
demonstrateTypeScriptMastery().catch(console.error);

// ===============================================================================
// 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED TYPESCRIPT DEVELOPMENT! 🎉
// ===============================================================================

console.log('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED TYPESCRIPT DEVELOPMENT! 🎉');
console.log('===============================================================================');

console.log('\n🎯 WHAT YOU\'VE ACCOMPLISHED:');
console.log('✅ Mastered advanced TypeScript types and generics');
console.log('✅ Implemented type-safe API clients and data validation');
console.log('✅ Built complex type systems with conditional and mapped types');
console.log('✅ Created enterprise-grade TypeScript applications');
console.log('✅ Applied TypeScript patterns used by Microsoft, Slack, and Airbnb');
console.log('✅ Learned advanced OOP patterns with TypeScript');

console.log('\n💰 SALARY IMPACT: +$60K-$120K (TypeScript expertise is highly valued)');
console.log('🏢 COMPANIES: Microsoft, Slack, Airbnb, Shopify, Discord, all modern startups');

console.log('\n===============================================================================');
console.log('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!');
console.log('===============================================================================');

console.log('\n🚀 STEP 1: ADD COMPREHENSIVE TYPES TO YOUR REACT COMPONENTS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📁 File to create: frontend/src/types/index.ts');
console.log('');
console.log('🎯 WHAT TO DO:');
console.log('1. Define comprehensive types for all One Piece entities');
console.log('2. Create API response types with proper error handling');
console.log('3. Add form validation schemas with TypeScript');
console.log('4. Implement type-safe state management');
console.log('5. Add utility types for complex operations');
console.log('');
console.log('📚 REFERENCE: Use the type definitions from this module');

console.log('\n🚀 STEP 2: CREATE TYPE-SAFE API CLIENT');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/services/ApiClient.ts');
console.log('');
console.log('interface ApiResponse<T> {');
console.log('    data: T;');
console.log('    success: boolean;');
console.log('    message?: string;');
console.log('    errors?: ValidationError[];');
console.log('}');
console.log('');
console.log('interface Character {');
console.log('    id: number;');
console.log('    name: string;');
console.log('    crew: string;');
console.log('    bounty: number;');
console.log('    price: number;');
console.log('    priceChange: number;');
console.log('    devilFruit?: DevilFruit;');
console.log('    hakiTypes: HakiType[];');
console.log('    isActive: boolean;');
console.log('    createdAt: string;');
console.log('    updatedAt: string;');
console.log('}');
console.log('');
console.log('class ApiClient {');
console.log('    private baseUrl: string;');
console.log('    private authToken?: string;');
console.log('    ');
console.log('    constructor(baseUrl: string) {');
console.log('        this.baseUrl = baseUrl;');
console.log('    }');
console.log('    ');
console.log('    async get<T>(endpoint: string): Promise<ApiResponse<T>> {');
console.log('        const response = await fetch(`${this.baseUrl}${endpoint}`, {');
console.log('            headers: this.getHeaders()');
console.log('        });');
console.log('        ');
console.log('        if (!response.ok) {');
console.log('            throw new ApiError(response.status, await response.text());');
console.log('        }');
console.log('        ');
console.log('        return response.json();');
console.log('    }');
console.log('    ');
console.log('    async post<T, U>(endpoint: string, data: T): Promise<ApiResponse<U>> {');
console.log('        const response = await fetch(`${this.baseUrl}${endpoint}`, {');
console.log('            method: "POST",');
console.log('            headers: this.getHeaders(),');
console.log('            body: JSON.stringify(data)');
console.log('        });');
console.log('        ');
console.log('        if (!response.ok) {');
console.log('            throw new ApiError(response.status, await response.text());');
console.log('        }');
console.log('        ');
console.log('        return response.json();');
console.log('    }');
console.log('    ');
console.log('    private getHeaders(): Record<string, string> {');
console.log('        const headers: Record<string, string> = {');
console.log('            "Content-Type": "application/json"');
console.log('        };');
console.log('        ');
console.log('        if (this.authToken) {');
console.log('            headers.Authorization = `Bearer ${this.authToken}`;');
console.log('        }');
console.log('        ');
console.log('        return headers;');
console.log('    }');
console.log('}');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- ApiClient implementation (lines 650-750)');
console.log('- Type definitions (lines 50-150)');
console.log('- Error handling patterns (lines 780-820)');

console.log('\n🚀 STEP 3: ADD TYPE-SAFE FORM VALIDATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: frontend/src/utils/validation.ts');
console.log('');
console.log('interface ValidationSchema<T> {');
console.log('    [K in keyof T]: ValidationRule<T[K]>;');
console.log('}');
console.log('');
console.log('interface ValidationRule<T> {');
console.log('    required?: boolean;');
console.log('    minLength?: number;');
console.log('    maxLength?: number;');
console.log('    min?: number;');
console.log('    max?: number;');
console.log('    pattern?: RegExp;');
console.log('    custom?: (value: T) => string | null;');
console.log('}');
console.log('');
console.log('class FormValidator<T> {');
console.log('    constructor(private schema: ValidationSchema<T>) {}');
console.log('    ');
console.log('    validate(data: T): ValidationResult {');
console.log('        const errors: ValidationError[] = [];');
console.log('        ');
console.log('        for (const [field, rule] of Object.entries(this.schema)) {');
console.log('            const value = data[field as keyof T];');
console.log('            const fieldErrors = this.validateField(field, value, rule);');
console.log('            errors.push(...fieldErrors);');
console.log('        }');
console.log('        ');
console.log('        return {');
console.log('            success: errors.length === 0,');
console.log('            errors');
console.log('        };');
console.log('    }');
console.log('    ');
console.log('    private validateField(field: string, value: any, rule: ValidationRule<any>): ValidationError[] {');
console.log('        const errors: ValidationError[] = [];');
console.log('        ');
console.log('        if (rule.required && (value === null || value === undefined || value === "")) {');
console.log('            errors.push({ field, message: `${field} is required` });');
console.log('        }');
console.log('        ');
console.log('        if (rule.minLength && typeof value === "string" && value.length < rule.minLength) {');
console.log('            errors.push({ field, message: `${field} must be at least ${rule.minLength} characters` });');
console.log('        }');
console.log('        ');
console.log('        if (rule.custom) {');
console.log('            const customError = rule.custom(value);');
console.log('            if (customError) {');
console.log('                errors.push({ field, message: customError });');
console.log('            }');
console.log('        }');
console.log('        ');
console.log('        return errors;');
console.log('    }');
console.log('}');
console.log('');
console.log('// Usage in your forms:');
console.log('const characterSchema: ValidationSchema<Character> = {');
console.log('    name: { required: true, minLength: 2, maxLength: 100 },');
console.log('    crew: { required: true, minLength: 2 },');
console.log('    bounty: { required: true, min: 0 },');
console.log('    price: { required: true, min: 0.01 }');
console.log('};');
console.log('');
console.log('🔧 USE PATTERNS FROM THIS MODULE:');
console.log('- Validation schemas (lines 400-450)');
console.log('- Type-safe validation (lines 500-600)');
console.log('- Generic validation patterns (lines 350-400)');

console.log('\n🚀 STEP 4: IMPLEMENT ADVANCED TYPE PATTERNS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 UPDATE: frontend/src/types/advanced.ts');
console.log('');
console.log('// Utility types for One Piece project');
console.log('type PartialCharacter = Partial<Character>;');
console.log('type RequiredCharacterFields = Required<Pick<Character, "name" | "crew" | "bounty">>;');
console.log('type CharacterUpdate = Omit<Character, "id" | "createdAt" | "updatedAt">;');
console.log('');
console.log('// Conditional types');
console.log('type ApiEndpoint<T> = T extends Character ? "/api/characters" : ');
console.log('                     T extends Trade ? "/api/trades" :');
console.log('                     T extends User ? "/api/users" : never;');
console.log('');
console.log('// Mapped types');
console.log('type CharacterKeys = keyof Character;');
console.log('type CharacterValues = Character[CharacterKeys];');
console.log('type ReadonlyCharacter = Readonly<Character>;');
console.log('');
console.log('// Generic repository pattern');
console.log('interface Repository<T, K = number> {');
console.log('    findById(id: K): Promise<T | null>;');
console.log('    findAll(): Promise<T[]>;');
console.log('    create(entity: Omit<T, "id">): Promise<T>;');
console.log('    update(id: K, updates: Partial<T>): Promise<T>;');
console.log('    delete(id: K): Promise<void>;');
console.log('}');
console.log('');
console.log('class CharacterRepository implements Repository<Character> {');
console.log('    constructor(private apiClient: ApiClient) {}');
console.log('    ');
console.log('    async findById(id: number): Promise<Character | null> {');
console.log('        try {');
console.log('            const response = await this.apiClient.get<Character>(`/characters/${id}`);');
console.log('            return response.data;');
console.log('        } catch (error) {');
console.log('            if (error instanceof ApiError && error.status === 404) {');
console.log('                return null;');
console.log('            }');
console.log('            throw error;');
console.log('        }');
console.log('    }');
console.log('    ');
console.log('    async findAll(): Promise<Character[]> {');
console.log('        const response = await this.apiClient.get<Character[]>("/characters");');
console.log('        return response.data;');
console.log('    }');
console.log('    ');
console.log('    async create(character: Omit<Character, "id">): Promise<Character> {');
console.log('        const response = await this.apiClient.post<Omit<Character, "id">, Character>("/characters", character);');
console.log('        return response.data;');
console.log('    }');
console.log('    ');
console.log('    async update(id: number, updates: Partial<Character>): Promise<Character> {');
console.log('        const response = await this.apiClient.put<Partial<Character>, Character>(`/characters/${id}`, updates);');
console.log('        return response.data;');
console.log('    }');
console.log('    ');
console.log('    async delete(id: number): Promise<void> {');
console.log('        await this.apiClient.delete(`/characters/${id}`);');
console.log('    }');
console.log('}');
console.log('');
console.log('🔧 BENEFITS OF ADVANCED TYPES:');
console.log('- Compile-time error detection');
console.log('- Better IDE autocomplete and refactoring');
console.log('- Self-documenting code');
console.log('- Reduced runtime errors');
console.log('- Easier maintenance and scaling');

console.log('\n🚀 STEP 5: ADD TYPESCRIPT TO YOUR NODE.JS BACKEND');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 UPDATE: services/api-gateway/server.ts (rename from .js)');
console.log('');
console.log('import express, { Request, Response, NextFunction } from "express";');
console.log('import cors from "cors";');
console.log('import helmet from "helmet";');
console.log('import rateLimit from "express-rate-limit";');
console.log('import jwt from "jsonwebtoken";');
console.log('');
console.log('interface AuthenticatedRequest extends Request {');
console.log('    user?: {');
console.log('        userId: number;');
console.log('        email: string;');
console.log('        role: string;');
console.log('    };');
console.log('}');
console.log('');
console.log('interface Character {');
console.log('    id: number;');
console.log('    name: string;');
console.log('    crew: string;');
console.log('    bounty: number;');
console.log('    price: number;');
console.log('    priceChange: number;');
console.log('    isActive: boolean;');
console.log('    createdAt: Date;');
console.log('    updatedAt: Date;');
console.log('}');
console.log('');
console.log('const app = express();');
console.log('');
console.log('// Type-safe middleware');
console.log('const authenticateToken = (req: AuthenticatedRequest, res: Response, next: NextFunction): void => {');
console.log('    const authHeader = req.headers.authorization;');
console.log('    const token = authHeader?.split(" ")[1];');
console.log('    ');
console.log('    if (!token) {');
console.log('        res.status(401).json({ error: "Access token required" });');
console.log('        return;');
console.log('    }');
console.log('    ');
console.log('    jwt.verify(token, process.env.JWT_SECRET!, (err, decoded) => {');
console.log('        if (err) {');
console.log('            res.status(403).json({ error: "Invalid token" });');
console.log('            return;');
console.log('        }');
console.log('        ');
console.log('        req.user = decoded as AuthenticatedRequest["user"];');
console.log('        next();');
console.log('    });');
console.log('};');
console.log('');
console.log('// Type-safe route handlers');
console.log('app.get("/api/characters", async (req: Request, res: Response<Character[]>) => {');
console.log('    try {');
console.log('        const characters = await getCharactersFromDB();');
console.log('        res.json(characters);');
console.log('    } catch (error) {');
console.log('        res.status(500).json({ error: "Failed to fetch characters" } as any);');
console.log('    }');
console.log('});');
console.log('');
console.log('app.post("/api/characters", authenticateToken, async (req: AuthenticatedRequest, res: Response<Character>) => {');
console.log('    try {');
console.log('        const characterData: Omit<Character, "id" | "createdAt" | "updatedAt"> = req.body;');
console.log('        const newCharacter = await createCharacterInDB(characterData);');
console.log('        res.status(201).json(newCharacter);');
console.log('    } catch (error) {');
console.log('        res.status(500).json({ error: "Failed to create character" } as any);');
console.log('    }');
console.log('});');
console.log('');
console.log('🔧 TYPESCRIPT BENEFITS FOR BACKEND:');
console.log('- Type-safe request/response handling');
console.log('- Better error detection during development');
console.log('- Improved API documentation through types');
console.log('- Enhanced IDE support for Node.js development');

console.log('\n🚀 STEP 6: TEST YOUR TYPESCRIPT IMPLEMENTATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🧪 TESTING STEPS:');
console.log('');
console.log('1. Install TypeScript and dependencies:');
console.log('   cd frontend');
console.log('   npm install typescript @types/react @types/node');
console.log('   npx tsc --init');
console.log('');
console.log('2. Configure TypeScript (tsconfig.json):');
console.log('   {');
console.log('     "compilerOptions": {');
console.log('       "target": "es5",');
console.log('       "lib": ["dom", "dom.iterable", "es6"],');
console.log('       "allowJs": true,');
console.log('       "skipLibCheck": true,');
console.log('       "esModuleInterop": true,');
console.log('       "allowSyntheticDefaultImports": true,');
console.log('       "strict": true,');
console.log('       "forceConsistentCasingInFileNames": true,');
console.log('       "moduleResolution": "node",');
console.log('       "resolveJsonModule": true,');
console.log('       "isolatedModules": true,');
console.log('       "noEmit": true,');
console.log('       "jsx": "react-jsx"');
console.log('     },');
console.log('     "include": ["src"]');
console.log('   }');
console.log('');
console.log('3. Test type checking:');
console.log('   npx tsc --noEmit');
console.log('   # Should show no type errors');
console.log('');
console.log('4. Test API client types:');
console.log('   // This should show TypeScript errors:');
console.log('   const character: Character = {');
console.log('       name: "Luffy", // Missing required fields');
console.log('   };');
console.log('');
console.log('5. Test form validation:');
console.log('   const validator = new FormValidator(characterSchema);');
console.log('   const result = validator.validate(invalidData);');
console.log('   // Should catch validation errors at compile time');
console.log('');
console.log('✅ SUCCESS CRITERIA:');
console.log('- TypeScript compiles without errors');
console.log('- IDE shows proper autocomplete and error highlighting');
console.log('- API calls are type-safe and catch errors at compile time');
console.log('- Form validation works with proper type checking');
console.log('- Backend API endpoints have proper type annotations');

console.log('\n===============================================================================');
console.log('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES');
console.log('===============================================================================');

console.log('\n🧩 MODULE CONNECTIONS:');
console.log('');
console.log('📚 Module 19 (React) → React components use TypeScript for type safety and better development experience');
console.log('📚 Module 16 (Node.js) → Backend API uses TypeScript for type-safe request/response handling');
console.log('📚 Module 15 (JavaScript) → TypeScript builds on JavaScript with static type checking');
console.log('📚 Module 7 (Security) → Type-safe authentication and authorization patterns');
console.log('📚 Module 11 (APIs) → API clients and endpoints use TypeScript for better reliability');
console.log('📚 Module 17 (Next.js) → Next.js applications benefit from TypeScript integration');

console.log('\n🎯 NEXT MODULES TO COMPLETE:');
console.log('1. Module 19: Apply TypeScript to your React components and hooks');
console.log('2. Module 16: Convert your Node.js API Gateway to TypeScript');
console.log('3. Module 17: Use TypeScript with Next.js for full-stack type safety');

console.log('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:');
console.log('🔗 TypeScript Handbook: https://www.typescriptlang.org/docs/');
console.log('🔗 React + TypeScript: https://react-typescript-cheatsheet.netlify.app/');
console.log('🔗 Node.js + TypeScript: https://nodejs.dev/learn/nodejs-with-typescript');
console.log('🔗 Advanced TypeScript: https://www.typescriptlang.org/docs/handbook/advanced-types.html');

console.log('\n🏴‍☠️ YOU\'RE NOW READY TO BUILD TYPE-SAFE, SCALABLE APPLICATIONS! ⚔️');
console.log('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!');
