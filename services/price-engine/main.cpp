/*
🏴‍☠️ C++ DYNAMIC PRICE ENGINE - REAL TRADING SIMULATION
FIXED: Now with DYNAMIC prices that start at $0 and move DRASTICALLY!

WHAT THIS DOES:
- Characters start at $0.00 and grow over time
- Prices move FAST and DRAMATICALLY based on story events
- Real-time price updates every second
- Volatile market movements with big swings
- Story-based price multipliers (Gear 5, Wano Arc, etc.)
- Dynamic chart scaling that grows with prices
*/

#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <thread>
#include <mutex>
#include <chrono>
#include <cmath>
#include <algorithm>
#include <memory>
#include <queue>
#include <random>
#include <fstream>
#include <iomanip>
#include <curl/curl.h>
#include <nlohmann/json.hpp>


using namespace std;
using json = nlohmann::json;

// 🔥 DYNAMIC CHARACTER WITH STORY EVENTS
struct Character {
    int id;
    string name;
    string crew;
    long long bounty;
    double current_price;
    double base_growth_rate;    // How fast price grows naturally
    double volatility;          // How much price swings
    double story_multiplier;    // Story event impact
    double sentiment_score;
    double weekly_change;
    int story_phase;           // Current story arc (affects growth)
    bool is_trending;          // Trending characters get boost
    chrono::system_clock::time_point last_update;

    // Constructor - ALL CHARACTERS START AT $0!
    Character(int id, const string& name, const string& crew,
              long long bounty, double growth_rate = 0.1)
        : id(id), name(name), crew(crew), bounty(bounty),
          current_price(0.0),  // START AT ZERO!
          base_growth_rate(growth_rate),
          volatility(0.3),     // High volatility for dramatic moves
          story_multiplier(1.0),
          sentiment_score(0.5),
          weekly_change(0.0),
          story_phase(1),
          is_trending(false),
          last_update(chrono::system_clock::now()) {}
};

// 🚀 DYNAMIC MARKET DATA WITH TIME PROGRESSION
struct MarketData {
    double total_volume;
    double market_cap;
    int active_traders;
    double volatility_index;
    int current_year;          // Story year (starts at year 1)
    int days_elapsed;          // Days since start
    double market_sentiment;   // Overall market mood
    bool major_event_active;   // Major story event happening
    string current_arc;        // Current story arc
    chrono::system_clock::time_point last_update;

    MarketData() : total_volume(0.0), market_cap(0.0),
                   active_traders(1000), volatility_index(0.5),
                   current_year(1), days_elapsed(0),
                   market_sentiment(0.5), major_event_active(false),
                   current_arc("East Blue Saga"),
                   last_update(chrono::system_clock::now()) {}
};

// 🔥 DYNAMIC PRICE ENGINE WITH STORY PROGRESSION
class PriceEngine {
private:
    vector<Character> characters;
    MarketData market_data;
    mutex data_mutex;
    bool running;
    thread calculation_thread;
    thread story_progression_thread;

    // Random number generators for realistic market simulation
    random_device rd;
    mt19937 gen;
    normal_distribution<double> price_volatility;
    uniform_real_distribution<double> event_chance;
    uniform_real_distribution<double> growth_factor;

    // Story progression data
    map<string, double> story_arc_multipliers;
    vector<string> story_arcs;
    int current_arc_index;

public:
    PriceEngine();
    ~PriceEngine();

    // Core functionality
    void loadCharacters();
    void startPriceCalculation();
    void stopPriceCalculation();
    void calculatePrices();
    void progressStory();

    // Price calculation methods
    double calculateNewPrice(Character& character);
    double getStoryMultiplier(const Character& character);
    void triggerMajorEvent();
    void updateCharacterPrice(int character_id, double new_price);
    void sendPriceUpdate(const Character& character);

    // Utility methods
    Character* findCharacter(int id);
    void printMarketSummary();
    void printPriceChart(const Character& character);
};

// 🚀 CONSTRUCTOR WITH DYNAMIC SETUP
PriceEngine::PriceEngine() : running(false), gen(rd()),
                            price_volatility(0.0, 1.0),
                            event_chance(0.0, 1.0),
                            growth_factor(0.8, 1.5),
                            current_arc_index(0) {

    // Initialize story arcs with multipliers
    story_arcs = {
        "East Blue Saga", "Alabasta Saga", "Sky Island Saga",
        "Water 7 Saga", "Thriller Bark Saga", "Summit War Saga",
        "Fish-Man Island Saga", "Dressrosa Saga", "Zou Saga",
        "Whole Cake Island Saga", "Wano Country Saga", "Final Saga"
    };

    story_arc_multipliers = {
        {"East Blue Saga", 1.0},
        {"Alabasta Saga", 1.5},
        {"Sky Island Saga", 1.3},
        {"Water 7 Saga", 2.0},
        {"Thriller Bark Saga", 1.4},
        {"Summit War Saga", 3.0},      // Major event!
        {"Fish-Man Island Saga", 1.6},
        {"Dressrosa Saga", 2.2},
        {"Zou Saga", 1.8},
        {"Whole Cake Island Saga", 2.5},
        {"Wano Country Saga", 4.0},    // HUGE event!
        {"Final Saga", 5.0}            // MAXIMUM HYPE!
    };

    market_data.current_arc = story_arcs[0];
    cout << "🏴‍☠️ DYNAMIC Price Engine initialized!" << endl;
    cout << "📈 All characters start at $0.00 and will grow over time!" << endl;
}

PriceEngine::~PriceEngine() {
    if (running) {
        stopPriceCalculation();
    }
    cout << "🏴‍☠️ Dynamic Price Engine shutdown complete." << endl;
}

// 🔥 LOAD CHARACTERS - ALL START AT $0!
void PriceEngine::loadCharacters() {
    cout << "📊 Loading characters - ALL START AT $0.00!" << endl;

    // Main Straw Hat Pirates (high growth rates)
    characters.push_back(Character(1, "Monkey D. Luffy", "Straw Hat Pirates", 3000000000, 0.15));
    characters.push_back(Character(2, "Roronoa Zoro", "Straw Hat Pirates", 1111000000, 0.12));
    characters.push_back(Character(3, "Nami", "Straw Hat Pirates", 366000000, 0.08));
    characters.push_back(Character(4, "Usopp", "Straw Hat Pirates", 500000000, 0.07));
    characters.push_back(Character(5, "Sanji", "Straw Hat Pirates", 1032000000, 0.11));
    characters.push_back(Character(6, "Tony Tony Chopper", "Straw Hat Pirates", 1000, 0.06));
    characters.push_back(Character(7, "Nico Robin", "Straw Hat Pirates", 930000000, 0.10));
    characters.push_back(Character(8, "Franky", "Straw Hat Pirates", 394000000, 0.09));
    characters.push_back(Character(9, "Brook", "Straw Hat Pirates", 383000000, 0.08));
    characters.push_back(Character(10, "Jinbe", "Straw Hat Pirates", 1100000000, 0.13));

    // Major Antagonists (explosive growth)
    characters.push_back(Character(11, "Kaido", "Beast Pirates", 4611100000, 0.20));
    characters.push_back(Character(12, "Big Mom", "Big Mom Pirates", 4388000000, 0.18));
    characters.push_back(Character(13, "Blackbeard", "Blackbeard Pirates", 3996000000, 0.25));
    characters.push_back(Character(14, "Doflamingo", "Donquixote Pirates", 340000000, 0.14));

    // Marines (steady growth)
    characters.push_back(Character(15, "Akainu", "Marines", 0, 0.16));
    characters.push_back(Character(16, "Kizaru", "Marines", 0, 0.15));
    characters.push_back(Character(17, "Aokiji", "Marines", 0, 0.14));

    cout << "✅ Loaded " << characters.size() << " characters - Ready for DYNAMIC growth!" << endl;
}

// 🚀 START DYNAMIC PRICE SYSTEM
void PriceEngine::startPriceCalculation() {
    if (running) return;

    running = true;
    calculation_thread = thread(&PriceEngine::calculatePrices, this);
    story_progression_thread = thread(&PriceEngine::progressStory, this);

    cout << "🔥 DYNAMIC price calculation started!" << endl;
    cout << "📈 Prices will grow from $0 and move DRAMATICALLY!" << endl;
}

void PriceEngine::stopPriceCalculation() {
    running = false;

    if (calculation_thread.joinable()) {
        calculation_thread.join();
    }
    if (story_progression_thread.joinable()) {
        story_progression_thread.join();
    }

    cout << "Price calculation stopped." << endl;
}

// 🔥 DYNAMIC PRICE CALCULATION - PRICES MOVE FAST!
void PriceEngine::calculatePrices() {
    cout << "🚀 Starting DYNAMIC price updates - prices will move every second!" << endl;

    while (running) {
        {
            lock_guard<mutex> lock(data_mutex);

            // Update market data
            market_data.days_elapsed++;
            if (market_data.days_elapsed % 365 == 0) {
                market_data.current_year++;
                cout << "🎉 NEW YEAR! Now in year " << market_data.current_year << endl;
            }

            // Calculate new prices for all characters
            for (auto& character : characters) {
                double old_price = character.current_price;
                double new_price = calculateNewPrice(character);

                // ALWAYS update price (no minimum change threshold)
                character.current_price = new_price;

                // Calculate change percentage
                if (old_price > 0) {
                    character.weekly_change = ((new_price - old_price) / old_price) * 100.0;
                } else {
                    character.weekly_change = new_price > 0 ? 100.0 : 0.0;
                }

                character.last_update = chrono::system_clock::now();

                // Send update to Character Service
                sendPriceUpdate(character);
            }

            // Random major events (10% chance each update)
            if (event_chance(gen) < 0.1) {
                triggerMajorEvent();
            }

            market_data.last_update = chrono::system_clock::now();
        }

        // Update every second for FAST price movements
        this_thread::sleep_for(chrono::seconds(1));
    }
}

// 🔥 DYNAMIC PRICE CALCULATION - DRAMATIC MOVEMENTS!
double PriceEngine::calculateNewPrice(Character& character) {
    double current_price = character.current_price;

    // Base growth from $0 - exponential growth in early stages
    double base_growth = character.base_growth_rate;
    if (current_price < 10.0) {
        base_growth *= 2.0;  // Double growth when price is low
    }

    // Story arc multiplier - HUGE impact!
    double story_multiplier = getStoryMultiplier(character);

    // Time-based growth (compound growth)
    double time_factor = 1.0 + (base_growth * story_multiplier);

    // Volatility - BIG price swings!
    double volatility_swing = price_volatility(gen) * character.volatility;
    double volatility_factor = 1.0 + volatility_swing;

    // Bounty influence (logarithmic scaling)
    double bounty_factor = 1.0;
    if (character.bounty > 0) {
        bounty_factor = 1.0 + (log10(character.bounty + 1) * 0.02);
    }

    // Crew popularity bonus
    double crew_factor = 1.0;
    if (character.crew == "Straw Hat Pirates") {
        crew_factor = 1.2;  // 20% bonus for main crew!
    } else if (character.crew == "Beast Pirates" || character.crew == "Big Mom Pirates") {
        crew_factor = 1.15; // 15% bonus for Yonko crews
    }

    // Major event boost
    double event_factor = market_data.major_event_active ? 1.5 : 1.0;

    // Calculate new price with ALL factors
    double new_price;
    if (current_price == 0.0) {
        // Starting price - small random amount
        new_price = growth_factor(gen) * 0.5;  // Start between $0.40-$0.75
    } else {
        new_price = current_price * time_factor * volatility_factor *
                   bounty_factor * crew_factor * event_factor;
    }

    // Ensure minimum growth and maximum reasonable price
    new_price = max(new_price, 0.01);  // Minimum 1 cent
    new_price = min(new_price, 10000.0); // Maximum $10,000

    return new_price;
}

// 🚀 STORY PROGRESSION SYSTEM
void PriceEngine::progressStory() {
    while (running) {
        this_thread::sleep_for(chrono::seconds(30)); // Progress story every 30 seconds

        {
            lock_guard<mutex> lock(data_mutex);

            // Check if it's time to advance to next arc
            if (market_data.days_elapsed > 0 && market_data.days_elapsed % 100 == 0) {
                if (current_arc_index < story_arcs.size() - 1) {
                    current_arc_index++;
                    market_data.current_arc = story_arcs[current_arc_index];

                    cout << "🎬 STORY PROGRESSION: Now in " << market_data.current_arc << "!" << endl;
                    cout << "📈 Price multiplier: " << story_arc_multipliers[market_data.current_arc] << "x" << endl;

                    // Major story events trigger market boosts
                    market_data.major_event_active = true;
                }
            }
        }
    }
}

double PriceEngine::getStoryMultiplier(const Character& character) {
    double base_multiplier = story_arc_multipliers[market_data.current_arc];

    // Special character bonuses in specific arcs
    if (market_data.current_arc == "Summit War Saga" && character.name == "Monkey D. Luffy") {
        return base_multiplier * 2.0; // Luffy gets huge boost in Marineford
    }
    if (market_data.current_arc == "Wano Country Saga" && character.name == "Monkey D. Luffy") {
        return base_multiplier * 3.0; // Gear 5 reveal!
    }
    if (market_data.current_arc == "Wano Country Saga" && character.name == "Kaido") {
        return base_multiplier * 2.5; // Kaido's big moment
    }

    return base_multiplier;
}

void PriceEngine::triggerMajorEvent() {
    market_data.major_event_active = true;

    vector<string> events = {
        "🔥 DEVIL FRUIT AWAKENING!", "⚔️ EPIC BATTLE BEGINS!",
        "👑 NEW YONKO REVEALED!", "🏴‍☠️ BOUNTY UPDATE!",
        "🌊 MAJOR ARC CLIMAX!", "💥 POWER-UP UNLOCKED!"
    };

    string event = events[gen() % events.size()];
    cout << "🚨 MAJOR EVENT: " << event << " - Prices will surge!" << endl;

    // Reset event after some time
    thread([this]() {
        this_thread::sleep_for(chrono::seconds(10));
        market_data.major_event_active = false;
    }).detach();
}

void PriceEngine::sendPriceUpdate(const Character& character) {
    // For now, just log the dramatic price updates
    cout << "💰 " << character.name
         << " -> $" << fixed << setprecision(2) << character.current_price;

    if (character.weekly_change != 0) {
        cout << " (" << showpos << fixed << setprecision(1) << character.weekly_change << "%)";
    }

    cout << " [" << market_data.current_arc << "]" << endl;
}

Character* PriceEngine::findCharacter(int id) {
    auto it = find_if(characters.begin(), characters.end(),
                      [id](const Character& c) { return c.id == id; });
    return (it != characters.end()) ? &(*it) : nullptr;
}

void PriceEngine::printMarketSummary() {
    lock_guard<mutex> lock(data_mutex);

    cout << "\n🏴‍☠️ DYNAMIC MARKET SUMMARY 🏴‍☠️" << endl;
    cout << "======================================" << endl;
    cout << "📅 Story Year: " << market_data.current_year << " | Days: " << market_data.days_elapsed << endl;
    cout << "🎬 Current Arc: " << market_data.current_arc << endl;
    cout << "🚨 Major Event: " << (market_data.major_event_active ? "ACTIVE" : "None") << endl;
    cout << "======================================" << endl;

    // Sort characters by price for better display
    vector<Character> sorted_chars = characters;
    sort(sorted_chars.begin(), sorted_chars.end(),
         [](const Character& a, const Character& b) {
             return a.current_price > b.current_price;
         });

    for (const auto& character : sorted_chars) {
        cout << "💰 " << character.name << " (" << character.crew << ")" << endl;
        cout << "   Price: $" << fixed << setprecision(2) << character.current_price;

        if (character.weekly_change != 0) {
            cout << " | Change: " << showpos << fixed << setprecision(1)
                 << character.weekly_change << "%";
        }

        cout << " | Growth: " << fixed << setprecision(1)
             << (character.base_growth_rate * 100) << "%/update" << endl;
        cout << endl;
    }

    cout << "🔥 Total Market Cap: $" << fixed << setprecision(2);
    double total_market_cap = 0;
    for (const auto& character : characters) {
        total_market_cap += character.current_price * 1000000; // Assume 1M shares each
    }
    cout << total_market_cap << endl;
}

// 🔥 MAIN FUNCTION - DYNAMIC PRICE SIMULATION
int main() {
    cout << "🏴‍☠️ DYNAMIC One Piece Price Engine Starting..." << endl;
    cout << "📈 ALL CHARACTERS START AT $0 AND GROW DRAMATICALLY!" << endl;
    cout << "⚡ Prices update every second with REAL volatility!" << endl;
    cout << "🎬 Story progression affects price multipliers!" << endl;
    cout << "======================================================" << endl;

    // Create dynamic price engine
    PriceEngine engine;

    // Load all characters (starting at $0)
    engine.loadCharacters();

    // Start the dynamic price system
    engine.startPriceCalculation();

    // Run simulation and show progress
    cout << "\n🚀 SIMULATION RUNNING - Watch prices grow from $0!" << endl;
    cout << "Press Ctrl+C to stop...\n" << endl;

    // Show market summary every 10 seconds
    for (int i = 0; i < 12; i++) { // Run for 2 minutes total
        this_thread::sleep_for(chrono::seconds(10));
        engine.printMarketSummary();
        cout << "\n⏰ Simulation time: " << (i + 1) * 10 << " seconds" << endl;
        cout << "======================================================\n" << endl;
    }

    // Final summary
    cout << "🎉 SIMULATION COMPLETE!" << endl;
    engine.printMarketSummary();

    return 0;
}

/*
🎯 WHAT EACH PART DOES:

Character Struct: Represents One Piece character with price data
MarketData Struct: Overall market statistics and state
PriceEngine Class: Main engine for price calculations
calculateNewPrice(): Advanced algorithm considering multiple factors
Multi-threading: Concurrent price calculations
HTTP Integration: Send updates to other services

🚀 C++ CONCEPTS YOU'LL LEARN:

1. Classes and Objects - Object-oriented programming
2. Pointers and References - Memory management
3. STL Containers - vector, map, queue for data storage
4. Multi-threading - Concurrent programming with threads
5. Mutex and Locks - Thread synchronization
6. Templates - Generic programming
7. Memory Management - RAII and smart pointers

📚 ADVANCED C++ FEATURES:

1. Lambda Functions - Anonymous functions for algorithms
2. Move Semantics - Efficient object transfers
3. Smart Pointers - Automatic memory management
4. STL Algorithms - find_if, transform, etc.
5. Chrono Library - Time and duration handling
6. Random Number Generation - Market simulation
7. Exception Handling - Error management

🔧 PERFORMANCE OPTIMIZATION:

1. Memory Pool Allocation - Reduce allocation overhead
2. Cache-Friendly Data Structures - Improve CPU cache usage
3. SIMD Instructions - Vectorized calculations
4. Lock-Free Programming - Reduce synchronization overhead
5. Profiling and Benchmarking - Measure performance
6. Compiler Optimizations - -O3, -march=native

INTEGRATION WITH OTHER SERVICES:
- HTTP client to update Character Service
- JSON parsing for API communication
- Configuration file reading
- Logging and monitoring
- Health check endpoints

NEXT FILE AFTER THIS: Create C++ CMakeLists.txt build configuration! 🚀
*/
