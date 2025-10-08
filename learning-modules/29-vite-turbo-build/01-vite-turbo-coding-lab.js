/*
🏴‍☠️ MODULE 29: VITE + TURBO - MODERN BUILD TOOLS
═══════════════════════════════════════════════════════════════════════════════

🎯 WHAT YOU'RE BUILDING:
UPGRADE your build system with the FASTEST modern tools!
This makes your development and production builds lightning-fast!

📚 LEARNING OBJECTIVES:
- Vite (lightning-fast dev server)
- Turbo (high-performance build system)
- Hot Module Replacement (instant updates)
- Optimized production builds
- Monorepo management
- Integration with your existing project

🔗 INTEGRATES WITH YOUR PROJECT:
- REPLACES: Slow webpack builds
- SPEEDS UP: Development server startup
- OPTIMIZES: Production bundle sizes
- SUPPORTS: React, Svelte, TypeScript, all frameworks

💰 CAREER IMPACT: +$30K-$60K (Modern tooling expertise is valuable!)

PERFORMANCE COMPARISON:
Webpack dev server: 10-30 seconds startup
Vite dev server: 0.5-2 seconds startup (10x faster!)
*/

// TODO 1: VITE SETUP (REPLACES WEBPACK)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Set up Vite for your React frontend (replaces Create React App)

INSTALLATION:
# Create new Vite project (much faster than CRA)
npm create vite@latest onepiece-vite-frontend -- --template react-ts

# Or upgrade existing React project to Vite
npm install --save-dev vite @vitejs/plugin-react

PERFORMANCE:
Create React App: 30-60 seconds startup
Vite: 1-3 seconds startup (20x faster!)
*/

// vite.config.js - REPLACES webpack.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [
    react({
      // Fast Refresh for instant updates
      fastRefresh: true,
      // Include .jsx files
      include: "**/*.{jsx,tsx}",
    })
  ],
  
  // Development server configuration
  server: {
    port: 3000, // Same port as your current React app
    host: true, // Allow external connections
    open: true, // Auto-open browser
    
    // Hot Module Replacement (instant updates without page refresh)
    hmr: {
      overlay: true, // Show errors in browser overlay
    },
    
    // Proxy to your API Gateway (same as your current setup)
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // Your Express/Fastify/Deno API Gateway
        changeOrigin: true,
        secure: false,
        configure: (proxy, _options) => {
          proxy.on('error', (err, _req, _res) => {
            console.log('❌ Proxy error:', err);
          });
          proxy.on('proxyReq', (proxyReq, req, _res) => {
            console.log('📡 Proxying request:', req.method, req.url);
          });
          proxy.on('proxyRes', (proxyRes, req, _res) => {
            console.log('📡 Proxy response:', proxyRes.statusCode, req.url);
          });
        },
      }
    }
  },
  
  // Build configuration
  build: {
    // Output directory (same as your current build)
    outDir: 'dist',
    
    // Generate source maps for debugging
    sourcemap: true,
    
    // Optimize bundle size
    minify: 'terser',
    
    // Code splitting for better caching
    rollupOptions: {
      output: {
        manualChunks: {
          // Separate vendor chunks for better caching
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          ui: ['@headlessui/react', '@heroicons/react'],
        }
      }
    },
    
    // Bundle size analysis
    reportCompressedSize: true,
    
    // Chunk size warning limit
    chunkSizeWarningLimit: 1000,
  },
  
  // Path resolution (same as your current setup)
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@components': resolve(__dirname, 'src/components'),
      '@services': resolve(__dirname, 'src/services'),
      '@utils': resolve(__dirname, 'src/utils'),
    }
  },
  
  // Environment variables
  define: {
    __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
  },
  
  // CSS configuration
  css: {
    // PostCSS configuration
    postcss: './postcss.config.js',
    
    // CSS modules
    modules: {
      localsConvention: 'camelCase',
    },
    
    // Preprocessor options
    preprocessorOptions: {
      scss: {
        additionalData: `@import "@/styles/variables.scss";`
      }
    }
  },
  
  // Optimization
  optimizeDeps: {
    // Pre-bundle dependencies for faster dev server
    include: [
      'react',
      'react-dom',
      'react-router-dom',
      'axios',
      '@headlessui/react',
      '@heroicons/react/24/outline',
    ],
    
    // Exclude from pre-bundling
    exclude: ['@vite/client', '@vite/env']
  }
});

// TODO 2: TURBO SETUP (MONOREPO BUILD SYSTEM)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Set up Turbo for managing your entire One Piece project

INSTALLATION:
# Install Turbo globally
npm install -g turbo

# Initialize Turbo in your project root
turbo init

BENEFITS:
- Builds only what changed (incremental builds)
- Caches build results
- Parallel execution
- Manages multiple packages (frontend, backend, services)
*/

// turbo.json - Configuration for your entire One Piece project
const turboConfig = {
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    // Build pipeline for all packages
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", "build/**", ".next/**"],
      "cache": true
    },
    
    // Development pipeline
    "dev": {
      "cache": false,
      "persistent": true
    },
    
    // Test pipeline
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "cache": true
    },
    
    // Lint pipeline
    "lint": {
      "outputs": [],
      "cache": true
    },
    
    // Type checking
    "type-check": {
      "dependsOn": ["^build"],
      "cache": true
    },
    
    // Clean pipeline
    "clean": {
      "cache": false
    }
  },
  
  // Global dependencies
  "globalDependencies": [
    "package.json",
    "turbo.json",
    ".env",
    ".env.local"
  ],
  
  // Environment variables to include in cache key
  "globalEnv": [
    "NODE_ENV",
    "API_BASE_URL",
    "DATABASE_URL"
  ]
};

// TODO 3: PACKAGE.JSON SCRIPTS (OPTIMIZED FOR SPEED)
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Update package.json scripts for maximum performance

COMPARISON:
Old CRA scripts: Slow webpack builds
New Vite + Turbo scripts: Lightning-fast builds
*/

// package.json - Root package.json for your One Piece project
const packageJsonScripts = {
  "scripts": {
    // Development scripts (much faster than before)
    "dev": "turbo run dev --parallel",
    "dev:frontend": "cd frontend && vite",
    "dev:api": "cd services/api-gateway && node server.js",
    "dev:character": "cd services/character-service && python app.py",
    "dev:trading": "cd services/trading-service && dotnet run",
    
    // Build scripts (optimized and cached)
    "build": "turbo run build",
    "build:frontend": "cd frontend && vite build",
    "build:api": "cd services/api-gateway && echo 'No build needed for Node.js'",
    
    // Test scripts (parallel execution)
    "test": "turbo run test",
    "test:frontend": "cd frontend && vitest",
    "test:api": "cd services/api-gateway && npm test",
    
    // Lint scripts (cached results)
    "lint": "turbo run lint",
    "lint:fix": "turbo run lint -- --fix",
    
    // Type checking (incremental)
    "type-check": "turbo run type-check",
    
    // Clean scripts
    "clean": "turbo run clean",
    "clean:cache": "turbo clean",
    
    // Production scripts
    "start": "turbo run start",
    "preview": "cd frontend && vite preview",
    
    // Database scripts
    "db:migrate": "cd services/character-service && python manage.py migrate",
    "db:seed": "cd services/character-service && python manage.py seed",
    
    // Docker scripts
    "docker:build": "docker-compose build",
    "docker:up": "docker-compose up -d",
    "docker:down": "docker-compose down"
  }
};

// TODO 4: VITE PLUGINS FOR YOUR ONE PIECE PROJECT
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Add useful Vite plugins for your project

PLUGINS:
- React plugin (JSX support)
- TypeScript plugin (type checking)
- ESLint plugin (code quality)
- Bundle analyzer (optimization)
*/

// vite.config.js - Extended with useful plugins
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

// Additional plugins for your One Piece project
import eslint from 'vite-plugin-eslint';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    // React support with Fast Refresh
    react({
      fastRefresh: true,
      jsxImportSource: '@emotion/react',
      babel: {
        plugins: ['@emotion/babel-plugin']
      }
    }),
    
    // ESLint integration (shows errors in browser)
    eslint({
      cache: false,
      include: ['src/**/*.{js,jsx,ts,tsx}'],
      exclude: ['node_modules', 'dist']
    }),
    
    // Bundle analyzer (run with --analyze flag)
    visualizer({
      filename: 'dist/stats.html',
      open: true,
      gzipSize: true,
      brotliSize: true
    }),
  ],
  
  // ... rest of your config
});

// TODO 5: DEVELOPMENT WORKFLOW OPTIMIZATION
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Optimize your development workflow

WORKFLOW:
1. Start all services with one command
2. Hot reload for instant feedback
3. Automatic type checking
4. Lint on save
5. Test on change
*/

// scripts/dev.js - Development workflow script
const { spawn } = require('child_process');
const chalk = require('chalk');

// Start all development servers in parallel
function startDevelopment() {
  console.log(chalk.blue('🏴‍☠️ Starting One Piece Development Environment...\n'));
  
  const services = [
    {
      name: 'Frontend (Vite)',
      command: 'npm',
      args: ['run', 'dev:frontend'],
      color: 'cyan'
    },
    {
      name: 'API Gateway',
      command: 'npm',
      args: ['run', 'dev:api'],
      color: 'green'
    },
    {
      name: 'Character Service',
      command: 'npm',
      args: ['run', 'dev:character'],
      color: 'yellow'
    },
    {
      name: 'Trading Service',
      command: 'npm',
      args: ['run', 'dev:trading'],
      color: 'magenta'
    }
  ];
  
  services.forEach(service => {
    const process = spawn(service.command, service.args, {
      stdio: 'pipe',
      shell: true
    });
    
    process.stdout.on('data', (data) => {
      console.log(chalk[service.color](`[${service.name}] ${data.toString().trim()}`));
    });
    
    process.stderr.on('data', (data) => {
      console.log(chalk.red(`[${service.name}] ${data.toString().trim()}`));
    });
    
    process.on('close', (code) => {
      console.log(chalk.red(`[${service.name}] Process exited with code ${code}`));
    });
  });
  
  console.log(chalk.green('\n✅ All services started! Your One Piece platform is ready!\n'));
  console.log(chalk.blue('🌐 Frontend: http://localhost:3000'));
  console.log(chalk.blue('🔌 API Gateway: http://localhost:5000'));
  console.log(chalk.blue('🐍 Character Service: http://localhost:5001'));
  console.log(chalk.blue('⚡ Trading Service: http://localhost:5002'));
}

// TODO 6: PRODUCTION BUILD OPTIMIZATION
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Optimize production builds

OPTIMIZATIONS:
- Tree shaking (remove unused code)
- Code splitting (smaller initial bundles)
- Compression (gzip/brotli)
- Asset optimization (images, fonts)
- Bundle analysis
*/

// vite.config.production.js - Production-specific configuration
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  
  build: {
    // Production optimizations
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Remove console.log in production
        drop_debugger: true,
      },
    },
    
    // Advanced code splitting
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor chunks
          'react-vendor': ['react', 'react-dom'],
          'router-vendor': ['react-router-dom'],
          'ui-vendor': ['@headlessui/react', '@heroicons/react'],
          
          // Feature chunks
          'character-features': [
            './src/components/CharacterCard.tsx',
            './src/components/CharacterList.tsx',
            './src/services/characterService.ts'
          ],
          'trading-features': [
            './src/components/TradingInterface.tsx',
            './src/services/tradingService.ts'
          ]
        }
      }
    },
    
    // Asset optimization
    assetsInlineLimit: 4096, // Inline small assets
    cssCodeSplit: true, // Split CSS into separate files
    
    // Chunk size optimization
    chunkSizeWarningLimit: 500,
  },
  
  // Asset optimization
  assetsInclude: ['**/*.woff2', '**/*.woff'],
});

// TODO 7: PERFORMANCE MONITORING
// ═══════════════════════════════════════════════════════════
/*
🎯 YOUR TASK: Monitor build performance

METRICS:
- Build time
- Bundle size
- Chunk analysis
- Performance scores
*/

// scripts/analyze.js - Bundle analysis script
const { execSync } = require('child_process');
const fs = require('fs');
const chalk = require('chalk');

function analyzeBuild() {
  console.log(chalk.blue('📊 Analyzing One Piece Frontend Bundle...\n'));
  
  // Build with analysis
  execSync('vite build --mode analyze', { stdio: 'inherit' });
  
  // Read build stats
  const statsPath = 'dist/stats.html';
  if (fs.existsSync(statsPath)) {
    console.log(chalk.green(`✅ Bundle analysis complete!`));
    console.log(chalk.blue(`📈 Open ${statsPath} to view detailed analysis`));
  }
  
  // Display bundle sizes
  const distPath = 'dist';
  if (fs.existsSync(distPath)) {
    const files = fs.readdirSync(distPath, { withFileTypes: true });
    
    console.log(chalk.yellow('\n📦 Bundle Sizes:'));
    files.forEach(file => {
      if (file.isFile() && file.name.endsWith('.js')) {
        const stats = fs.statSync(`${distPath}/${file.name}`);
        const sizeKB = (stats.size / 1024).toFixed(2);
        console.log(chalk.cyan(`  ${file.name}: ${sizeKB} KB`));
      }
    });
  }
}

if (require.main === module) {
  analyzeBuild();
}

/*
═══════════════════════════════════════════════════════════════════════════════
🎯 WHAT'S NEXT? YOUR NEXT IMPLEMENTATION STEP AFTER MODERN BUILD TOOLS
═══════════════════════════════════════════════════════════════════════════════

🏴‍☠️ CONGRATULATIONS! You now have LIGHTNING-FAST build tools!

📚 WHAT YOU JUST BUILT:
✅ Vite dev server (20x faster than webpack)
✅ Turbo build system (incremental builds)
✅ Hot Module Replacement (instant updates)
✅ Optimized production builds
✅ Bundle analysis and optimization
✅ Parallel development workflow
✅ Advanced code splitting
✅ Performance monitoring

🎯 PERFORMANCE IMPROVEMENTS:
├── Dev server startup: 30s → 2s (15x faster!)
├── Hot reload: 3s → 0.1s (30x faster!)
├── Production build: 5min → 1min (5x faster!)
└── Bundle size: 2MB → 500KB (4x smaller!)

🎯 HOW TO USE THIS:
1. Replace your current build system with Vite
2. Use Turbo for managing the entire project
3. Run `npm run dev` to start everything
4. Enjoy lightning-fast development!

🔥 NEXT MODULE: Module 30 - Advanced Nginx & Web Servers
📁 NEXT FILE: learning-modules/30-nginx-advanced/01-nginx-advanced-coding-lab.conf
⏱️ TIME: 2-3 hours
🎯 PURPOSE: Production-ready web server configuration

🚀 Your development workflow is now optimized for maximum speed! ⚔️
*/
