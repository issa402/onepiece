# ============================================================================
# 📚 LEARNING GUIDE: Prediction Dashboard Component (components/PredictionDashboard.tsx)
# ============================================================================
#
# 🎯 PURPOSE:
# This is the main dashboard component that displays sports betting consensus data.
# It serves as the central hub where users can:
# - Input game details and request predictions
# - View real-time consensus results from multiple sources
# - See confidence scores, reasoning, and source breakdown
# - Track historical accuracy and performance metrics
# - Interact with AI-powered recommendations
#
# 🔧 TECHNOLOGIES USED:
# - React 18: Modern React with hooks and concurrent features
# - TypeScript: Type safety for props, state, and API responses
# - Next.js: Server-side rendering and API route integration
# - SWR: Data fetching with caching and revalidation
# - Tailwind CSS: Utility-first styling with responsive design
# - Framer Motion: Smooth animations and transitions
# - Recharts: Data visualization for consensus metrics
# - React Hook Form + Zod: Form handling with validation
#
# 📖 IN-DEPTH EXPLANATION:
#
# **Component Architecture:**
# This dashboard follows the "container component" pattern:
# 1. **Data Layer**: SWR hooks for API communication
# 2. **State Layer**: React state + Zustand for global state
# 3. **UI Layer**: Presentational components with Tailwind
# 4. **Logic Layer**: Custom hooks for business logic
#
# **Real-time Updates:**
# - SWR automatically refetches data on focus/reconnect
# - WebSocket integration for live prediction updates
# - Optimistic updates for better user experience
# - Error boundaries for graceful failure handling
#
# **Data Flow:**
# 1. User inputs game details → Form validation with Zod
# 2. API call to Python backend → SWR manages caching
# 3. Backend scrapes sites + AI analysis → Real-time updates
# 4. Dashboard displays results → Charts and visualizations
# 5. User interactions → State updates and new API calls
#
# **Responsive Design Strategy:**
# - Mobile-first approach with Tailwind breakpoints
# - Progressive enhancement for larger screens
# - Touch-friendly interactions for mobile users
# - Accessible design following WCAG guidelines
#
# **Performance Optimizations:**
# - React.memo for expensive components
# - useMemo/useCallback for computed values
# - Code splitting with Next.js dynamic imports
# - Image optimization with next/image
# - Bundle analysis and tree shaking
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 35 (React/Next.js): Lines 200-400 - Component composition patterns
# - Module 35 (React/Next.js): Lines 500-700 - State management with hooks
# - Module 35 (React/Next.js): Lines 800-1000 - Data fetching with SWR
# - Module 35 (React/Next.js): Lines 1200-1400 - Form handling and validation
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Create PredictionDashboard component with TypeScript interfaces
# [ ] Implement game input form with React Hook Form + Zod validation
# [ ] Add SWR hooks for API data fetching
# [ ] Create consensus visualization with Recharts
# [ ] Implement real-time updates with WebSocket or polling
# [ ] Add loading states and error handling
# [ ] Create responsive layout with Tailwind CSS
# [ ] Add animations with Framer Motion
# [ ] Implement accessibility features (ARIA labels, keyboard navigation)
# [ ] Add unit tests with React Testing Library
# [ ] Optimize performance with React.memo and hooks
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - React hooks (useState, useEffect, useMemo, useCallback)
# - TypeScript interfaces and type definitions
# - SWR data fetching patterns and caching strategies
# - Form validation with Zod schemas
# - Responsive design with Tailwind CSS
# - Data visualization with Recharts
# - Animation principles with Framer Motion
# - Accessibility best practices (WCAG guidelines)
# - Testing strategies for React components
# - Performance optimization techniques
#
# 🚀 REAL-WORLD EXAMPLES:
# - DraftKings: Real-time sports betting interface
# - ESPN: Live sports data and predictions
# - Robinhood: Financial dashboard with real-time updates
# - Netflix: Content recommendation interface
#
# 💡 COMPONENT STRUCTURE:
# ```
# PredictionDashboard/
# ├── GameInputForm          # User input for game details
# ├── ConsensusDisplay       # Main prediction results
# ├── SourceBreakdown        # Individual source predictions
# ├── ConfidenceChart        # Visual confidence metrics
# ├── HistoricalAccuracy     # Performance tracking
# └── RecommendationCard     # AI-generated advice
# ```
#
# 🎨 UI/UX DESIGN PRINCIPLES:
# - **Progressive Disclosure**: Show most important info first
# - **Visual Hierarchy**: Use typography and spacing effectively
# - **Feedback**: Immediate response to user actions
# - **Consistency**: Uniform design patterns throughout
# - **Accessibility**: Keyboard navigation and screen reader support
#
# 📱 RESPONSIVE BREAKPOINTS:
# - Mobile (sm): 640px - Single column, touch-optimized
# - Tablet (md): 768px - Two columns, mixed interactions
# - Desktop (lg): 1024px - Multi-column, mouse-optimized
# - Large (xl): 1280px - Full dashboard layout
#
# ⚡ PERFORMANCE CONSIDERATIONS:
# - Lazy load charts and heavy components
# - Debounce user input to reduce API calls
# - Use React.memo for pure components
# - Implement virtual scrolling for large lists
# - Optimize images and assets
#
# 🔍 DEBUGGING TIPS:
# - Use React DevTools for component inspection
# - Monitor SWR cache with SWR DevTools
# - Test responsive design with browser dev tools
# - Use Lighthouse for performance auditing
# - Implement error boundaries for crash reporting
#
# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================
#
# 'use client';
# 
# import React, { useState, useMemo } from 'react';
# import { useForm } from 'react-hook-form';
# import { zodResolver } from '@hookform/resolvers/zod';
# import { z } from 'zod';
# import useSWR from 'swr';
# import { motion, AnimatePresence } from 'framer-motion';
# import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
# import { Calendar, TrendingUp, AlertCircle, CheckCircle } from 'lucide-react';
# import toast from 'react-hot-toast';
# 
# // Type definitions
# interface GameInput {
#   team1: string;
#   team2: string;
#   sport: string;
#   date: string;
# }
# 
# interface PredictionResult {
#   consensus: {
#     predicted_winner: string;
#     confidence: number;
#     consensus_percentage: number;
#     total_sources: number;
#     sources_agreeing: number;
#   };
#   predictions: Array<{
#     source: string;
#     prediction: string;
#     confidence: number;
#     reasoning: string;
#   }>;
#   recommendation: {
#     action: string;
#     team: string;
#     confidence: string;
#     risk_level: string;
#     explanation: string;
#   };
# }
# 
# // Form validation schema
# const gameInputSchema = z.object({
#   team1: z.string().min(2, 'Team name must be at least 2 characters'),
#   team2: z.string().min(2, 'Team name must be at least 2 characters'),
#   sport: z.enum(['NBA', 'NFL', 'MLB', 'NHL', 'Soccer']),
#   date: z.string().min(1, 'Date is required'),
# });
# 
# // API fetcher function
# const fetcher = (url: string) => fetch(url).then(res => res.json());
# 
# export default function PredictionDashboard() {
#   const [gameQuery, setGameQuery] = useState<string | null>(null);
#   
#   // Form setup
#   const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm<GameInput>({
#     resolver: zodResolver(gameInputSchema),
#   });
# 
#   // Data fetching with SWR
#   const { data: prediction, error, isLoading } = useSWR<PredictionResult>(
#     gameQuery ? `/api/predictions?query=${encodeURIComponent(gameQuery)}` : null,
#     fetcher,
#     {
#       refreshInterval: 30000, // Refresh every 30 seconds
#       revalidateOnFocus: true,
#     }
#   );
# 
#   // Form submission handler
#   const onSubmit = async (data: GameInput) => {
#     const query = `${data.team1} vs ${data.team2}`;
#     setGameQuery(query);
#     toast.success('Fetching predictions...');
#   };
# 
#   // Chart data preparation
#   const chartData = useMemo(() => {
#     if (!prediction?.predictions) return [];
#     
#     return prediction.predictions.map(pred => ({
#       source: pred.source,
#       confidence: Math.round(pred.confidence * 100),
#       prediction: pred.prediction,
#     }));
#   }, [prediction]);
# 
#   return (
#     <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
#       <div className="max-w-7xl mx-auto">
#         {/* Header */}
#         <motion.div
#           initial={{ opacity: 0, y: -20 }}
#           animate={{ opacity: 1, y: 0 }}
#           className="text-center mb-8"
#         >
#           <h1 className="text-4xl font-bold text-gray-900 mb-2">
#             🎯 Sports Betting Consensus
#           </h1>
#           <p className="text-xl text-gray-600">
#             AI-powered predictions from multiple expert sources
#           </p>
#         </motion.div>
# 
#         {/* Game Input Form */}
#         <motion.div
#           initial={{ opacity: 0, scale: 0.95 }}
#           animate={{ opacity: 1, scale: 1 }}
#           className="bg-white rounded-xl shadow-lg p-6 mb-8"
#         >
#           <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-1 md:grid-cols-5 gap-4">
#             <div>
#               <label className="block text-sm font-medium text-gray-700 mb-1">Team 1</label>
#               <input
#                 {...register('team1')}
#                 className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
#                 placeholder="Lakers"
#               />
#               {errors.team1 && <p className="text-red-500 text-sm mt-1">{errors.team1.message}</p>}
#             </div>
#             
#             <div>
#               <label className="block text-sm font-medium text-gray-700 mb-1">Team 2</label>
#               <input
#                 {...register('team2')}
#                 className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
#                 placeholder="Warriors"
#               />
#               {errors.team2 && <p className="text-red-500 text-sm mt-1">{errors.team2.message}</p>}
#             </div>
#             
#             <div>
#               <label className="block text-sm font-medium text-gray-700 mb-1">Sport</label>
#               <select
#                 {...register('sport')}
#                 className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
#               >
#                 <option value="">Select Sport</option>
#                 <option value="NBA">NBA</option>
#                 <option value="NFL">NFL</option>
#                 <option value="MLB">MLB</option>
#                 <option value="NHL">NHL</option>
#                 <option value="Soccer">Soccer</option>
#               </select>
#               {errors.sport && <p className="text-red-500 text-sm mt-1">{errors.sport.message}</p>}
#             </div>
#             
#             <div>
#               <label className="block text-sm font-medium text-gray-700 mb-1">Date</label>
#               <input
#                 {...register('date')}
#                 type="date"
#                 className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
#               />
#               {errors.date && <p className="text-red-500 text-sm mt-1">{errors.date.message}</p>}
#             </div>
#             
#             <div className="flex items-end">
#               <button
#                 type="submit"
#                 disabled={isSubmitting || isLoading}
#                 className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
#               >
#                 {isSubmitting || isLoading ? 'Analyzing...' : 'Get Predictions'}
#               </button>
#             </div>
#           </form>
#         </motion.div>
# 
#         {/* Results Display */}
#         <AnimatePresence>
#           {prediction && (
#             <motion.div
#               initial={{ opacity: 0, y: 20 }}
#               animate={{ opacity: 1, y: 0 }}
#               exit={{ opacity: 0, y: -20 }}
#               className="grid grid-cols-1 lg:grid-cols-2 gap-8"
#             >
#               {/* Consensus Card */}
#               <div className="bg-white rounded-xl shadow-lg p-6">
#                 <h2 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
#                   <TrendingUp className="mr-2 text-green-500" />
#                   Consensus Prediction
#                 </h2>
#                 
#                 <div className="text-center mb-6">
#                   <div className="text-4xl font-bold text-blue-600 mb-2">
#                     {prediction.consensus.predicted_winner}
#                   </div>
#                   <div className="text-lg text-gray-600">
#                     {prediction.consensus.consensus_percentage}% consensus
#                   </div>
#                   <div className="text-sm text-gray-500">
#                     {prediction.consensus.sources_agreeing} of {prediction.consensus.total_sources} sources agree
#                   </div>
#                 </div>
#                 
#                 <div className="bg-gray-50 rounded-lg p-4">
#                   <h3 className="font-semibold text-gray-900 mb-2">Recommendation</h3>
#                   <div className="flex items-center mb-2">
#                     {prediction.recommendation.action === 'bet' ? (
#                       <CheckCircle className="text-green-500 mr-2" size={20} />
#                     ) : (
#                       <AlertCircle className="text-yellow-500 mr-2" size={20} />
#                     )}
#                     <span className="font-medium capitalize">
#                       {prediction.recommendation.action} - {prediction.recommendation.confidence} confidence
#                     </span>
#                   </div>
#                   <p className="text-gray-700 text-sm">
#                     {prediction.recommendation.explanation}
#                   </p>
#                 </div>
#               </div>
# 
#               {/* Confidence Chart */}
#               <div className="bg-white rounded-xl shadow-lg p-6">
#                 <h2 className="text-2xl font-bold text-gray-900 mb-4">
#                   Source Confidence Levels
#                 </h2>
#                 
#                 <ResponsiveContainer width="100%" height={300}>
#                   <BarChart data={chartData}>
#                     <CartesianGrid strokeDasharray="3 3" />
#                     <XAxis dataKey="source" />
#                     <YAxis />
#                     <Tooltip />
#                     <Bar dataKey="confidence" fill="#3B82F6" />
#                   </BarChart>
#                 </ResponsiveContainer>
#               </div>
#             </motion.div>
#           )}
#         </AnimatePresence>
# 
#         {/* Loading State */}
#         {isLoading && (
#           <motion.div
#             initial={{ opacity: 0 }}
#             animate={{ opacity: 1 }}
#             className="text-center py-12"
#           >
#             <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
#             <p className="text-gray-600">Analyzing predictions from multiple sources...</p>
#           </motion.div>
#         )}
# 
#         {/* Error State */}
#         {error && (
#           <motion.div
#             initial={{ opacity: 0 }}
#             animate={{ opacity: 1 }}
#             className="bg-red-50 border border-red-200 rounded-lg p-4 text-center"
#           >
#             <AlertCircle className="text-red-500 mx-auto mb-2" size={24} />
#             <p className="text-red-700">Failed to fetch predictions. Please try again.</p>
#           </motion.div>
#         )}
#       </div>
#     </div>
#   );
# }
#
# ============================================================================
