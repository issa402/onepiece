#!/usr/bin/env python3
"""
🏴‍☠️ DYNAMIC PRICE ENGINE - PYTHON VERSION
FIXED: Prices start at $0 and move DRAMATICALLY!

This replaces the static price system with REAL dynamic prices that:
- Start at $0.00 for all characters
- Grow exponentially over time
- Have dramatic volatility swings
- Include story arc multipliers
- Update every second with WebSocket broadcasts
"""

import asyncio
import json
import random
import time
import math
from datetime import datetime, timedelta
from typing import Dict, List
import websockets
import requests

class Character:
    def __init__(self, id: int, name: str, crew: str, bounty: int, growth_rate: float = 0.1):
        self.id = id
        self.name = name
        self.crew = crew
        self.bounty = bounty
        self.current_price = 0.0  # START AT ZERO!
        self.base_growth_rate = growth_rate
        self.volatility = 0.3  # High volatility for dramatic moves
        self.story_multiplier = 1.0
        self.sentiment_score = 0.5
        self.weekly_change = 0.0
        self.story_phase = 1
        self.is_trending = False
        self.last_update = datetime.now()

class MarketData:
    def __init__(self):
        self.total_volume = 0.0
        self.market_cap = 0.0
        self.active_traders = 1000
        self.volatility_index = 0.5
        self.current_year = 1
        self.days_elapsed = 0
        self.market_sentiment = 0.5
        self.major_event_active = False
        self.current_arc = "East Blue Saga"
        self.last_update = datetime.now()

class DynamicPriceEngine:
    def __init__(self):
        self.characters: List[Character] = []
        self.market_data = MarketData()
        self.running = False
        
        # Story progression data
        self.story_arcs = [
            "East Blue Saga", "Alabasta Saga", "Sky Island Saga", 
            "Water 7 Saga", "Thriller Bark Saga", "Summit War Saga",
            "Fish-Man Island Saga", "Dressrosa Saga", "Zou Saga",
            "Whole Cake Island Saga", "Wano Country Saga", "Final Saga"
        ]
        
        self.story_arc_multipliers = {
            "East Blue Saga": 1.0,
            "Alabasta Saga": 1.5,
            "Sky Island Saga": 1.3,
            "Water 7 Saga": 2.0,
            "Thriller Bark Saga": 1.4,
            "Summit War Saga": 3.0,      # Major event!
            "Fish-Man Island Saga": 1.6,
            "Dressrosa Saga": 2.2,
            "Zou Saga": 1.8,
            "Whole Cake Island Saga": 2.5,
            "Wano Country Saga": 4.0,    # HUGE event!
            "Final Saga": 5.0            # MAXIMUM HYPE!
        }
        
        self.current_arc_index = 0
        self.websocket_clients = set()
        
        print("🏴‍☠️ DYNAMIC Price Engine initialized!")
        print("📈 All characters start at $0.00 and will grow over time!")

    def load_characters(self):
        """Load characters - ALL START AT $0!"""
        print("📊 Loading characters - ALL START AT $0.00!")
        
        # Main Straw Hat Pirates (high growth rates)
        self.characters.extend([
            Character(1, "Monkey D. Luffy", "Straw Hat Pirates", 3000000000, 0.15),
            Character(2, "Roronoa Zoro", "Straw Hat Pirates", 1111000000, 0.12),
            Character(3, "Nami", "Straw Hat Pirates", 366000000, 0.08),
            Character(4, "Usopp", "Straw Hat Pirates", 500000000, 0.07),
            Character(5, "Sanji", "Straw Hat Pirates", 1032000000, 0.11),
            Character(6, "Tony Tony Chopper", "Straw Hat Pirates", 1000, 0.06),
            Character(7, "Nico Robin", "Straw Hat Pirates", 930000000, 0.10),
            Character(8, "Franky", "Straw Hat Pirates", 394000000, 0.09),
            Character(9, "Brook", "Straw Hat Pirates", 383000000, 0.08),
            Character(10, "Jinbe", "Straw Hat Pirates", 1100000000, 0.13),
        ])
        
        # Major Antagonists (explosive growth)
        self.characters.extend([
            Character(11, "Kaido", "Beast Pirates", 4611100000, 0.20),
            Character(12, "Big Mom", "Big Mom Pirates", 4388000000, 0.18),
            Character(13, "Blackbeard", "Blackbeard Pirates", 3996000000, 0.25),
            Character(14, "Doflamingo", "Donquixote Pirates", 340000000, 0.14),
        ])
        
        # Marines (steady growth)
        self.characters.extend([
            Character(15, "Akainu", "Marines", 0, 0.16),
            Character(16, "Kizaru", "Marines", 0, 0.15),
            Character(17, "Aokiji", "Marines", 0, 0.14),
        ])
        
        print(f"✅ Loaded {len(self.characters)} characters - Ready for DYNAMIC growth!")

    def get_story_multiplier(self, character: Character) -> float:
        """Get story arc multiplier for character"""
        base_multiplier = self.story_arc_multipliers[self.market_data.current_arc]
        
        # Special character bonuses in specific arcs
        if self.market_data.current_arc == "Summit War Saga" and character.name == "Monkey D. Luffy":
            return base_multiplier * 2.0  # Luffy gets huge boost in Marineford
        if self.market_data.current_arc == "Wano Country Saga" and character.name == "Monkey D. Luffy":
            return base_multiplier * 3.0  # Gear 5 reveal!
        if self.market_data.current_arc == "Wano Country Saga" and character.name == "Kaido":
            return base_multiplier * 2.5  # Kaido's big moment
        
        return base_multiplier

    def calculate_new_price(self, character: Character) -> float:
        """Calculate new price with DRAMATIC movements!"""
        current_price = character.current_price
        
        # Base growth from $0 - exponential growth in early stages
        base_growth = character.base_growth_rate
        if current_price < 10.0:
            base_growth *= 2.0  # Double growth when price is low
        
        # Story arc multiplier - HUGE impact!
        story_multiplier = self.get_story_multiplier(character)
        
        # Time-based growth (compound growth)
        time_factor = 1.0 + (base_growth * story_multiplier)
        
        # Volatility - BIG price swings!
        volatility_swing = random.gauss(0, 1) * character.volatility
        volatility_factor = 1.0 + volatility_swing
        
        # Bounty influence (logarithmic scaling)
        bounty_factor = 1.0
        if character.bounty > 0:
            bounty_factor = 1.0 + (math.log10(character.bounty + 1) * 0.02)
        
        # Crew popularity bonus
        crew_factor = 1.0
        if character.crew == "Straw Hat Pirates":
            crew_factor = 1.2  # 20% bonus for main crew!
        elif character.crew in ["Beast Pirates", "Big Mom Pirates"]:
            crew_factor = 1.15  # 15% bonus for Yonko crews
        
        # Major event boost
        event_factor = 1.5 if self.market_data.major_event_active else 1.0
        
        # Calculate new price with ALL factors
        if current_price == 0.0:
            # Starting price - small random amount
            new_price = random.uniform(0.4, 0.75)  # Start between $0.40-$0.75
        else:
            new_price = current_price * time_factor * volatility_factor * bounty_factor * crew_factor * event_factor
        
        # Ensure minimum growth and maximum reasonable price
        new_price = max(new_price, 0.01)  # Minimum 1 cent
        new_price = min(new_price, 10000.0)  # Maximum $10,000
        
        return new_price

    def trigger_major_event(self):
        """Trigger random major events"""
        self.market_data.major_event_active = True
        
        events = [
            "🔥 DEVIL FRUIT AWAKENING!", "⚔️ EPIC BATTLE BEGINS!", 
            "👑 NEW YONKO REVEALED!", "🏴‍☠️ BOUNTY UPDATE!",
            "🌊 MAJOR ARC CLIMAX!", "💥 POWER-UP UNLOCKED!"
        ]
        
        event = random.choice(events)
        print(f"🚨 MAJOR EVENT: {event} - Prices will surge!")
        
        # Reset event after 10 seconds
        asyncio.create_task(self.reset_event())

    async def reset_event(self):
        """Reset major event after delay"""
        await asyncio.sleep(10)
        self.market_data.major_event_active = False

    async def progress_story(self):
        """Progress through story arcs"""
        while self.running:
            await asyncio.sleep(30)  # Progress story every 30 seconds
            
            # Check if it's time to advance to next arc
            if self.market_data.days_elapsed > 0 and self.market_data.days_elapsed % 100 == 0:
                if self.current_arc_index < len(self.story_arcs) - 1:
                    self.current_arc_index += 1
                    self.market_data.current_arc = self.story_arcs[self.current_arc_index]
                    
                    print(f"🎬 STORY PROGRESSION: Now in {self.market_data.current_arc}!")
                    print(f"📈 Price multiplier: {self.story_arc_multipliers[self.market_data.current_arc]}x")
                    
                    # Major story events trigger market boosts
                    self.market_data.major_event_active = True

    async def calculate_prices(self):
        """Main price calculation loop"""
        print("🚀 Starting DYNAMIC price updates - prices will move every second!")
        
        while self.running:
            # Update market data
            self.market_data.days_elapsed += 1
            if self.market_data.days_elapsed % 365 == 0:
                self.market_data.current_year += 1
                print(f"🎉 NEW YEAR! Now in year {self.market_data.current_year}")
            
            # Calculate new prices for all characters
            for character in self.characters:
                old_price = character.current_price
                new_price = self.calculate_new_price(character)
                
                # ALWAYS update price
                character.current_price = new_price
                
                # Calculate change percentage
                if old_price > 0:
                    character.weekly_change = ((new_price - old_price) / old_price) * 100.0
                else:
                    character.weekly_change = 100.0 if new_price > 0 else 0.0
                
                character.last_update = datetime.now()
                
                # Send price update
                await self.send_price_update(character)
            
            # Random major events (10% chance each update)
            if random.random() < 0.1:
                self.trigger_major_event()
            
            self.market_data.last_update = datetime.now()
            
            # Update every second for FAST price movements
            await asyncio.sleep(1)

    async def send_price_update(self, character: Character):
        """Send price update via WebSocket"""
        update_data = {
            "type": "price_update",
            "character": {
                "id": character.id,
                "name": character.name,
                "crew": character.crew,
                "current_price": round(character.current_price, 2),
                "weekly_change": round(character.weekly_change, 2),
                "market_cap": round(character.current_price * 1000000, 2),
                "story_arc": self.market_data.current_arc
            },
            "timestamp": datetime.now().isoformat()
        }
        
        # Send to all connected WebSocket clients
        if self.websocket_clients:
            message = json.dumps(update_data)
            disconnected = set()
            for client in self.websocket_clients:
                try:
                    await client.send(message)
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)
            
            # Remove disconnected clients
            self.websocket_clients -= disconnected
        
        # Also log to console
        print(f"💰 {character.name} -> ${character.current_price:.2f} "
              f"({character.weekly_change:+.1f}%) [{self.market_data.current_arc}]")

    async def websocket_handler(self, websocket, path):
        """Handle WebSocket connections"""
        self.websocket_clients.add(websocket)
        print(f"📡 New WebSocket client connected. Total: {len(self.websocket_clients)}")
        
        try:
            # Send initial market data
            initial_data = {
                "type": "market_data",
                "characters": [
                    {
                        "id": char.id,
                        "name": char.name,
                        "crew": char.crew,
                        "current_price": round(char.current_price, 2),
                        "weekly_change": round(char.weekly_change, 2),
                        "market_cap": round(char.current_price * 1000000, 2)
                    }
                    for char in self.characters
                ],
                "market_data": {
                    "current_arc": self.market_data.current_arc,
                    "current_year": self.market_data.current_year,
                    "days_elapsed": self.market_data.days_elapsed,
                    "major_event_active": self.market_data.major_event_active
                }
            }
            await websocket.send(json.dumps(initial_data))
            
            # Keep connection alive
            await websocket.wait_closed()
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            self.websocket_clients.discard(websocket)
            print(f"📡 WebSocket client disconnected. Total: {len(self.websocket_clients)}")

    def print_market_summary(self):
        """Print current market summary"""
        print("\n🏴‍☠️ DYNAMIC MARKET SUMMARY 🏴‍☠️")
        print("=" * 50)
        print(f"📅 Story Year: {self.market_data.current_year} | Days: {self.market_data.days_elapsed}")
        print(f"🎬 Current Arc: {self.market_data.current_arc}")
        print(f"🚨 Major Event: {'ACTIVE' if self.market_data.major_event_active else 'None'}")
        print("=" * 50)
        
        # Sort characters by price
        sorted_chars = sorted(self.characters, key=lambda x: x.current_price, reverse=True)
        
        for character in sorted_chars[:10]:  # Top 10
            print(f"💰 {character.name} ({character.crew})")
            print(f"   Price: ${character.current_price:.2f} | Change: {character.weekly_change:+.1f}%")
        
        total_market_cap = sum(char.current_price * 1000000 for char in self.characters)
        print(f"\n🔥 Total Market Cap: ${total_market_cap:,.2f}")

    async def start(self):
        """Start the dynamic price engine"""
        self.running = True
        
        # Load characters
        self.load_characters()
        
        # Start background tasks
        price_task = asyncio.create_task(self.calculate_prices())
        story_task = asyncio.create_task(self.progress_story())
        
        # Start WebSocket server
        websocket_server = await websockets.serve(
            self.websocket_handler, "localhost", 8765
        )
        
        print("🚀 DYNAMIC price engine started!")
        print("📡 WebSocket server running on ws://localhost:8765")
        print("📈 Prices will grow from $0 and move DRAMATICALLY!")
        print("Press Ctrl+C to stop...")
        
        try:
            # Print market summary every 10 seconds
            while self.running:
                await asyncio.sleep(10)
                self.print_market_summary()
        except KeyboardInterrupt:
            print("\n🛑 Stopping price engine...")
            self.running = False
            
            # Cancel tasks
            price_task.cancel()
            story_task.cancel()
            websocket_server.close()
            await websocket_server.wait_closed()
            
            print("🏴‍☠️ Dynamic Price Engine stopped.")

if __name__ == "__main__":
    engine = DynamicPriceEngine()
    asyncio.run(engine.start())
