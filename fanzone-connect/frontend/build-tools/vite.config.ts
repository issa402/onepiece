/**
 * 🏆 FANZONE CONNECT - VITE BUILD CONFIGURATION
 * Learning Module: 29 (Vite/Turbo Build)
 * World Cup 2026 Fan Platform - Ultra-Fast Build System with Advanced Optimization
 */

import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react-swc';
import { resolve } from 'path';
import { visualizer } from 'rollup-plugin-visualizer';
import { compression } from 'vite-plugin-compression';
import { createHtmlPlugin } from 'vite-plugin-html';
import { VitePWA } from 'vite-plugin-pwa';
import { splitVendorChunkPlugin } from 'vite';

// =====================================================
// MODULE 29: VITE/TURBO BUILD - ADVANCED CONFIGURATION
// =====================================================

export default defineConfig(({ command, mode }) => {
  // Load environment variables
  const env = loadEnv(mode, process.cwd(), '');
  
  const isProduction = mode === 'production';
  const isDevelopment = mode === 'development';
  
  console.log(`🏆 Building FANZONE CONNECT for World Cup 2026`);
  console.log(`⚡ Mode: ${mode}`);
  console.log(`🚀 Command: ${command}`);
  
  return {
    // Base configuration
    base: env.VITE_BASE_URL || '/',
    
    // Development server configuration
    server: {
      host: '0.0.0.0',
      port: parseInt(env.VITE_PORT || '3000'),
      strictPort: true,
      open: false,
      cors: true,
      
      // Hot Module Replacement
      hmr: {
        overlay: true,
        clientPort: parseInt(env.VITE_HMR_PORT || '3000'),
      },
      
      // Proxy configuration for API calls
      proxy: {
        '/api': {
          target: env.VITE_API_URL || 'http://localhost:8000',
          changeOrigin: true,
          secure: false,
          ws: true, // Enable WebSocket proxying
        },
        '/ws': {
          target: env.VITE_WS_URL || 'ws://localhost:8000',
          ws: true,
          changeOrigin: true,
        },
      },
    },
    
    // Preview server (for production builds)
    preview: {
      host: '0.0.0.0',
      port: parseInt(env.VITE_PREVIEW_PORT || '4173'),
      strictPort: true,
      open: false,
    },
    
    // Path resolution
    resolve: {
      alias: {
        '@': resolve(__dirname, 'src'),
        '@components': resolve(__dirname, 'src/components'),
        '@pages': resolve(__dirname, 'src/pages'),
        '@hooks': resolve(__dirname, 'src/hooks'),
        '@utils': resolve(__dirname, 'src/utils'),
        '@types': resolve(__dirname, 'src/types'),
        '@assets': resolve(__dirname, 'src/assets'),
        '@styles': resolve(__dirname, 'src/styles'),
        '@api': resolve(__dirname, 'src/api'),
        '@store': resolve(__dirname, 'src/store'),
      },
    },
    
    // Plugin configuration
    plugins: [
      // React with SWC for ultra-fast compilation
      react({
        // Enable React Fast Refresh
        fastRefresh: true,
        
        // SWC configuration for optimal performance
        jsxImportSource: '@emotion/react',
        plugins: [
          // Emotion plugin for CSS-in-JS
          ['@swc/plugin-emotion', {}],
        ],
      }),
      
      // HTML template processing
      createHtmlPlugin({
        minify: isProduction,
        inject: {
          data: {
            title: 'FANZONE CONNECT - World Cup 2026',
            description: 'The ultimate fan experience platform for FIFA World Cup 2026',
            keywords: 'World Cup 2026, FIFA, Football, Soccer, Fan Zone, USA, Canada, Mexico',
            author: 'FANZONE CONNECT Team',
            viewport: 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no',
            themeColor: '#1e40af',
            appleTouchIcon: '/icons/apple-touch-icon.png',
            favicon: '/favicon.ico',
            manifest: '/manifest.json',
          },
        },
      }),
      
      // Progressive Web App
      VitePWA({
        registerType: 'autoUpdate',
        workbox: {
          globPatterns: ['**/*.{js,css,html,ico,png,svg,woff2}'],
          runtimeCaching: [
            {
              urlPattern: /^https:\/\/api\.fanzoneconnect\.com\/.*/i,
              handler: 'NetworkFirst',
              options: {
                cacheName: 'api-cache',
                expiration: {
                  maxEntries: 100,
                  maxAgeSeconds: 60 * 60 * 24, // 24 hours
                },
              },
            },
            {
              urlPattern: /^https:\/\/cdn\.fanzoneconnect\.com\/.*/i,
              handler: 'CacheFirst',
              options: {
                cacheName: 'static-resources',
                expiration: {
                  maxEntries: 200,
                  maxAgeSeconds: 60 * 60 * 24 * 30, // 30 days
                },
              },
            },
          ],
        },
        manifest: {
          name: 'FANZONE CONNECT - World Cup 2026',
          short_name: 'FANZONE',
          description: 'The ultimate fan experience platform for FIFA World Cup 2026',
          theme_color: '#1e40af',
          background_color: '#ffffff',
          display: 'standalone',
          orientation: 'portrait-primary',
          scope: '/',
          start_url: '/',
          icons: [
            {
              src: '/icons/icon-192x192.png',
              sizes: '192x192',
              type: 'image/png',
            },
            {
              src: '/icons/icon-512x512.png',
              sizes: '512x512',
              type: 'image/png',
            },
          ],
        },
      }),
      
      // Bundle analyzer (production only)
      isProduction && visualizer({
        filename: 'dist/stats.html',
        open: false,
        gzipSize: true,
        brotliSize: true,
      }),
      
      // Compression (production only)
      isProduction && compression({
        algorithm: 'gzip',
        ext: '.gz',
      }),
      
      isProduction && compression({
        algorithm: 'brotliCompress',
        ext: '.br',
      }),
      
      // Vendor chunk splitting for better caching
      splitVendorChunkPlugin(),
    ].filter(Boolean),
    
    // CSS configuration
    css: {
      // CSS modules
      modules: {
        localsConvention: 'camelCaseOnly',
        generateScopedName: isProduction 
          ? '[hash:base64:8]' 
          : '[name]__[local]__[hash:base64:5]',
      },
      
      // PostCSS configuration
      postcss: {
        plugins: [
          require('tailwindcss'),
          require('autoprefixer'),
          ...(isProduction ? [require('cssnano')] : []),
        ],
      },
      
      // CSS preprocessing
      preprocessorOptions: {
        scss: {
          additionalData: `
            @import "@styles/variables.scss";
            @import "@styles/mixins.scss";
          `,
        },
      },
    },
    
    // Build configuration
    build: {
      // Output directory
      outDir: 'dist',
      assetsDir: 'assets',
      
      // Source maps
      sourcemap: isDevelopment || env.VITE_SOURCEMAP === 'true',
      
      // Minification
      minify: isProduction ? 'esbuild' : false,
      
      // Target browsers
      target: ['es2020', 'edge88', 'firefox78', 'chrome87', 'safari13.1'],
      
      // Chunk size warnings
      chunkSizeWarningLimit: 1000,
      
      // Rollup options
      rollupOptions: {
        input: {
          main: resolve(__dirname, 'index.html'),
        },
        
        output: {
          // Manual chunk splitting for optimal caching
          manualChunks: {
            // Vendor chunks
            'react-vendor': ['react', 'react-dom'],
            'router-vendor': ['react-router-dom'],
            'ui-vendor': ['@headlessui/react', '@heroicons/react'],
            'animation-vendor': ['framer-motion'],
            'chart-vendor': ['recharts', 'd3'],
            'date-vendor': ['date-fns'],
            'form-vendor': ['react-hook-form', 'yup'],
            
            // Feature chunks
            'match-features': [
              './src/components/MatchCard',
              './src/components/MatchDetails',
              './src/pages/MatchPage',
            ],
            'fan-features': [
              './src/components/FanProfile',
              './src/components/FanEvents',
              './src/pages/FanZone',
            ],
            'admin-features': [
              './src/pages/AdminDashboard',
              './src/components/AdminPanel',
            ],
          },
          
          // Asset naming
          assetFileNames: (assetInfo) => {
            const info = assetInfo.name.split('.');
            const ext = info[info.length - 1];
            
            if (/\.(png|jpe?g|svg|gif|tiff|bmp|ico)$/i.test(assetInfo.name)) {
              return `images/[name]-[hash][extname]`;
            }
            
            if (/\.(woff2?|eot|ttf|otf)$/i.test(assetInfo.name)) {
              return `fonts/[name]-[hash][extname]`;
            }
            
            return `assets/[name]-[hash][extname]`;
          },
          
          chunkFileNames: 'js/[name]-[hash].js',
          entryFileNames: 'js/[name]-[hash].js',
        },
        
        // External dependencies (for library builds)
        external: isDevelopment ? [] : [],
      },
      
      // ESBuild options
      esbuild: {
        // Remove console logs in production
        drop: isProduction ? ['console', 'debugger'] : [],
        
        // Legal comments
        legalComments: 'none',
      },
      
      // Terser options (if using terser instead of esbuild)
      terserOptions: {
        compress: {
          drop_console: isProduction,
          drop_debugger: isProduction,
        },
      },
    },
    
    // Optimization configuration
    optimizeDeps: {
      // Pre-bundle dependencies
      include: [
        'react',
        'react-dom',
        'react-router-dom',
        '@headlessui/react',
        '@heroicons/react/24/outline',
        '@heroicons/react/24/solid',
        'framer-motion',
        'recharts',
        'date-fns',
        'react-hook-form',
        'yup',
      ],
      
      // Exclude from pre-bundling
      exclude: [
        // Large libraries that should be loaded on demand
        'three',
        '@tensorflow/tfjs',
      ],
      
      // ESBuild options for dependency optimization
      esbuildOptions: {
        target: 'es2020',
      },
    },
    
    // Environment variables
    define: {
      __APP_VERSION__: JSON.stringify(process.env.npm_package_version || '1.0.0'),
      __BUILD_TIME__: JSON.stringify(new Date().toISOString()),
      __WORLD_CUP_YEAR__: JSON.stringify('2026'),
    },
    
    // Worker configuration
    worker: {
      format: 'es',
      plugins: [
        // Worker-specific plugins
      ],
    },
    
    // Experimental features
    experimental: {
      // Enable build time imports
      buildAdvancedBaseOptions: {},
    },
  };
});

// Export additional configuration for tools
export const buildConfig = {
  // Bundle analysis
  analyze: process.env.ANALYZE === 'true',
  
  // Performance budgets
  budgets: {
    maximumError: 2000, // 2MB
    maximumWarning: 1500, // 1.5MB
  },
  
  // World Cup 2026 specific optimizations
  worldCup2026: {
    // Optimize for match day traffic spikes
    chunkStrategy: 'aggressive',
    
    // Preload critical World Cup resources
    preloadResources: [
      '/api/matches/live',
      '/api/teams/favorites',
      '/api/events/nearby',
    ],
    
    // Service worker caching strategy
    cachingStrategy: 'network-first-with-fallback',
  },
};
