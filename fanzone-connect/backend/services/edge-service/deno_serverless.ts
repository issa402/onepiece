/**
 * 🏆 FANZONE CONNECT - DENO EDGE SERVICE
 * Learning Modules: 26 (Deno Backend), 27 (Edge/Serverless)
 * World Cup 2026 Fan Platform - Ultra-Fast Edge Computing with Deno
 */

import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { Redis } from "https://deno.land/x/redis@v0.32.1/mod.ts";
import { crypto } from "https://deno.land/std@0.208.0/crypto/mod.ts";

// =====================================================
// MODULE 26: DENO BACKEND - MODERN RUNTIME
// =====================================================

interface WorldCupConfig {
  readonly REDIS_URL: string;
  readonly JWT_SECRET: string;
  readonly API_VERSION: string;
  readonly RATE_LIMIT_REQUESTS: number;
  readonly RATE_LIMIT_WINDOW: number;
  readonly CACHE_TTL: number;
}

const config: WorldCupConfig = {
  REDIS_URL: Deno.env.get("REDIS_URL") || "redis://redis:6379",
  JWT_SECRET: Deno.env.get("JWT_SECRET") || "worldcup2026-secret",
  API_VERSION: "v1",
  RATE_LIMIT_REQUESTS: 100,
  RATE_LIMIT_WINDOW: 60, // seconds
  CACHE_TTL: 300, // 5 minutes
};

// Global Redis connection
let redis: Redis;

// =====================================================
// WORLD CUP 2026 TYPES
// =====================================================

interface MatchData {
  id: string;
  homeTeam: {
    name: string;
    code: string;
    flag: string;
  };
  awayTeam: {
    name: string;
    code: string;
    flag: string;
  };
  venue: {
    name: string;
    city: string;
    country: string;
  };
  dateTime: string;
  status: "scheduled" | "live" | "finished";
  score?: {
    home: number;
    away: number;
  };
  phase: string;
}

interface FanLocation {
  userId: string;
  latitude: number;
  longitude: number;
  city: string;
  country: string;
  timestamp: string;
}

interface EdgeResponse<T = unknown> {
  success: boolean;
  data?: T;
  error?: string;
  timestamp: string;
  processingTime: number;
  edge: string;
}

// =====================================================
// MODULE 27: EDGE/SERVERLESS - PERFORMANCE UTILITIES
// =====================================================

class PerformanceTracker {
  private startTime: number;
  
  constructor() {
    this.startTime = performance.now();
  }
  
  getElapsedTime(): number {
    return performance.now() - this.startTime;
  }
}

class RateLimiter {
  private redis: Redis;
  
  constructor(redisClient: Redis) {
    this.redis = redisClient;
  }
  
  async checkLimit(identifier: string): Promise<boolean> {
    const key = `rate_limit:${identifier}`;
    const current = await this.redis.get(key);
    
    if (current === null) {
      await this.redis.setex(key, config.RATE_LIMIT_WINDOW, "1");
      return true;
    }
    
    const count = parseInt(current);
    if (count >= config.RATE_LIMIT_REQUESTS) {
      return false;
    }
    
    await this.redis.incr(key);
    return true;
  }
}

class EdgeCache {
  private redis: Redis;
  
  constructor(redisClient: Redis) {
    this.redis = redisClient;
  }
  
  async get<T>(key: string): Promise<T | null> {
    try {
      const cached = await this.redis.get(key);
      return cached ? JSON.parse(cached) : null;
    } catch (error) {
      console.error("❌ Cache get error:", error);
      return null;
    }
  }
  
  async set(key: string, value: unknown, ttl: number = config.CACHE_TTL): Promise<void> {
    try {
      await this.redis.setex(key, ttl, JSON.stringify(value));
    } catch (error) {
      console.error("❌ Cache set error:", error);
    }
  }
  
  async invalidate(pattern: string): Promise<void> {
    try {
      const keys = await this.redis.keys(pattern);
      if (keys.length > 0) {
        await this.redis.del(...keys);
      }
    } catch (error) {
      console.error("❌ Cache invalidation error:", error);
    }
  }
}

// =====================================================
// WORLD CUP 2026 EDGE SERVICES
// =====================================================

class WorldCupEdgeService {
  private cache: EdgeCache;
  private rateLimiter: RateLimiter;
  
  constructor(redisClient: Redis) {
    this.cache = new EdgeCache(redisClient);
    this.rateLimiter = new RateLimiter(redisClient);
  }
  
  async getLiveMatches(): Promise<MatchData[]> {
    const cacheKey = "worldcup:live_matches";
    
    // Try cache first
    const cached = await this.cache.get<MatchData[]>(cacheKey);
    if (cached) {
      return cached;
    }
    
    // Mock live matches data (in production, fetch from main API)
    const liveMatches: MatchData[] = [
      {
        id: "match_001",
        homeTeam: {
          name: "Brazil",
          code: "BRA",
          flag: "https://flagcdn.com/w40/br.png"
        },
        awayTeam: {
          name: "Argentina",
          code: "ARG",
          flag: "https://flagcdn.com/w40/ar.png"
        },
        venue: {
          name: "MetLife Stadium",
          city: "New York",
          country: "USA"
        },
        dateTime: "2026-07-14T20:00:00Z",
        status: "live",
        score: {
          home: 2,
          away: 1
        },
        phase: "Final"
      },
      {
        id: "match_002",
        homeTeam: {
          name: "France",
          code: "FRA",
          flag: "https://flagcdn.com/w40/fr.png"
        },
        awayTeam: {
          name: "Spain",
          code: "ESP",
          flag: "https://flagcdn.com/w40/es.png"
        },
        venue: {
          name: "SoFi Stadium",
          city: "Los Angeles",
          country: "USA"
        },
        dateTime: "2026-07-13T17:00:00Z",
        status: "live",
        score: {
          home: 0,
          away: 1
        },
        phase: "Semi-Final"
      }
    ];
    
    // Cache for 30 seconds (live data changes frequently)
    await this.cache.set(cacheKey, liveMatches, 30);
    
    return liveMatches;
  }
  
  async getNearbyFans(location: FanLocation, radiusKm: number = 10): Promise<FanLocation[]> {
    const cacheKey = `nearby_fans:${location.userId}:${radiusKm}`;
    
    // Try cache first
    const cached = await this.cache.get<FanLocation[]>(cacheKey);
    if (cached) {
      return cached;
    }
    
    // Mock nearby fans (in production, use geospatial queries)
    const nearbyFans: FanLocation[] = [
      {
        userId: "fan_001",
        latitude: location.latitude + 0.01,
        longitude: location.longitude + 0.01,
        city: location.city,
        country: location.country,
        timestamp: new Date().toISOString()
      },
      {
        userId: "fan_002",
        latitude: location.latitude - 0.005,
        longitude: location.longitude + 0.008,
        city: location.city,
        country: location.country,
        timestamp: new Date().toISOString()
      }
    ];
    
    // Cache for 2 minutes
    await this.cache.set(cacheKey, nearbyFans, 120);
    
    return nearbyFans;
  }
  
  async getMatchPredictions(matchId: string): Promise<Record<string, number>> {
    const cacheKey = `predictions:${matchId}`;
    
    const cached = await this.cache.get<Record<string, number>>(cacheKey);
    if (cached) {
      return cached;
    }
    
    // Mock AI predictions (in production, call ML service)
    const predictions = {
      homeWin: 0.45,
      draw: 0.25,
      awayWin: 0.30,
      over2_5Goals: 0.65,
      bothTeamsScore: 0.72
    };
    
    // Cache predictions for 1 hour
    await this.cache.set(cacheKey, predictions, 3600);
    
    return predictions;
  }
}

// =====================================================
// HTTP REQUEST HANDLERS
// =====================================================

async function handleRequest(request: Request): Promise<Response> {
  const tracker = new PerformanceTracker();
  const url = new URL(request.url);
  const pathname = url.pathname;
  
  // CORS headers
  const corsHeaders = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  };
  
  // Handle preflight requests
  if (request.method === "OPTIONS") {
    return new Response(null, { status: 200, headers: corsHeaders });
  }
  
  // Rate limiting
  const clientIP = request.headers.get("x-forwarded-for") || "unknown";
  const rateLimiter = new RateLimiter(redis);
  
  if (!(await rateLimiter.checkLimit(clientIP))) {
    return createErrorResponse("Rate limit exceeded", 429, tracker);
  }
  
  const worldCupService = new WorldCupEdgeService(redis);
  
  try {
    // Route handling
    if (pathname === "/api/v1/matches/live") {
      const matches = await worldCupService.getLiveMatches();
      return createSuccessResponse(matches, tracker, corsHeaders);
    }
    
    if (pathname === "/api/v1/fans/nearby" && request.method === "POST") {
      const body = await request.json() as FanLocation;
      const radiusKm = parseInt(url.searchParams.get("radius") || "10");
      
      const nearbyFans = await worldCupService.getNearbyFans(body, radiusKm);
      return createSuccessResponse(nearbyFans, tracker, corsHeaders);
    }
    
    if (pathname.startsWith("/api/v1/matches/") && pathname.endsWith("/predictions")) {
      const matchId = pathname.split("/")[4];
      const predictions = await worldCupService.getMatchPredictions(matchId);
      return createSuccessResponse(predictions, tracker, corsHeaders);
    }
    
    if (pathname === "/api/v1/health") {
      const health = {
        status: "healthy",
        service: "fanzone-edge-service",
        version: "1.0.0",
        timestamp: new Date().toISOString(),
        deno_version: Deno.version.deno,
        uptime: performance.now()
      };
      return createSuccessResponse(health, tracker, corsHeaders);
    }
    
    // 404 for unknown routes
    return createErrorResponse("Endpoint not found", 404, tracker, corsHeaders);
    
  } catch (error) {
    console.error("❌ Request handling error:", error);
    return createErrorResponse("Internal server error", 500, tracker, corsHeaders);
  }
}

function createSuccessResponse<T>(
  data: T, 
  tracker: PerformanceTracker, 
  headers: Record<string, string> = {}
): Response {
  const response: EdgeResponse<T> = {
    success: true,
    data,
    timestamp: new Date().toISOString(),
    processingTime: tracker.getElapsedTime(),
    edge: "deno-edge"
  };
  
  return new Response(JSON.stringify(response), {
    status: 200,
    headers: {
      "Content-Type": "application/json",
      ...headers
    }
  });
}

function createErrorResponse(
  error: string, 
  status: number, 
  tracker: PerformanceTracker,
  headers: Record<string, string> = {}
): Response {
  const response: EdgeResponse = {
    success: false,
    error,
    timestamp: new Date().toISOString(),
    processingTime: tracker.getElapsedTime(),
    edge: "deno-edge"
  };
  
  return new Response(JSON.stringify(response), {
    status,
    headers: {
      "Content-Type": "application/json",
      ...headers
    }
  });
}

// =====================================================
// MAIN SERVER INITIALIZATION
// =====================================================

async function initializeServer() {
  console.log("🏆 FANZONE CONNECT - Deno Edge Service Starting...");
  console.log("🌍 World Cup 2026 Fan Platform - Ultra-Fast Edge Computing");
  
  try {
    // Initialize Redis connection
    redis = new Redis({
      hostname: "redis",
      port: 6379,
    });
    
    await redis.ping();
    console.log("✅ Redis connection established");
    
    // Start HTTP server
    const port = parseInt(Deno.env.get("PORT") || "8080");
    
    console.log(`🚀 Deno Edge Service running on port ${port}`);
    console.log(`📊 Rate limit: ${config.RATE_LIMIT_REQUESTS} requests per ${config.RATE_LIMIT_WINDOW}s`);
    console.log(`💾 Cache TTL: ${config.CACHE_TTL}s`);
    console.log("="*50);
    
    await serve(handleRequest, { port });
    
  } catch (error) {
    console.error("❌ Failed to initialize server:", error);
    Deno.exit(1);
  }
}

// Handle graceful shutdown
Deno.addSignalListener("SIGINT", async () => {
  console.log("\n🛑 Shutting down Deno Edge Service...");
  
  if (redis) {
    await redis.quit();
    console.log("✅ Redis connection closed");
  }
  
  console.log("🏁 Deno Edge Service shutdown complete");
  Deno.exit(0);
});

// Start the server
if (import.meta.main) {
  await initializeServer();
}
