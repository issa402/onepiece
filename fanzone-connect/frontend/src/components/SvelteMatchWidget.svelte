<!--
🏆 FANZONE CONNECT - SVELTE MATCH WIDGET
Learning Modules: 28 (Svelte Frontend), 43 (Caching Strategies)
World Cup 2026 Fan Platform - Ultra-Lightweight Match Widget with Smart Caching
-->

<script lang="ts">
  import { onMount, onDestroy } from 'svelte';
  import { writable, derived } from 'svelte/store';
  import { fade, fly, scale } from 'svelte/transition';
  import { quintOut } from 'svelte/easing';

  // =====================================================
  // MODULE 28: SVELTE FRONTEND - REACTIVE STORES
  // =====================================================

  interface Team {
    name: string;
    code: string;
    flag: string;
    ranking: number;
  }

  interface Match {
    id: string;
    homeTeam: Team;
    awayTeam: Team;
    venue: {
      name: string;
      city: string;
    };
    dateTime: string;
    status: 'scheduled' | 'live' | 'finished';
    score?: {
      home: number;
      away: number;
    };
    phase: string;
    minute?: number;
  }

  // Props
  export let matchId: string;
  export let autoRefresh: boolean = true;
  export let refreshInterval: number = 30000; // 30 seconds
  export let showPredictions: boolean = true;
  export let compact: boolean = false;

  // Reactive stores
  const match = writable<Match | null>(null);
  const loading = writable<boolean>(true);
  const error = writable<string | null>(null);
  const predictions = writable<Record<string, number> | null>(null);
  const lastUpdated = writable<Date | null>(null);

  // Derived stores
  const isLive = derived(match, $match => $match?.status === 'live');
  const timeUntilMatch = derived(match, $match => {
    if (!$match || $match.status !== 'scheduled') return null;
    
    const matchTime = new Date($match.dateTime);
    const now = new Date();
    const diff = matchTime.getTime() - now.getTime();
    
    if (diff <= 0) return 'Starting soon';
    
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    if (days > 0) return `${days}d ${hours}h`;
    if (hours > 0) return `${hours}h ${minutes}m`;
    return `${minutes}m`;
  });

  // =====================================================
  // MODULE 43: CACHING STRATEGIES - SMART CACHING
  // =====================================================

  class MatchCache {
    private cache = new Map<string, { data: any; timestamp: number; ttl: number }>();
    
    set(key: string, data: any, ttl: number = 30000): void {
      this.cache.set(key, {
        data,
        timestamp: Date.now(),
        ttl
      });
    }
    
    get(key: string): any | null {
      const cached = this.cache.get(key);
      if (!cached) return null;
      
      if (Date.now() - cached.timestamp > cached.ttl) {
        this.cache.delete(key);
        return null;
      }
      
      return cached.data;
    }
    
    invalidate(key: string): void {
      this.cache.delete(key);
    }
    
    clear(): void {
      this.cache.clear();
    }
  }

  const cache = new MatchCache();
  let refreshTimer: number | null = null;
  let websocket: WebSocket | null = null;

  // API functions with caching
  async function fetchMatchData(): Promise<void> {
    try {
      loading.set(true);
      error.set(null);

      // Check cache first
      const cacheKey = `match:${matchId}`;
      const cached = cache.get(cacheKey);
      
      if (cached) {
        match.set(cached);
        loading.set(false);
        return;
      }

      // Fetch from API
      const response = await fetch(`/api/v1/matches/${matchId}`);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const matchData: Match = await response.json();
      
      // Cache with different TTL based on match status
      const ttl = matchData.status === 'live' ? 10000 : 60000; // 10s for live, 60s for others
      cache.set(cacheKey, matchData, ttl);
      
      match.set(matchData);
      lastUpdated.set(new Date());
      
    } catch (err) {
      console.error('❌ Error fetching match data:', err);
      error.set(err instanceof Error ? err.message : 'Failed to load match data');
    } finally {
      loading.set(false);
    }
  }

  async function fetchPredictions(): Promise<void> {
    if (!showPredictions) return;

    try {
      const cacheKey = `predictions:${matchId}`;
      const cached = cache.get(cacheKey);
      
      if (cached) {
        predictions.set(cached);
        return;
      }

      const response = await fetch(`/api/v1/matches/${matchId}/predictions`);
      if (response.ok) {
        const predictionData = await response.json();
        
        // Cache predictions for 1 hour
        cache.set(cacheKey, predictionData, 3600000);
        predictions.set(predictionData);
      }
    } catch (err) {
      console.error('⚠️ Error fetching predictions:', err);
    }
  }

  function setupWebSocket(): void {
    if (!$isLive) return;

    try {
      websocket = new WebSocket(`wss://api.fanzoneconnect.com/ws/matches/${matchId}`);
      
      websocket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.type === 'match_update') {
            // Invalidate cache and update match data
            cache.invalidate(`match:${matchId}`);
            match.set(data.match);
            lastUpdated.set(new Date());
          }
        } catch (err) {
          console.error('❌ WebSocket message error:', err);
        }
      };

      websocket.onerror = (err) => {
        console.error('❌ WebSocket error:', err);
      };

      websocket.onclose = () => {
        // Reconnect after 5 seconds if match is still live
        if ($isLive) {
          setTimeout(setupWebSocket, 5000);
        }
      };

    } catch (err) {
      console.error('❌ WebSocket setup error:', err);
    }
  }

  function setupRefreshTimer(): void {
    if (!autoRefresh) return;

    refreshTimer = setInterval(() => {
      fetchMatchData();
    }, refreshInterval);
  }

  function formatTime(dateTime: string): string {
    return new Date(dateTime).toLocaleTimeString('en-US', {
      hour: '2-digit',
      minute: '2-digit',
      timeZoneName: 'short'
    });
  }

  function getStatusColor(status: string): string {
    switch (status) {
      case 'live': return 'text-red-500 animate-pulse';
      case 'finished': return 'text-gray-500';
      default: return 'text-blue-500';
    }
  }

  // Lifecycle
  onMount(async () => {
    await fetchMatchData();
    await fetchPredictions();
    
    // Setup real-time updates for live matches
    if ($isLive) {
      setupWebSocket();
    }
    
    setupRefreshTimer();
  });

  onDestroy(() => {
    if (refreshTimer) {
      clearInterval(refreshTimer);
    }
    
    if (websocket) {
      websocket.close();
    }
    
    cache.clear();
  });

  // Reactive statements
  $: if ($match?.status === 'live' && !websocket) {
    setupWebSocket();
  }

  $: if ($match?.status !== 'live' && websocket) {
    websocket.close();
    websocket = null;
  }
</script>

<!-- =====================================================
     SVELTE TEMPLATE WITH ANIMATIONS
     ===================================================== -->

<div 
  class="match-widget {compact ? 'compact' : 'full'}"
  class:live={$isLive}
  in:fade={{ duration: 300 }}
>
  {#if $loading}
    <div class="loading-state" in:scale={{ duration: 200, easing: quintOut }}>
      <div class="spinner"></div>
      <p>Loading match data...</p>
    </div>
  
  {:else if $error}
    <div class="error-state" in:fly={{ y: 20, duration: 300 }}>
      <p class="error-message">❌ {$error}</p>
      <button on:click={fetchMatchData} class="retry-btn">
        Retry
      </button>
    </div>
  
  {:else if $match}
    <div class="match-content" in:fly={{ y: 20, duration: 400, delay: 100 }}>
      <!-- Match Header -->
      <div class="match-header">
        <span class="phase-badge">{$match.phase}</span>
        <span class="status {getStatusColor($match.status)}">
          {#if $match.status === 'live'}
            🔴 LIVE {$match.minute ? `${$match.minute}'` : ''}
          {:else if $match.status === 'finished'}
            FINAL
          {:else}
            {$timeUntilMatch}
          {/if}
        </span>
      </div>

      <!-- Teams and Score -->
      <div class="teams-container">
        <!-- Home Team -->
        <div class="team home-team">
          <img src={$match.homeTeam.flag} alt={$match.homeTeam.name} class="flag" />
          <div class="team-info">
            <h3 class="team-name">{$match.homeTeam.name}</h3>
            <span class="team-ranking">#{$match.homeTeam.ranking}</span>
          </div>
        </div>

        <!-- Score or VS -->
        <div class="score-container">
          {#if $match.score}
            <div class="score" in:scale={{ duration: 300 }}>
              <span class="home-score">{$match.score.home}</span>
              <span class="separator">-</span>
              <span class="away-score">{$match.score.away}</span>
            </div>
          {:else}
            <div class="vs">VS</div>
          {/if}
        </div>

        <!-- Away Team -->
        <div class="team away-team">
          <div class="team-info">
            <h3 class="team-name">{$match.awayTeam.name}</h3>
            <span class="team-ranking">#{$match.awayTeam.ranking}</span>
          </div>
          <img src={$match.awayTeam.flag} alt={$match.awayTeam.name} class="flag" />
        </div>
      </div>

      <!-- Match Details -->
      {#if !compact}
        <div class="match-details" in:fade={{ delay: 200, duration: 300 }}>
          <div class="venue">
            📍 {$match.venue.name}, {$match.venue.city}
          </div>
          <div class="datetime">
            🕒 {formatTime($match.dateTime)}
          </div>
        </div>

        <!-- Predictions -->
        {#if showPredictions && $predictions}
          <div class="predictions" in:fly={{ y: 20, delay: 300, duration: 300 }}>
            <h4>AI Predictions</h4>
            <div class="prediction-bars">
              <div class="prediction">
                <span>Home Win</span>
                <div class="bar">
                  <div class="fill" style="width: {$predictions.homeWin * 100}%"></div>
                </div>
                <span>{Math.round($predictions.homeWin * 100)}%</span>
              </div>
              <div class="prediction">
                <span>Draw</span>
                <div class="bar">
                  <div class="fill" style="width: {$predictions.draw * 100}%"></div>
                </div>
                <span>{Math.round($predictions.draw * 100)}%</span>
              </div>
              <div class="prediction">
                <span>Away Win</span>
                <div class="bar">
                  <div class="fill" style="width: {$predictions.awayWin * 100}%"></div>
                </div>
                <span>{Math.round($predictions.awayWin * 100)}%</span>
              </div>
            </div>
          </div>
        {/if}
      {/if}

      <!-- Last Updated -->
      {#if $lastUpdated}
        <div class="last-updated">
          Last updated: {$lastUpdated.toLocaleTimeString()}
        </div>
      {/if}
    </div>
  {/if}
</div>

<!-- =====================================================
     SVELTE STYLES WITH CSS VARIABLES
     ===================================================== -->

<style>
  .match-widget {
    --primary-color: #1e40af;
    --secondary-color: #f59e0b;
    --success-color: #10b981;
    --error-color: #ef4444;
    --live-color: #dc2626;
    --text-primary: #1f2937;
    --text-secondary: #6b7280;
    --bg-primary: #ffffff;
    --bg-secondary: #f9fafb;
    --border-color: #e5e7eb;
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    
    background: var(--bg-primary);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: var(--shadow);
    transition: all 0.3s ease;
    max-width: 500px;
    margin: 0 auto;
  }

  .match-widget.live {
    border-color: var(--live-color);
    box-shadow: 0 0 20px rgba(220, 38, 38, 0.2);
  }

  .match-widget.compact {
    padding: 1rem;
    max-width: 350px;
  }

  .loading-state, .error-state {
    text-align: center;
    padding: 2rem;
  }

  .spinner {
    width: 40px;
    height: 40px;
    border: 4px solid var(--border-color);
    border-top: 4px solid var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin: 0 auto 1rem;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .match-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
  }

  .phase-badge {
    background: var(--primary-color);
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 600;
  }

  .status {
    font-weight: 700;
    font-size: 0.875rem;
  }

  .teams-container {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 1rem;
    align-items: center;
    margin-bottom: 1rem;
  }

  .team {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .away-team {
    justify-content: flex-end;
    flex-direction: row-reverse;
  }

  .flag {
    width: 48px;
    height: 32px;
    object-fit: cover;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .team-info {
    text-align: center;
  }

  .away-team .team-info {
    text-align: right;
  }

  .team-name {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0 0 0.25rem 0;
  }

  .team-ranking {
    font-size: 0.875rem;
    color: var(--text-secondary);
  }

  .score-container {
    text-align: center;
  }

  .score {
    font-size: 2rem;
    font-weight: 900;
    color: var(--text-primary);
  }

  .separator {
    margin: 0 0.5rem;
    color: var(--text-secondary);
  }

  .vs {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text-secondary);
  }

  .match-details {
    display: flex;
    justify-content: space-between;
    padding: 1rem 0;
    border-top: 1px solid var(--border-color);
    font-size: 0.875rem;
    color: var(--text-secondary);
  }

  .predictions {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
  }

  .predictions h4 {
    margin: 0 0 0.75rem 0;
    font-size: 1rem;
    color: var(--text-primary);
  }

  .prediction {
    display: grid;
    grid-template-columns: 80px 1fr 40px;
    gap: 0.5rem;
    align-items: center;
    margin-bottom: 0.5rem;
    font-size: 0.875rem;
  }

  .bar {
    height: 8px;
    background: var(--bg-secondary);
    border-radius: 4px;
    overflow: hidden;
  }

  .fill {
    height: 100%;
    background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
    transition: width 0.5s ease;
  }

  .last-updated {
    text-align: center;
    font-size: 0.75rem;
    color: var(--text-secondary);
    margin-top: 1rem;
    padding-top: 0.5rem;
    border-top: 1px solid var(--border-color);
  }

  .retry-btn {
    background: var(--primary-color);
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.2s;
  }

  .retry-btn:hover {
    background: #1d4ed8;
  }

  .error-message {
    color: var(--error-color);
    margin-bottom: 1rem;
  }

  /* Responsive design */
  @media (max-width: 480px) {
    .match-widget {
      padding: 1rem;
    }
    
    .teams-container {
      gap: 0.5rem;
    }
    
    .team-name {
      font-size: 1rem;
    }
    
    .score {
      font-size: 1.5rem;
    }
  }
</style>
