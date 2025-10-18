# 🏴‍☠️ REACT & NEXT.JS FRONTEND MASTERY - COMPLETE TUTORIAL
## Build Modern Web Applications Like a True Pirate Captain

---

# 🎯 **WHAT IS REACT & NEXT.JS AND WHY DO WE NEED THEM?**

## **🤔 THE PROBLEM THEY SOLVE**

**Before React & Next.js (The Dark Ages):**
```html
<!-- Vanilla HTML/JavaScript - Nightmare to maintain -->
<div id="character-list"></div>
<script>
  // Manually manipulate DOM
  function updateCharacterList(characters) {
    const container = document.getElementById('character-list');
    container.innerHTML = ''; // Clear everything
    
    characters.forEach(character => {
      const div = document.createElement('div');
      div.innerHTML = `
        <h3>${character.name}</h3>
        <p>Bounty: ${character.bounty}</p>
        <button onclick="deleteCharacter('${character.id}')">Delete</button>
      `;
      container.appendChild(div);
    });
  }
  
  // State management nightmare
  let characters = [];
  let loading = false;
  let error = null;
  // ... hundreds of global variables
</script>
```

**PROBLEMS:**
❌ **DOM Manipulation Hell** - Manually updating HTML elements everywhere  
❌ **State Management Chaos** - Global variables scattered throughout code  
❌ **No Component Reusability** - Copy-paste code for similar UI elements  
❌ **SEO Problems** - Search engines can't see JavaScript-generated content  
❌ **Performance Issues** - Entire page re-renders on every change  
❌ **Developer Experience** - No hot reload, debugging nightmares  

## **✅ REACT & NEXT.JS TO THE RESCUE**

**With React & Next.js:**
```tsx
// Modern React Component - Clean and Maintainable
import { useState, useEffect } from 'react';

interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
}

export default function CharacterList() {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchCharacters();
  }, []);

  const fetchCharacters = async () => {
    try {
      const response = await fetch('/api/characters');
      const data = await response.json();
      setCharacters(data);
    } catch (err) {
      setError('Failed to fetch characters');
    } finally {
      setLoading(false);
    }
  };

  if (loading) return <div>Loading pirates...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="character-grid">
      {characters.map(character => (
        <CharacterCard 
          key={character.id} 
          character={character} 
          onDelete={() => deleteCharacter(character.id)}
        />
      ))}
    </div>
  );
}
```

**BENEFITS:**
✅ **Component-Based Architecture** - Reusable, maintainable UI pieces  
✅ **Declarative Programming** - Describe what UI should look like, not how to build it  
✅ **Automatic State Management** - React handles DOM updates efficiently  
✅ **Server-Side Rendering** - Next.js makes your app SEO-friendly and fast  
✅ **Amazing Developer Experience** - Hot reload, TypeScript support, debugging tools  
✅ **Performance Optimization** - Virtual DOM, code splitting, image optimization  

---

# 📚 **LEARNING OBJECTIVES - WHAT YOU'LL MASTER**

By the end of this module, you'll be able to:

## **🎯 REACT MASTERY:**
✅ **Build reusable components** with props, state, and lifecycle methods  
✅ **Manage complex state** with useState, useReducer, and Context API  
✅ **Handle side effects** with useEffect and custom hooks  
✅ **Optimize performance** with useMemo, useCallback, and React.memo  
✅ **Handle forms and validation** with controlled components and libraries  

## **🎯 NEXT.JS MASTERY:**
✅ **Build full-stack applications** with API routes and server-side rendering  
✅ **Implement routing** with App Router and dynamic routes  
✅ **Optimize performance** with image optimization, code splitting, and caching  
✅ **Deploy applications** to Vercel, Netlify, and other platforms  
✅ **Handle authentication** with NextAuth.js and JWT tokens  

## **🎯 INTEGRATION MASTERY:**
✅ **Connect to REST APIs** with fetch, Axios, and SWR  
✅ **Implement real-time features** with WebSockets and Server-Sent Events  
✅ **Style applications** with Tailwind CSS, CSS Modules, and styled-components  
✅ **Test components** with Jest, React Testing Library, and Playwright  

---

# 🚀 **LESSON 1: REACT FUNDAMENTALS - COMPONENTS AND JSX**

## **🔍 WHAT IS REACT?**

React is a **JavaScript library for building user interfaces** - think of it as "LEGO blocks for web pages."

### **📊 TRADITIONAL WEB VS REACT COMPARISON:**

```html
<!-- TRADITIONAL WEB (Imperative) -->
<div id="counter">0</div>
<button id="increment">+</button>
<button id="decrement">-</button>

<script>
  let count = 0;
  const counterDiv = document.getElementById('counter');
  const incrementBtn = document.getElementById('increment');
  const decrementBtn = document.getElementById('decrement');
  
  incrementBtn.addEventListener('click', () => {
    count++;
    counterDiv.textContent = count; // Manual DOM update
  });
  
  decrementBtn.addEventListener('click', () => {
    count--;
    counterDiv.textContent = count; // Manual DOM update
  });
</script>
```

```tsx
// REACT (Declarative)
import { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <div>{count}</div>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  );
}
// React automatically updates DOM when state changes!
```

## **📝 JSX - JAVASCRIPT + HTML MAGIC**

JSX lets you write HTML-like syntax in JavaScript:

```tsx
// JSX looks like HTML but it's actually JavaScript
const element = <h1>Hello, One Piece!</h1>;

// JSX compiles to regular JavaScript function calls
const element = React.createElement('h1', null, 'Hello, One Piece!');

// JSX with expressions (anything in {} is JavaScript)
const character = 'Luffy';
const bounty = 3000000000;

const characterCard = (
  <div className="character-card">
    <h2>{character}</h2>
    <p>Bounty: {bounty.toLocaleString()} berries</p>
    <p>Status: {bounty > 1000000000 ? 'Emperor Level' : 'Rising Star'}</p>
    {/* This is a comment in JSX */}
  </div>
);
```

## **🧩 COMPONENTS - BUILDING BLOCKS OF REACT**

### **FUNCTIONAL COMPONENTS (Modern Way):**

```tsx
// Simple component with no props
function WelcomeMessage() {
  return <h1>Welcome to the Grand Line!</h1>;
}

// Component with props (like function parameters)
interface CharacterProps {
  name: string;
  bounty: number;
  crew: string;
  devilFruit?: string;
}

function CharacterCard({ name, bounty, crew, devilFruit }: CharacterProps) {
  return (
    <div className="character-card">
      <h3>{name}</h3>
      <p><strong>Crew:</strong> {crew}</p>
      <p><strong>Bounty:</strong> {bounty.toLocaleString()} berries</p>
      {devilFruit && <p><strong>Devil Fruit:</strong> {devilFruit}</p>}
    </div>
  );
}

// Using the component
function App() {
  return (
    <div>
      <WelcomeMessage />
      <CharacterCard 
        name="Monkey D. Luffy"
        bounty={3000000000}
        crew="Straw Hat Pirates"
        devilFruit="Gomu Gomu no Mi"
      />
      <CharacterCard 
        name="Roronoa Zoro"
        bounty={1111000000}
        crew="Straw Hat Pirates"
      />
    </div>
  );
}
```

### **COMPONENT COMPOSITION:**

```tsx
// Small, focused components
function Avatar({ src, alt }: { src: string; alt: string }) {
  return <img src={src} alt={alt} className="avatar" />;
}

function UserInfo({ name, role }: { name: string; role: string }) {
  return (
    <div className="user-info">
      <h4>{name}</h4>
      <span className="role">{role}</span>
    </div>
  );
}

// Compose them into larger components
function UserCard({ user }: { user: { name: string; role: string; avatar: string } }) {
  return (
    <div className="user-card">
      <Avatar src={user.avatar} alt={user.name} />
      <UserInfo name={user.name} role={user.role} />
    </div>
  );
}

// Even larger composition
function UserList({ users }: { users: User[] }) {
  return (
    <div className="user-list">
      {users.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}
```

---

# 🎨 **LESSON 3: STYLING AND UI COMPONENTS**

## **🔍 STYLING APPROACHES IN REACT**

### **📊 CSS MODULES (Scoped CSS):**

```css
/* CharacterCard.module.css */
.card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  padding: 20px;
  margin: 10px;
  color: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.name {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.bounty {
  font-size: 1.2rem;
  color: #ffd700;
}

.crew {
  font-style: italic;
  opacity: 0.9;
}
```

```tsx
// CharacterCard.tsx
import styles from './CharacterCard.module.css';

interface CharacterCardProps {
  character: {
    id: string;
    name: string;
    bounty: number;
    crew: string;
  };
}

function CharacterCard({ character }: CharacterCardProps) {
  return (
    <div className={styles.card}>
      <h3 className={styles.name}>{character.name}</h3>
      <p className={styles.bounty}>
        💰 {character.bounty.toLocaleString()} berries
      </p>
      <p className={styles.crew}>⚓ {character.crew}</p>
    </div>
  );
}
```

### **📊 TAILWIND CSS (Utility-First):**

```tsx
// Same component with Tailwind CSS
function CharacterCard({ character }: CharacterCardProps) {
  return (
    <div className="bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl p-6 m-3 text-white shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300">
      <h3 className="text-xl font-bold mb-2">{character.name}</h3>
      <p className="text-yellow-300 text-lg">
        💰 {character.bounty.toLocaleString()} berries
      </p>
      <p className="italic opacity-90">⚓ {character.crew}</p>
    </div>
  );
}
```

### **📊 STYLED-COMPONENTS (CSS-in-JS):**

```tsx
import styled from 'styled-components';

const Card = styled.div`
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 12px;
  padding: 20px;
  margin: 10px;
  color: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
`;

const Name = styled.h3`
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 10px;
`;

const Bounty = styled.p`
  font-size: 1.2rem;
  color: #ffd700;
`;

const Crew = styled.p`
  font-style: italic;
  opacity: 0.9;
`;

function CharacterCard({ character }: CharacterCardProps) {
  return (
    <Card>
      <Name>{character.name}</Name>
      <Bounty>💰 {character.bounty.toLocaleString()} berries</Bounty>
      <Crew>⚓ {character.crew}</Crew>
    </Card>
  );
}
```

## **🎨 BUILDING A COMPLETE UI COMPONENT LIBRARY**

```tsx
// Button.tsx - Reusable button component
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  loading?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
}

function Button({
  variant = 'primary',
  size = 'medium',
  disabled = false,
  loading = false,
  children,
  onClick
}: ButtonProps) {
  const baseClasses = 'font-semibold rounded-lg transition-all duration-200 focus:outline-none focus:ring-2';

  const variantClasses = {
    primary: 'bg-blue-600 hover:bg-blue-700 text-white focus:ring-blue-500',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-500',
    danger: 'bg-red-600 hover:bg-red-700 text-white focus:ring-red-500'
  };

  const sizeClasses = {
    small: 'px-3 py-1.5 text-sm',
    medium: 'px-4 py-2 text-base',
    large: 'px-6 py-3 text-lg'
  };

  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]} ${
    disabled || loading ? 'opacity-50 cursor-not-allowed' : ''
  }`;

  return (
    <button
      className={classes}
      disabled={disabled || loading}
      onClick={onClick}
    >
      {loading ? (
        <div className="flex items-center">
          <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
          Loading...
        </div>
      ) : (
        children
      )}
    </button>
  );
}

// Modal.tsx - Reusable modal component
interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}

function Modal({ isOpen, onClose, title, children }: ModalProps) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto">
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={onClose}
      ></div>

      {/* Modal */}
      <div className="flex min-h-full items-center justify-center p-4">
        <div className="relative bg-white rounded-lg shadow-xl max-w-md w-full">
          {/* Header */}
          <div className="flex items-center justify-between p-6 border-b">
            <h3 className="text-lg font-semibold">{title}</h3>
            <button
              onClick={onClose}
              className="text-gray-400 hover:text-gray-600"
            >
              ✕
            </button>
          </div>

          {/* Content */}
          <div className="p-6">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}

// Form components
interface InputProps {
  label: string;
  type?: string;
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  error?: string;
  required?: boolean;
}

function Input({ label, type = 'text', value, onChange, placeholder, error, required }: InputProps) {
  return (
    <div className="mb-4">
      <label className="block text-sm font-medium text-gray-700 mb-2">
        {label} {required && <span className="text-red-500">*</span>}
      </label>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={placeholder}
        className={`w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 ${
          error ? 'border-red-500' : 'border-gray-300'
        }`}
      />
      {error && <p className="mt-1 text-sm text-red-500">{error}</p>}
    </div>
  );
}
```

---

# 🌐 **LESSON 4: NEXT.JS - FULL-STACK REACT FRAMEWORK**

## **🔍 WHAT IS NEXT.JS?**

Next.js is **React with superpowers** - it adds server-side rendering, routing, API routes, and optimization out of the box.

### **📊 REACT VS NEXT.JS COMPARISON:**

```tsx
// REACT (Client-Side Only)
// App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/characters" element={<CharactersPage />} />
        <Route path="/characters/:id" element={<CharacterDetailPage />} />
      </Routes>
    </BrowserRouter>
  );
}

// Problems:
// - No SEO (search engines see empty page)
// - Slow initial load (everything loads on client)
// - No API routes (need separate backend)
```

```tsx
// NEXT.JS (Full-Stack)
// File-based routing - no router setup needed!

// app/page.tsx (Home page)
export default function HomePage() {
  return <h1>Welcome to One Piece Trading!</h1>;
}

// app/characters/page.tsx (Characters page)
export default function CharactersPage() {
  return <div>Character list here</div>;
}

// app/characters/[id]/page.tsx (Dynamic route)
export default function CharacterDetailPage({ params }: { params: { id: string } }) {
  return <div>Character {params.id} details</div>;
}

// app/api/characters/route.ts (API endpoint)
export async function GET() {
  const characters = await fetchCharactersFromDB();
  return Response.json(characters);
}

// Benefits:
// ✅ SEO-friendly (server-side rendering)
// ✅ Fast initial load (pre-rendered pages)
// ✅ Built-in API routes (full-stack in one project)
```

## **🏗️ NEXT.JS APP ROUTER STRUCTURE**

```
app/
├── layout.tsx          # Root layout (wraps all pages)
├── page.tsx           # Home page (/)
├── loading.tsx        # Loading UI
├── error.tsx          # Error UI
├── not-found.tsx      # 404 page
├── globals.css        # Global styles
├── characters/
│   ├── page.tsx       # /characters
│   ├── loading.tsx    # Loading for characters
│   └── [id]/
│       ├── page.tsx   # /characters/[id]
│       └── edit/
│           └── page.tsx # /characters/[id]/edit
├── api/
│   ├── characters/
│   │   └── route.ts   # GET/POST /api/characters
│   └── characters/
│       └── [id]/
│           └── route.ts # GET/PUT/DELETE /api/characters/[id]
└── components/
    ├── CharacterCard.tsx
    ├── Navigation.tsx
    └── ui/
        ├── Button.tsx
        └── Modal.tsx
```

## **🎯 BUILDING A COMPLETE NEXT.JS APPLICATION**

### **ROOT LAYOUT:**

```tsx
// app/layout.tsx
import './globals.css';
import { Inter } from 'next/font/google';
import Navigation from './components/Navigation';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: 'One Piece Trading Platform',
  description: 'Trade your favorite One Piece characters',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation />
        <main className="container mx-auto px-4 py-8">
          {children}
        </main>
      </body>
    </html>
  );
}
```

### **HOME PAGE WITH SERVER COMPONENTS:**

```tsx
// app/page.tsx
import Link from 'next/link';
import { Suspense } from 'react';
import CharacterGrid from './components/CharacterGrid';
import LoadingSpinner from './components/LoadingSpinner';

// This is a Server Component (runs on server)
export default function HomePage() {
  return (
    <div>
      <section className="text-center py-12">
        <h1 className="text-4xl font-bold mb-4">
          🏴‍☠️ One Piece Trading Platform
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Discover, trade, and collect your favorite pirates!
        </p>
        <Link
          href="/characters"
          className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors"
        >
          Explore Characters
        </Link>
      </section>

      <section className="mt-12">
        <h2 className="text-2xl font-bold mb-6">Featured Characters</h2>
        <Suspense fallback={<LoadingSpinner />}>
          <FeaturedCharacters />
        </Suspense>
      </section>
    </div>
  );
}

// Server Component that fetches data
async function FeaturedCharacters() {
  // This runs on the server
  const response = await fetch('http://localhost:3000/api/characters?featured=true', {
    cache: 'no-store' // Always fetch fresh data
  });

  if (!response.ok) {
    throw new Error('Failed to fetch featured characters');
  }

  const characters = await response.json();

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {characters.map((character: any) => (
        <CharacterCard key={character.id} character={character} />
      ))}
    </div>
  );
}
```

### **API ROUTES:**

```tsx
// app/api/characters/route.ts
import { NextRequest, NextResponse } from 'next/server';

// Mock database
const characters = [
  {
    id: '1',
    name: 'Monkey D. Luffy',
    bounty: 3000000000,
    crew: 'Straw Hat Pirates',
    devilFruit: 'Gomu Gomu no Mi',
    image: '/images/luffy.jpg',
    featured: true
  },
  {
    id: '2',
    name: 'Roronoa Zoro',
    bounty: 1111000000,
    crew: 'Straw Hat Pirates',
    image: '/images/zoro.jpg',
    featured: true
  }
];

// GET /api/characters
export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const featured = searchParams.get('featured');
  const search = searchParams.get('search');

  let filteredCharacters = characters;

  if (featured === 'true') {
    filteredCharacters = characters.filter(char => char.featured);
  }

  if (search) {
    filteredCharacters = filteredCharacters.filter(char =>
      char.name.toLowerCase().includes(search.toLowerCase())
    );
  }

  return NextResponse.json(filteredCharacters);
}

// POST /api/characters
export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    // Validation
    if (!body.name || !body.bounty || !body.crew) {
      return NextResponse.json(
        { error: 'Missing required fields' },
        { status: 400 }
      );
    }

    const newCharacter = {
      id: (characters.length + 1).toString(),
      ...body,
      featured: false
    };

    characters.push(newCharacter);

    return NextResponse.json(newCharacter, { status: 201 });
  } catch (error) {
    return NextResponse.json(
      { error: 'Invalid JSON' },
      { status: 400 }
    );
  }
}
```

### **DYNAMIC ROUTES:**

```tsx
// app/characters/[id]/page.tsx
import { notFound } from 'next/navigation';
import Image from 'next/image';
import Link from 'next/link';

interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
  devilFruit?: string;
  image: string;
}

// Generate static params for static generation
export async function generateStaticParams() {
  const response = await fetch('http://localhost:3000/api/characters');
  const characters = await response.json();

  return characters.map((character: Character) => ({
    id: character.id,
  }));
}

// Generate metadata for SEO
export async function generateMetadata({ params }: { params: { id: string } }) {
  const character = await getCharacter(params.id);

  if (!character) {
    return {
      title: 'Character Not Found',
    };
  }

  return {
    title: `${character.name} - One Piece Trading`,
    description: `${character.name} from ${character.crew} with bounty ${character.bounty.toLocaleString()} berries`,
  };
}

async function getCharacter(id: string): Promise<Character | null> {
  const response = await fetch(`http://localhost:3000/api/characters/${id}`, {
    cache: 'force-cache' // Cache for static generation
  });

  if (!response.ok) {
    return null;
  }

  return response.json();
}

export default async function CharacterDetailPage({ params }: { params: { id: string } }) {
  const character = await getCharacter(params.id);

  if (!character) {
    notFound(); // Shows 404 page
  }

  return (
    <div className="max-w-4xl mx-auto">
      <Link
        href="/characters"
        className="text-blue-600 hover:text-blue-800 mb-6 inline-block"
      >
        ← Back to Characters
      </Link>

      <div className="bg-white rounded-lg shadow-lg overflow-hidden">
        <div className="md:flex">
          <div className="md:w-1/3">
            <Image
              src={character.image}
              alt={character.name}
              width={400}
              height={400}
              className="w-full h-64 md:h-full object-cover"
            />
          </div>

          <div className="md:w-2/3 p-8">
            <h1 className="text-3xl font-bold mb-4">{character.name}</h1>

            <div className="space-y-3">
              <div>
                <span className="font-semibold">Crew:</span> {character.crew}
              </div>

              <div>
                <span className="font-semibold">Bounty:</span>{' '}
                <span className="text-2xl font-bold text-yellow-600">
                  {character.bounty.toLocaleString()} berries
                </span>
              </div>

              {character.devilFruit && (
                <div>
                  <span className="font-semibold">Devil Fruit:</span> {character.devilFruit}
                </div>
              )}
            </div>

            <div className="mt-8 space-x-4">
              <button className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700">
                Add to Collection
              </button>
              <button className="bg-green-600 text-white px-6 py-2 rounded-lg hover:bg-green-700">
                Start Trade
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
```

---

# 🔄 **LESSON 5: DATA FETCHING AND STATE MANAGEMENT**

## **🔍 CLIENT-SIDE DATA FETCHING WITH SWR**

SWR (Stale-While-Revalidate) is a powerful data fetching library that makes API calls simple and efficient.

```tsx
// Install: npm install swr
import useSWR from 'swr';

// Fetcher function
const fetcher = (url: string) => fetch(url).then(res => res.json());

// Custom hook for characters
function useCharacters() {
  const { data, error, isLoading, mutate } = useSWR('/api/characters', fetcher);

  return {
    characters: data,
    isLoading,
    isError: error,
    refresh: mutate
  };
}

// Component using the hook
function CharacterList() {
  const { characters, isLoading, isError, refresh } = useCharacters();

  if (isLoading) return <div>Loading pirates...</div>;
  if (isError) return <div>Failed to load characters</div>;

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl font-bold">Characters</h2>
        <button
          onClick={() => refresh()}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Refresh
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {characters?.map((character: any) => (
          <CharacterCard key={character.id} character={character} />
        ))}
      </div>
    </div>
  );
}

// Advanced SWR with mutations
function useCharacterMutations() {
  const { mutate } = useSWR('/api/characters', fetcher);

  const createCharacter = async (characterData: any) => {
    // Optimistic update
    mutate(
      (currentData: any[]) => [...currentData, { ...characterData, id: 'temp' }],
      false // Don't revalidate immediately
    );

    try {
      const response = await fetch('/api/characters', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(characterData)
      });

      if (!response.ok) throw new Error('Failed to create character');

      // Revalidate to get the real data
      mutate();
    } catch (error) {
      // Revert optimistic update on error
      mutate();
      throw error;
    }
  };

  const deleteCharacter = async (id: string) => {
    // Optimistic update
    mutate(
      (currentData: any[]) => currentData.filter(char => char.id !== id),
      false
    );

    try {
      const response = await fetch(`/api/characters/${id}`, {
        method: 'DELETE'
      });

      if (!response.ok) throw new Error('Failed to delete character');

      mutate();
    } catch (error) {
      mutate();
      throw error;
    }
  };

  return { createCharacter, deleteCharacter };
}
```

## **🎛️ GLOBAL STATE MANAGEMENT WITH ZUSTAND**

```tsx
// Install: npm install zustand
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// Define store interface
interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
}

interface TradingStore {
  // State
  characters: Character[];
  favorites: string[];
  cart: string[];
  user: { id: string; name: string } | null;

  // Actions
  setCharacters: (characters: Character[]) => void;
  addToFavorites: (characterId: string) => void;
  removeFromFavorites: (characterId: string) => void;
  addToCart: (characterId: string) => void;
  removeFromCart: (characterId: string) => void;
  clearCart: () => void;
  setUser: (user: { id: string; name: string } | null) => void;
}

// Create store with persistence
const useTradingStore = create<TradingStore>()(
  persist(
    (set, get) => ({
      // Initial state
      characters: [],
      favorites: [],
      cart: [],
      user: null,

      // Actions
      setCharacters: (characters) => set({ characters }),

      addToFavorites: (characterId) => set((state) => ({
        favorites: state.favorites.includes(characterId)
          ? state.favorites
          : [...state.favorites, characterId]
      })),

      removeFromFavorites: (characterId) => set((state) => ({
        favorites: state.favorites.filter(id => id !== characterId)
      })),

      addToCart: (characterId) => set((state) => ({
        cart: state.cart.includes(characterId)
          ? state.cart
          : [...state.cart, characterId]
      })),

      removeFromCart: (characterId) => set((state) => ({
        cart: state.cart.filter(id => id !== characterId)
      })),

      clearCart: () => set({ cart: [] }),

      setUser: (user) => set({ user })
    }),
    {
      name: 'trading-store', // localStorage key
      partialize: (state) => ({
        favorites: state.favorites,
        cart: state.cart,
        user: state.user
      }) // Only persist these fields
    }
  )
);

// Using the store in components
function CharacterCard({ character }: { character: Character }) {
  const { favorites, cart, addToFavorites, removeFromFavorites, addToCart } = useTradingStore();

  const isFavorite = favorites.includes(character.id);
  const isInCart = cart.includes(character.id);

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-xl font-bold mb-2">{character.name}</h3>
      <p className="text-gray-600 mb-2">{character.crew}</p>
      <p className="text-lg font-semibold text-yellow-600 mb-4">
        {character.bounty.toLocaleString()} berries
      </p>

      <div className="flex space-x-2">
        <button
          onClick={() =>
            isFavorite
              ? removeFromFavorites(character.id)
              : addToFavorites(character.id)
          }
          className={`px-3 py-1 rounded ${
            isFavorite
              ? 'bg-red-500 text-white'
              : 'bg-gray-200 text-gray-700'
          }`}
        >
          {isFavorite ? '❤️ Favorited' : '🤍 Favorite'}
        </button>

        <button
          onClick={() => addToCart(character.id)}
          disabled={isInCart}
          className={`px-3 py-1 rounded ${
            isInCart
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-blue-500 text-white hover:bg-blue-600'
          }`}
        >
          {isInCart ? 'In Cart' : 'Add to Cart'}
        </button>
      </div>
    </div>
  );
}

// Cart component
function Cart() {
  const { cart, characters, removeFromCart, clearCart } = useTradingStore();

  const cartCharacters = characters.filter(char => cart.includes(char.id));
  const totalValue = cartCharacters.reduce((sum, char) => sum + char.bounty, 0);

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold">Shopping Cart</h2>
        <button
          onClick={clearCart}
          className="text-red-600 hover:text-red-800"
        >
          Clear All
        </button>
      </div>

      {cartCharacters.length === 0 ? (
        <p className="text-gray-500">Your cart is empty</p>
      ) : (
        <>
          <div className="space-y-3 mb-4">
            {cartCharacters.map(character => (
              <div key={character.id} className="flex justify-between items-center">
                <div>
                  <h4 className="font-semibold">{character.name}</h4>
                  <p className="text-sm text-gray-600">{character.bounty.toLocaleString()} berries</p>
                </div>
                <button
                  onClick={() => removeFromCart(character.id)}
                  className="text-red-600 hover:text-red-800"
                >
                  Remove
                </button>
              </div>
            ))}
          </div>

          <div className="border-t pt-4">
            <div className="flex justify-between items-center mb-4">
              <span className="text-lg font-semibold">Total:</span>
              <span className="text-xl font-bold text-green-600">
                {totalValue.toLocaleString()} berries
              </span>
            </div>

            <button className="w-full bg-green-600 text-white py-2 rounded-lg hover:bg-green-700">
              Proceed to Checkout
            </button>
          </div>
        </>
      )}
    </div>
  );
}
```

---

# 🎯 **HANDS-ON EXERCISES - BUILD YOUR SKILLS**

## **🏋️ EXERCISE 1: BUILD A CHARACTER SEARCH AND FILTER SYSTEM**

**OBJECTIVE:** Create a comprehensive search and filtering interface for the One Piece characters.

**REQUIREMENTS:**
- Search by character name
- Filter by crew
- Filter by bounty range
- Sort by name, bounty, or crew
- Pagination for large datasets
- URL state management (search params)

**STARTER CODE:**
```tsx
// components/CharacterSearch.tsx
import { useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';

interface SearchFilters {
  search: string;
  crew: string;
  minBounty: number;
  maxBounty: number;
  sortBy: 'name' | 'bounty' | 'crew';
  sortOrder: 'asc' | 'desc';
  page: number;
}

export default function CharacterSearch() {
  const router = useRouter();
  const searchParams = useSearchParams();

  const [filters, setFilters] = useState<SearchFilters>({
    search: searchParams.get('search') || '',
    crew: searchParams.get('crew') || '',
    minBounty: parseInt(searchParams.get('minBounty') || '0'),
    maxBounty: parseInt(searchParams.get('maxBounty') || '10000000000'),
    sortBy: (searchParams.get('sortBy') as any) || 'name',
    sortOrder: (searchParams.get('sortOrder') as any) || 'asc',
    page: parseInt(searchParams.get('page') || '1')
  });

  // TODO: Implement search logic
  // TODO: Update URL when filters change
  // TODO: Fetch and display filtered results

  return (
    <div>
      {/* TODO: Build search interface */}
    </div>
  );
}
```

**SUCCESS CRITERIA:**
- All filters work correctly
- URL updates when filters change
- Results update in real-time
- Pagination works properly
- Loading states are handled

## **🏋️ EXERCISE 2: BUILD A REAL-TIME TRADING SYSTEM**

**OBJECTIVE:** Create a real-time trading interface where users can make offers and see live updates.

**REQUIREMENTS:**
- WebSocket connection for real-time updates
- Trading interface with offer/counter-offer system
- Real-time notifications
- Trade history
- User authentication

**STARTER CODE:**
```tsx
// hooks/useWebSocket.ts
import { useEffect, useRef, useState } from 'react';

interface UseWebSocketOptions {
  onMessage?: (data: any) => void;
  onConnect?: () => void;
  onDisconnect?: () => void;
}

export function useWebSocket(url: string, options: UseWebSocketOptions = {}) {
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    // TODO: Implement WebSocket connection
    // TODO: Handle reconnection logic
    // TODO: Implement message handling

    return () => {
      // TODO: Cleanup WebSocket connection
    };
  }, [url]);

  const sendMessage = (message: any) => {
    // TODO: Implement message sending
  };

  return { isConnected, sendMessage };
}

// components/TradingInterface.tsx
export default function TradingInterface() {
  // TODO: Implement trading interface
  // TODO: Connect to WebSocket
  // TODO: Handle trade offers
  // TODO: Show real-time updates

  return (
    <div>
      {/* TODO: Build trading interface */}
    </div>
  );
}
```

## **🏋️ EXERCISE 3: BUILD A RESPONSIVE DASHBOARD**

**OBJECTIVE:** Create a comprehensive dashboard showing trading statistics, favorite characters, and recent activity.

**REQUIREMENTS:**
- Responsive grid layout
- Interactive charts (using Chart.js or Recharts)
- Real-time data updates
- Customizable widgets
- Dark/light theme toggle

**BONUS CHALLENGES:**
- Drag-and-drop widget reordering
- Export data functionality
- Advanced filtering and date ranges
- Mobile-optimized interface

---

# ⚠️ **COMMON MISTAKES - AVOID THESE PITFALLS**

## **❌ MISTAKE 1: NOT USING KEYS PROPERLY IN LISTS**

```tsx
// ❌ WRONG - Using array index as key
function CharacterList({ characters }) {
  return (
    <div>
      {characters.map((character, index) => (
        <CharacterCard key={index} character={character} />
        // Problem: React can't track items properly when list changes
      ))}
    </div>
  );
}

// ✅ CORRECT - Using unique, stable keys
function CharacterList({ characters }) {
  return (
    <div>
      {characters.map((character) => (
        <CharacterCard key={character.id} character={character} />
        // React can efficiently update the list
      ))}
    </div>
  );
}
```

## **❌ MISTAKE 2: MUTATING STATE DIRECTLY**

```tsx
// ❌ WRONG - Mutating state directly
function TodoList() {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    todos.push({ id: Date.now(), text }); // Mutating state!
    setTodos(todos); // React won't detect the change
  };

  const toggleTodo = (id) => {
    const todo = todos.find(t => t.id === id);
    todo.completed = !todo.completed; // Mutating nested object!
    setTodos(todos);
  };
}

// ✅ CORRECT - Creating new state objects
function TodoList() {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    setTodos([...todos, { id: Date.now(), text, completed: false }]);
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id
        ? { ...todo, completed: !todo.completed }
        : todo
    ));
  };
}
```

## **❌ MISTAKE 3: USEEFFECT DEPENDENCY ISSUES**

```tsx
// ❌ WRONG - Missing dependencies
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, []); // Missing userId dependency!

  // User won't update when userId changes
}

// ❌ WRONG - Unnecessary dependencies causing infinite loops
function SearchResults({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    search(query).then(setResults);
  }, [query, results]); // results dependency causes infinite loop!
}

// ✅ CORRECT - Proper dependencies
function UserProfile({ userId }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId]); // Include all dependencies
}

function SearchResults({ query }) {
  const [results, setResults] = useState([]);

  useEffect(() => {
    search(query).then(setResults);
  }, [query]); // Only include external dependencies
}
```

## **❌ MISTAKE 4: NOT HANDLING LOADING AND ERROR STATES**

```tsx
// ❌ WRONG - No loading or error handling
function CharacterList() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetch('/api/characters')
      .then(res => res.json())
      .then(setCharacters);
  }, []);

  return (
    <div>
      {characters.map(char => <CharacterCard key={char.id} character={char} />)}
    </div>
  );
  // Users see empty list while loading, no error feedback
}

// ✅ CORRECT - Proper loading and error states
function CharacterList() {
  const [characters, setCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    setError(null);

    fetch('/api/characters')
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch');
        return res.json();
      })
      .then(data => {
        setCharacters(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div>Loading characters...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {characters.map(char => <CharacterCard key={char.id} character={char} />)}
    </div>
  );
}
```

---

# 🏢 **STARTUP VS ENTERPRISE - DIFFERENT APPROACHES**

## **🚀 STARTUP APPROACH:**

### **CHARACTERISTICS:**
- **Move Fast:** Ship features quickly, iterate based on user feedback
- **Simple Architecture:** Monolithic Next.js app with basic state management
- **Minimal Tooling:** Basic CI/CD, simple monitoring
- **Small Team:** 2-5 frontend developers, everyone touches everything

### **TYPICAL STARTUP STACK:**
```tsx
// Simple Next.js app structure
app/
├── page.tsx                 # Home page
├── characters/
│   └── page.tsx            # Characters list
├── api/
│   └── characters/
│       └── route.ts        # Simple API routes
└── components/
    ├── CharacterCard.tsx   # Basic components
    └── Layout.tsx

// Basic state management with useState/useContext
const AppContext = createContext();

function App({ children }) {
  const [user, setUser] = useState(null);
  const [characters, setCharacters] = useState([]);

  return (
    <AppContext.Provider value={{ user, setUser, characters, setCharacters }}>
      {children}
    </AppContext.Provider>
  );
}

// Simple data fetching
function CharacterList() {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetch('/api/characters')
      .then(res => res.json())
      .then(setCharacters);
  }, []);

  return (
    <div>
      {characters.map(char => <CharacterCard key={char.id} character={char} />)}
    </div>
  );
}
```

### **DEPLOYMENT:**
- **Hosting:** Vercel, Netlify (simple deployment)
- **Database:** Supabase, PlanetScale (managed services)
- **Monitoring:** Basic Vercel analytics
- **CI/CD:** GitHub Actions (basic)

## **🏢 ENTERPRISE APPROACH:**

### **CHARACTERISTICS:**
- **Reliability First:** Extensive testing, performance optimization
- **Complex Architecture:** Micro-frontends, advanced state management
- **Comprehensive Tooling:** Advanced CI/CD, monitoring, A/B testing
- **Large Teams:** 20+ frontend developers, specialized roles

### **TYPICAL ENTERPRISE STACK:**
```tsx
// Complex Next.js app with micro-frontends
apps/
├── shell/                   # Main shell application
├── characters/              # Characters micro-frontend
├── trading/                 # Trading micro-frontend
└── admin/                   # Admin micro-frontend

packages/
├── ui/                      # Shared UI components
├── utils/                   # Shared utilities
├── types/                   # Shared TypeScript types
└── config/                  # Shared configuration

// Advanced state management with Redux Toolkit
import { configureStore } from '@reduxjs/toolkit';
import { charactersApi } from './api/charactersApi';
import { tradingApi } from './api/tradingApi';

export const store = configureStore({
  reducer: {
    characters: charactersSlice.reducer,
    trading: tradingSlice.reducer,
    user: userSlice.reducer,
    [charactersApi.reducerPath]: charactersApi.reducer,
    [tradingApi.reducerPath]: tradingApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: [FLUSH, REHYDRATE, PAUSE, PERSIST, PURGE, REGISTER],
      },
    })
    .concat(charactersApi.middleware)
    .concat(tradingApi.middleware),
});

// Advanced data fetching with RTK Query
export const charactersApi = createApi({
  reducerPath: 'charactersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: '/api/characters',
    prepareHeaders: (headers, { getState }) => {
      const token = (getState() as RootState).auth.token;
      if (token) {
        headers.set('authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  tagTypes: ['Character'],
  endpoints: (builder) => ({
    getCharacters: builder.query<Character[], void>({
      query: () => '',
      providesTags: ['Character'],
    }),
    createCharacter: builder.mutation<Character, Partial<Character>>({
      query: (character) => ({
        url: '',
        method: 'POST',
        body: character,
      }),
      invalidatesTags: ['Character'],
    }),
  }),
});

// Component with advanced patterns
function CharacterList() {
  const {
    data: characters,
    error,
    isLoading,
    refetch
  } = useGetCharactersQuery();

  const [createCharacter] = useCreateCharacterMutation();

  // Advanced error handling
  if (error) {
    return <ErrorBoundary error={error} onRetry={refetch} />;
  }

  // Advanced loading states
  if (isLoading) {
    return <CharacterListSkeleton />;
  }

  return (
    <div>
      <VirtualizedList
        items={characters}
        renderItem={({ item }) => <CharacterCard character={item} />}
        itemHeight={200}
      />
    </div>
  );
}
```

### **DEPLOYMENT:**
- **Hosting:** AWS CloudFront + S3, Google Cloud CDN
- **Database:** AWS RDS, Google Cloud SQL (with read replicas)
- **Monitoring:** DataDog, New Relic, Sentry
- **CI/CD:** Jenkins, GitLab CI, AWS CodePipeline
- **A/B Testing:** LaunchDarkly, Optimizely
- **Performance:** Lighthouse CI, Bundle analyzer

---

# 💰 **CAREER PROGRESSION & SALARY INFORMATION**

## **📈 REACT/NEXT.JS DEVELOPER CAREER PATH:**

### **🌱 JUNIOR FRONTEND DEVELOPER (0-2 years)**
**SKILLS:**
- Basic React components and hooks
- HTML, CSS, JavaScript fundamentals
- Simple state management
- Basic Next.js routing

**SALARY RANGES:**
- **Startup:** $55K - $75K
- **Mid-size:** $65K - $85K
- **Enterprise:** $75K - $95K
- **FAANG:** $110K - $140K (total comp)

### **⚡ MID-LEVEL FRONTEND DEVELOPER (2-5 years)**
**SKILLS:**
- Advanced React patterns
- State management (Redux, Zustand)
- Performance optimization
- Testing (Jest, React Testing Library)
- TypeScript proficiency

**SALARY RANGES:**
- **Startup:** $75K - $110K
- **Mid-size:** $90K - $120K
- **Enterprise:** $110K - $140K
- **FAANG:** $160K - $220K (total comp)

### **🚀 SENIOR FRONTEND DEVELOPER (5+ years)**
**SKILLS:**
- Architecture design
- Team leadership
- Performance at scale
- Accessibility expertise
- Full-stack capabilities

**SALARY RANGES:**
- **Startup:** $110K - $160K
- **Mid-size:** $130K - $170K
- **Enterprise:** $150K - $200K
- **FAANG:** $250K - $400K (total comp)

### **👑 PRINCIPAL/STAFF FRONTEND ENGINEER (8+ years)**
**SKILLS:**
- Cross-team technical leadership
- Framework architecture decisions
- Mentoring and hiring
- Industry expertise

**SALARY RANGES:**
- **Startup:** $160K - $220K + equity
- **Mid-size:** $180K - $250K
- **Enterprise:** $220K - $300K
- **FAANG:** $400K - $600K+ (total comp)

## **🎯 COMPANIES HIRING REACT/NEXT.JS DEVELOPERS:**

### **🚀 STARTUPS:**
- **Vercel** - Next.js creators, web development platform
- **Linear** - Issue tracking (built with React/Next.js)
- **Notion** - Productivity platform
- **Framer** - Design and prototyping tool

### **🏢 ENTERPRISE:**
- **Netflix** - Streaming platform UI
- **Airbnb** - Travel platform
- **Uber** - Ride-sharing and delivery apps
- **Shopify** - E-commerce platform

### **🏛️ FAANG:**
- **Meta** - Facebook, Instagram, WhatsApp
- **Netflix** - Content delivery platform
- **Amazon** - AWS Console, retail platform
- **Google** - Various products and services

---

# 🎉 **CONGRATULATIONS - YOU'RE NOW A REACT/NEXT.JS PIRATE!**

## **🏆 WHAT YOU'VE MASTERED:**

✅ **React Fundamentals** - Components, hooks, state management
✅ **Next.js Framework** - SSR, routing, API routes, optimization
✅ **Modern Styling** - CSS Modules, Tailwind, styled-components
✅ **Data Fetching** - SWR, RTK Query, server components
✅ **State Management** - useState, useReducer, Context, Zustand
✅ **Performance Optimization** - Code splitting, image optimization
✅ **Testing Strategies** - Jest, React Testing Library
✅ **Career Awareness** - Know your worth and growth path

## **🚀 NEXT STEPS:**

1. **Practice:** Build the exercises in this module
2. **Integrate:** Connect with your TypeScript/Node.js backend
3. **Advance:** Add AI/LLM integration (Module 36)
4. **Scale:** Learn ETL and data pipelines (Module 37)
5. **Specialize:** Build MCP servers (Module 38)

## **🏴‍☠️ FINAL PROJECT CHALLENGE:**

Build a complete One Piece Trading Platform with:
- **Character browsing** with search and filters
- **Real-time trading** with WebSocket connections
- **User authentication** and profiles
- **Responsive design** for all devices
- **Performance optimization** for large datasets
- **Comprehensive testing** suite

**🌊 You're now ready to build amazing React applications that would make even the Pirate King proud! The Grand Line of frontend development awaits!** ⚔️

---

# 🎛️ **LESSON 2: STATE MANAGEMENT WITH HOOKS**

## **🔍 WHAT IS STATE?**

State is **data that can change over time** and affects what the user sees.

### **📊 useState HOOK - MANAGING SIMPLE STATE:**

```tsx
import { useState } from 'react';

function BountyTracker() {
  // useState returns [currentValue, setterFunction]
  const [bounty, setBounty] = useState(0);
  const [characterName, setCharacterName] = useState('');
  const [isWanted, setIsWanted] = useState(false);

  const increaseBounty = () => {
    setBounty(bounty + 100000000); // Add 100 million berries
  };

  const toggleWantedStatus = () => {
    setIsWanted(!isWanted);
  };

  return (
    <div className="bounty-tracker">
      <h2>Bounty Tracker</h2>
      
      <input 
        type="text"
        placeholder="Character name"
        value={characterName}
        onChange={(e) => setCharacterName(e.target.value)}
      />
      
      <div className="bounty-display">
        <h3>{characterName || 'Unknown Pirate'}</h3>
        <p>Current Bounty: {bounty.toLocaleString()} berries</p>
        <p>Status: {isWanted ? '🚨 WANTED' : '✅ Clean Record'}</p>
      </div>
      
      <div className="controls">
        <button onClick={increaseBounty}>
          Increase Bounty (+100M)
        </button>
        <button onClick={toggleWantedStatus}>
          Toggle Wanted Status
        </button>
      </div>
    </div>
  );
}
```

### **📊 useEffect HOOK - HANDLING SIDE EFFECTS:**

```tsx
import { useState, useEffect } from 'react';

interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
}

function CharacterList() {
  const [characters, setCharacters] = useState<Character[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // useEffect runs after component mounts and on dependencies change
  useEffect(() => {
    fetchCharacters();
  }, []); // Empty dependency array = run once on mount

  // Another useEffect that runs when characters change
  useEffect(() => {
    document.title = `${characters.length} Pirates Found`;
  }, [characters]); // Runs when characters array changes

  // Cleanup effect (like componentWillUnmount)
  useEffect(() => {
    const interval = setInterval(() => {
      console.log('Checking for new bounties...');
    }, 30000);

    // Cleanup function
    return () => {
      clearInterval(interval);
    };
  }, []);

  const fetchCharacters = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await fetch('/api/characters');
      if (!response.ok) {
        throw new Error('Failed to fetch characters');
      }
      
      const data = await response.json();
      setCharacters(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">🌊 Loading pirates...</div>;
  }

  if (error) {
    return (
      <div className="error">
        <p>❌ Error: {error}</p>
        <button onClick={fetchCharacters}>Try Again</button>
      </div>
    );
  }

  return (
    <div className="character-list">
      <h2>Pirate Crew ({characters.length})</h2>
      <button onClick={fetchCharacters}>Refresh</button>
      
      <div className="character-grid">
        {characters.map(character => (
          <div key={character.id} className="character-card">
            <h3>{character.name}</h3>
            <p>Crew: {character.crew}</p>
            <p>Bounty: {character.bounty.toLocaleString()}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### **📊 useReducer HOOK - COMPLEX STATE MANAGEMENT:**

```tsx
import { useReducer } from 'react';

// Define state shape
interface CrewState {
  members: Character[];
  totalBounty: number;
  captain: string | null;
  isRecruiting: boolean;
}

// Define action types
type CrewAction = 
  | { type: 'ADD_MEMBER'; payload: Character }
  | { type: 'REMOVE_MEMBER'; payload: string }
  | { type: 'SET_CAPTAIN'; payload: string }
  | { type: 'TOGGLE_RECRUITING' }
  | { type: 'RESET_CREW' };

// Reducer function (like Redux)
function crewReducer(state: CrewState, action: CrewAction): CrewState {
  switch (action.type) {
    case 'ADD_MEMBER':
      const newMembers = [...state.members, action.payload];
      return {
        ...state,
        members: newMembers,
        totalBounty: newMembers.reduce((sum, member) => sum + member.bounty, 0)
      };
      
    case 'REMOVE_MEMBER':
      const filteredMembers = state.members.filter(member => member.id !== action.payload);
      return {
        ...state,
        members: filteredMembers,
        totalBounty: filteredMembers.reduce((sum, member) => sum + member.bounty, 0),
        captain: state.captain === action.payload ? null : state.captain
      };
      
    case 'SET_CAPTAIN':
      return {
        ...state,
        captain: action.payload
      };
      
    case 'TOGGLE_RECRUITING':
      return {
        ...state,
        isRecruiting: !state.isRecruiting
      };
      
    case 'RESET_CREW':
      return {
        members: [],
        totalBounty: 0,
        captain: null,
        isRecruiting: false
      };
      
    default:
      return state;
  }
}

// Component using useReducer
function CrewManager() {
  const [crewState, dispatch] = useReducer(crewReducer, {
    members: [],
    totalBounty: 0,
    captain: null,
    isRecruiting: false
  });

  const addMember = (character: Character) => {
    dispatch({ type: 'ADD_MEMBER', payload: character });
  };

  const removeMember = (memberId: string) => {
    dispatch({ type: 'REMOVE_MEMBER', payload: memberId });
  };

  const setCaptain = (memberId: string) => {
    dispatch({ type: 'SET_CAPTAIN', payload: memberId });
  };

  return (
    <div className="crew-manager">
      <h2>Crew Management</h2>
      
      <div className="crew-stats">
        <p>Members: {crewState.members.length}</p>
        <p>Total Bounty: {crewState.totalBounty.toLocaleString()}</p>
        <p>Captain: {crewState.captain || 'None'}</p>
        <p>Recruiting: {crewState.isRecruiting ? 'Yes' : 'No'}</p>
      </div>
      
      <div className="crew-controls">
        <button onClick={() => dispatch({ type: 'TOGGLE_RECRUITING' })}>
          {crewState.isRecruiting ? 'Stop Recruiting' : 'Start Recruiting'}
        </button>
        <button onClick={() => dispatch({ type: 'RESET_CREW' })}>
          Disband Crew
        </button>
      </div>
      
      <div className="member-list">
        {crewState.members.map(member => (
          <div key={member.id} className="member-card">
            <h4>{member.name}</h4>
            <p>Bounty: {member.bounty.toLocaleString()}</p>
            <button onClick={() => setCaptain(member.id)}>
              Make Captain
            </button>
            <button onClick={() => removeMember(member.id)}>
              Remove
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
```
