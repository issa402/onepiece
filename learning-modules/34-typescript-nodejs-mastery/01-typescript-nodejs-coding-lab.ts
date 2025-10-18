/**
 * 🏴‍☠️ ONE PIECE TRADING PLATFORM - TYPESCRIPT & NODE.JS CODING LAB
 * 
 * This file contains comprehensive TypeScript and Node.js examples
 * demonstrating all concepts from basic types to advanced patterns.
 * 
 * Run this file with: npx ts-node 01-typescript-nodejs-coding-lab.ts
 */

import { EventEmitter } from 'events';
import { promises as fs } from 'fs';
import { createReadStream, createWriteStream } from 'fs';
import { pipeline } from 'stream/promises';

// ============================================================================
// 🎯 SECTION 1: TYPESCRIPT FUNDAMENTALS
// ============================================================================

console.log('🏴‍☠️ Starting One Piece Trading Platform Demo...\n');

// Basic Types and Interfaces
interface Character {
    id: string;
    name: string;
    bounty: number;
    crew: string;
    devilFruit?: string;
    haki: HakiType[];
    isActive: boolean;
    createdAt: Date;
    updatedAt: Date;
}

// Union Types and Enums
type HakiType = 'Observation' | 'Armament' | 'Conqueror\'s';
type CharacterStatus = 'active' | 'inactive' | 'unknown';

enum CrewType {
    PIRATE = 'pirate',
    MARINE = 'marine',
    REVOLUTIONARY = 'revolutionary',
    BOUNTY_HUNTER = 'bounty_hunter'
}

// Advanced Types
type CharacterKeys = keyof Character;
type OptionalCharacter = Partial<Character>;
type RequiredCharacter = Required<Character>;
type CharacterWithoutId = Omit<Character, 'id'>;

// Generic Types
interface Repository<T> {
    findAll(): Promise<T[]>;
    findById(id: string): Promise<T | null>;
    create(data: Omit<T, 'id' | 'createdAt' | 'updatedAt'>): Promise<T>;
    update(id: string, data: Partial<T>): Promise<T | null>;
    delete(id: string): Promise<boolean>;
}

// ============================================================================
// 🎯 SECTION 2: CLASSES AND INHERITANCE
// ============================================================================

abstract class BaseEntity {
    constructor(
        public id: string,
        public createdAt: Date = new Date(),
        public updatedAt: Date = new Date()
    ) {}

    abstract validate(): boolean;
    
    touch(): void {
        this.updatedAt = new Date();
    }
}

class CharacterEntity extends BaseEntity implements Character {
    constructor(
        id: string,
        public name: string,
        public bounty: number,
        public crew: string,
        public haki: HakiType[] = [],
        public isActive: boolean = true,
        public devilFruit?: string,
        createdAt?: Date,
        updatedAt?: Date
    ) {
        super(id, createdAt, updatedAt);
    }

    validate(): boolean {
        return this.name.length > 0 && 
               this.bounty >= 0 && 
               this.crew.length > 0;
    }

    // Method to calculate power level based on bounty and abilities
    calculatePowerLevel(): number {
        let powerLevel = Math.log10(this.bounty + 1) * 100;
        
        // Bonus for Haki types
        powerLevel += this.haki.length * 50;
        
        // Special bonus for Conqueror's Haki
        if (this.haki.includes('Conqueror\'s')) {
            powerLevel += 200;
        }
        
        // Devil Fruit bonus
        if (this.devilFruit) {
            powerLevel += 150;
        }
        
        return Math.round(powerLevel);
    }

    // Method to introduce the character
    introduce(): string {
        const hakiList = this.haki.length > 0 ? ` I can use ${this.haki.join(', ')} Haki.` : '';
        const fruitInfo = this.devilFruit ? ` I ate the ${this.devilFruit}.` : '';
        
        return `Ahoy! I'm ${this.name} from the ${this.crew}! My bounty is ${this.bounty.toLocaleString()} berries.${hakiList}${fruitInfo}`;
    }

    // Static method to create character from plain object
    static fromObject(obj: any): CharacterEntity {
        return new CharacterEntity(
            obj.id,
            obj.name,
            obj.bounty,
            obj.crew,
            obj.haki || [],
            obj.isActive !== false,
            obj.devilFruit,
            obj.createdAt ? new Date(obj.createdAt) : undefined,
            obj.updatedAt ? new Date(obj.updatedAt) : undefined
        );
    }
}

// ============================================================================
// 🎯 SECTION 3: GENERIC REPOSITORY IMPLEMENTATION
// ============================================================================

class InMemoryRepository<T extends BaseEntity> implements Repository<T> {
    private items: T[] = [];
    private nextId = 1;

    async findAll(): Promise<T[]> {
        // Simulate async database operation
        await this.delay(50);
        return [...this.items];
    }

    async findById(id: string): Promise<T | null> {
        await this.delay(25);
        return this.items.find(item => item.id === id) || null;
    }

    async create(data: Omit<T, 'id' | 'createdAt' | 'updatedAt'>): Promise<T> {
        await this.delay(100);
        
        const item = {
            ...data,
            id: this.nextId.toString(),
            createdAt: new Date(),
            updatedAt: new Date()
        } as T;
        
        this.nextId++;
        this.items.push(item);
        return item;
    }

    async update(id: string, data: Partial<T>): Promise<T | null> {
        await this.delay(75);
        
        const index = this.items.findIndex(item => item.id === id);
        if (index === -1) return null;
        
        this.items[index] = {
            ...this.items[index],
            ...data,
            updatedAt: new Date()
        };
        
        return this.items[index];
    }

    async delete(id: string): Promise<boolean> {
        await this.delay(50);
        
        const index = this.items.findIndex(item => item.id === id);
        if (index === -1) return false;
        
        this.items.splice(index, 1);
        return true;
    }

    // Helper method to simulate database delay
    private delay(ms: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Additional utility methods
    async count(): Promise<number> {
        await this.delay(25);
        return this.items.length;
    }

    async findWhere(predicate: (item: T) => boolean): Promise<T[]> {
        await this.delay(50);
        return this.items.filter(predicate);
    }
}

// ============================================================================
// 🎯 SECTION 4: SERVICE LAYER WITH BUSINESS LOGIC
// ============================================================================

class CharacterService {
    constructor(private repository: Repository<CharacterEntity>) {}

    async getAllCharacters(): Promise<CharacterEntity[]> {
        return await this.repository.findAll();
    }

    async getCharacterById(id: string): Promise<CharacterEntity | null> {
        return await this.repository.findById(id);
    }

    async createCharacter(data: {
        name: string;
        bounty: number;
        crew: string;
        devilFruit?: string;
        haki?: HakiType[];
    }): Promise<CharacterEntity> {
        // Validation
        if (!data.name || data.name.trim().length < 2) {
            throw new Error('Character name must be at least 2 characters long');
        }
        
        if (data.bounty < 0) {
            throw new Error('Bounty cannot be negative');
        }
        
        if (!data.crew || data.crew.trim().length < 2) {
            throw new Error('Crew name must be at least 2 characters long');
        }

        const character = new CharacterEntity(
            '', // ID will be set by repository
            data.name.trim(),
            data.bounty,
            data.crew.trim(),
            data.haki || [],
            true,
            data.devilFruit?.trim()
        );

        if (!character.validate()) {
            throw new Error('Character validation failed');
        }

        return await this.repository.create(character);
    }

    async updateCharacter(id: string, data: Partial<{
        name: string;
        bounty: number;
        crew: string;
        devilFruit: string;
        haki: HakiType[];
        isActive: boolean;
    }>): Promise<CharacterEntity | null> {
        const existing = await this.repository.findById(id);
        if (!existing) {
            throw new Error('Character not found');
        }

        // Validate updates
        if (data.name !== undefined && data.name.trim().length < 2) {
            throw new Error('Character name must be at least 2 characters long');
        }
        
        if (data.bounty !== undefined && data.bounty < 0) {
            throw new Error('Bounty cannot be negative');
        }

        return await this.repository.update(id, data);
    }

    async deleteCharacter(id: string): Promise<boolean> {
        const existing = await this.repository.findById(id);
        if (!existing) {
            throw new Error('Character not found');
        }

        return await this.repository.delete(id);
    }

    async searchCharactersByName(query: string): Promise<CharacterEntity[]> {
        const allCharacters = await this.repository.findAll();
        return allCharacters.filter(char => 
            char.name.toLowerCase().includes(query.toLowerCase())
        );
    }

    async getCharactersByBountyRange(min: number, max: number): Promise<CharacterEntity[]> {
        const allCharacters = await this.repository.findAll();
        return allCharacters.filter(char => 
            char.bounty >= min && char.bounty <= max
        );
    }

    async getTopCharactersByBounty(limit: number = 10): Promise<CharacterEntity[]> {
        const allCharacters = await this.repository.findAll();
        return allCharacters
            .sort((a, b) => b.bounty - a.bounty)
            .slice(0, limit);
    }

    async calculateTotalBounty(): Promise<number> {
        const allCharacters = await this.repository.findAll();
        return allCharacters.reduce((total, char) => total + char.bounty, 0);
    }

    async getCrewStatistics(): Promise<{ [crew: string]: { count: number; totalBounty: number; averageBounty: number } }> {
        const allCharacters = await this.repository.findAll();
        const stats: { [crew: string]: { count: number; totalBounty: number; averageBounty: number } } = {};

        for (const character of allCharacters) {
            if (!stats[character.crew]) {
                stats[character.crew] = { count: 0, totalBounty: 0, averageBounty: 0 };
            }
            
            stats[character.crew].count++;
            stats[character.crew].totalBounty += character.bounty;
        }

        // Calculate averages
        for (const crew in stats) {
            stats[crew].averageBounty = Math.round(stats[crew].totalBounty / stats[crew].count);
        }

        return stats;
    }
}

// ============================================================================
// 🎯 SECTION 5: EVENT-DRIVEN ARCHITECTURE
// ============================================================================

class TradingPlatformEvents extends EventEmitter {
    emitCharacterCreated(character: CharacterEntity): void {
        this.emit('character:created', character);
    }

    emitCharacterUpdated(character: CharacterEntity): void {
        this.emit('character:updated', character);
    }

    emitCharacterDeleted(characterId: string): void {
        this.emit('character:deleted', characterId);
    }

    emitTradeCompleted(trade: { buyerId: string; sellerId: string; characterId: string; amount: number }): void {
        this.emit('trade:completed', trade);
    }
}

// Event handlers
class EventHandlers {
    static onCharacterCreated(character: CharacterEntity): void {
        console.log(`📢 New character joined the seas: ${character.name} with bounty ${character.bounty.toLocaleString()}`);
    }

    static onCharacterUpdated(character: CharacterEntity): void {
        console.log(`📝 Character updated: ${character.name}`);
    }

    static onCharacterDeleted(characterId: string): void {
        console.log(`💀 Character removed from the seas: ${characterId}`);
    }

    static onTradeCompleted(trade: { buyerId: string; sellerId: string; characterId: string; amount: number }): void {
        console.log(`💰 Trade completed: Character ${trade.characterId} traded for ${trade.amount.toLocaleString()} berries`);
    }
}

// ============================================================================
// 🎯 SECTION 6: ASYNC OPERATIONS AND ERROR HANDLING
// ============================================================================

class AsyncOperationsDemo {
    // Sequential processing (slow)
    static async processCharactersSequentially(characters: CharacterEntity[]): Promise<string[]> {
        console.log('⏳ Processing characters sequentially...');
        const results: string[] = [];
        
        for (const character of characters) {
            await AsyncOperationsDemo.delay(100); // Simulate API call
            results.push(`Processed ${character.name}`);
        }
        
        return results;
    }

    // Parallel processing (fast)
    static async processCharactersInParallel(characters: CharacterEntity[]): Promise<string[]> {
        console.log('⚡ Processing characters in parallel...');
        
        const promises = characters.map(async (character) => {
            await AsyncOperationsDemo.delay(100); // Simulate API call
            return `Processed ${character.name}`;
        });
        
        return await Promise.all(promises);
    }

    // Error handling with retry logic
    static async fetchCharacterWithRetry(id: string, maxRetries: number = 3): Promise<CharacterEntity | null> {
        let lastError: Error | null = null;
        
        for (let attempt = 1; attempt <= maxRetries; attempt++) {
            try {
                console.log(`🔄 Attempt ${attempt} to fetch character ${id}`);
                
                // Simulate API call that might fail
                if (Math.random() < 0.7) { // 70% chance of failure
                    throw new Error(`Network error fetching character ${id}`);
                }
                
                // Success case
                return new CharacterEntity(id, 'Test Character', 1000000, 'Test Crew');
                
            } catch (error) {
                lastError = error as Error;
                console.log(`❌ Attempt ${attempt} failed: ${error.message}`);
                
                if (attempt < maxRetries) {
                    const delay = Math.pow(2, attempt) * 1000; // Exponential backoff
                    console.log(`⏳ Waiting ${delay}ms before retry...`);
                    await AsyncOperationsDemo.delay(delay);
                }
            }
        }
        
        console.log(`💥 All ${maxRetries} attempts failed. Last error: ${lastError?.message}`);
        return null;
    }

    // Timeout handling
    static async fetchWithTimeout<T>(promise: Promise<T>, timeoutMs: number): Promise<T> {
        const timeoutPromise = new Promise<never>((_, reject) => {
            setTimeout(() => reject(new Error(`Operation timed out after ${timeoutMs}ms`)), timeoutMs);
        });
        
        return Promise.race([promise, timeoutPromise]);
    }

    private static delay(ms: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// ============================================================================
// 🎯 SECTION 7: FILE OPERATIONS AND STREAMS
// ============================================================================

class FileOperationsDemo {
    static async saveCharactersToFile(characters: CharacterEntity[], filename: string): Promise<void> {
        try {
            const data = JSON.stringify(characters, null, 2);
            await fs.writeFile(filename, data, 'utf8');
            console.log(`💾 Saved ${characters.length} characters to ${filename}`);
        } catch (error) {
            console.error(`❌ Failed to save characters: ${error.message}`);
            throw error;
        }
    }

    static async loadCharactersFromFile(filename: string): Promise<CharacterEntity[]> {
        try {
            const data = await fs.readFile(filename, 'utf8');
            const parsed = JSON.parse(data);
            
            return parsed.map((obj: any) => CharacterEntity.fromObject(obj));
        } catch (error) {
            console.error(`❌ Failed to load characters: ${error.message}`);
            return [];
        }
    }

    // Stream processing for large files
    static async processLargeCharacterFile(inputFile: string, outputFile: string): Promise<void> {
        const readStream = createReadStream(inputFile);
        const writeStream = createWriteStream(outputFile);
        
        // Transform stream to process each character
        const transformStream = new (require('stream').Transform)({
            objectMode: true,
            transform(chunk: any, encoding: any, callback: any) {
                try {
                    const character = JSON.parse(chunk.toString());
                    character.powerLevel = character.bounty * 0.001; // Add power level
                    
                    this.push(JSON.stringify(character) + '\n');
                    callback();
                } catch (error) {
                    callback(error);
                }
            }
        });
        
        try {
            await pipeline(readStream, transformStream, writeStream);
            console.log(`🔄 Processed large file: ${inputFile} -> ${outputFile}`);
        } catch (error) {
            console.error(`❌ Stream processing failed: ${error.message}`);
            throw error;
        }
    }
}

// ============================================================================
// 🎯 SECTION 8: DEMO EXECUTION - PUTTING IT ALL TOGETHER
// ============================================================================

async function runOnePieceTradingPlatformDemo(): Promise<void> {
    console.log('🏴‍☠️ ONE PIECE TRADING PLATFORM DEMO');
    console.log('=====================================\n');

    // Initialize components
    const repository = new InMemoryRepository<CharacterEntity>();
    const characterService = new CharacterService(repository);
    const events = new TradingPlatformEvents();

    // Set up event listeners
    events.on('character:created', EventHandlers.onCharacterCreated);
    events.on('character:updated', EventHandlers.onCharacterUpdated);
    events.on('character:deleted', EventHandlers.onCharacterDeleted);
    events.on('trade:completed', EventHandlers.onTradeCompleted);

    try {
        // 1. Create sample characters
        console.log('1️⃣ Creating Straw Hat Pirates...\n');

        const luffy = await characterService.createCharacter({
            name: 'Monkey D. Luffy',
            bounty: 3000000000,
            crew: 'Straw Hat Pirates',
            devilFruit: 'Gomu Gomu no Mi (Hito Hito no Mi, Model: Nika)',
            haki: ['Observation', 'Armament', 'Conqueror\'s']
        });
        events.emitCharacterCreated(luffy);

        const zoro = await characterService.createCharacter({
            name: 'Roronoa Zoro',
            bounty: 1111000000,
            crew: 'Straw Hat Pirates',
            haki: ['Observation', 'Armament']
        });
        events.emitCharacterCreated(zoro);

        const nami = await characterService.createCharacter({
            name: 'Nami',
            bounty: 366000000,
            crew: 'Straw Hat Pirates',
            haki: []
        });
        events.emitCharacterCreated(nami);

        const sanji = await characterService.createCharacter({
            name: 'Vinsmoke Sanji',
            bounty: 1032000000,
            crew: 'Straw Hat Pirates',
            haki: ['Observation', 'Armament']
        });
        events.emitCharacterCreated(sanji);

        // 2. Display character information
        console.log('\n2️⃣ Character Introductions:\n');
        const allCharacters = await characterService.getAllCharacters();

        for (const character of allCharacters) {
            console.log(`${character.introduce()}`);
            console.log(`   Power Level: ${character.calculatePowerLevel()}`);
            console.log('');
        }

        // 3. Demonstrate search functionality
        console.log('3️⃣ Search Functionality:\n');

        const luffySearch = await characterService.searchCharactersByName('luffy');
        console.log(`🔍 Search for 'luffy': Found ${luffySearch.length} character(s)`);

        const highBountyCharacters = await characterService.getCharactersByBountyRange(1000000000, 5000000000);
        console.log(`💰 Characters with bounty 1B-5B: ${highBountyCharacters.length} found`);

        const topCharacters = await characterService.getTopCharactersByBounty(3);
        console.log(`🏆 Top 3 characters by bounty:`);
        topCharacters.forEach((char, index) => {
            console.log(`   ${index + 1}. ${char.name}: ${char.bounty.toLocaleString()} berries`);
        });

        // 4. Update character
        console.log('\n4️⃣ Character Updates:\n');

        const updatedLuffy = await characterService.updateCharacter(luffy.id, {
            bounty: 3500000000, // Bounty increase after latest arc
            haki: ['Observation', 'Armament', 'Conqueror\'s'] // Advanced Conqueror's Haki
        });

        if (updatedLuffy) {
            events.emitCharacterUpdated(updatedLuffy);
            console.log(`✨ Updated Luffy's bounty to ${updatedLuffy.bounty.toLocaleString()}`);
        }

        // 5. Crew statistics
        console.log('\n5️⃣ Crew Statistics:\n');

        const totalBounty = await characterService.calculateTotalBounty();
        console.log(`💎 Total bounty of all characters: ${totalBounty.toLocaleString()} berries`);

        const crewStats = await characterService.getCrewStatistics();
        console.log('📊 Crew Statistics:');
        for (const [crew, stats] of Object.entries(crewStats)) {
            console.log(`   ${crew}: ${stats.count} members, ${stats.totalBounty.toLocaleString()} total bounty, ${stats.averageBounty.toLocaleString()} average`);
        }

        // 6. Demonstrate async operations
        console.log('\n6️⃣ Async Operations Performance:\n');

        const characters = await characterService.getAllCharacters();

        // Sequential processing
        const startSequential = Date.now();
        await AsyncOperationsDemo.processCharactersSequentially(characters);
        const sequentialTime = Date.now() - startSequential;
        console.log(`⏱️  Sequential processing took: ${sequentialTime}ms`);

        // Parallel processing
        const startParallel = Date.now();
        await AsyncOperationsDemo.processCharactersInParallel(characters);
        const parallelTime = Date.now() - startParallel;
        console.log(`⚡ Parallel processing took: ${parallelTime}ms`);
        console.log(`🚀 Parallel was ${Math.round(sequentialTime / parallelTime)}x faster!`);

        // 7. Error handling demonstration
        console.log('\n7️⃣ Error Handling & Retry Logic:\n');

        const fetchResult = await AsyncOperationsDemo.fetchCharacterWithRetry('test-id', 3);
        if (fetchResult) {
            console.log(`✅ Successfully fetched character: ${fetchResult.name}`);
        } else {
            console.log('❌ Failed to fetch character after all retries');
        }

        // 8. File operations
        console.log('\n8️⃣ File Operations:\n');

        const filename = 'characters.json';
        await FileOperationsDemo.saveCharactersToFile(allCharacters, filename);

        const loadedCharacters = await FileOperationsDemo.loadCharactersFromFile(filename);
        console.log(`📁 Loaded ${loadedCharacters.length} characters from file`);

        // 9. Simulate trading events
        console.log('\n9️⃣ Trading Simulation:\n');

        events.emitTradeCompleted({
            buyerId: 'trader1',
            sellerId: 'trader2',
            characterId: luffy.id,
            amount: 5000000000
        });

        events.emitTradeCompleted({
            buyerId: 'trader3',
            sellerId: 'trader1',
            characterId: zoro.id,
            amount: 2000000000
        });

        // 10. Advanced TypeScript features demonstration
        console.log('\n🔟 Advanced TypeScript Features:\n');

        // Utility types
        type CharacterUpdate = Partial<Pick<Character, 'name' | 'bounty' | 'crew'>>;
        const updateData: CharacterUpdate = { bounty: 4000000000 };
        console.log('✨ Using utility types for type-safe updates');

        // Generic constraints
        function getEntityId<T extends { id: string }>(entity: T): string {
            return entity.id;
        }

        const luffyId = getEntityId(luffy);
        console.log(`🆔 Luffy's ID using generic function: ${luffyId}`);

        // Conditional types
        type IsArray<T> = T extends any[] ? true : false;
        type HakiIsArray = IsArray<HakiType[]>; // true
        type NameIsArray = IsArray<string>; // false
        console.log('🔍 Conditional types help with complex type logic');

        console.log('\n🎉 Demo completed successfully!');
        console.log('=====================================');

    } catch (error) {
        console.error('💥 Demo failed:', error.message);
        if (error.stack) {
            console.error('Stack trace:', error.stack);
        }
    }
}

// ============================================================================
// 🎯 MAIN EXECUTION
// ============================================================================

// Run the demo when this file is executed directly
if (require.main === module) {
    runOnePieceTradingPlatformDemo()
        .then(() => {
            console.log('\n🏴‍☠️ Thank you for exploring the One Piece Trading Platform!');
            console.log('🌊 May your code be as adventurous as the Grand Line!');
            process.exit(0);
        })
        .catch((error) => {
            console.error('💥 Fatal error:', error);
            process.exit(1);
        });
}

// Export for use in other modules
export {
    Character,
    CharacterEntity,
    CharacterService,
    InMemoryRepository,
    TradingPlatformEvents,
    AsyncOperationsDemo,
    FileOperationsDemo
};
