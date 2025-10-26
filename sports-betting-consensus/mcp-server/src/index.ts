# ============================================================================
# 📚 LEARNING GUIDE: MCP Server Implementation (mcp-server/src/index.ts)
# ============================================================================
#
# 🎯 PURPOSE:
# This MCP (Model Context Protocol) server exposes sports betting consensus data
# as tools that AI agents can use programmatically. It enables:
# - AI assistants to query betting predictions and consensus data
# - Automated analysis and recommendation generation
# - Integration with Claude, GPT, and other AI agents
# - Structured access to sports betting insights
# - Real-time data feeds for AI-powered applications
#
# 🔧 TECHNOLOGIES USED:
# - Model Context Protocol (MCP): Standard for AI agent tool integration
# - TypeScript: Type-safe server development
# - Express.js: HTTP server for MCP endpoints
# - Zod: Runtime type validation and schema definition
# - Winston: Structured logging and monitoring
# - JWT: Authentication for secure tool access
# - Rate Limiting: Prevent abuse and ensure fair usage
#
# 📖 IN-DEPTH EXPLANATION:
#
# **What is MCP (Model Context Protocol)?**
# MCP is a standardized protocol that allows AI agents to:
# 1. Discover available tools and their capabilities
# 2. Execute tools with structured parameters
# 3. Receive structured responses for further processing
# 4. Maintain context across multiple tool calls
# 5. Handle authentication and authorization
#
# **MCP vs Traditional APIs:**
# - Traditional API: Human developers integrate manually
# - MCP: AI agents integrate automatically using tool descriptions
# - MCP provides schema-driven tool discovery
# - Built-in support for complex workflows and chaining
#
# **Tool Categories in This Server:**
# 1. **Query Tools**: Get predictions, consensus, historical data
# 2. **Analysis Tools**: Calculate accuracy, trends, performance
# 3. **Recommendation Tools**: Generate betting advice
# 4. **Monitoring Tools**: Health checks, system status
#
# **MCP Tool Structure:**
# ```typescript
# {
#   name: "get_consensus_prediction",
#   description: "Get consensus betting prediction for a game",
#   inputSchema: {
#     type: "object",
#     properties: {
#       team1: { type: "string" },
#       team2: { type: "string" },
#       sport: { type: "string" }
#     }
#   }
# }
# ```
#
# **Authentication Flow:**
# 1. AI agent requests access token
# 2. Server validates credentials and issues JWT
# 3. Agent includes token in tool execution requests
# 4. Server validates token and executes tool
# 5. Structured response returned to agent
#
# **Real-world AI Agent Workflows:**
# - "Analyze Lakers vs Warriors game and recommend bet"
# - "Compare accuracy of different prediction sources"
# - "Find best betting opportunities for tonight's games"
# - "Track my betting performance over last month"
#
# 📚 LEARNING MODULE REFERENCES:
# - Module 34 (TypeScript/Node.js): Lines 300-500 - Express.js server setup
# - Module 36 (AI/LLM Integration): Lines 1000-1200 - Tool integration patterns
# - Module 35 (React/Next.js): Lines 600-800 - API design principles
#
# ✅ IMPLEMENTATION CHECKLIST:
# [ ] Set up MCP server with Express.js and TypeScript
# [ ] Define tool schemas with Zod validation
# [ ] Implement authentication with JWT tokens
# [ ] Create sports betting query tools
# [ ] Add consensus calculation tools
# [ ] Implement historical analysis tools
# [ ] Add rate limiting and security measures
# [ ] Create comprehensive logging and monitoring
# [ ] Add health check and status endpoints
# [ ] Implement error handling and validation
# [ ] Add integration tests for all tools
#
# 🎓 WHAT YOU NEED TO LEARN/UNDERSTAND:
# - Model Context Protocol specification and standards
# - Tool schema design and validation
# - JWT authentication and authorization
# - Express.js middleware and routing
# - TypeScript interfaces and type safety
# - Zod schema validation and runtime checking
# - Rate limiting and security best practices
# - Structured logging and monitoring
# - API design for AI agent consumption
# - Error handling and graceful degradation
#
# 🚀 REAL-WORLD EXAMPLES:
# - Anthropic: Claude can use MCP tools for external data
# - OpenAI: GPT agents integrate with MCP servers
# - GitHub Copilot: Uses MCP for code repository access
# - Slack bots: MCP integration for workspace tools
#
# 💡 MCP TOOL EXAMPLES:
#
# **Tool 1: Get Consensus Prediction**
# ```typescript
# {
#   name: "get_consensus_prediction",
#   description: "Get AI-powered consensus prediction for a sports game",
#   inputSchema: {
#     type: "object",
#     properties: {
#       team1: { type: "string", description: "First team name" },
#       team2: { type: "string", description: "Second team name" },
#       sport: { type: "string", enum: ["NBA", "NFL", "MLB", "NHL"] },
#       date: { type: "string", format: "date" }
#     },
#     required: ["team1", "team2", "sport"]
#   }
# }
# ```
#
# **Tool 2: Analyze Source Accuracy**
# ```typescript
# {
#   name: "analyze_source_accuracy",
#   description: "Analyze historical accuracy of prediction sources",
#   inputSchema: {
#     type: "object",
#     properties: {
#       sources: { type: "array", items: { type: "string" } },
#       timeframe: { type: "string", enum: ["7d", "30d", "90d", "1y"] },
#       sport: { type: "string" }
#     }
#   }
# }
# ```
#
# **Tool 3: Find Best Bets**
# ```typescript
# {
#   name: "find_best_betting_opportunities",
#   description: "Find games with highest consensus and confidence",
#   inputSchema: {
#     type: "object",
#     properties: {
#       date: { type: "string", format: "date" },
#       min_consensus: { type: "number", minimum: 0.5, maximum: 1.0 },
#       min_confidence: { type: "number", minimum: 0.5, maximum: 1.0 },
#       sports: { type: "array", items: { type: "string" } }
#     }
#   }
# }
# ```
#
# 🔐 SECURITY CONSIDERATIONS:
# - Validate all input parameters with Zod schemas
# - Implement rate limiting per API key/user
# - Use HTTPS for all communications
# - Sanitize responses to prevent data leakage
# - Log all tool executions for audit trails
# - Implement proper error handling without exposing internals
#
# 📊 MONITORING AND ANALYTICS:
# - Track tool usage patterns and popularity
# - Monitor response times and error rates
# - Analyze AI agent behavior and workflows
# - Alert on unusual usage patterns
# - Generate usage reports for optimization
#
# 🔍 DEBUGGING MCP INTEGRATION:
# - Use MCP client tools for testing
# - Log all requests and responses
# - Validate schemas with sample data
# - Test with different AI agents (Claude, GPT)
# - Monitor network traffic and latency
#
# ============================================================================
# 📝 REFERENCE IMPLEMENTATION (Check your code against this)
# ============================================================================
#
# import express from 'express';
# import cors from 'cors';
# import helmet from 'helmet';
# import { z } from 'zod';
# import winston from 'winston';
# import jwt from 'jsonwebtoken';
# import rateLimit from 'express-rate-limit';
# import { MCPServer } from '@modelcontextprotocol/sdk';
# 
# // Type definitions
# interface MCPTool {
#   name: string;
#   description: string;
#   inputSchema: z.ZodSchema;
#   handler: (params: any) => Promise<any>;
# }
# 
# interface ConsensusData {
#   predicted_winner: string;
#   confidence: number;
#   consensus_percentage: number;
#   sources: Array<{
#     name: string;
#     prediction: string;
#     confidence: number;
#   }>;
# }
# 
# // Zod schemas for validation
# const GameQuerySchema = z.object({
#   team1: z.string().min(2),
#   team2: z.string().min(2),
#   sport: z.enum(['NBA', 'NFL', 'MLB', 'NHL', 'Soccer']),
#   date: z.string().optional(),
# });
# 
# const AccuracyAnalysisSchema = z.object({
#   sources: z.array(z.string()).optional(),
#   timeframe: z.enum(['7d', '30d', '90d', '1y']).default('30d'),
#   sport: z.string().optional(),
# });
# 
# // Logger setup
# const logger = winston.createLogger({
#   level: 'info',
#   format: winston.format.combine(
#     winston.format.timestamp(),
#     winston.format.json()
#   ),
#   transports: [
#     new winston.transports.File({ filename: 'mcp-server.log' }),
#     new winston.transports.Console()
#   ],
# });
# 
# class SportsBettingMCPServer {
#   private app: express.Application;
#   private mcpServer: MCPServer;
#   private tools: Map<string, MCPTool> = new Map();
# 
#   constructor() {
#     this.app = express();
#     this.mcpServer = new MCPServer({
#       name: 'sports-betting-consensus',
#       version: '1.0.0',
#     });
#     
#     this.setupMiddleware();
#     this.registerTools();
#     this.setupRoutes();
#   }
# 
#   private setupMiddleware() {
#     // Security middleware
#     this.app.use(helmet());
#     this.app.use(cors({
#       origin: process.env.ALLOWED_ORIGINS?.split(',') || ['http://localhost:3000'],
#       credentials: true,
#     }));
# 
#     // Rate limiting
#     const limiter = rateLimit({
#       windowMs: 15 * 60 * 1000, // 15 minutes
#       max: 100, // limit each IP to 100 requests per windowMs
#       message: 'Too many requests from this IP',
#     });
#     this.app.use(limiter);
# 
#     // Body parsing
#     this.app.use(express.json({ limit: '10mb' }));
#     this.app.use(express.urlencoded({ extended: true }));
# 
#     // Logging middleware
#     this.app.use((req, res, next) => {
#       logger.info(`${req.method} ${req.path}`, {
#         ip: req.ip,
#         userAgent: req.get('User-Agent'),
#       });
#       next();
#     });
#   }
# 
#   private registerTools() {
#     // Tool 1: Get Consensus Prediction
#     this.tools.set('get_consensus_prediction', {
#       name: 'get_consensus_prediction',
#       description: 'Get AI-powered consensus prediction for a sports game',
#       inputSchema: GameQuerySchema,
#       handler: this.getConsensusPrediction.bind(this),
#     });
# 
#     // Tool 2: Analyze Source Accuracy
#     this.tools.set('analyze_source_accuracy', {
#       name: 'analyze_source_accuracy',
#       description: 'Analyze historical accuracy of prediction sources',
#       inputSchema: AccuracyAnalysisSchema,
#       handler: this.analyzeSourceAccuracy.bind(this),
#     });
# 
#     // Tool 3: Find Best Betting Opportunities
#     this.tools.set('find_best_opportunities', {
#       name: 'find_best_opportunities',
#       description: 'Find games with highest consensus and confidence for betting',
#       inputSchema: z.object({
#         date: z.string().optional(),
#         min_consensus: z.number().min(0.5).max(1.0).default(0.7),
#         min_confidence: z.number().min(0.5).max(1.0).default(0.7),
#         sports: z.array(z.string()).optional(),
#       }),
#       handler: this.findBestOpportunities.bind(this),
#     });
# 
#     // Register tools with MCP server
#     for (const [name, tool] of this.tools) {
#       this.mcpServer.setRequestHandler({ method: `tools/${name}` }, async (request) => {
#         try {
#           const validatedParams = tool.inputSchema.parse(request.params);
#           const result = await tool.handler(validatedParams);
#           return { content: [{ type: 'text', text: JSON.stringify(result) }] };
#         } catch (error) {
#           logger.error(`Tool execution failed: ${name}`, { error: error.message });
#           throw error;
#         }
#       });
#     }
#   }
# 
#   private async getConsensusPrediction(params: z.infer<typeof GameQuerySchema>): Promise<ConsensusData> {
#     logger.info('Getting consensus prediction', params);
#     
#     // Call the Python backend API
#     const response = await fetch(`${process.env.PYTHON_API_URL}/api/v1/predictions/consensus`, {
#       method: 'POST',
#       headers: { 'Content-Type': 'application/json' },
#       body: JSON.stringify(params),
#     });
# 
#     if (!response.ok) {
#       throw new Error(`Failed to get consensus: ${response.statusText}`);
#     }
# 
#     const data = await response.json();
#     return data;
#   }
# 
#   private async analyzeSourceAccuracy(params: z.infer<typeof AccuracyAnalysisSchema>) {
#     logger.info('Analyzing source accuracy', params);
#     
#     // Implementation would call analytics API
#     return {
#       timeframe: params.timeframe,
#       sources: [
#         { name: 'ESPN', accuracy: 0.72, total_predictions: 150 },
#         { name: 'CBS Sports', accuracy: 0.68, total_predictions: 142 },
#         { name: 'The Athletic', accuracy: 0.75, total_predictions: 98 },
#       ],
#       overall_accuracy: 0.71,
#     };
#   }
# 
#   private async findBestOpportunities(params: any) {
#     logger.info('Finding best betting opportunities', params);
#     
#     // Implementation would query database for high-confidence predictions
#     return {
#       opportunities: [
#         {
#           game: 'Lakers vs Warriors',
#           predicted_winner: 'Lakers',
#           consensus: 0.85,
#           confidence: 0.78,
#           recommendation: 'Strong bet recommendation',
#         },
#       ],
#       total_found: 1,
#       criteria: params,
#     };
#   }
# 
#   private setupRoutes() {
#     // Health check
#     this.app.get('/health', (req, res) => {
#       res.json({
#         status: 'healthy',
#         timestamp: new Date().toISOString(),
#         tools: Array.from(this.tools.keys()),
#       });
#     });
# 
#     // MCP tool discovery
#     this.app.get('/tools', (req, res) => {
#       const toolDescriptions = Array.from(this.tools.values()).map(tool => ({
#         name: tool.name,
#         description: tool.description,
#         inputSchema: tool.inputSchema._def,
#       }));
#       
#       res.json({ tools: toolDescriptions });
#     });
# 
#     // MCP tool execution endpoint
#     this.app.post('/tools/:toolName', async (req, res) => {
#       const { toolName } = req.params;
#       const tool = this.tools.get(toolName);
# 
#       if (!tool) {
#         return res.status(404).json({ error: 'Tool not found' });
#       }
# 
#       try {
#         const validatedParams = tool.inputSchema.parse(req.body);
#         const result = await tool.handler(validatedParams);
#         res.json({ result });
#       } catch (error) {
#         logger.error(`Tool execution failed: ${toolName}`, { error: error.message });
#         res.status(400).json({ error: error.message });
#       }
#     });
#   }
# 
#   public start(port: number = 3001) {
#     this.app.listen(port, () => {
#       logger.info(`MCP Server running on port ${port}`);
#       logger.info(`Available tools: ${Array.from(this.tools.keys()).join(', ')}`);
#     });
#   }
# }
# 
# // Start the server
# const server = new SportsBettingMCPServer();
# server.start(parseInt(process.env.PORT || '3001'));
# 
# export default SportsBettingMCPServer;
#
# ============================================================================
