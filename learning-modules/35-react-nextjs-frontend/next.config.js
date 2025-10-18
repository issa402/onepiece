/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable experimental features
  experimental: {
    // Enable Server Components (default in App Router)
    serverComponentsExternalPackages: ['@prisma/client'],
  },

  // Image optimization configuration
  images: {
    domains: [
      'localhost',
      'example.com',
      'images.unsplash.com',
      'cdn.onepiece.com'
    ],
    formats: ['image/webp', 'image/avif'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },

  // Compiler options
  compiler: {
    // Remove console.log in production
    removeConsole: process.env.NODE_ENV === 'production',
  },

  // Headers for security and performance
  async headers() {
    return [
      {
        source: '/(.*)',
        headers: [
          {
            key: 'X-Frame-Options',
            value: 'DENY',
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff',
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin',
          },
        ],
      },
    ];
  },

  // Redirects
  async redirects() {
    return [
      {
        source: '/home',
        destination: '/',
        permanent: true,
      },
    ];
  },

  // Rewrites for API proxying
  async rewrites() {
    return [
      {
        source: '/api/external/:path*',
        destination: 'https://api.onepiece.com/:path*',
      },
    ];
  },

  // Environment variables
  env: {
    CUSTOM_KEY: process.env.CUSTOM_KEY,
  },

  // Bundle analyzer (uncomment to analyze bundle size)
  // webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
  //   if (process.env.ANALYZE) {
  //     const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
  //     config.plugins.push(
  //       new BundleAnalyzerPlugin({
  //         analyzerMode: 'server',
  //         analyzerPort: isServer ? 8888 : 8889,
  //         openAnalyzer: true,
  //       })
  //     );
  //   }
  //   return config;
  // },

  // TypeScript configuration
  typescript: {
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    ignoreBuildErrors: false,
  },

  // ESLint configuration
  eslint: {
    // Warning: This allows production builds to successfully complete even if
    // your project has ESLint errors.
    ignoreDuringBuilds: false,
  },

  // Output configuration
  output: 'standalone',

  // Trailing slash configuration
  trailingSlash: false,

  // React strict mode
  reactStrictMode: true,

  // SWC minification
  swcMinify: true,

  // Powered by header
  poweredByHeader: false,
};

module.exports = nextConfig;
