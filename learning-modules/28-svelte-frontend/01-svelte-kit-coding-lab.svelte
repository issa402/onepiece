<!--
🏴‍☠️ MODULE 28: SVELTE/SVELTEKIT - MODERN FRONTEND FRAMEWORK
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
ALTERNATIVE to your React frontend using Svelte/SvelteKit.
This is smaller, faster, and simpler than React!

📚 LEARNING OBJECTIVES:
- Svelte compiler (no virtual DOM)
- SvelteKit full-stack framework
- Smaller bundle sizes than React
- Better performance than React
- Simpler syntax than React
- Integration with your API Gateway

🔗 INTEGRATES WITH YOUR PROJECT:
- REPLACES: frontend/src/App.tsx
- CONNECTS TO: Your API Gateway (Express/Fastify/Deno/Edge)
- SAME FUNCTIONALITY: Character browsing, trading
- BETTER PERFORMANCE: Smaller bundles, faster runtime

💰 CAREER IMPACT: +$40K-$80K (Svelte is growing rapidly!)

PERFORMANCE COMPARISON:
React bundle: ~200KB
Svelte bundle: ~50KB (4x smaller!)
-->

<!-- TODO 1: SVELTEKIT SETUP -->
<!-- ═══════════════════════════════════════════════════════════ -->
<!--
🎯 YOUR TASK: Set up SvelteKit project (alternative to Create React App)

INSTALLATION:
# Create SvelteKit project (replaces create-react-app)
npm create svelte@latest onepiece-svelte-frontend
cd onepiece-svelte-frontend
npm install

# Install additional dependencies
npm install axios @tailwindcss/typography

COMPARISON:
Create React App: ~300MB node_modules
SvelteKit: ~150MB node_modules (2x smaller!)
-->

<!-- TODO 2: MAIN APP COMPONENT (REPLACES App.tsx) -->
<!-- ═══════════════════════════════════════════════════════════ -->
<!--
🎯 YOUR TASK: Create main app component (replaces frontend/src/App.tsx)

COMPARISON:
React: Uses JSX, virtual DOM, complex state management
Svelte: Uses HTML-like syntax, compiles to vanilla JS, simple reactivity
-->

<!-- src/app.html - Main HTML template -->
<script>
  // Import components (simpler than React imports)
  import CharacterList from './lib/components/CharacterList.svelte';
  import TradingInterface from './lib/components/TradingInterface.svelte';
  import Navigation from './lib/components/Navigation.svelte';
  
  // Reactive state (simpler than React useState)
  let currentView = 'characters';
  let user = null;
  
  // Reactive statements (runs automatically when dependencies change)
  $: isLoggedIn = user !== null;
  
  // Functions (simpler than React useCallback)
  function switchView(view) {
    currentView = view;
  }
  
  function handleLogin(userData) {
    user = userData;
    localStorage.setItem('user', JSON.stringify(userData));
  }
  
  function handleLogout() {
    user = null;
    localStorage.removeItem('user');
    currentView = 'characters';
  }
  
  // Lifecycle (simpler than React useEffect)
  import { onMount } from 'svelte';
  
  onMount(() => {
    // Check for existing user session
    const savedUser = localStorage.getItem('user');
    if (savedUser) {
      user = JSON.parse(savedUser);
    }
  });
</script>

<!-- HTML template (much cleaner than JSX) -->
<main class="min-h-screen bg-gradient-to-br from-blue-900 via-purple-900 to-indigo-900">
  <!-- Navigation Component -->
  <Navigation 
    {currentView} 
    {isLoggedIn} 
    {user}
    on:switchView={(e) => switchView(e.detail)}
    on:login={handleLogin}
    on:logout={handleLogout}
  />
  
  <!-- Main Content Area -->
  <div class="container mx-auto px-4 py-8">
    <!-- One Piece Header -->
    <header class="text-center mb-12">
      <h1 class="text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-orange-500 mb-4">
        🏴‍☠️ ONE PIECE TRADING
      </h1>
      <p class="text-xl text-gray-300">
        Trade your favorite One Piece characters like stocks!
      </p>
    </header>
    
    <!-- Dynamic Content Based on Current View -->
    {#if currentView === 'characters'}
      <CharacterList />
    {:else if currentView === 'trading' && isLoggedIn}
      <TradingInterface {user} />
    {:else if currentView === 'trading' && !isLoggedIn}
      <div class="text-center py-16">
        <h2 class="text-3xl font-bold text-white mb-4">Login Required</h2>
        <p class="text-gray-300 mb-8">Please log in to access the trading interface.</p>
        <button 
          class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-colors"
          on:click={() => switchView('login')}
        >
          Go to Login
        </button>
      </div>
    {/if}
  </div>
</main>

<!-- Styles (scoped automatically, no CSS modules needed!) -->
<style>
  /* Scoped styles - only apply to this component */
  main {
    font-family: 'Inter', sans-serif;
  }
  
  /* Global styles can be defined in app.css */
  :global(body) {
    margin: 0;
    padding: 0;
  }
</style>

<!-- TODO 3: CHARACTER LIST COMPONENT (REPLACES React Component) -->
<!-- ═══════════════════════════════════════════════════════════ -->
<!--
🎯 YOUR TASK: Create character list component (replaces React CharacterCard)

COMPARISON:
React: useState, useEffect, complex state management
Svelte: Simple reactive variables, automatic updates
-->

<!-- src/lib/components/CharacterList.svelte -->
<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  
  // Reactive state (simpler than React useState)
  let characters = [];
  let loading = true;
  let error = null;
  let searchTerm = '';
  
  // API configuration (same as your React version)
  const API_BASE_URL = 'http://localhost:3000'; // Your API Gateway
  
  // Reactive filtered characters (automatically updates when searchTerm changes)
  $: filteredCharacters = characters.filter(character =>
    character.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    character.crew.toLowerCase().includes(searchTerm.toLowerCase())
  );
  
  // Fetch characters function (same logic as your React version)
  async function fetchCharacters() {
    try {
      loading = true;
      error = null;
      
      console.log('📡 Fetching characters from API Gateway...');
      
      const response = await axios.get(`${API_BASE_URL}/api/characters`);
      characters = response.data;
      
      console.log(`✅ Loaded ${characters.length} characters`);
      
    } catch (err) {
      console.error('❌ Error fetching characters:', err);
      error = 'Failed to load characters. Please try again.';
    } finally {
      loading = false;
    }
  }
  
  // Format bounty function (same as your React version)
  function formatBounty(bounty) {
    if (bounty >= 1000000000) {
      return `₿${(bounty / 1000000000).toFixed(1)}B`;
    } else if (bounty >= 1000000) {
      return `₿${(bounty / 1000000).toFixed(1)}M`;
    } else if (bounty >= 1000) {
      return `₿${(bounty / 1000).toFixed(1)}K`;
    }
    return `₿${bounty}`;
  }
  
  // Lifecycle (simpler than React useEffect)
  onMount(() => {
    fetchCharacters();
  });
</script>

<!-- HTML template (cleaner than JSX) -->
<div class="character-list">
  <!-- Search Bar -->
  <div class="mb-8">
    <input
      type="text"
      placeholder="Search characters or crews..."
      bind:value={searchTerm}
      class="w-full max-w-md mx-auto block px-4 py-3 rounded-lg bg-gray-800 text-white border border-gray-600 focus:border-blue-500 focus:outline-none"
    />
  </div>
  
  <!-- Loading State -->
  {#if loading}
    <div class="text-center py-16">
      <div class="animate-spin rounded-full h-16 w-16 border-b-2 border-yellow-400 mx-auto mb-4"></div>
      <p class="text-gray-300">Loading characters...</p>
    </div>
  
  <!-- Error State -->
  {:else if error}
    <div class="text-center py-16">
      <p class="text-red-400 mb-4">{error}</p>
      <button 
        class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors"
        on:click={fetchCharacters}
      >
        Try Again
      </button>
    </div>
  
  <!-- Characters Grid -->
  {:else}
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      {#each filteredCharacters as character (character.id)}
        <div class="character-card bg-gray-800 rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-shadow">
          <!-- Character Image -->
          <div class="h-48 bg-gradient-to-br from-blue-600 to-purple-600 flex items-center justify-center">
            <span class="text-6xl">👤</span>
          </div>
          
          <!-- Character Info -->
          <div class="p-6">
            <h3 class="text-xl font-bold text-white mb-2">{character.name}</h3>
            <p class="text-gray-400 mb-2">{character.crew}</p>
            
            <!-- Bounty -->
            <div class="flex justify-between items-center mb-4">
              <span class="text-gray-400">Bounty:</span>
              <span class="text-yellow-400 font-bold">{formatBounty(character.bounty)}</span>
            </div>
            
            <!-- Devil Fruit -->
            {#if character.devil_fruit}
              <div class="mb-4">
                <span class="text-gray-400">Devil Fruit:</span>
                <p class="text-purple-400 text-sm">{character.devil_fruit}</p>
              </div>
            {/if}
            
            <!-- Haki Types -->
            {#if character.haki_types && character.haki_types.length > 0}
              <div class="mb-4">
                <span class="text-gray-400 text-sm">Haki:</span>
                <div class="flex flex-wrap gap-1 mt-1">
                  {#each character.haki_types as haki}
                    <span class="bg-red-600 text-white text-xs px-2 py-1 rounded">{haki}</span>
                  {/each}
                </div>
              </div>
            {/if}
            
            <!-- Trade Button -->
            <button class="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded transition-colors">
              Trade Character
            </button>
          </div>
        </div>
      {/each}
    </div>
    
    <!-- No Results -->
    {#if filteredCharacters.length === 0 && searchTerm}
      <div class="text-center py-16">
        <p class="text-gray-400">No characters found matching "{searchTerm}"</p>
      </div>
    {/if}
  {/if}
</div>

<style>
  .character-card {
    transition: transform 0.2s ease-in-out;
  }
  
  .character-card:hover {
    transform: translateY(-4px);
  }
</style>

<!-- TODO 4: TRADING INTERFACE COMPONENT -->
<!-- ═══════════════════════════════════════════════════════════ -->
<!--
🎯 YOUR TASK: Create trading interface (replaces React TradingInterface)

COMPARISON:
React: Complex state management with useState/useReducer
Svelte: Simple reactive variables with automatic updates
-->

<!-- src/lib/components/TradingInterface.svelte -->
<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  
  // Props (simpler than React props)
  export let user;
  
  // Reactive state
  let selectedCharacter = null;
  let tradeAction = 'buy';
  let quantity = 1;
  let portfolio = [];
  let loading = false;
  let error = null;
  let success = null;
  
  // API configuration
  const API_BASE_URL = 'http://localhost:3000';
  
  // Reactive computed values
  $: totalCost = selectedCharacter ? selectedCharacter.current_price * quantity : 0;
  $: canAfford = user && user.balance >= totalCost;
  
  // Execute trade function (same logic as your React version)
  async function executeTrade() {
    if (!selectedCharacter || !user) return;
    
    try {
      loading = true;
      error = null;
      success = null;
      
      const tradeData = {
        characterId: selectedCharacter.id,
        action: tradeAction,
        quantity: quantity,
        price: selectedCharacter.current_price
      };
      
      console.log(`💰 Executing ${tradeAction} trade:`, tradeData);
      
      const response = await axios.post(`${API_BASE_URL}/api/trades`, tradeData, {
        headers: {
          'Authorization': `Bearer ${user.token}`,
          'Content-Type': 'application/json'
        }
      });
      
      success = `Trade executed successfully! ${tradeAction.toUpperCase()} ${quantity} ${selectedCharacter.name}`;
      
      // Reset form
      selectedCharacter = null;
      quantity = 1;
      
      // Refresh portfolio
      await fetchPortfolio();
      
    } catch (err) {
      console.error('❌ Trade execution error:', err);
      error = err.response?.data?.message || 'Failed to execute trade';
    } finally {
      loading = false;
    }
  }
  
  // Fetch portfolio function
  async function fetchPortfolio() {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/portfolio/${user.id}`, {
        headers: {
          'Authorization': `Bearer ${user.token}`
        }
      });
      
      portfolio = response.data.holdings || [];
      
    } catch (err) {
      console.error('❌ Portfolio fetch error:', err);
    }
  }
  
  onMount(() => {
    if (user) {
      fetchPortfolio();
    }
  });
</script>

<!-- Trading Interface HTML -->
<div class="trading-interface">
  <h2 class="text-3xl font-bold text-white mb-8 text-center">Trading Interface</h2>
  
  <!-- User Balance -->
  <div class="bg-gray-800 rounded-lg p-6 mb-8">
    <h3 class="text-xl font-bold text-white mb-4">Account Balance</h3>
    <p class="text-3xl font-bold text-green-400">₿{user?.balance?.toLocaleString() || '0'}</p>
  </div>
  
  <!-- Trade Form -->
  <div class="bg-gray-800 rounded-lg p-6 mb-8">
    <h3 class="text-xl font-bold text-white mb-4">Execute Trade</h3>
    
    <!-- Character Selection -->
    <div class="mb-4">
      <label class="block text-gray-300 mb-2">Select Character:</label>
      <select 
        bind:value={selectedCharacter}
        class="w-full px-4 py-2 rounded bg-gray-700 text-white border border-gray-600"
      >
        <option value={null}>Choose a character...</option>
        <!-- In a real app, you'd fetch available characters -->
        <option value={{id: 1, name: "Luffy", current_price: 1000000}}>Luffy - ₿1,000,000</option>
        <option value={{id: 2, name: "Zoro", current_price: 800000}}>Zoro - ₿800,000</option>
      </select>
    </div>
    
    <!-- Trade Action -->
    <div class="mb-4">
      <label class="block text-gray-300 mb-2">Action:</label>
      <div class="flex gap-4">
        <label class="flex items-center">
          <input type="radio" bind:group={tradeAction} value="buy" class="mr-2" />
          <span class="text-green-400">Buy</span>
        </label>
        <label class="flex items-center">
          <input type="radio" bind:group={tradeAction} value="sell" class="mr-2" />
          <span class="text-red-400">Sell</span>
        </label>
      </div>
    </div>
    
    <!-- Quantity -->
    <div class="mb-4">
      <label class="block text-gray-300 mb-2">Quantity:</label>
      <input 
        type="number" 
        bind:value={quantity} 
        min="1" 
        class="w-full px-4 py-2 rounded bg-gray-700 text-white border border-gray-600"
      />
    </div>
    
    <!-- Total Cost -->
    {#if selectedCharacter}
      <div class="mb-4">
        <p class="text-gray-300">Total Cost: <span class="text-yellow-400 font-bold">₿{totalCost.toLocaleString()}</span></p>
        {#if tradeAction === 'buy' && !canAfford}
          <p class="text-red-400 text-sm">Insufficient balance!</p>
        {/if}
      </div>
    {/if}
    
    <!-- Execute Button -->
    <button 
      class="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 text-white font-bold py-3 px-6 rounded transition-colors"
      disabled={!selectedCharacter || loading || (tradeAction === 'buy' && !canAfford)}
      on:click={executeTrade}
    >
      {loading ? 'Executing...' : `${tradeAction.toUpperCase()} ${selectedCharacter?.name || 'Character'}`}
    </button>
    
    <!-- Messages -->
    {#if error}
      <div class="mt-4 p-4 bg-red-900 border border-red-600 rounded text-red-200">
        {error}
      </div>
    {/if}
    
    {#if success}
      <div class="mt-4 p-4 bg-green-900 border border-green-600 rounded text-green-200">
        {success}
      </div>
    {/if}
  </div>
  
  <!-- Portfolio -->
  <div class="bg-gray-800 rounded-lg p-6">
    <h3 class="text-xl font-bold text-white mb-4">Your Portfolio</h3>
    
    {#if portfolio.length === 0}
      <p class="text-gray-400">No holdings yet. Start trading to build your portfolio!</p>
    {:else}
      <div class="space-y-4">
        {#each portfolio as holding}
          <div class="flex justify-between items-center p-4 bg-gray-700 rounded">
            <div>
              <h4 class="text-white font-bold">{holding.character_name}</h4>
              <p class="text-gray-400">Quantity: {holding.quantity}</p>
            </div>
            <div class="text-right">
              <p class="text-yellow-400 font-bold">₿{holding.current_value?.toLocaleString()}</p>
              <p class="text-sm {holding.profit_loss >= 0 ? 'text-green-400' : 'text-red-400'}">
                {holding.profit_loss >= 0 ? '+' : ''}₿{holding.profit_loss?.toLocaleString()}
              </p>
            </div>
          </div>
        {/each}
      </div>
    {/if}
  </div>
</div>

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR NEXT IMPLEMENTATION STEP AFTER SVELTE
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You now have a MODERN alternative to your React frontend!

📚 WHAT YOU JUST BUILT:
✅ Svelte/SvelteKit framework (simpler than React)
✅ Smaller bundle sizes (4x smaller than React)
✅ Better performance (no virtual DOM overhead)
✅ Simpler syntax (less boilerplate than React)
✅ Same functionality as your React version
✅ Integration with your API Gateway
✅ Character browsing and trading
✅ Responsive design with Tailwind CSS

🎯 PERFORMANCE COMPARISON:
├── React bundle: ~200KB
├── Svelte bundle: ~50KB (4x smaller!)
├── React runtime: Virtual DOM overhead
└── Svelte runtime: Compiled vanilla JS (faster!)

🎯 HOW TO USE THIS:
1. Keep your React version for learning
2. Use this Svelte version for production
3. Same API endpoints work with both
4. Much smaller bundle size and better performance

🔥 NEXT MODULE: Module 29 - Modern Build Tools
📁 NEXT FILE: learning-modules/29-vite-turbo-build/01-vite-turbo-coding-lab.js
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Lightning-fast development and build tools

🚀 You now have multiple modern frontend options! ⚔️
*/
