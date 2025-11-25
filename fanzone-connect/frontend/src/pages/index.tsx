/**
 * 🏆 FANZONE CONNECT - MAIN HOMEPAGE
 * Learning Modules: 17 (Next.js Fullstack), 29 (Vite/Turbo Build), 39 (React/TypeScript Mastery)
 * World Cup 2026 Fan Platform - Next.js Homepage with Server-Side Rendering
 */

import React, { useState, useEffect } from 'react';
import { GetServerSideProps, NextPage } from 'next';
import Head from 'next/head';
import Image from 'next/image';
import Link from 'next/link';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Calendar, 
  MapPin, 
  Users, 
  Trophy, 
  Globe, 
  Zap,
  ArrowRight,
  Play,
  Star
} from 'lucide-react';

// TypeScript interfaces for World Cup data
interface Match {
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
  };
  dateTime: string;
  status: 'scheduled' | 'live' | 'finished';
  phase: string;
}

interface HomePageProps {
  featuredMatches: Match[];
  totalFans: number;
  liveEvents: number;
  countriesCount: number;
}

const HomePage: NextPage<HomePageProps> = ({
  featuredMatches,
  totalFans,
  liveEvents,
  countriesCount
}) => {
  const [currentMatchIndex, setCurrentMatchIndex] = useState(0);
  const [isVideoPlaying, setIsVideoPlaying] = useState(false);

  // Auto-rotate featured matches
  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentMatchIndex((prev) => 
        (prev + 1) % featuredMatches.length
      );
    }, 5000);

    return () => clearInterval(interval);
  }, [featuredMatches.length]);

  const stats = [
    {
      icon: Users,
      value: totalFans.toLocaleString(),
      label: "Registered Fans",
      color: "text-blue-600"
    },
    {
      icon: Zap,
      value: liveEvents.toString(),
      label: "Live Events",
      color: "text-red-600"
    },
    {
      icon: Globe,
      value: countriesCount.toString(),
      label: "Countries",
      color: "text-green-600"
    },
    {
      icon: Trophy,
      value: "2026",
      label: "World Cup",
      color: "text-yellow-600"
    }
  ];

  return (
    <>
      <Head>
        <title>FANZONE CONNECT - World Cup 2026 Fan Platform</title>
        <meta 
          name="description" 
          content="Join millions of fans for FIFA World Cup 2026 in USA, Canada & Mexico. Connect, celebrate, and experience the ultimate fan platform." 
        />
        <meta name="keywords" content="World Cup 2026, FIFA, Football, Soccer, Fan Platform, USA, Canada, Mexico" />
        <meta property="og:title" content="FANZONE CONNECT - World Cup 2026" />
        <meta property="og:description" content="The ultimate fan experience for FIFA World Cup 2026" />
        <meta property="og:image" content="/images/worldcup2026-hero.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <link rel="canonical" href="https://fanzoneconnect.com" />
      </Head>

      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center overflow-hidden bg-gradient-to-br from-blue-900 via-purple-900 to-red-900">
        {/* Background Video */}
        <div className="absolute inset-0 z-0">
          <video
            autoPlay
            muted
            loop
            playsInline
            className="w-full h-full object-cover opacity-30"
          >
            <source src="/videos/worldcup2026-hero.mp4" type="video/mp4" />
          </video>
        </div>

        {/* Hero Content */}
        <div className="relative z-10 text-center text-white px-4 max-w-6xl mx-auto">
          <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 1 }}
          >
            <h1 className="text-6xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-yellow-400 via-red-500 to-blue-500 bg-clip-text text-transparent">
              FANZONE CONNECT
            </h1>
            
            <motion.p 
              className="text-xl md:text-2xl mb-8 text-gray-200"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ delay: 0.5, duration: 1 }}
            >
              The Ultimate Fan Experience for FIFA World Cup 2026
            </motion.p>

            <motion.div 
              className="flex flex-wrap justify-center gap-4 mb-12"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 1, duration: 0.8 }}
            >
              <div className="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-6 py-3">
                <Image src="/flags/usa.png" alt="USA" width={24} height={16} className="rounded" />
                <span className="font-semibold">USA</span>
              </div>
              <div className="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-6 py-3">
                <Image src="/flags/canada.png" alt="Canada" width={24} height={16} className="rounded" />
                <span className="font-semibold">CANADA</span>
              </div>
              <div className="flex items-center space-x-2 bg-white/10 backdrop-blur-sm rounded-full px-6 py-3">
                <Image src="/flags/mexico.png" alt="Mexico" width={24} height={16} className="rounded" />
                <span className="font-semibold">MEXICO</span>
              </div>
            </motion.div>

            <motion.div 
              className="flex flex-col sm:flex-row gap-4 justify-center"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 1.5, duration: 0.8 }}
            >
              <Link href="/register">
                <motion.button
                  className="bg-gradient-to-r from-yellow-400 to-orange-500 text-black font-bold py-4 px-8 rounded-full text-lg hover:from-yellow-500 hover:to-orange-600 transition-all shadow-lg"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  Join the Fan Zone
                  <ArrowRight className="inline ml-2 w-5 h-5" />
                </motion.button>
              </Link>

              <motion.button
                onClick={() => setIsVideoPlaying(true)}
                className="bg-white/20 backdrop-blur-sm text-white font-bold py-4 px-8 rounded-full text-lg hover:bg-white/30 transition-all border border-white/30"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                <Play className="inline mr-2 w-5 h-5" />
                Watch Trailer
              </motion.button>
            </motion.div>
          </motion.div>
        </div>

        {/* Floating Stats */}
        <motion.div 
          className="absolute bottom-10 left-1/2 transform -translate-x-1/2 flex flex-wrap justify-center gap-6"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 2, duration: 1 }}
        >
          {stats.map((stat, index) => (
            <motion.div
              key={stat.label}
              className="bg-white/10 backdrop-blur-sm rounded-lg p-4 text-center min-w-[120px]"
              whileHover={{ scale: 1.05, y: -5 }}
              transition={{ delay: index * 0.1 }}
            >
              <stat.icon className={`w-8 h-8 mx-auto mb-2 ${stat.color}`} />
              <div className="text-2xl font-bold text-white">{stat.value}</div>
              <div className="text-sm text-gray-300">{stat.label}</div>
            </motion.div>
          ))}
        </motion.div>
      </section>

      {/* Featured Matches Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-gray-800 mb-4">
              Featured Matches
            </h2>
            <p className="text-xl text-gray-600">
              Don't miss the most exciting matches of World Cup 2026
            </p>
          </motion.div>

          {/* Match Carousel */}
          <div className="relative">
            <AnimatePresence mode="wait">
              {featuredMatches.length > 0 && (
                <motion.div
                  key={currentMatchIndex}
                  className="bg-white rounded-2xl shadow-xl p-8 max-w-4xl mx-auto"
                  initial={{ opacity: 0, x: 100 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -100 }}
                  transition={{ duration: 0.5 }}
                >
                  {(() => {
                    const match = featuredMatches[currentMatchIndex];
                    return (
                      <div className="flex items-center justify-between">
                        {/* Home Team */}
                        <div className="flex items-center space-x-4 flex-1">
                          <Image
                            src={match.homeTeam.flag}
                            alt={match.homeTeam.name}
                            width={60}
                            height={40}
                            className="rounded shadow-md"
                          />
                          <div>
                            <h3 className="text-2xl font-bold text-gray-800">
                              {match.homeTeam.name}
                            </h3>
                            <p className="text-gray-600">{match.homeTeam.code}</p>
                          </div>
                        </div>

                        {/* Match Info */}
                        <div className="text-center mx-8">
                          <div className="text-4xl font-bold text-gray-400 mb-2">VS</div>
                          <div className="bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-medium mb-2">
                            {match.phase}
                          </div>
                          <div className="flex items-center justify-center text-gray-600 mb-1">
                            <Calendar className="w-4 h-4 mr-2" />
                            <span className="text-sm">
                              {new Date(match.dateTime).toLocaleDateString()}
                            </span>
                          </div>
                          <div className="flex items-center justify-center text-gray-600">
                            <MapPin className="w-4 h-4 mr-2" />
                            <span className="text-sm">{match.venue.city}</span>
                          </div>
                        </div>

                        {/* Away Team */}
                        <div className="flex items-center space-x-4 flex-1 justify-end">
                          <div className="text-right">
                            <h3 className="text-2xl font-bold text-gray-800">
                              {match.awayTeam.name}
                            </h3>
                            <p className="text-gray-600">{match.awayTeam.code}</p>
                          </div>
                          <Image
                            src={match.awayTeam.flag}
                            alt={match.awayTeam.name}
                            width={60}
                            height={40}
                            className="rounded shadow-md"
                          />
                        </div>
                      </div>
                    );
                  })()}
                </motion.div>
              )}
            </AnimatePresence>

            {/* Match Navigation Dots */}
            <div className="flex justify-center mt-8 space-x-2">
              {featuredMatches.map((_, index) => (
                <button
                  key={index}
                  onClick={() => setCurrentMatchIndex(index)}
                  className={`w-3 h-3 rounded-full transition-all ${
                    index === currentMatchIndex
                      ? 'bg-blue-600 scale-125'
                      : 'bg-gray-300 hover:bg-gray-400'
                  }`}
                />
              ))}
            </div>
          </div>

          {/* View All Matches Button */}
          <motion.div 
            className="text-center mt-12"
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 0.8 }}
            viewport={{ once: true }}
          >
            <Link href="/matches">
              <motion.button
                className="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold py-4 px-8 rounded-full text-lg hover:from-blue-700 hover:to-purple-700 transition-all shadow-lg"
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
              >
                View All Matches
                <ArrowRight className="inline ml-2 w-5 h-5" />
              </motion.button>
            </Link>
          </motion.div>
        </div>
      </section>

      {/* Video Modal */}
      <AnimatePresence>
        {isVideoPlaying && (
          <motion.div
            className="fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-50"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setIsVideoPlaying(false)}
          >
            <motion.div
              className="relative max-w-4xl w-full mx-4"
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              exit={{ scale: 0.8 }}
              onClick={(e) => e.stopPropagation()}
            >
              <video
                autoPlay
                controls
                className="w-full rounded-lg"
              >
                <source src="/videos/fanzone-connect-trailer.mp4" type="video/mp4" />
              </video>
              <button
                onClick={() => setIsVideoPlaying(false)}
                className="absolute top-4 right-4 text-white bg-black bg-opacity-50 rounded-full p-2 hover:bg-opacity-75 transition-all"
              >
                ✕
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
};

// Server-Side Rendering for SEO and Performance
export const getServerSideProps: GetServerSideProps = async (context) => {
  try {
    // Fetch data from our API Gateway
    const baseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
    
    // Fetch featured matches
    const matchesResponse = await fetch(`${baseUrl}/api/matches/featured`);
    const featuredMatches = matchesResponse.ok ? await matchesResponse.json() : [];
    
    // Fetch platform stats
    const statsResponse = await fetch(`${baseUrl}/api/stats/platform`);
    const stats = statsResponse.ok ? await statsResponse.json() : {
      totalFans: 1250000,
      liveEvents: 15,
      countriesCount: 48
    };

    return {
      props: {
        featuredMatches: featuredMatches.slice(0, 5), // Limit to 5 matches
        totalFans: stats.totalFans,
        liveEvents: stats.liveEvents,
        countriesCount: stats.countriesCount,
      },
    };
  } catch (error) {
    console.error('Error fetching homepage data:', error);
    
    // Fallback data
    return {
      props: {
        featuredMatches: [],
        totalFans: 1250000,
        liveEvents: 15,
        countriesCount: 48,
      },
    };
  }
};

export default HomePage;
