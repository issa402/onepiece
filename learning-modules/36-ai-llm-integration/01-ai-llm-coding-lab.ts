/**
 * 🤖 ONE PIECE TRADING PLATFORM - AI/LLM INTEGRATION CODING LAB
 * 
 * This file contains comprehensive AI/LLM integration examples
 * demonstrating all concepts from basic API calls to advanced agentic workflows.
 * 
 * To run this lab:
 * 1. Install dependencies: npm install openai @anthropic-ai/sdk
 * 2. Set environment variables: OPENAI_API_KEY, ANTHROPIC_API_KEY
 * 3. Run: tsx 01-ai-llm-coding-lab.ts
 */

import OpenAI from 'openai';
import Anthropic from '@anthropic-ai/sdk';

// ============================================================================
// 🎯 SECTION 1: TYPE DEFINITIONS AND INTERFACES
// ============================================================================

interface Character {
  id: string;
  name: string;
  bounty: number;
  crew: string;
  devilFruit?: string;
  haki: string[];
  description: string;
  powerLevel?: number;
}

interface CharacterAnalysis {
  powerLevel: number;
  fightingStyle: string;
  personality: string[];
  strengths: string[];
  weaknesses: string[];
  marketPrediction: {
    currentValue: number;
    predictedValue: number;
    confidence: number;
    reasoning: string;
  };
}

interface AIProvider {
  name: string;
  generateText(prompt: string, options?: any): Promise<string>;
  generateStructured(prompt: string, schema: any): Promise<any>;
  streamText(prompt: string, onChunk: (chunk: string) => void): Promise<void>;
}

interface TradingRecommendation {
  action: 'buy' | 'sell' | 'hold';
  character: Character;
  confidence: number;
  reasoning: string;
  targetPrice?: number;
  timeframe: string;
}

// ============================================================================
// 🎯 SECTION 2: AI PROVIDER IMPLEMENTATIONS
// ============================================================================

export class OpenAIProvider implements AIProvider {
  name = 'openai';
  private client: OpenAI;

  constructor(apiKey: string) {
    this.client = new OpenAI({ apiKey });
  }

  async generateText(prompt: string, options: any = {}): Promise<string> {
    try {
      const response = await this.client.chat.completions.create({
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 1000,
        temperature: 0.7,
        ...options
      });
      
      return response.choices[0].message.content || '';
    } catch (error) {
      console.error('OpenAI API error:', error);
      throw new Error(`OpenAI generation failed: ${error.message}`);
    }
  }

  async generateStructured(prompt: string, schema: any): Promise<any> {
    try {
      const response = await this.client.chat.completions.create({
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
        functions: [{
          name: 'extract_data',
          description: 'Extract structured data according to schema',
          parameters: schema
        }],
        function_call: { name: 'extract_data' }
      });
      
      const functionCall = response.choices[0].message.function_call;
      if (!functionCall?.arguments) {
        throw new Error('No function call response received');
      }
      
      return JSON.parse(functionCall.arguments);
    } catch (error) {
      console.error('OpenAI structured generation error:', error);
      throw new Error(`OpenAI structured generation failed: ${error.message}`);
    }
  }

  async streamText(prompt: string, onChunk: (chunk: string) => void): Promise<void> {
    try {
      const stream = await this.client.chat.completions.create({
        model: 'gpt-4',
        messages: [{ role: 'user', content: prompt }],
        stream: true,
        max_tokens: 1000
      });

      for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content || '';
        if (content) {
          onChunk(content);
        }
      }
    } catch (error) {
      console.error('OpenAI streaming error:', error);
      throw new Error(`OpenAI streaming failed: ${error.message}`);
    }
  }
}

export class AnthropicProvider implements AIProvider {
  name = 'anthropic';
  private client: Anthropic;

  constructor(apiKey: string) {
    this.client = new Anthropic({ apiKey });
  }

  async generateText(prompt: string, options: any = {}): Promise<string> {
    try {
      const response = await this.client.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1000,
        messages: [{ role: 'user', content: prompt }],
        ...options
      });
      
      const content = response.content[0];
      return content.type === 'text' ? content.text : '';
    } catch (error) {
      console.error('Anthropic API error:', error);
      throw new Error(`Anthropic generation failed: ${error.message}`);
    }
  }

  async generateStructured(prompt: string, schema: any): Promise<any> {
    const structuredPrompt = `
      ${prompt}
      
      Please respond with valid JSON that matches this exact schema:
      ${JSON.stringify(schema, null, 2)}
      
      Ensure all required fields are included and data types match the schema.
    `;
    
    try {
      const response = await this.generateText(structuredPrompt);
      
      // Extract JSON from response (handle cases where AI adds explanation)
      const jsonMatch = response.match(/\{[\s\S]*\}/);
      if (!jsonMatch) {
        throw new Error('No JSON found in response');
      }
      
      return JSON.parse(jsonMatch[0]);
    } catch (error) {
      console.error('Anthropic structured generation error:', error);
      throw new Error(`Anthropic structured generation failed: ${error.message}`);
    }
  }

  async streamText(prompt: string, onChunk: (chunk: string) => void): Promise<void> {
    try {
      const stream = await this.client.messages.create({
        model: 'claude-3-sonnet-20240229',
        max_tokens: 1000,
        messages: [{ role: 'user', content: prompt }],
        stream: true,
      });

      for await (const chunk of stream) {
        if (chunk.type === 'content_block_delta' && chunk.delta.type === 'text_delta') {
          onChunk(chunk.delta.text);
        }
      }
    } catch (error) {
      console.error('Anthropic streaming error:', error);
      throw new Error(`Anthropic streaming failed: ${error.message}`);
    }
  }
}

// ============================================================================
// 🎯 SECTION 3: CHARACTER ANALYSIS SERVICE
// ============================================================================

export class CharacterAnalysisService {
  private aiProvider: AIProvider;

  constructor(provider: AIProvider) {
    this.aiProvider = provider;
  }

  async analyzeCharacter(character: Character): Promise<CharacterAnalysis> {
    const prompt = `
      You are an expert One Piece analyst and trading advisor. Analyze this character comprehensively:
      
      Character: ${character.name}
      Crew: ${character.crew}
      Bounty: ${character.bounty.toLocaleString()} berries
      Devil Fruit: ${character.devilFruit || 'None'}
      Haki: ${character.haki.join(', ') || 'None'}
      Description: ${character.description}
      
      Provide a detailed analysis considering:
      1. Combat abilities and power scaling
      2. Character development and story importance
      3. Fan popularity and cultural impact
      4. Rarity and uniqueness of abilities
      5. Market trends and trading potential
      
      Be objective but engaging in your analysis.
    `;

    const schema = {
      type: 'object',
      properties: {
        powerLevel: { 
          type: 'number', 
          minimum: 1, 
          maximum: 100,
          description: 'Overall power level on 1-100 scale'
        },
        fightingStyle: { 
          type: 'string',
          description: 'Primary fighting style and approach'
        },
        personality: { 
          type: 'array', 
          items: { type: 'string' },
          description: 'Key personality traits'
        },
        strengths: { 
          type: 'array', 
          items: { type: 'string' },
          description: 'Character strengths and advantages'
        },
        weaknesses: { 
          type: 'array', 
          items: { type: 'string' },
          description: 'Character weaknesses and limitations'
        },
        marketPrediction: {
          type: 'object',
          properties: {
            currentValue: { 
              type: 'number',
              description: 'Current estimated market value in berries'
            },
            predictedValue: { 
              type: 'number',
              description: 'Predicted value in 6 months'
            },
            confidence: { 
              type: 'number', 
              minimum: 0, 
              maximum: 1,
              description: 'Confidence in prediction (0-1)'
            },
            reasoning: { 
              type: 'string',
              description: 'Detailed reasoning for market prediction'
            }
          },
          required: ['currentValue', 'predictedValue', 'confidence', 'reasoning']
        }
      },
      required: ['powerLevel', 'fightingStyle', 'personality', 'strengths', 'weaknesses', 'marketPrediction']
    };

    try {
      const analysis = await this.aiProvider.generateStructured(prompt, schema);
      return this.validateAndSanitizeAnalysis(analysis);
    } catch (error) {
      console.error('Character analysis failed:', error);
      throw new Error(`Failed to analyze character ${character.name}: ${error.message}`);
    }
  }

  private validateAndSanitizeAnalysis(analysis: any): CharacterAnalysis {
    // Ensure power level is within bounds
    analysis.powerLevel = Math.max(1, Math.min(100, analysis.powerLevel || 50));
    
    // Ensure confidence is within bounds
    if (analysis.marketPrediction) {
      analysis.marketPrediction.confidence = Math.max(0, Math.min(1, analysis.marketPrediction.confidence || 0.5));
    }
    
    // Ensure arrays exist and have content
    analysis.personality = Array.isArray(analysis.personality) ? analysis.personality : ['Unknown'];
    analysis.strengths = Array.isArray(analysis.strengths) ? analysis.strengths : ['To be determined'];
    analysis.weaknesses = Array.isArray(analysis.weaknesses) ? analysis.weaknesses : ['To be determined'];
    
    // Ensure market prediction exists
    if (!analysis.marketPrediction) {
      analysis.marketPrediction = {
        currentValue: 1000000,
        predictedValue: 1000000,
        confidence: 0.5,
        reasoning: 'Analysis incomplete'
      };
    }
    
    return analysis as CharacterAnalysis;
  }

  async generatePersonalizedRecommendations(
    userPreferences: string[],
    tradingHistory: any[],
    availableCharacters: Character[],
    count: number = 5
  ): Promise<TradingRecommendation[]> {
    const prompt = `
      As an expert One Piece trading advisor, recommend characters for a user with these preferences:
      
      User Preferences: ${userPreferences.join(', ')}
      Recent Trading History: ${JSON.stringify(tradingHistory.slice(-3))}
      
      Available Characters:
      ${availableCharacters.map(c => `- ${c.name} (${c.crew}) - ${c.bounty.toLocaleString()} berries`).join('\n')}
      
      Provide ${count} personalized recommendations considering:
      1. User's stated preferences and interests
      2. Their trading patterns and risk tolerance
      3. Character potential and market trends
      4. Portfolio diversification opportunities
      
      For each recommendation, specify buy/sell/hold action with clear reasoning.
    `;

    const schema = {
      type: 'object',
      properties: {
        recommendations: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              action: { type: 'string', enum: ['buy', 'sell', 'hold'] },
              characterName: { type: 'string' },
              confidence: { type: 'number', minimum: 0, maximum: 1 },
              reasoning: { type: 'string' },
              targetPrice: { type: 'number' },
              timeframe: { type: 'string' }
            },
            required: ['action', 'characterName', 'confidence', 'reasoning', 'timeframe']
          }
        }
      },
      required: ['recommendations']
    };

    try {
      const result = await this.aiProvider.generateStructured(prompt, schema);
      
      return result.recommendations.map((rec: any) => {
        const character = availableCharacters.find(c => 
          c.name.toLowerCase().includes(rec.characterName.toLowerCase())
        );
        
        if (!character) {
          console.warn(`Character not found: ${rec.characterName}`);
          return null;
        }
        
        return {
          action: rec.action,
          character,
          confidence: Math.max(0, Math.min(1, rec.confidence)),
          reasoning: rec.reasoning,
          targetPrice: rec.targetPrice,
          timeframe: rec.timeframe
        } as TradingRecommendation;
      }).filter(Boolean);
    } catch (error) {
      console.error('Recommendation generation failed:', error);
      throw new Error(`Failed to generate recommendations: ${error.message}`);
    }
  }
}

// ============================================================================
// 🎯 SECTION 4: STREAMING AI SERVICE
// ============================================================================

export class StreamingAIService {
  private aiProvider: AIProvider;

  constructor(provider: AIProvider) {
    this.aiProvider = provider;
  }

  async streamCharacterAnalysis(
    character: Character,
    onChunk: (chunk: string) => void,
    onComplete: (fullResponse: string) => void,
    onError: (error: Error) => void
  ): Promise<void> {
    let fullResponse = '';
    
    const prompt = `
      Provide an engaging, detailed analysis of ${character.name} from One Piece.
      
      Character Details:
      - Name: ${character.name}
      - Crew: ${character.crew}
      - Bounty: ${character.bounty.toLocaleString()} berries
      - Devil Fruit: ${character.devilFruit || 'None'}
      - Haki: ${character.haki.join(', ') || 'None'}
      - Description: ${character.description}
      
      Write this as an exciting character profile that would captivate One Piece fans.
      Include their abilities, personality, role in the story, and what makes them unique.
      
      Structure your response with clear sections:
      1. Character Overview
      2. Abilities and Powers
      3. Personality and Motivations
      4. Story Impact and Development
      5. Trading Potential and Market Analysis
      
      Make it informative but entertaining, like a professional trading card description.
    `;

    try {
      await this.aiProvider.streamText(prompt, (chunk: string) => {
        fullResponse += chunk;
        onChunk(chunk);
      });
      
      onComplete(fullResponse);
    } catch (error) {
      onError(error as Error);
    }
  }

  async streamTradingAdvice(
    query: string,
    context: any,
    onChunk: (chunk: string) => void,
    onComplete: (fullResponse: string) => void,
    onError: (error: Error) => void
  ): Promise<void> {
    let fullResponse = '';
    
    const prompt = `
      You are an expert One Piece character trading advisor. A user is asking for advice:
      
      User Query: "${query}"
      
      Context:
      - User's Portfolio: ${JSON.stringify(context.portfolio || [])}
      - Market Conditions: ${JSON.stringify(context.marketConditions || {})}
      - User's Risk Tolerance: ${context.riskTolerance || 'moderate'}
      
      Provide helpful, actionable trading advice. Be specific about:
      1. Recommended actions (buy/sell/hold)
      2. Reasoning behind recommendations
      3. Risk assessment and mitigation
      4. Market timing considerations
      5. Alternative strategies to consider
      
      Be professional but engaging, like a knowledgeable friend giving advice.
    `;

    try {
      await this.aiProvider.streamText(prompt, (chunk: string) => {
        fullResponse += chunk;
        onChunk(chunk);
      });
      
      onComplete(fullResponse);
    } catch (error) {
      onError(error as Error);
    }
  }
}

// ============================================================================
// 🎯 SECTION 5: DEMO DATA AND EXECUTION
// ============================================================================

// Sample character data for testing
const SAMPLE_CHARACTERS: Character[] = [
  {
    id: '1',
    name: 'Monkey D. Luffy',
    bounty: 3000000000,
    crew: 'Straw Hat Pirates',
    devilFruit: 'Gomu Gomu no Mi (Hito Hito no Mi, Model: Nika)',
    haki: ['Observation', 'Armament', 'Conqueror\'s'],
    description: 'Captain of the Straw Hat Pirates and aspiring Pirate King. Known for his rubber powers and indomitable will.'
  },
  {
    id: '2',
    name: 'Roronoa Zoro',
    bounty: 1111000000,
    crew: 'Straw Hat Pirates',
    haki: ['Observation', 'Armament'],
    description: 'Swordsman of the Straw Hat Pirates, aiming to become the world\'s greatest swordsman. Master of the three-sword style.'
  },
  {
    id: '3',
    name: 'Nami',
    bounty: 366000000,
    crew: 'Straw Hat Pirates',
    haki: [],
    description: 'Navigator of the Straw Hat Pirates with exceptional weather prediction skills and the Clima-Tact weapon.'
  }
];

/**
 * 🚀 MAIN DEMO FUNCTION
 * 
 * This function demonstrates all AI/LLM integration concepts
 */
export async function runOnePieceAIDemo(): Promise<void> {
  console.log('🤖 ONE PIECE AI/LLM INTEGRATION DEMO');
  console.log('=====================================');
  console.log('');

  // Check for API keys
  const openaiKey = process.env.OPENAI_API_KEY;
  const anthropicKey = process.env.ANTHROPIC_API_KEY;

  if (!openaiKey && !anthropicKey) {
    console.log('❌ No API keys found. Please set OPENAI_API_KEY or ANTHROPIC_API_KEY environment variables.');
    console.log('');
    console.log('Example:');
    console.log('export OPENAI_API_KEY="your-openai-key-here"');
    console.log('export ANTHROPIC_API_KEY="your-anthropic-key-here"');
    return;
  }

  try {
    // Initialize AI providers
    const providers: AIProvider[] = [];
    
    if (openaiKey) {
      providers.push(new OpenAIProvider(openaiKey));
      console.log('✅ OpenAI provider initialized');
    }
    
    if (anthropicKey) {
      providers.push(new AnthropicProvider(anthropicKey));
      console.log('✅ Anthropic provider initialized');
    }

    console.log('');

    // Demo 1: Character Analysis
    console.log('🎯 DEMO 1: CHARACTER ANALYSIS');
    console.log('------------------------------');
    
    const analysisService = new CharacterAnalysisService(providers[0]);
    const character = SAMPLE_CHARACTERS[0];
    
    console.log(`Analyzing ${character.name}...`);
    
    try {
      const analysis = await analysisService.analyzeCharacter(character);
      
      console.log('📊 Analysis Results:');
      console.log(`   Power Level: ${analysis.powerLevel}/100`);
      console.log(`   Fighting Style: ${analysis.fightingStyle}`);
      console.log(`   Personality: ${analysis.personality.join(', ')}`);
      console.log(`   Market Value: ${analysis.marketPrediction.currentValue.toLocaleString()} berries`);
      console.log(`   Predicted Value: ${analysis.marketPrediction.predictedValue.toLocaleString()} berries`);
      console.log(`   Confidence: ${(analysis.marketPrediction.confidence * 100).toFixed(1)}%`);
      console.log(`   Reasoning: ${analysis.marketPrediction.reasoning}`);
    } catch (error) {
      console.log(`❌ Analysis failed: ${error.message}`);
    }

    console.log('');

    // Demo 2: Streaming Analysis
    console.log('🌊 DEMO 2: STREAMING ANALYSIS');
    console.log('------------------------------');
    
    const streamingService = new StreamingAIService(providers[0]);
    
    console.log(`Streaming analysis for ${SAMPLE_CHARACTERS[1].name}...`);
    console.log('');
    
    let streamedContent = '';
    
    await streamingService.streamCharacterAnalysis(
      SAMPLE_CHARACTERS[1],
      (chunk: string) => {
        process.stdout.write(chunk);
        streamedContent += chunk;
      },
      (fullResponse: string) => {
        console.log('\n');
        console.log('✅ Streaming complete!');
      },
      (error: Error) => {
        console.log(`\n❌ Streaming failed: ${error.message}`);
      }
    );

    console.log('');

    // Demo 3: Personalized Recommendations
    console.log('🎯 DEMO 3: PERSONALIZED RECOMMENDATIONS');
    console.log('----------------------------------------');
    
    const userPreferences = ['strong fighters', 'swordsmen', 'loyal crew members'];
    const tradingHistory = [
      { action: 'buy', character: 'Zoro', price: 800000000 },
      { action: 'sell', character: 'Buggy', price: 15000000 }
    ];
    
    console.log('Generating personalized recommendations...');
    
    try {
      const recommendations = await analysisService.generatePersonalizedRecommendations(
        userPreferences,
        tradingHistory,
        SAMPLE_CHARACTERS,
        3
      );
      
      console.log('💡 Recommendations:');
      recommendations.forEach((rec, index) => {
        console.log(`   ${index + 1}. ${rec.action.toUpperCase()} ${rec.character.name}`);
        console.log(`      Confidence: ${(rec.confidence * 100).toFixed(1)}%`);
        console.log(`      Timeframe: ${rec.timeframe}`);
        console.log(`      Reasoning: ${rec.reasoning}`);
        if (rec.targetPrice) {
          console.log(`      Target Price: ${rec.targetPrice.toLocaleString()} berries`);
        }
        console.log('');
      });
    } catch (error) {
      console.log(`❌ Recommendations failed: ${error.message}`);
    }

    console.log('🎉 Demo completed successfully!');
    console.log('');
    console.log('✅ Concepts Demonstrated:');
    console.log('   - Multiple AI provider integration');
    console.log('   - Structured data extraction');
    console.log('   - Streaming AI responses');
    console.log('   - Personalized recommendations');
    console.log('   - Error handling and validation');
    console.log('   - Cost-optimized API usage');

  } catch (error) {
    console.error('❌ Demo failed:', error);
  }
}

// Run the demo if this file is executed directly
if (require.main === module) {
  runOnePieceAIDemo().catch(console.error);
}
