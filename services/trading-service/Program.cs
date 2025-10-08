/*
🏴‍☠️ TRADING SERVICE - C# .NET CORE WEB API BLUEPRINT
Your mission: Build a trading engine for buying/selling One Piece character stocks

WHAT YOU'RE BUILDING:
- C# Web API with ASP.NET Core
- Trading engine business logic
- Portfolio management system
- Database operations with Entity Framework
- HTTP client communication with Character Service

LEARNING OBJECTIVES:
- C# programming language fundamentals
- ASP.NET Core Web API development
- Entity Framework Core (ORM)
- Dependency Injection in .NET
- HTTP client communication between services
- Business logic implementation
- Error handling and validation in C#
*/

// TODO 1: USING STATEMENTS
// Add these using statements at the top:
// using Microsoft.EntityFrameworkCore;
// using Microsoft.AspNetCore.Mvc;
// using System.ComponentModel.DataAnnotations;
// using System.Text.Json;
// using Microsoft.Extensions.DependencyInjection;
// using Microsoft.Extensions.Hosting;
// using Microsoft.Extensions.Configuration;

// WRITE YOUR USING STATEMENTS HERE:


// TODO 2: MAIN PROGRAM CLASS
// namespace TradingService
// {
//     public class Program
//     {
//         public static void Main(string[] args)
//         {
//             // Create web application builder
//             // Configure services (database, HTTP client, etc.)
//             // Configure middleware pipeline
//             // Run the application
//         }
//     }
// }

// TODO 3: CONFIGURE SERVICES METHOD
// Add this method to configure dependency injection:
// public static void ConfigureServices(WebApplicationBuilder builder)
// {
//     // Add Entity Framework with MySQL
//     // Add HTTP client for Character Service communication
//     // Add controllers and API explorer
//     // Add CORS policy
//     // Add logging services
// }

// TODO 4: CONFIGURE MIDDLEWARE METHOD  
// Add this method to configure request pipeline:
// public static void ConfigureMiddleware(WebApplication app)
// {
//     // Add development exception page
//     // Add CORS middleware
//     // Add routing
//     // Map controllers
//     // Add health check endpoint
// }

/*
🎯 WHAT EACH PART DOES:

Program.cs: Entry point for your C# application
ConfigureServices: Sets up dependency injection container
ConfigureMiddleware: Sets up request processing pipeline
Using statements: Import necessary .NET libraries

🚀 C# CONCEPTS YOU'LL LEARN:

1. Namespace organization
2. Static methods and classes
3. Dependency injection pattern
4. Configuration management
5. Middleware pipeline
6. HTTP client setup
7. Entity Framework setup

📚 ASP.NET CORE CONCEPTS:

1. WebApplicationBuilder - Configures the app
2. Services container - Dependency injection
3. Middleware pipeline - Request processing
4. Controllers - Handle HTTP requests
5. Entity Framework - Database ORM
6. Configuration - App settings management

🔧 .NET PROJECT STRUCTURE:

Program.cs - Application entry point
Controllers/ - API endpoint handlers
Models/ - Data models and DTOs
Services/ - Business logic
Data/ - Database context and configurations

NEXT FILE AFTER THIS: Create TradingController.cs! 🚀
*/
