/*
🏴‍☠️ NEXT.JS FULL-STACK MASTERY - REACT + SERVER-SIDE
═══════════════════════════════════════════════════════════

🎯 WHAT YOU'LL LEARN BY CODING THIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ API Routes - Serverless backend endpoints
✅ Data Fetching - SSR, SSG, ISR strategies
✅ Middleware & Edge Functions - Request processing
✅ Server Components - React Server Components
✅ Authentication - NextAuth.js integration
✅ Database Integration - Prisma ORM
✅ Deployment - Vercel and production optimization
✅ Performance - Caching and optimization

💰 SALARY IMPACT: +$70K-?20K (Next.js is HOT in market)
🏢 COMPANIES: Vercel, Netflix, Hulu, TikTok, Twitch

📚 NEXT.JS CONCEPTS YOU'LL MASTER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔌 API ROUTES:
• File-based routing under /pages/api
• Serverless functions for backend logic
• Request/response handling
• Middleware and error handling

📊 DATA FETCHING STRATEGIES:
• getServerSideProps - Server-side rendering per request
• getStaticProps - Static generation at build time
• getStaticPaths - Dynamic static generation
• Incremental Static Regeneration (ISR)

⚡ MIDDLEWARE & EDGE:
• Edge functions for global performance
• Authentication middleware
• Redirects and rewrites
• Header manipulation

🧩 SERVER COMPONENTS:
• React Server Components
• Client vs Server component boundaries
• Streaming and Suspense
• Data fetching in components

🔧 NEXT.JS SYNTAX YOU'LL USE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. API ROUTES:
   // pages/api/characters/[id].js
   export default async function handler(req, res) {
       const { id } = req.query;
       
       if (req.method === 'GET') {
           const character = await getCharacter(id);
           res.status(200).json(character);
       } else {
           res.setHeader('Allow', ['GET']);
           res.status(405).end(`Method ${req.method} Not Allowed`);
       }
   }

2. SERVER-SIDE RENDERING:
   export async function getServerSideProps(context) {
       const characters = await fetchCharacters();
       
       return {
           props: {
               characters,
           },
       };
   }

3. STATIC GENERATION:
   export async function getStaticProps() {
       const characters = await fetchCharacters();
       
       return {
           props: {
               characters,
           },
           revalidate: 60, // ISR - revalidate every 60 seconds
       };
   }

4. MIDDLEWARE:
   // middleware.js
   import { NextResponse } from 'next/server';
   
   export function middleware(request) {
       if (request.nextUrl.pathname.startsWith('/api/admin')) {
           // Check authentication
           const token = request.cookies.get('auth-token');
           if (!token) {
               return NextResponse.redirect(new URL('/login', request.url));
           }
       }
   }
*/

// 🧪 HANDS-ON LAB 1: API ROUTES
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 API ROUTES EXPLAINED:
Next.js API routes provide a serverless backend within your React app.
Each file in pages/api becomes an endpoint. This is perfect for building
full-stack applications without separate backend servers.

REAL-WORLD EXAMPLE:
E-commerce site with product API, user authentication, payment processing,
and admin dashboard - all in one Next.js application.

IN ONE PIECE PROJECT:
Character management API, trading endpoints, price updates, user
authentication, real-time WebSocket connections.
*/

// TODO 1: BASIC API ROUTES
// YOUR CODE HERE - Create character API endpoints:


// TODO 2: DYNAMIC API ROUTES
// YOUR CODE HERE - Handle dynamic parameters:


// TODO 3: API MIDDLEWARE
// YOUR CODE HERE - Add authentication and validation:


// 🧪 HANDS-ON LAB 2: DATA FETCHING STRATEGIES
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 DATA FETCHING EXPLAINED:
Next.js offers multiple data fetching strategies for different use cases:
- SSR for dynamic content that changes per request
- SSG for static content that can be pre-built
- ISR for static content that updates periodically

REAL-WORLD EXAMPLE:
Blog with static posts (SSG), user dashboard (SSR), and product catalog
with periodic updates (ISR).

IN ONE PIECE PROJECT:
Character list (SSG), user portfolio (SSR), price data (ISR),
trading history (SSR).
*/

// TODO 4: SERVER-SIDE RENDERING
// YOUR CODE HERE - Implement SSR for dynamic content:


// TODO 5: STATIC GENERATION
// YOUR CODE HERE - Implement SSG for static content:


// TODO 6: INCREMENTAL STATIC REGENERATION
// YOUR CODE HERE - Implement ISR for periodic updates:


// 🧪 HANDS-ON LAB 3: AUTHENTICATION & SECURITY
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/*
📚 AUTHENTICATION EXPLAINED:
NextAuth.js provides easy authentication with multiple providers.
Combined with middleware, you can protect routes and API endpoints.

REAL-WORLD EXAMPLE:
Social media app with Google/GitHub login, protected user profiles,
admin dashboard, and API rate limiting.

IN ONE PIECE PROJECT:
User registration/login, protected trading features, admin character
management, secure API endpoints.
*/

// TODO 7: NEXTAUTH SETUP
// YOUR CODE HERE - Configure authentication:


// TODO 8: PROTECTED ROUTES
// YOUR CODE HERE - Protect pages and API routes:


// TODO 9: MIDDLEWARE AUTHENTICATION
// YOUR CODE HERE - Add authentication middleware:


/*
═══════════════════════════════════════════════════════════
🏆 COMPLETE CODE SOLUTION (SCROLL DOWN TO CHECK YOUR WORK)
═══════════════════════════════════════════════════════════
*/

// 🔥 COMPLETE NEXT.JS IMPLEMENTATION

// 1. API ROUTES IMPLEMENTATION

// pages/api/characters/index.js
export default async function charactersHandler(req, res) {
    const { method } = req;
    
    try {
        switch (method) {
            case 'GET':
                return await handleGetCharacters(req, res);
            case 'POST':
                return await handleCreateCharacter(req, res);
            default:
                res.setHeader('Allow', ['GET', 'POST']);
                return res.status(405).json({ error: `Method ${method} Not Allowed` });
        }
    } catch (error) {
        console.error('API Error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}

async function handleGetCharacters(req, res) {
    const { crew, limit = 10, page = 1 } = req.query;
    
    try {
        // Simulate database query
        let characters = await getCharactersFromDB();
        
        // Filter by crew if specified
        if (crew) {
            characters = characters.filter(char => 
                char.crew.toLowerCase().includes(crew.toLowerCase())
            );
        }
        
        // Pagination
        const startIndex = (page - 1) * limit;
        const endIndex = startIndex + parseInt(limit);
        const paginatedCharacters = characters.slice(startIndex, endIndex);
        
        return res.status(200).json({
            characters: paginatedCharacters,
            pagination: {
                total: characters.length,
                page: parseInt(page),
                limit: parseInt(limit),
                totalPages: Math.ceil(characters.length / limit)
            }
        });
    } catch (error) {
        console.error('Failed to fetch characters:', error);
        return res.status(500).json({ error: 'Failed to fetch characters' });
    }
}

async function handleCreateCharacter(req, res) {
    const { name, crew, bounty, description } = req.body;
    
    // Validation
    if (!name || !crew) {
        return res.status(400).json({ 
            error: 'Name and crew are required',
            details: { name: !name, crew: !crew }
        });
    }
    
    try {
        const newCharacter = {
            id: Date.now(), // In real app, use proper ID generation
            name,
            crew,
            bounty: parseInt(bounty) || 0,
            description: description || '',
            createdAt: new Date().toISOString(),
            isActive: true
        };
        
        // Save to database
        await saveCharacterToDB(newCharacter);
        
        return res.status(201).json({ 
            character: newCharacter,
            message: 'Character created successfully'
        });
    } catch (error) {
        console.error('Failed to create character:', error);
        return res.status(500).json({ error: 'Failed to create character' });
    }
}

// pages/api/characters/[id].js
export default async function characterHandler(req, res) {
    const { method, query: { id } } = req;
    
    try {
        switch (method) {
            case 'GET':
                return await handleGetCharacter(req, res, id);
            case 'PUT':
                return await handleUpdateCharacter(req, res, id);
            case 'DELETE':
                return await handleDeleteCharacter(req, res, id);
            default:
                res.setHeader('Allow', ['GET', 'PUT', 'DELETE']);
                return res.status(405).json({ error: `Method ${method} Not Allowed` });
        }
    } catch (error) {
        console.error('API Error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}

async function handleGetCharacter(req, res, id) {
    try {
        const character = await getCharacterFromDB(id);
        
        if (!character) {
            return res.status(404).json({ error: 'Character not found' });
        }
        
        return res.status(200).json({ character });
    } catch (error) {
        console.error('Failed to fetch character:', error);
        return res.status(500).json({ error: 'Failed to fetch character' });
    }
}

async function handleUpdateCharacter(req, res, id) {
    const updates = req.body;
    
    try {
        const character = await getCharacterFromDB(id);
        
        if (!character) {
            return res.status(404).json({ error: 'Character not found' });
        }
        
        const updatedCharacter = {
            ...character,
            ...updates,
            updatedAt: new Date().toISOString()
        };
        
        await updateCharacterInDB(id, updatedCharacter);
        
        return res.status(200).json({ 
            character: updatedCharacter,
            message: 'Character updated successfully'
        });
    } catch (error) {
        console.error('Failed to update character:', error);
        return res.status(500).json({ error: 'Failed to update character' });
    }
}

// pages/api/trading/portfolio.js
import { getSession } from 'next-auth/react';

export default async function portfolioHandler(req, res) {
    const session = await getSession({ req });
    
    if (!session) {
        return res.status(401).json({ error: 'Authentication required' });
    }
    
    const { method } = req;
    
    try {
        switch (method) {
            case 'GET':
                return await handleGetPortfolio(req, res, session.user.id);
            case 'POST':
                return await handleCreateTrade(req, res, session.user.id);
            default:
                res.setHeader('Allow', ['GET', 'POST']);
                return res.status(405).json({ error: `Method ${method} Not Allowed` });
        }
    } catch (error) {
        console.error('Portfolio API Error:', error);
        return res.status(500).json({ error: 'Internal Server Error' });
    }
}

async function handleGetPortfolio(req, res, userId) {
    try {
        const portfolio = await getUserPortfolio(userId);
        const totalValue = portfolio.reduce((sum, holding) => 
            sum + (holding.quantity * holding.currentPrice), 0
        );
        
        return res.status(200).json({
            portfolio,
            summary: {
                totalValue,
                totalHoldings: portfolio.length,
                lastUpdated: new Date().toISOString()
            }
        });
    } catch (error) {
        console.error('Failed to fetch portfolio:', error);
        return res.status(500).json({ error: 'Failed to fetch portfolio' });
    }
}

// 2. DATA FETCHING STRATEGIES IMPLEMENTATION

// pages/characters/index.js - Static Generation with ISR
import { useState } from 'react';
import Link from 'next/link';
import { GetStaticProps } from 'next';

export default function CharactersPage({ characters, lastUpdated }) {
    const [searchTerm, setSearchTerm] = useState('');
    
    const filteredCharacters = characters.filter(character =>
        character.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        character.crew.toLowerCase().includes(searchTerm.toLowerCase())
    );
    
    return (
        <div className="characters-page">
            <h1>🏴‍☠️ One Piece Characters</h1>
            <p>Last updated: {new Date(lastUpdated).toLocaleString()}</p>
            
            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search characters or crews..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="search-input"
                />
            </div>
            
            <div className="characters-grid">
                {filteredCharacters.map(character => (
                    <div key={character.id} className="character-card">
                        <h3>{character.name}</h3>
                        <p>Crew: {character.crew}</p>
                        <p>Bounty: ₿{character.bounty.toLocaleString()}</p>
                        <Link href={`/characters/${character.id}`}>
                            <a className="view-details">View Details</a>
                        </Link>
                    </div>
                ))}
            </div>
            
            <style jsx>{`
                .characters-page {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 2rem;
                }
                
                .search-input {
                    width: 100%;
                    max-width: 400px;
                    padding: 0.5rem;
                    margin-bottom: 2rem;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                
                .characters-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                    gap: 1rem;
                }
                
                .character-card {
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 1rem;
                    background: white;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                
                .view-details {
                    color: #0070f3;
                    text-decoration: none;
                }
                
                .view-details:hover {
                    text-decoration: underline;
                }
            `}</style>
        </div>
    );
}

export const getStaticProps: GetStaticProps = async () => {
    try {
        // Fetch characters data
        const characters = await getCharactersFromDB();
        
        return {
            props: {
                characters,
                lastUpdated: new Date().toISOString()
            },
            // Incremental Static Regeneration
            // Revalidate every 5 minutes
            revalidate: 300
        };
    } catch (error) {
        console.error('Failed to fetch characters for static generation:', error);
        
        return {
            props: {
                characters: [],
                lastUpdated: new Date().toISOString()
            },
            revalidate: 60 // Retry more frequently on error
        };
    }
};

// pages/characters/[id].js - Dynamic Static Generation
import { GetStaticProps, GetStaticPaths } from 'next';
import { useRouter } from 'next/router';

export default function CharacterPage({ character, error }) {
    const router = useRouter();
    
    if (router.isFallback) {
        return <div>Loading character...</div>;
    }
    
    if (error) {
        return (
            <div className="error-page">
                <h1>Character Not Found</h1>
                <p>{error}</p>
                <button onClick={() => router.back()}>Go Back</button>
            </div>
        );
    }
    
    return (
        <div className="character-detail">
            <button onClick={() => router.back()} className="back-button">
                ← Back to Characters
            </button>
            
            <div className="character-header">
                <h1>{character.name}</h1>
                <p className="crew">Member of {character.crew}</p>
            </div>
            
            <div className="character-stats">
                <div className="stat">
                    <label>Bounty:</label>
                    <span>₿{character.bounty.toLocaleString()}</span>
                </div>
                <div className="stat">
                    <label>Status:</label>
                    <span className={character.isActive ? 'active' : 'inactive'}>
                        {character.isActive ? 'Active' : 'Inactive'}
                    </span>
                </div>
                <div className="stat">
                    <label>First Appearance:</label>
                    <span>{new Date(character.createdAt).toLocaleDateString()}</span>
                </div>
            </div>
            
            {character.description && (
                <div className="character-description">
                    <h3>About {character.name}</h3>
                    <p>{character.description}</p>
                </div>
            )}
            
            <style jsx>{`
                .character-detail {
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 2rem;
                }
                
                .back-button {
                    background: #0070f3;
                    color: white;
                    border: none;
                    padding: 0.5rem 1rem;
                    border-radius: 4px;
                    cursor: pointer;
                    margin-bottom: 2rem;
                }
                
                .character-header h1 {
                    margin: 0;
                    color: #333;
                }
                
                .crew {
                    color: #666;
                    font-size: 1.1rem;
                    margin: 0.5rem 0;
                }
                
                .character-stats {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 1rem;
                    margin: 2rem 0;
                }
                
                .stat {
                    padding: 1rem;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    background: #f9f9f9;
                }
                
                .stat label {
                    font-weight: bold;
                    display: block;
                    margin-bottom: 0.5rem;
                }
                
                .active {
                    color: green;
                }
                
                .inactive {
                    color: red;
                }
                
                .character-description {
                    margin-top: 2rem;
                    padding: 1rem;
                    background: #f5f5f5;
                    border-radius: 4px;
                }
            `}</style>
        </div>
    );
}

export const getStaticPaths: GetStaticPaths = async () => {
    try {
        // Get all character IDs for static generation
        const characters = await getCharactersFromDB();
        const paths = characters.map(character => ({
            params: { id: character.id.toString() }
        }));
        
        return {
            paths,
            // Enable ISR for new characters
            fallback: 'blocking'
        };
    } catch (error) {
        console.error('Failed to generate static paths:', error);
        
        return {
            paths: [],
            fallback: 'blocking'
        };
    }
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
    try {
        const character = await getCharacterFromDB(params.id);
        
        if (!character) {
            return {
                props: {
                    error: 'Character not found'
                },
                revalidate: 60
            };
        }
        
        return {
            props: {
                character
            },
            revalidate: 300 // Revalidate every 5 minutes
        };
    } catch (error) {
        console.error('Failed to fetch character:', error);
        
        return {
            props: {
                error: 'Failed to load character data'
            },
            revalidate: 60
        };
    }
};

// pages/dashboard.js - Server-Side Rendering for user data
import { getSession } from 'next-auth/react';
import { GetServerSideProps } from 'next';

export default function Dashboard({ user, portfolio, recentTrades }) {
    const totalValue = portfolio.reduce((sum, holding) => 
        sum + (holding.quantity * holding.currentPrice), 0
    );
    
    return (
        <div className="dashboard">
            <h1>Welcome back, {user.name}! 🏴‍☠️</h1>
            
            <div className="dashboard-stats">
                <div className="stat-card">
                    <h3>Portfolio Value</h3>
                    <p className="value">₿{totalValue.toLocaleString()}</p>
                </div>
                <div className="stat-card">
                    <h3>Holdings</h3>
                    <p className="value">{portfolio.length}</p>
                </div>
                <div className="stat-card">
                    <h3>Recent Trades</h3>
                    <p className="value">{recentTrades.length}</p>
                </div>
            </div>
            
            <div className="dashboard-sections">
                <section className="portfolio-section">
                    <h2>Your Portfolio</h2>
                    <div className="holdings-list">
                        {portfolio.map(holding => (
                            <div key={holding.characterId} className="holding-item">
                                <span className="character-name">{holding.characterName}</span>
                                <span className="quantity">{holding.quantity} shares</span>
                                <span className="value">₿{(holding.quantity * holding.currentPrice).toLocaleString()}</span>
                            </div>
                        ))}
                    </div>
                </section>
                
                <section className="trades-section">
                    <h2>Recent Trades</h2>
                    <div className="trades-list">
                        {recentTrades.map(trade => (
                            <div key={trade.id} className="trade-item">
                                <span className={`trade-type ${trade.type}`}>{trade.type.toUpperCase()}</span>
                                <span className="character-name">{trade.characterName}</span>
                                <span className="quantity">{trade.quantity} shares</span>
                                <span className="price">₿{trade.price}</span>
                                <span className="date">{new Date(trade.createdAt).toLocaleDateString()}</span>
                            </div>
                        ))}
                    </div>
                </section>
            </div>
            
            <style jsx>{`
                .dashboard {
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 2rem;
                }
                
                .dashboard-stats {
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                    gap: 1rem;
                    margin: 2rem 0;
                }
                
                .stat-card {
                    padding: 1.5rem;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    text-align: center;
                }
                
                .value {
                    font-size: 2rem;
                    font-weight: bold;
                    color: #0070f3;
                    margin: 0;
                }
                
                .dashboard-sections {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 2rem;
                    margin-top: 2rem;
                }
                
                .holding-item, .trade-item {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 1rem;
                    border-bottom: 1px solid #eee;
                }
                
                .trade-type.buy {
                    color: green;
                }
                
                .trade-type.sell {
                    color: red;
                }
                
                @media (max-width: 768px) {
                    .dashboard-sections {
                        grid-template-columns: 1fr;
                    }
                }
            `}</style>
        </div>
    );
}

export const getServerSideProps: GetServerSideProps = async (context) => {
    const session = await getSession(context);
    
    if (!session) {
        return {
            redirect: {
                destination: '/login',
                permanent: false,
            },
        };
    }
    
    try {
        // Fetch user-specific data
        const [portfolio, recentTrades] = await Promise.all([
            getUserPortfolio(session.user.id),
            getRecentTrades(session.user.id, 10)
        ]);
        
        return {
            props: {
                user: session.user,
                portfolio,
                recentTrades
            }
        };
    } catch (error) {
        console.error('Failed to fetch dashboard data:', error);
        
        return {
            props: {
                user: session.user,
                portfolio: [],
                recentTrades: [],
                error: 'Failed to load dashboard data'
            }
        };
    }
};

// Database helper functions (would be in separate files)
async function getCharactersFromDB() {
    // In real app, this would connect to your database
    return [
        {
            id: 1,
            name: 'Monkey D. Luffy',
            crew: 'Straw Hat Pirates',
            bounty: 3000000000,
            description: 'Captain of the Straw Hat Pirates and future Pirate King',
            isActive: true,
            createdAt: '2023-01-01T00:00:00Z'
        },
        {
            id: 2,
            name: 'Roronoa Zoro',
            crew: 'Straw Hat Pirates',
            bounty: 1111000000,
            description: 'Swordsman of the Straw Hat Pirates',
            isActive: true,
            createdAt: '2023-01-01T00:00:00Z'
        },
        {
            id: 3,
            name: 'Nami',
            crew: 'Straw Hat Pirates',
            bounty: 366000000,
            description: 'Navigator of the Straw Hat Pirates',
            isActive: true,
            createdAt: '2023-01-01T00:00:00Z'
        }
    ];
}

async function getCharacterFromDB(id) {
    const characters = await getCharactersFromDB();
    return characters.find(char => char.id === parseInt(id));
}

async function saveCharacterToDB(character) {
    // In real app, save to database
    console.log('Saving character:', character);
    return character;
}

async function updateCharacterInDB(id, updates) {
    // In real app, update in database
    console.log('Updating character:', id, updates);
    return updates;
}

async function getUserPortfolio(userId) {
    // In real app, fetch from database
    return [
        {
            characterId: 1,
            characterName: 'Monkey D. Luffy',
            quantity: 100,
            currentPrice: 150.50,
            purchasePrice: 120.00
        },
        {
            characterId: 2,
            characterName: 'Roronoa Zoro',
            quantity: 50,
            currentPrice: 95.25,
            purchasePrice: 80.00
        }
    ];
}

async function getRecentTrades(userId, limit) {
    // In real app, fetch from database
    return [
        {
            id: 1,
            type: 'buy',
            characterName: 'Monkey D. Luffy',
            quantity: 10,
            price: 150.50,
            createdAt: '2023-12-01T10:00:00Z'
        },
        {
            id: 2,
            type: 'sell',
            characterName: 'Nami',
            quantity: 5,
            price: 75.25,
            createdAt: '2023-11-30T15:30:00Z'
        }
    ];
}

// ===============================================================================
// 🏴‍☠️ CONGRATULATIONS! YOU'VE MASTERED NEXT.JS FULL-STACK DEVELOPMENT! 🎉
// ===============================================================================

console.log('\n🏴‍☠️ CONGRATULATIONS! YOU\'VE MASTERED NEXT.JS FULL-STACK DEVELOPMENT! 🎉');
console.log('===============================================================================');

console.log('\n🎯 WHAT YOU\'VE ACCOMPLISHED:');
console.log('✅ Mastered Next.js App Router and server-side rendering');
console.log('✅ Implemented full-stack authentication with NextAuth.js');
console.log('✅ Built API routes with proper error handling and validation');
console.log('✅ Created dynamic pages with static generation and ISR');
console.log('✅ Added middleware for authentication and security');
console.log('✅ Applied Next.js patterns used by Vercel, TikTok, and Netflix');

console.log('\n💰 SALARY IMPACT: +$70K-$140K (Next.js is the leading React framework)');
console.log('🏢 COMPANIES: Vercel, TikTok, Netflix, Twitch, Hulu, all modern React companies');

console.log('\n===============================================================================');
console.log('🎯 NOW IMPLEMENT THIS IN YOUR ONE PIECE PROJECT!');
console.log('===============================================================================');

console.log('\n🚀 STEP 1: MIGRATE YOUR REACT APP TO NEXT.JS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📁 Create new Next.js project: frontend-nextjs/');
console.log('');
console.log('🎯 WHAT TO DO:');
console.log('1. Create new Next.js project with App Router');
console.log('2. Migrate your React components to Next.js pages');
console.log('3. Add server-side rendering for character data');
console.log('4. Implement API routes for backend integration');
console.log('5. Add authentication with NextAuth.js');
console.log('');
console.log('📚 REFERENCE: Use the Next.js patterns from this module');

console.log('\n🚀 STEP 2: CREATE NEXT.JS PROJECT STRUCTURE');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 SETUP COMMANDS:');
console.log('');
console.log('# Create Next.js project');
console.log('npx create-next-app@latest frontend-nextjs --typescript --tailwind --eslint --app');
console.log('cd frontend-nextjs');
console.log('');
console.log('# Install additional dependencies');
console.log('npm install next-auth prisma @prisma/client');
console.log('npm install @types/node @types/react @types/react-dom');
console.log('');
console.log('# Project structure:');
console.log('frontend-nextjs/');
console.log('├── app/');
console.log('│   ├── (auth)/');
console.log('│   │   ├── login/');
console.log('│   │   │   └── page.tsx');
console.log('│   │   └── register/');
console.log('│   │       └── page.tsx');
console.log('│   ├── characters/');
console.log('│   │   ├── [id]/');
console.log('│   │   │   └── page.tsx');
console.log('│   │   └── page.tsx');
console.log('│   ├── dashboard/');
console.log('│   │   └── page.tsx');
console.log('│   ├── api/');
console.log('│   │   ├── auth/');
console.log('│   │   │   └── [...nextauth]/');
console.log('│   │   │       └── route.ts');
console.log('│   │   ├── characters/');
console.log('│   │   │   ├── [id]/');
console.log('│   │   │   │   └── route.ts');
console.log('│   │   │   └── route.ts');
console.log('│   │   └── trades/');
console.log('│   │       └── route.ts');
console.log('│   ├── globals.css');
console.log('│   ├── layout.tsx');
console.log('│   └── page.tsx');
console.log('├── components/');
console.log('│   ├── Characters/');
console.log('│   ├── Trading/');
console.log('│   └── UI/');
console.log('├── lib/');
console.log('│   ├── auth.ts');
console.log('│   ├── db.ts');
console.log('│   └── utils.ts');
console.log('└── middleware.ts');
console.log('');
console.log('🔧 COPY FROM THIS MODULE:');
console.log('- Next.js project structure (lines 50-150)');
console.log('- App Router patterns (lines 200-300)');
console.log('- API routes implementation (lines 400-500)');

console.log('\n🚀 STEP 3: IMPLEMENT SERVER-SIDE RENDERING FOR CHARACTERS');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: app/characters/page.tsx');
console.log('');
console.log('import { Suspense } from "react";');
console.log('import CharacterList from "@/components/Characters/CharacterList";');
console.log('import LoadingSkeleton from "@/components/UI/LoadingSkeleton";');
console.log('');
console.log('interface Character {');
console.log('    id: number;');
console.log('    name: string;');
console.log('    crew: string;');
console.log('    bounty: number;');
console.log('    price: number;');
console.log('    priceChange: number;');
console.log('}');
console.log('');
console.log('async function getCharacters(): Promise<Character[]> {');
console.log('    // Server-side data fetching');
console.log('    const res = await fetch(`${process.env.API_URL}/api/characters`, {');
console.log('        next: { revalidate: 60 } // ISR: revalidate every 60 seconds');
console.log('    });');
console.log('    ');
console.log('    if (!res.ok) {');
console.log('        throw new Error("Failed to fetch characters");');
console.log('    }');
console.log('    ');
console.log('    return res.json();');
console.log('}');
console.log('');
console.log('export default async function CharactersPage() {');
console.log('    const characters = await getCharacters();');
console.log('    ');
console.log('    return (');
console.log('        <div className="container mx-auto px-4 py-8">');
console.log('            <h1 className="text-3xl font-bold mb-8">🏴‍☠️ One Piece Characters</h1>');
console.log('            ');
console.log('            <Suspense fallback={<LoadingSkeleton />}>');
console.log('                <CharacterList characters={characters} />');
console.log('            </Suspense>');
console.log('        </div>');
console.log('    );');
console.log('}');
console.log('');
console.log('// Generate static params for dynamic routes');
console.log('export async function generateStaticParams() {');
console.log('    const characters = await getCharacters();');
console.log('    ');
console.log('    return characters.map((character) => ({');
console.log('        id: character.id.toString()');
console.log('    }));');
console.log('}');
console.log('');
console.log('🔧 NEXT.JS BENEFITS:');
console.log('- Server-side rendering for better SEO');
console.log('- Incremental Static Regeneration (ISR) for performance');
console.log('- Automatic code splitting and optimization');
console.log('- Built-in image optimization');

console.log('\n🚀 STEP 4: CREATE API ROUTES FOR BACKEND INTEGRATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: app/api/characters/route.ts');
console.log('');
console.log('import { NextRequest, NextResponse } from "next/server";');
console.log('import { getServerSession } from "next-auth";');
console.log('import { authOptions } from "@/lib/auth";');
console.log('');
console.log('export async function GET(request: NextRequest) {');
console.log('    try {');
console.log('        // Forward request to your API Gateway');
console.log('        const response = await fetch(`${process.env.API_GATEWAY_URL}/api/characters`, {');
console.log('            headers: {');
console.log('                "Content-Type": "application/json"');
console.log('            }');
console.log('        });');
console.log('        ');
console.log('        if (!response.ok) {');
console.log('            throw new Error("Failed to fetch characters");');
console.log('        }');
console.log('        ');
console.log('        const characters = await response.json();');
console.log('        return NextResponse.json(characters);');
console.log('    } catch (error) {');
console.log('        console.error("API Error:", error);');
console.log('        return NextResponse.json(');
console.log('            { error: "Failed to fetch characters" },');
console.log('            { status: 500 }');
console.log('        );');
console.log('    }');
console.log('}');
console.log('');
console.log('export async function POST(request: NextRequest) {');
console.log('    try {');
console.log('        // Check authentication');
console.log('        const session = await getServerSession(authOptions);');
console.log('        if (!session) {');
console.log('            return NextResponse.json(');
console.log('                { error: "Unauthorized" },');
console.log('                { status: 401 }');
console.log('            );');
console.log('        }');
console.log('        ');
console.log('        const body = await request.json();');
console.log('        ');
console.log('        // Forward to API Gateway with authentication');
console.log('        const response = await fetch(`${process.env.API_GATEWAY_URL}/api/characters`, {');
console.log('            method: "POST",');
console.log('            headers: {');
console.log('                "Content-Type": "application/json",');
console.log('                "Authorization": `Bearer ${session.accessToken}`');
console.log('            },');
console.log('            body: JSON.stringify(body)');
console.log('        });');
console.log('        ');
console.log('        if (!response.ok) {');
console.log('            throw new Error("Failed to create character");');
console.log('        }');
console.log('        ');
console.log('        const character = await response.json();');
console.log('        return NextResponse.json(character, { status: 201 });');
console.log('    } catch (error) {');
console.log('        console.error("API Error:", error);');
console.log('        return NextResponse.json(');
console.log('            { error: "Failed to create character" },');
console.log('            { status: 500 }');
console.log('        );');
console.log('    }');
console.log('}');
console.log('');
console.log('🔧 API ROUTE BENEFITS:');
console.log('- Server-side API integration');
console.log('- Built-in authentication handling');
console.log('- Type-safe request/response handling');
console.log('- Automatic error handling and logging');

console.log('\n🚀 STEP 5: ADD NEXTAUTH.JS AUTHENTICATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: lib/auth.ts');
console.log('');
console.log('import { NextAuthOptions } from "next-auth";');
console.log('import CredentialsProvider from "next-auth/providers/credentials";');
console.log('import { compare } from "bcryptjs";');
console.log('');
console.log('export const authOptions: NextAuthOptions = {');
console.log('    providers: [');
console.log('        CredentialsProvider({');
console.log('            name: "credentials",');
console.log('            credentials: {');
console.log('                email: { label: "Email", type: "email" },');
console.log('                password: { label: "Password", type: "password" }');
console.log('            },');
console.log('            async authorize(credentials) {');
console.log('                if (!credentials?.email || !credentials?.password) {');
console.log('                    return null;');
console.log('                }');
console.log('                ');
console.log('                // Call your API Gateway for authentication');
console.log('                const response = await fetch(`${process.env.API_GATEWAY_URL}/api/auth/login`, {');
console.log('                    method: "POST",');
console.log('                    headers: { "Content-Type": "application/json" },');
console.log('                    body: JSON.stringify({');
console.log('                        email: credentials.email,');
console.log('                        password: credentials.password');
console.log('                    })');
console.log('                });');
console.log('                ');
console.log('                if (!response.ok) {');
console.log('                    return null;');
console.log('                }');
console.log('                ');
console.log('                const { user, token } = await response.json();');
console.log('                ');
console.log('                return {');
console.log('                    id: user.id,');
console.log('                    email: user.email,');
console.log('                    name: user.name,');
console.log('                    role: user.role,');
console.log('                    accessToken: token');
console.log('                };');
console.log('            }');
console.log('        })');
console.log('    ],');
console.log('    callbacks: {');
console.log('        async jwt({ token, user }) {');
console.log('            if (user) {');
console.log('                token.accessToken = user.accessToken;');
console.log('                token.role = user.role;');
console.log('            }');
console.log('            return token;');
console.log('        },');
console.log('        async session({ session, token }) {');
console.log('            session.accessToken = token.accessToken;');
console.log('            session.user.role = token.role;');
console.log('            return session;');
console.log('        }');
console.log('    },');
console.log('    pages: {');
console.log('        signIn: "/login",');
console.log('        signUp: "/register"');
console.log('    },');
console.log('    session: {');
console.log('        strategy: "jwt"');
console.log('    }');
console.log('};');
console.log('');
console.log('📝 CREATE: app/api/auth/[...nextauth]/route.ts');
console.log('');
console.log('import NextAuth from "next-auth";');
console.log('import { authOptions } from "@/lib/auth";');
console.log('');
console.log('const handler = NextAuth(authOptions);');
console.log('');
console.log('export { handler as GET, handler as POST };');
console.log('');
console.log('🔧 NEXTAUTH.JS BENEFITS:');
console.log('- Built-in authentication flows');
console.log('- Session management');
console.log('- Multiple provider support');
console.log('- Secure JWT handling');

console.log('\n🚀 STEP 6: ADD MIDDLEWARE FOR ROUTE PROTECTION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('📝 CREATE: middleware.ts');
console.log('');
console.log('import { withAuth } from "next-auth/middleware";');
console.log('import { NextResponse } from "next/server";');
console.log('');
console.log('export default withAuth(');
console.log('    function middleware(req) {');
console.log('        // Check role-based access');
console.log('        if (req.nextUrl.pathname.startsWith("/admin") && req.nextauth.token?.role !== "admin") {');
console.log('            return NextResponse.rewrite(new URL("/unauthorized", req.url));');
console.log('        }');
console.log('        ');
console.log('        if (req.nextUrl.pathname.startsWith("/dashboard") && !req.nextauth.token) {');
console.log('            return NextResponse.rewrite(new URL("/login", req.url));');
console.log('        }');
console.log('    },');
console.log('    {');
console.log('        callbacks: {');
console.log('            authorized: ({ token }) => !!token');
console.log('        }');
console.log('    }');
console.log(');');
console.log('');
console.log('export const config = {');
console.log('    matcher: [');
console.log('        "/dashboard/:path*",');
console.log('        "/admin/:path*",');
console.log('        "/api/protected/:path*"');
console.log('    ]');
console.log('};');
console.log('');
console.log('🔧 MIDDLEWARE BENEFITS:');
console.log('- Route-level authentication');
console.log('- Role-based access control');
console.log('- Automatic redirects');
console.log('- Server-side protection');

console.log('\n🚀 STEP 7: TEST YOUR NEXT.JS IMPLEMENTATION');
console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
console.log('🧪 TESTING STEPS:');
console.log('');
console.log('1. Start your Next.js development server:');
console.log('   cd frontend-nextjs');
console.log('   npm run dev');
console.log('');
console.log('2. Test server-side rendering:');
console.log('   # Visit http://localhost:3000/characters');
console.log('   # View page source - should show pre-rendered HTML with character data');
console.log('');
console.log('3. Test API routes:');
console.log('   curl http://localhost:3000/api/characters');
console.log('   # Should return character data from your API Gateway');
console.log('');
console.log('4. Test authentication:');
console.log('   # Visit http://localhost:3000/login');
console.log('   # Try logging in with valid credentials');
console.log('   # Should redirect to dashboard after successful login');
console.log('');
console.log('5. Test protected routes:');
console.log('   # Visit http://localhost:3000/dashboard without login');
console.log('   # Should redirect to login page');
console.log('');
console.log('6. Test ISR (Incremental Static Regeneration):');
console.log('   # Update character data in your API');
console.log('   # Refresh /characters page after 60 seconds');
console.log('   # Should show updated data');
console.log('');
console.log('✅ SUCCESS CRITERIA:');
console.log('- Next.js app starts without errors');
console.log('- Server-side rendering works (check page source)');
console.log('- API routes successfully proxy to your API Gateway');
console.log('- Authentication flow works end-to-end');
console.log('- Protected routes redirect unauthenticated users');
console.log('- ISR updates data automatically');

console.log('\n===============================================================================');
console.log('🔗 HOW THIS CONNECTS TO OTHER LEARNING MODULES');
console.log('===============================================================================');

console.log('\n🧩 MODULE CONNECTIONS:');
console.log('');
console.log('📚 Module 19 (React) → Next.js is built on React and uses all React patterns');
console.log('📚 Module 18 (TypeScript) → Next.js has excellent TypeScript integration');
console.log('📚 Module 16 (Node.js) → Next.js API routes run on Node.js and integrate with your API Gateway');
console.log('📚 Module 7 (Security) → NextAuth.js provides secure authentication and session management');
console.log('📚 Module 11 (APIs) → Next.js API routes act as a proxy layer to your microservices');
console.log('📚 Module 6 (System Design) → Next.js provides the frontend layer in your microservices architecture');

console.log('\n🎯 NEXT MODULES TO COMPLETE:');
console.log('1. Module 18: Add comprehensive TypeScript to your Next.js application');
console.log('2. Module 7: Implement advanced security features with NextAuth.js');
console.log('3. Module 6: Design the complete system architecture with Next.js as the frontend');

console.log('\n📚 RECOMMENDED RESOURCES FOR CONTINUED LEARNING:');
console.log('🔗 Next.js Documentation: https://nextjs.org/docs');
console.log('🔗 NextAuth.js: https://next-auth.js.org/');
console.log('🔗 Next.js + TypeScript: https://nextjs.org/docs/basic-features/typescript');
console.log('🔗 Next.js Deployment: https://nextjs.org/docs/deployment');

console.log('\n🏴‍☠️ YOU\'RE NOW READY TO BUILD PRODUCTION-READY FULL-STACK APPLICATIONS! ⚔️');
console.log('📖 REFERENCE: Check MASTER-BLUEPRINT-ARCHITECTURE.md for the complete system overview!');
