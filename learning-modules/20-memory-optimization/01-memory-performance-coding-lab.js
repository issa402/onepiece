/*
🏴‍☠️ ONE PIECE TRADING PLATFORM - MEMORY OPTIMIZATION & PERFORMANCE LAB
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'LL MASTER FOR YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ FRONTEND MEMORY OPTIMIZATION - React, DOM, bundle size reduction
✅ BACKEND MEMORY MANAGEMENT - Node.js heap, garbage collection, memory leaks
✅ DATABASE MEMORY EFFICIENCY - Query optimization, connection pooling
✅ CACHING STRATEGIES - Redis, in-memory caches, CDN optimization
✅ BUNDLE OPTIMIZATION - Code splitting, tree shaking, lazy loading
✅ MEMORY PROFILING - Chrome DevTools, Node.js profiling, monitoring
✅ PRODUCTION OPTIMIZATION - Memory limits, scaling, performance tuning

💰 SALARY IMPACT: +$80K-$200K (Memory optimization is critical for senior roles)
🏢 COMPANIES: All FAANG, Netflix, Uber, high-traffic applications

🔗 HOW THIS CONNECTS TO YOUR ONE PIECE PROJECT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 YOUR CURRENT PERFORMANCE CHALLENGES:
   - Large character datasets → Memory-efficient data structures
   - Real-time price updates → Optimized WebSocket handling
   - User portfolios → Efficient state management
   - Trading history → Pagination and virtualization

🎯 WHAT YOU'LL OPTIMIZE:
   - React components with thousands of characters
   - Node.js API Gateway memory usage
   - Database query result caching
   - WebSocket connection management
   - Bundle size for faster loading
   - Memory leaks in long-running processes

📚 MEMORY OPTIMIZATION CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 FRONTEND MEMORY OPTIMIZATION:
• Virtual scrolling for large lists
• React memoization and optimization
• Bundle splitting and lazy loading
• DOM manipulation efficiency
• Memory leak detection and prevention

⚡ BACKEND MEMORY MANAGEMENT:
• Node.js heap optimization
• Garbage collection tuning
• Memory leak detection
• Stream processing for large data
• Connection pooling and resource management

🗄️ DATABASE MEMORY EFFICIENCY:
• Query result caching
• Connection pool optimization
• Index memory usage
• Query optimization for memory
• Pagination strategies

🔧 MEMORY OPTIMIZATION SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. REACT MEMORY OPTIMIZATION:
   const MemoizedComponent = React.memo(Component, (prev, next) => {
       return prev.id === next.id; // Custom comparison
   });
   
   const memoizedValue = useMemo(() => {
       return expensiveCalculation(data);
   }, [data]);

2. NODE.JS MEMORY MANAGEMENT:
   // Monitor memory usage
   const memUsage = process.memoryUsage();
   console.log('Heap Used:', memUsage.heapUsed / 1024 / 1024, 'MB');
   
   // Stream processing for large data
   const stream = fs.createReadStream('large-file.json');

3. EFFICIENT DATA STRUCTURES:
   // Use Map for O(1) lookups instead of arrays
   const characterMap = new Map();
   characterMap.set(id, character);
   
   // WeakMap for automatic garbage collection
   const weakMap = new WeakMap();

4. MEMORY PROFILING:
   // Chrome DevTools Memory tab
   // Node.js --inspect flag
   // Performance monitoring
*/

console.log('🏴‍☠️ Memory Optimization & Performance - One Piece Trading Platform');

// ═══════════════════════════════════════════════════════════
// 🧪 HANDS-ON LAB 1: FRONTEND MEMORY OPTIMIZATION
// ═══════════════════════════════════════════════════════════

/*
📚 FRONTEND MEMORY CHALLENGES:

🔥 COMMON MEMORY ISSUES:

1. MEMORY LEAKS:
   - Event listeners not removed
   - Closures holding references
   - Timers not cleared
   - DOM nodes not released

2. INEFFICIENT RENDERING:
   - Unnecessary re-renders
   - Large DOM trees
   - Heavy computations on every render
   - No virtualization for large lists

3. BUNDLE SIZE:
   - Unused dependencies
   - No code splitting
   - Large images/assets
   - No tree shaking

FRONTEND OPTIMIZATION TECHNIQUES:
- Virtual scrolling for character lists
- React memoization patterns
- Lazy loading and code splitting
- Efficient state management
- Memory leak prevention

🎯 YOUR CODING MISSION:
Optimize One Piece frontend for memory efficiency!
*/

// TODO 1: VIRTUAL SCROLLING FOR CHARACTER LISTS
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement virtual scrolling for large character lists

Create file: frontend/src/components/VirtualCharacterList.tsx
*/

// FILE: frontend/src/components/VirtualCharacterList.tsx
// YOUR CODE HERE - Create virtual scrolling component:

import React, { useState, useEffect, useMemo, useCallback } from 'react';

interface VirtualListProps {
    items: Character[];
    itemHeight: number;
    containerHeight: number;
    renderItem: (item: Character, index: number) => React.ReactNode;
}

const VirtualCharacterList: React.FC<VirtualListProps> = ({
    items,
    itemHeight,
    containerHeight,
    renderItem
}) => {
    const [scrollTop, setScrollTop] = useState(0);
    
    // Calculate visible range
    const visibleCount = Math.ceil(containerHeight / itemHeight);
    const startIndex = Math.floor(scrollTop / itemHeight);
    const endIndex = Math.min(startIndex + visibleCount + 1, items.length);
    
    // Memoize visible items to prevent unnecessary recalculations
    const visibleItems = useMemo(() => {
        return items.slice(startIndex, endIndex);
    }, [items, startIndex, endIndex]);
    
    // Optimize scroll handler
    const handleScroll = useCallback((e: React.UIEvent<HTMLDivElement>) => {
        setScrollTop(e.currentTarget.scrollTop);
    }, []);
    
    const totalHeight = items.length * itemHeight;
    const offsetY = startIndex * itemHeight;
    
    return (
        <div
            style={{ height: containerHeight, overflow: 'auto' }}
            onScroll={handleScroll}
        >
            <div style={{ height: totalHeight, position: 'relative' }}>
                <div style={{ transform: `translateY(${offsetY}px)` }}>
                    {visibleItems.map((item, index) => (
                        <div key={item.id} style={{ height: itemHeight }}>
                            {renderItem(item, startIndex + index)}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

// TODO 2: MEMORY-EFFICIENT STATE MANAGEMENT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create memory-efficient state management

Create file: frontend/src/hooks/useMemoryEfficientState.ts
*/

// FILE: frontend/src/hooks/useMemoryEfficientState.ts
// YOUR CODE HERE - Create memory-efficient state hook:

import { useState, useCallback, useRef, useEffect } from 'react';

// Memory-efficient character cache
class CharacterCache {
    private cache = new Map<number, Character>();
    private maxSize = 1000; // Limit cache size
    private accessOrder = new Set<number>();
    
    get(id: number): Character | undefined {
        const character = this.cache.get(id);
        if (character) {
            // Update access order for LRU
            this.accessOrder.delete(id);
            this.accessOrder.add(id);
        }
        return character;
    }
    
    set(id: number, character: Character): void {
        // Remove oldest if cache is full
        if (this.cache.size >= this.maxSize && !this.cache.has(id)) {
            const oldestId = this.accessOrder.values().next().value;
            this.cache.delete(oldestId);
            this.accessOrder.delete(oldestId);
        }
        
        this.cache.set(id, character);
        this.accessOrder.add(id);
    }
    
    clear(): void {
        this.cache.clear();
        this.accessOrder.clear();
    }
    
    getMemoryUsage(): number {
        return this.cache.size;
    }
}

const characterCache = new CharacterCache();

export function useMemoryEfficientCharacters() {
    const [characters, setCharacters] = useState<Character[]>([]);
    const [loading, setLoading] = useState(false);
    const abortControllerRef = useRef<AbortController | null>(null);
    
    const loadCharacters = useCallback(async (page: number = 1, limit: number = 50) => {
        // Cancel previous request
        if (abortControllerRef.current) {
            abortControllerRef.current.abort();
        }
        
        abortControllerRef.current = new AbortController();
        setLoading(true);
        
        try {
            const response = await fetch(
                `/api/characters?page=${page}&limit=${limit}`,
                { signal: abortControllerRef.current.signal }
            );
            
            const newCharacters = await response.json();
            
            // Cache characters efficiently
            newCharacters.forEach((char: Character) => {
                characterCache.set(char.id, char);
            });
            
            setCharacters(newCharacters);
        } catch (error) {
            if (error.name !== 'AbortError') {
                console.error('Failed to load characters:', error);
            }
        } finally {
            setLoading(false);
        }
    }, []);
    
    // Cleanup on unmount
    useEffect(() => {
        return () => {
            if (abortControllerRef.current) {
                abortControllerRef.current.abort();
            }
        };
    }, []);
    
    const getCachedCharacter = useCallback((id: number) => {
        return characterCache.get(id);
    }, []);
    
    const clearCache = useCallback(() => {
        characterCache.clear();
    }, []);
    
    const getCacheStats = useCallback(() => {
        return {
            size: characterCache.getMemoryUsage(),
            maxSize: 1000
        };
    }, []);
    
    return {
        characters,
        loading,
        loadCharacters,
        getCachedCharacter,
        clearCache,
        getCacheStats
    };
}

// TODO 3: MEMORY LEAK PREVENTION
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create memory leak prevention utilities

Create file: frontend/src/utils/memoryUtils.ts
*/

// FILE: frontend/src/utils/memoryUtils.ts
// YOUR CODE HERE - Create memory leak prevention utilities:

export class MemoryLeakDetector {
    private eventListeners = new Set<() => void>();
    private timers = new Set<NodeJS.Timeout>();
    private intervals = new Set<NodeJS.Timeout>();
    private observers = new Set<MutationObserver | IntersectionObserver>();
    
    // Track event listeners
    addEventListenerTracked<K extends keyof WindowEventMap>(
        target: EventTarget,
        type: K,
        listener: (this: Window, ev: WindowEventMap[K]) => any,
        options?: boolean | AddEventListenerOptions
    ): () => void {
        target.addEventListener(type, listener, options);
        
        const cleanup = () => {
            target.removeEventListener(type, listener, options);
            this.eventListeners.delete(cleanup);
        };
        
        this.eventListeners.add(cleanup);
        return cleanup;
    }
    
    // Track timers
    setTimeoutTracked(callback: () => void, delay: number): NodeJS.Timeout {
        const timer = setTimeout(() => {
            callback();
            this.timers.delete(timer);
        }, delay);
        
        this.timers.add(timer);
        return timer;
    }
    
    setIntervalTracked(callback: () => void, delay: number): NodeJS.Timeout {
        const interval = setInterval(callback, delay);
        this.intervals.add(interval);
        return interval;
    }
    
    // Track observers
    addObserverTracked(observer: MutationObserver | IntersectionObserver): void {
        this.observers.add(observer);
    }
    
    // Cleanup all tracked resources
    cleanup(): void {
        // Remove event listeners
        this.eventListeners.forEach(cleanup => cleanup());
        this.eventListeners.clear();
        
        // Clear timers
        this.timers.forEach(timer => clearTimeout(timer));
        this.timers.clear();
        
        // Clear intervals
        this.intervals.forEach(interval => clearInterval(interval));
        this.intervals.clear();
        
        // Disconnect observers
        this.observers.forEach(observer => observer.disconnect());
        this.observers.clear();
    }
    
    // Get memory usage stats
    getStats(): {
        eventListeners: number;
        timers: number;
        intervals: number;
        observers: number;
    } {
        return {
            eventListeners: this.eventListeners.size,
            timers: this.timers.size,
            intervals: this.intervals.size,
            observers: this.observers.size
        };
    }
}

// React hook for automatic cleanup
export function useMemoryLeakPrevention() {
    const detectorRef = useRef(new MemoryLeakDetector());
    
    useEffect(() => {
        return () => {
            detectorRef.current.cleanup();
        };
    }, []);
    
    return detectorRef.current;
}

// Performance monitoring utilities
export class PerformanceMonitor {
    private static instance: PerformanceMonitor;
    private metrics = new Map<string, number[]>();
    
    static getInstance(): PerformanceMonitor {
        if (!PerformanceMonitor.instance) {
            PerformanceMonitor.instance = new PerformanceMonitor();
        }
        return PerformanceMonitor.instance;
    }
    
    measureRenderTime(componentName: string, renderFn: () => void): void {
        const start = performance.now();
        renderFn();
        const end = performance.now();
        
        const duration = end - start;
        
        if (!this.metrics.has(componentName)) {
            this.metrics.set(componentName, []);
        }
        
        const times = this.metrics.get(componentName)!;
        times.push(duration);
        
        // Keep only last 100 measurements
        if (times.length > 100) {
            times.shift();
        }
        
        // Log slow renders
        if (duration > 16) { // 60fps = 16.67ms per frame
            console.warn(`Slow render detected: ${componentName} took ${duration.toFixed(2)}ms`);
        }
    }
    
    getAverageRenderTime(componentName: string): number {
        const times = this.metrics.get(componentName);
        if (!times || times.length === 0) return 0;
        
        return times.reduce((sum, time) => sum + time, 0) / times.length;
    }
    
    getMetrics(): Record<string, { average: number; count: number }> {
        const result: Record<string, { average: number; count: number }> = {};
        
        this.metrics.forEach((times, componentName) => {
            result[componentName] = {
                average: this.getAverageRenderTime(componentName),
                count: times.length
            };
        });
        
        return result;
    }
}

// ═══════════════════════════════════════════════════════════
// 🧪 HANDS-ON LAB 2: BACKEND MEMORY MANAGEMENT
// ═══════════════════════════════════════════════════════════

/*
📚 NODE.JS MEMORY MANAGEMENT:

🔥 COMMON BACKEND MEMORY ISSUES:

1. MEMORY LEAKS:
   - Unclosed database connections
   - Event emitter listeners not removed
   - Circular references
   - Global variables accumulation

2. INEFFICIENT DATA PROCESSING:
   - Loading entire datasets into memory
   - No streaming for large files
   - Inefficient algorithms
   - Poor garbage collection

3. CONNECTION MANAGEMENT:
   - Too many open connections
   - No connection pooling
   - WebSocket connections not cleaned up
   - Cache growing indefinitely

BACKEND OPTIMIZATION TECHNIQUES:
- Stream processing for large data
- Connection pooling and limits
- Memory monitoring and alerts
- Garbage collection optimization
- Efficient data structures

🎯 YOUR CODING MISSION:
Optimize One Piece backend for memory efficiency!
*/

// TODO 4: NODE.JS MEMORY MONITORING
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Create Node.js memory monitoring service

Create file: services/api-gateway/utils/memoryMonitor.js
*/

// FILE: services/api-gateway/utils/memoryMonitor.js
// YOUR CODE HERE - Create memory monitoring service:

const EventEmitter = require('events');

class MemoryMonitor extends EventEmitter {
    constructor(options = {}) {
        super();
        this.thresholds = {
            warning: options.warningThreshold || 0.8, // 80% of heap limit
            critical: options.criticalThreshold || 0.9, // 90% of heap limit
            ...options.thresholds
        };
        this.interval = options.interval || 30000; // 30 seconds
        this.isMonitoring = false;
        this.metrics = [];
        this.maxMetrics = 100; // Keep last 100 measurements
    }

    start() {
        if (this.isMonitoring) return;

        this.isMonitoring = true;
        this.monitoringInterval = setInterval(() => {
            this.checkMemoryUsage();
        }, this.interval);

        console.log('🧠 Memory monitoring started');
    }

    stop() {
        if (!this.isMonitoring) return;

        clearInterval(this.monitoringInterval);
        this.isMonitoring = false;
        console.log('🧠 Memory monitoring stopped');
    }

    checkMemoryUsage() {
        const memUsage = process.memoryUsage();
        const heapUsedMB = memUsage.heapUsed / 1024 / 1024;
        const heapTotalMB = memUsage.heapTotal / 1024 / 1024;
        const externalMB = memUsage.external / 1024 / 1024;
        const rssMB = memUsage.rss / 1024 / 1024;

        const heapUsageRatio = memUsage.heapUsed / memUsage.heapTotal;

        const metric = {
            timestamp: new Date(),
            heapUsed: heapUsedMB,
            heapTotal: heapTotalMB,
            external: externalMB,
            rss: rssMB,
            heapUsageRatio
        };

        // Store metric
        this.metrics.push(metric);
        if (this.metrics.length > this.maxMetrics) {
            this.metrics.shift();
        }

        // Check thresholds
        if (heapUsageRatio >= this.thresholds.critical) {
            this.emit('critical', metric);
            console.error('🚨 CRITICAL: Memory usage at', (heapUsageRatio * 100).toFixed(1), '%');
        } else if (heapUsageRatio >= this.thresholds.warning) {
            this.emit('warning', metric);
            console.warn('⚠️ WARNING: Memory usage at', (heapUsageRatio * 100).toFixed(1), '%');
        }

        this.emit('metric', metric);
    }

    getMemoryStats() {
        if (this.metrics.length === 0) return null;

        const latest = this.metrics[this.metrics.length - 1];
        const avg = this.metrics.reduce((sum, m) => sum + m.heapUsed, 0) / this.metrics.length;
        const max = Math.max(...this.metrics.map(m => m.heapUsed));

        return {
            current: latest,
            average: avg,
            maximum: max,
            samples: this.metrics.length
        };
    }

    forceGarbageCollection() {
        if (global.gc) {
            console.log('🗑️ Forcing garbage collection...');
            const before = process.memoryUsage().heapUsed;
            global.gc();
            const after = process.memoryUsage().heapUsed;
            const freed = (before - after) / 1024 / 1024;
            console.log(`🗑️ Freed ${freed.toFixed(2)} MB of memory`);
            return freed;
        } else {
            console.warn('⚠️ Garbage collection not available. Start Node.js with --expose-gc flag');
            return 0;
        }
    }
}

// TODO 5: STREAM PROCESSING FOR LARGE DATA
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Implement stream processing for large datasets

Create file: services/api-gateway/utils/streamProcessor.js
*/

// FILE: services/api-gateway/utils/streamProcessor.js
// YOUR CODE HERE - Create stream processing utilities:

const { Transform, Readable, Writable } = require('stream');
const { pipeline } = require('stream/promises');

class CharacterStreamProcessor {
    constructor() {
        this.batchSize = 100;
        this.processedCount = 0;
    }

    // Create readable stream from database cursor
    createCharacterStream(databaseCursor) {
        return new Readable({
            objectMode: true,
            async read() {
                try {
                    const character = await databaseCursor.next();
                    if (character) {
                        this.push(character);
                    } else {
                        this.push(null); // End stream
                    }
                } catch (error) {
                    this.destroy(error);
                }
            }
        });
    }

    // Transform stream for character processing
    createProcessingTransform() {
        return new Transform({
            objectMode: true,
            transform(character, encoding, callback) {
                try {
                    // Process character data efficiently
                    const processedCharacter = {
                        id: character.id,
                        name: character.name,
                        crew: character.crew,
                        bounty: character.bounty,
                        currentPrice: this.calculateCurrentPrice(character),
                        priceChange24h: this.calculatePriceChange(character),
                        // Only include necessary fields to reduce memory
                    };

                    callback(null, processedCharacter);
                } catch (error) {
                    callback(error);
                }
            },

            calculateCurrentPrice(character) {
                // Efficient price calculation
                return character.bounty * 0.001 + Math.random() * 10;
            },

            calculatePriceChange(character) {
                // Efficient price change calculation
                return (Math.random() - 0.5) * 20;
            }
        });
    }

    // Batch processing transform
    createBatchTransform(batchSize = 100) {
        let batch = [];

        return new Transform({
            objectMode: true,
            transform(chunk, encoding, callback) {
                batch.push(chunk);

                if (batch.length >= batchSize) {
                    this.push(batch);
                    batch = [];
                }
                callback();
            },

            flush(callback) {
                if (batch.length > 0) {
                    this.push(batch);
                }
                callback();
            }
        });
    }

    // Memory-efficient response writer
    createResponseWriter(res) {
        let isFirst = true;

        return new Writable({
            objectMode: true,
            write(batch, encoding, callback) {
                try {
                    if (isFirst) {
                        res.write('[');
                        isFirst = false;
                    } else {
                        res.write(',');
                    }

                    // Write batch as JSON
                    const batchJson = batch.map(item => JSON.stringify(item)).join(',');
                    res.write(batchJson);

                    callback();
                } catch (error) {
                    callback(error);
                }
            },

            final(callback) {
                res.write(']');
                res.end();
                callback();
            }
        });
    }

    // Process large character dataset with streaming
    async processLargeCharacterDataset(databaseCursor, res) {
        try {
            const sourceStream = this.createCharacterStream(databaseCursor);
            const processTransform = this.createProcessingTransform();
            const batchTransform = this.createBatchTransform(this.batchSize);
            const responseWriter = this.createResponseWriter(res);

            // Set response headers for streaming
            res.setHeader('Content-Type', 'application/json');
            res.setHeader('Transfer-Encoding', 'chunked');

            // Pipeline streams together
            await pipeline(
                sourceStream,
                processTransform,
                batchTransform,
                responseWriter
            );

            console.log(`✅ Processed ${this.processedCount} characters via streaming`);
        } catch (error) {
            console.error('❌ Stream processing error:', error);
            if (!res.headersSent) {
                res.status(500).json({ error: 'Stream processing failed' });
            }
        }
    }
}

module.exports = { MemoryMonitor, CharacterStreamProcessor };

// ===============================================================================
// 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED MEMORY OPTIMIZATION! 🎉
// ===============================================================================

console.log('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED MEMORY OPTIMIZATION! 🎉');
console.log('===============================================================================');

console.log('\n🎯 WHAT YOU\'VE ACCOMPLISHED:');
console.log('✅ Mastered frontend memory optimization with virtual scrolling and memoization');
console.log('✅ Implemented backend memory management with monitoring and stream processing');
console.log('✅ Built memory-efficient data structures and caching strategies');
console.log('✅ Created memory leak detection and prevention systems');
console.log('✅ Applied performance optimization patterns used by Netflix, Facebook, and Google');
console.log('✅ Learned production-grade memory profiling and monitoring');

console.log('\n💰 SALARY IMPACT: +$80K-$200K (Memory optimization is critical for senior/staff roles)');
console.log('🏢 COMPANIES: All FAANG, Netflix, Uber, high-traffic applications, performance teams');

console.log('\n===============================================================================');
console.log('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!');
console.log('===============================================================================');

console.log('\n🚀 STEP 1: OPTIMIZE YOUR REACT CHARACTER LIST');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📁 File to update: frontend/src/components/Characters/CharacterList.tsx');
console.log('');
console.log('🎯 WHAT TO DO:');
console.log('1. Replace regular list with virtual scrolling');
console.log('2. Add React.memo with custom comparison');
console.log('3. Implement memory-efficient state management');
console.log('4. Add memory leak prevention');
console.log('5. Monitor component render performance');
console.log('');
console.log('📚 REFERENCE: Use the VirtualCharacterList from this module');

console.log('\n🚀 STEP 2: ADD MEMORY MONITORING TO YOUR API GATEWAY');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 UPDATE: services/api-gateway/server.js');
console.log('');
console.log('const { MemoryMonitor } = require("./utils/memoryMonitor");');
console.log('');
console.log('// Initialize memory monitoring');
console.log('const memoryMonitor = new MemoryMonitor({');
console.log('    warningThreshold: 0.8,');
console.log('    criticalThreshold: 0.9,');
console.log('    interval: 30000');
console.log('});');
console.log('');
console.log('// Start monitoring');
console.log('memoryMonitor.start();');
console.log('');
console.log('// Handle memory alerts');
console.log('memoryMonitor.on("warning", (metric) => {');
console.log('    console.warn(`⚠️ Memory warning: ${metric.heapUsed.toFixed(2)}MB used`);');
console.log('    // Optional: Clear caches, reduce connections');
console.log('});');
console.log('');
console.log('memoryMonitor.on("critical", (metric) => {');
console.log('    console.error(`🚨 Critical memory usage: ${metric.heapUsed.toFixed(2)}MB`);');
console.log('    // Force garbage collection');
console.log('    memoryMonitor.forceGarbageCollection();');
console.log('});');
console.log('');
console.log('// Memory stats endpoint');
console.log('app.get("/api/memory-stats", (req, res) => {');
console.log('    const stats = memoryMonitor.getMemoryStats();');
console.log('    res.json(stats);');
console.log('});');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- MemoryMonitor class (lines 350-450)');
console.log('- Memory threshold handling (lines 400-420)');
console.log('- Garbage collection utilities (lines 460-480)');

console.log('\n🚀 STEP 3: IMPLEMENT STREAM PROCESSING FOR LARGE DATASETS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 UPDATE: services/character-service/app.py');
console.log('');
console.log('const { CharacterStreamProcessor } = require("../shared/utils/streamProcessor");');
console.log('');
console.log('// Stream large character datasets');
console.log('app.get("/api/characters/stream", async (req, res) => {');
console.log('    try {');
console.log('        const processor = new CharacterStreamProcessor();');
console.log('        ');
console.log('        // Get database cursor for streaming');
console.log('        const cursor = await db.characters.find({}).cursor();');
console.log('        ');
console.log('        // Process with streaming (memory-efficient)');
console.log('        await processor.processLargeCharacterDataset(cursor, res);');
console.log('    } catch (error) {');
console.log('        console.error("Stream processing error:", error);');
console.log('        res.status(500).json({ error: "Failed to stream characters" });');
console.log('    }');
console.log('});');
console.log('');
console.log('// Memory-efficient pagination');
console.log('app.get("/api/characters", async (req, res) => {');
console.log('    const page = parseInt(req.query.page) || 1;');
console.log('    const limit = Math.min(parseInt(req.query.limit) || 50, 100); // Max 100');
console.log('    const offset = (page - 1) * limit;');
console.log('    ');
console.log('    try {');
console.log('        // Use database-level pagination (memory efficient)');
console.log('        const characters = await db.characters.find({})');
console.log('            .skip(offset)');
console.log('            .limit(limit)');
console.log('            .lean(); // Mongoose: return plain objects');
console.log('        ');
console.log('        const total = await db.characters.countDocuments({});');
console.log('        ');
console.log('        res.json({');
console.log('            data: characters,');
console.log('            pagination: {');
console.log('                page,');
console.log('                limit,');
console.log('                total,');
console.log('                pages: Math.ceil(total / limit)');
console.log('            }');
console.log('        });');
console.log('    } catch (error) {');
console.log('        res.status(500).json({ error: error.message });');
console.log('    }');
console.log('});');
console.log('');
console.log('🔧 STREAM PROCESSING BENEFITS:');
console.log('- Process datasets larger than available RAM');
console.log('- Constant memory usage regardless of data size');
console.log('- Better user experience with progressive loading');
console.log('- Reduced server memory pressure');

console.log('\n🚀 STEP 4: ADD MEMORY-EFFICIENT CACHING');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: shared/cache/memoryEfficientCache.js');
console.log('');
console.log('class LRUCache {');
console.log('    constructor(maxSize = 1000, maxMemoryMB = 100) {');
console.log('        this.maxSize = maxSize;');
console.log('        this.maxMemory = maxMemoryMB * 1024 * 1024; // Convert to bytes');
console.log('        this.cache = new Map();');
console.log('        this.accessOrder = new Set();');
console.log('        this.currentMemory = 0;');
console.log('    }');
console.log('    ');
console.log('    set(key, value) {');
console.log('        const serialized = JSON.stringify(value);');
console.log('        const size = Buffer.byteLength(serialized, "utf8");');
console.log('        ');
console.log('        // Check memory limits');
console.log('        while (this.currentMemory + size > this.maxMemory && this.cache.size > 0) {');
console.log('            this.evictLRU();');
console.log('        }');
console.log('        ');
console.log('        // Check size limits');
console.log('        while (this.cache.size >= this.maxSize && this.cache.size > 0) {');
console.log('            this.evictLRU();');
console.log('        }');
console.log('        ');
console.log('        // Add to cache');
console.log('        if (this.cache.has(key)) {');
console.log('            this.currentMemory -= this.cache.get(key).size;');
console.log('        }');
console.log('        ');
console.log('        this.cache.set(key, { value, size });');
console.log('        this.currentMemory += size;');
console.log('        this.accessOrder.add(key);');
console.log('    }');
console.log('    ');
console.log('    get(key) {');
console.log('        if (!this.cache.has(key)) return undefined;');
console.log('        ');
console.log('        // Update access order');
console.log('        this.accessOrder.delete(key);');
console.log('        this.accessOrder.add(key);');
console.log('        ');
console.log('        return this.cache.get(key).value;');
console.log('    }');
console.log('    ');
console.log('    evictLRU() {');
console.log('        const oldestKey = this.accessOrder.values().next().value;');
console.log('        if (oldestKey) {');
console.log('            const item = this.cache.get(oldestKey);');
console.log('            this.currentMemory -= item.size;');
console.log('            this.cache.delete(oldestKey);');
console.log('            this.accessOrder.delete(oldestKey);');
console.log('        }');
console.log('    }');
console.log('    ');
console.log('    getStats() {');
console.log('        return {');
console.log('            size: this.cache.size,');
console.log('            maxSize: this.maxSize,');
console.log('            memoryUsageMB: (this.currentMemory / 1024 / 1024).toFixed(2),');
console.log('            maxMemoryMB: (this.maxMemory / 1024 / 1024).toFixed(2)');
console.log('        };');
console.log('    }');
console.log('}');
console.log('');
console.log('// Usage in your services');
console.log('const characterCache = new LRUCache(1000, 50); // 1000 items, 50MB max');
console.log('');
console.log('🔧 MEMORY-EFFICIENT CACHING BENEFITS:');
console.log('- Automatic memory limit enforcement');
console.log('- LRU eviction prevents memory leaks');
console.log('- Size-based and memory-based limits');
console.log('- Real-time memory usage tracking');

console.log('\n🚀 STEP 5: TEST YOUR MEMORY OPTIMIZATIONS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🧪 TESTING STEPS:');
console.log('');
console.log('1. Start your application with memory monitoring:');
console.log('   # Start Node.js with garbage collection exposed');
console.log('   node --expose-gc --inspect services/api-gateway/server.js');
console.log('   ');
console.log('   # Start React with memory profiling');
console.log('   cd frontend && npm start');
console.log('');
console.log('2. Test frontend memory optimization:');
console.log('   - Open Chrome DevTools → Memory tab');
console.log('   - Take heap snapshot before loading characters');
console.log('   - Load 1000+ characters with virtual scrolling');
console.log('   - Take another heap snapshot');
console.log('   - Compare memory usage (should be minimal increase)');
console.log('');
console.log('3. Test backend memory monitoring:');
console.log('   curl http://localhost:5000/api/memory-stats');
console.log('   # Should show current memory usage and statistics');
console.log('');
console.log('4. Test stream processing:');
console.log('   curl http://localhost:5000/api/characters/stream');
console.log('   # Should stream large datasets without memory spikes');
console.log('');
console.log('5. Load test memory efficiency:');
console.log('   # Install artillery for load testing');
console.log('   npm install -g artillery');
console.log('   ');
console.log('   # Create load test config');
console.log('   artillery quick --count 100 --num 10 http://localhost:5000/api/characters');
console.log('   ');
console.log('   # Monitor memory during load test');
console.log('   watch -n 1 "curl -s http://localhost:5000/api/memory-stats | jq"');
console.log('');
console.log('6. Test memory leak prevention:');
console.log('   - Navigate between pages multiple times');
console.log('   - Check Chrome DevTools → Memory → Performance monitor');
console.log('   - Memory usage should remain stable');
console.log('');
console.log('✅ SUCCESS CRITERIA:');
console.log('- Virtual scrolling handles 10,000+ items smoothly');
console.log('- Memory usage remains stable during navigation');
console.log('- Backend memory monitoring shows healthy metrics');
console.log('- Stream processing works without memory spikes');
console.log('- Load testing shows consistent memory usage');
console.log('- No memory leaks detected in Chrome DevTools');

console.log('\n===============================================================================');
console.log('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES');
console.log('===============================================================================');

console.log('\n🧩 MODULE CONNECTIONS:');
console.log('');
console.log('📚 Module 19 (React) → Enhanced with memory-efficient components and virtual scrolling');
console.log('📚 Module 16 (Node.js) → API Gateway includes memory monitoring and stream processing');
console.log('📚 Module 3 (Database) → Combined with memory-efficient caching and query optimization');
console.log('📚 Module 8 (Monitoring) → Memory metrics integrated with Prometheus and Grafana');
console.log('📚 Module 6 (System Design) → Memory optimization patterns for microservices architecture');
console.log('📚 Module 18 (TypeScript) → Type-safe memory management and performance monitoring');

console.log('\n🎯 NEXT MODULES TO COMPLETE:');
console.log('1. Module 8: Add memory metrics to your monitoring dashboard');
console.log('2. Module 4: Containerize with proper memory limits and monitoring');
console.log('3. Module 9: Deploy with cloud-based memory monitoring and auto-scaling');

console.log('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:');
console.log('🔗 Chrome DevTools Memory: https://developer.chrome.com/docs/devtools/memory-problems/');
console.log('🔗 Node.js Memory Best Practices: https://nodejs.org/en/docs/guides/simple-profiling/');
console.log('🔗 React Performance: https://react.dev/learn/render-and-commit');
console.log('🔗 V8 Memory Management: https://v8.dev/blog/memory');

console.log('\n🏴‍☠️ YOU\'RE NOW A MEMORY OPTIMIZATION EXPERT! ⚔️');
console.log('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for complete system overview!');
