/**
 * 🏆 FANZONE CONNECT - MATCH CARD COMPONENT
 * Learning Modules: 15 (JavaScript), 18 (TypeScript), 19 (React), 35 (React/Next.js)
 * World Cup 2026 Fan Platform - Interactive Match Display Component
 */

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Clock, MapPin, Users, Heart, Share2, Calendar } from 'lucide-react';

// TypeScript interfaces for World Cup match data
interface Team {
  id: string;
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
    capacity: number;
  };
  dateTime: string;
  status: 'scheduled' | 'live' | 'finished';
  score?: {
    home: number;
    away: number;
  };
  phase: string;
  ticketsAvailable: number;
  fanZoneEvents: number;
}

interface MatchCardProps {
  match: Match;
  onLike: (matchId: string) => void;
  onShare: (matchId: string) => void;
  onJoinFanZone: (matchId: string) => void;
  isLiked: boolean;
  className?: string;
}

const MatchCard: React.FC<MatchCardProps> = ({
  match,
  onLike,
  onShare,
  onJoinFanZone,
  isLiked,
  className = ''
}) => {
  const [isHovered, setIsHovered] = useState(false);
  const [timeUntilMatch, setTimeUntilMatch] = useState('');
  const [isLiveAnimating, setIsLiveAnimating] = useState(false);

  // Real-time countdown for World Cup matches
  useEffect(() => {
    const updateCountdown = () => {
      const matchDate = new Date(match.dateTime);
      const now = new Date();
      const diff = matchDate.getTime() - now.getTime();

      if (diff > 0) {
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));

        if (days > 0) {
          setTimeUntilMatch(`${days}d ${hours}h`);
        } else if (hours > 0) {
          setTimeUntilMatch(`${hours}h ${minutes}m`);
        } else {
          setTimeUntilMatch(`${minutes}m`);
        }
      } else {
        setTimeUntilMatch('Match Started');
      }
    };

    updateCountdown();
    const interval = setInterval(updateCountdown, 60000); // Update every minute

    return () => clearInterval(interval);
  }, [match.dateTime]);

  // Live match animation effect
  useEffect(() => {
    if (match.status === 'live') {
      const interval = setInterval(() => {
        setIsLiveAnimating(prev => !prev);
      }, 1000);
      return () => clearInterval(interval);
    }
  }, [match.status]);

  const formatDateTime = (dateTime: string) => {
    return new Date(dateTime).toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  const getStatusColor = () => {
    switch (match.status) {
      case 'live': return 'text-red-500';
      case 'finished': return 'text-gray-500';
      default: return 'text-blue-500';
    }
  };

  const getStatusBadge = () => {
    switch (match.status) {
      case 'live':
        return (
          <motion.div
            className={`px-2 py-1 rounded-full text-xs font-bold text-white ${
              isLiveAnimating ? 'bg-red-600' : 'bg-red-500'
            }`}
            animate={{ scale: isLiveAnimating ? 1.05 : 1 }}
            transition={{ duration: 0.5 }}
          >
            🔴 LIVE
          </motion.div>
        );
      case 'finished':
        return (
          <div className="px-2 py-1 bg-gray-500 text-white rounded-full text-xs font-bold">
            FINAL
          </div>
        );
      default:
        return (
          <div className="px-2 py-1 bg-blue-500 text-white rounded-full text-xs font-bold">
            {timeUntilMatch}
          </div>
        );
    }
  };

  return (
    <motion.div
      className={`bg-white rounded-xl shadow-lg overflow-hidden border border-gray-200 hover:shadow-xl transition-all duration-300 ${className}`}
      whileHover={{ y: -4 }}
      onHoverStart={() => setIsHovered(true)}
      onHoverEnd={() => setIsHovered(false)}
      layout
    >
      {/* Header with status and phase */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white p-4">
        <div className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Calendar className="w-4 h-4" />
            <span className="text-sm font-medium">{match.phase}</span>
          </div>
          {getStatusBadge()}
        </div>
      </div>

      {/* Teams and Score */}
      <div className="p-6">
        <div className="flex items-center justify-between mb-4">
          {/* Home Team */}
          <motion.div 
            className="flex items-center space-x-3 flex-1"
            whileHover={{ scale: 1.02 }}
          >
            <img
              src={match.homeTeam.flag}
              alt={match.homeTeam.name}
              className="w-12 h-8 object-cover rounded shadow-sm"
            />
            <div>
              <h3 className="font-bold text-gray-800">{match.homeTeam.name}</h3>
              <p className="text-sm text-gray-500">#{match.homeTeam.ranking}</p>
            </div>
          </motion.div>

          {/* Score or VS */}
          <div className="mx-4 text-center">
            {match.score ? (
              <motion.div 
                className="text-3xl font-bold text-gray-800"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ type: "spring", stiffness: 300 }}
              >
                {match.score.home} - {match.score.away}
              </motion.div>
            ) : (
              <div className="text-2xl font-bold text-gray-400">VS</div>
            )}
          </div>

          {/* Away Team */}
          <motion.div 
            className="flex items-center space-x-3 flex-1 justify-end"
            whileHover={{ scale: 1.02 }}
          >
            <div className="text-right">
              <h3 className="font-bold text-gray-800">{match.awayTeam.name}</h3>
              <p className="text-sm text-gray-500">#{match.awayTeam.ranking}</p>
            </div>
            <img
              src={match.awayTeam.flag}
              alt={match.awayTeam.name}
              className="w-12 h-8 object-cover rounded shadow-sm"
            />
          </motion.div>
        </div>

        {/* Match Details */}
        <div className="space-y-2 mb-4">
          <div className="flex items-center text-gray-600">
            <Clock className="w-4 h-4 mr-2" />
            <span className="text-sm">{formatDateTime(match.dateTime)}</span>
          </div>
          <div className="flex items-center text-gray-600">
            <MapPin className="w-4 h-4 mr-2" />
            <span className="text-sm">{match.venue.name}, {match.venue.city}</span>
          </div>
          <div className="flex items-center text-gray-600">
            <Users className="w-4 h-4 mr-2" />
            <span className="text-sm">{match.venue.capacity.toLocaleString()} capacity</span>
          </div>
        </div>

        {/* Fan Zone Info */}
        <div className="bg-gradient-to-r from-yellow-50 to-orange-50 rounded-lg p-3 mb-4">
          <div className="flex justify-between items-center">
            <div>
              <p className="text-sm font-medium text-gray-800">
                🎉 {match.fanZoneEvents} Fan Zone Events
              </p>
              <p className="text-xs text-gray-600">
                {match.ticketsAvailable} tickets available
              </p>
            </div>
            <motion.button
              onClick={() => onJoinFanZone(match.id)}
              className="bg-gradient-to-r from-yellow-400 to-orange-400 text-white px-4 py-2 rounded-lg text-sm font-medium hover:from-yellow-500 hover:to-orange-500 transition-all"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Join Fan Zone
            </motion.button>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex justify-between items-center">
          <motion.button
            onClick={() => onLike(match.id)}
            className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-all ${
              isLiked 
                ? 'bg-red-100 text-red-600' 
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Heart className={`w-4 h-4 ${isLiked ? 'fill-current' : ''}`} />
            <span className="text-sm font-medium">
              {isLiked ? 'Liked' : 'Like'}
            </span>
          </motion.button>

          <motion.button
            onClick={() => onShare(match.id)}
            className="flex items-center space-x-2 px-4 py-2 bg-blue-100 text-blue-600 rounded-lg hover:bg-blue-200 transition-all"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Share2 className="w-4 h-4" />
            <span className="text-sm font-medium">Share</span>
          </motion.button>
        </div>
      </div>

      {/* Hover overlay for additional info */}
      <AnimatePresence>
        {isHovered && (
          <motion.div
            className="absolute inset-0 bg-black bg-opacity-10 flex items-center justify-center"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
          >
            <motion.div
              className="bg-white rounded-lg p-4 shadow-lg"
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.8, opacity: 0 }}
            >
              <p className="text-sm text-gray-600 text-center">
                Click to view match details
              </p>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
};

export default MatchCard;
