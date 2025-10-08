/*
🏴‍☠️ TRADING MODELS - C# DATA MODELS BLUEPRINT
Your mission: Create data models for trading operations and database entities

WHAT YOU'RE BUILDING:
- Entity Framework models for database tables
- Data Transfer Objects (DTOs) for API communication
- Validation attributes for data integrity
- Enums for trade types and statuses
- Model relationships and navigation properties

LEARNING OBJECTIVES:
- C# class and property syntax
- Entity Framework Code First approach
- Data annotations and validation
- Enum types and their usage
- Object-oriented programming concepts
- Navigation properties and relationships
*/

// TODO 1: USING STATEMENTS
// Add these using statements:
// using System.ComponentModel.DataAnnotations;
// using System.ComponentModel.DataAnnotations.Schema;
// using Microsoft.EntityFrameworkCore;

// WRITE YOUR USING STATEMENTS HERE:


// TODO 2: TRADE TYPE ENUM
// namespace TradingService.Models
// {
//     public enum TradeType
//     {
//         // Define enum values for BUY and SELL
//         // BUY = 1,
//         // SELL = 2
//     }
// }

// TODO 3: TRADE STATUS ENUM
// public enum TradeStatus
// {
//     // Define enum values for trade statuses
//     // PENDING = 1,
//     // COMPLETED = 2,
//     // CANCELLED = 3,
//     // FAILED = 4
// }

// TODO 4: PORTFOLIO MODEL (Database Entity)
// [Table("portfolios")]
// public class Portfolio
// {
//     // Primary key
//     // [Key]
//     // public int Id { get; set; }
//     
//     // Foreign key to User
//     // [Required]
//     // public int UserId { get; set; }
//     
//     // Foreign key to Character
//     // [Required]
//     // public int CharacterId { get; set; }
//     
//     // Number of shares owned
//     // [Required]
//     // [Range(0, int.MaxValue)]
//     // public int Quantity { get; set; }
//     
//     // Average purchase price
//     // [Required]
//     // [Column(TypeName = "decimal(10,2)")]
//     // public decimal AveragePrice { get; set; }
//     
//     // Total amount invested
//     // [Required]
//     // [Column(TypeName = "decimal(12,2)")]
//     // public decimal TotalInvested { get; set; }
//     
//     // Timestamps
//     // public DateTime CreatedAt { get; set; }
//     // public DateTime UpdatedAt { get; set; }
// }

// TODO 5: TRADE MODEL (Database Entity)
// [Table("trades")]
// public class Trade
// {
//     // Primary key
//     // [Key]
//     // public int Id { get; set; }
//     
//     // User who made the trade
//     // [Required]
//     // public int UserId { get; set; }
//     
//     // Character being traded
//     // [Required]
//     // public int CharacterId { get; set; }
//     
//     // Trade type (BUY/SELL)
//     // [Required]
//     // public TradeType TradeType { get; set; }
//     
//     // Number of shares
//     // [Required]
//     // [Range(1, int.MaxValue)]
//     // public int Quantity { get; set; }
//     
//     // Price per share at time of trade
//     // [Required]
//     // [Column(TypeName = "decimal(10,2)")]
//     // public decimal Price { get; set; }
//     
//     // Total trade amount
//     // [Required]
//     // [Column(TypeName = "decimal(12,2)")]
//     // public decimal TotalAmount { get; set; }
//     
//     // Trade status
//     // [Required]
//     // public TradeStatus Status { get; set; }
//     
//     // Trade timestamp
//     // public DateTime Timestamp { get; set; }
// }

// TODO 6: BUY ORDER DTO (Data Transfer Object)
// public class BuyOrderDto
// {
//     // User making the purchase
//     // [Required]
//     // public int UserId { get; set; }
//     
//     // Character to buy
//     // [Required]
//     // public int CharacterId { get; set; }
//     
//     // Number of shares to buy
//     // [Required]
//     // [Range(1, 10000, ErrorMessage = "Quantity must be between 1 and 10,000")]
//     // public int Quantity { get; set; }
//     
//     // Maximum price willing to pay (optional for market orders)
//     // [Range(0.01, 999999.99)]
//     // public decimal? MaxPrice { get; set; }
// }

// TODO 7: SELL ORDER DTO
// public class SellOrderDto
// {
//     // User making the sale
//     // [Required]
//     // public int UserId { get; set; }
//     
//     // Character to sell
//     // [Required]
//     // public int CharacterId { get; set; }
//     
//     // Number of shares to sell
//     // [Required]
//     // [Range(1, int.MaxValue)]
//     // public int Quantity { get; set; }
//     
//     // Minimum price willing to accept (optional)
//     // [Range(0.01, 999999.99)]
//     // public decimal? MinPrice { get; set; }
// }

// TODO 8: TRADE RESULT DTO
// public class TradeResultDto
// {
//     // Trade ID
//     // public int TradeId { get; set; }
//     
//     // Success status
//     // public bool Success { get; set; }
//     
//     // Trade details
//     // public int UserId { get; set; }
//     // public int CharacterId { get; set; }
//     // public string CharacterName { get; set; }
//     // public TradeType TradeType { get; set; }
//     // public int Quantity { get; set; }
//     // public decimal Price { get; set; }
//     // public decimal TotalAmount { get; set; }
//     
//     // Updated balances
//     // public decimal NewBalance { get; set; }
//     // public int NewQuantity { get; set; }
//     
//     // Timestamp
//     // public DateTime Timestamp { get; set; }
//     
//     // Error message if failed
//     // public string? ErrorMessage { get; set; }
// }

// TODO 9: PORTFOLIO DTO
// public class PortfolioDto
// {
//     // User information
//     // public int UserId { get; set; }
//     // public decimal TotalBalance { get; set; }
//     // public decimal TotalInvested { get; set; }
//     // public decimal TotalValue { get; set; }
//     // public decimal TotalGainLoss { get; set; }
//     
//     // Holdings list
//     // public List<PortfolioHoldingDto> Holdings { get; set; }
// }

// TODO 10: PORTFOLIO HOLDING DTO
// public class PortfolioHoldingDto
// {
//     // Character information
//     // public int CharacterId { get; set; }
//     // public string CharacterName { get; set; }
//     // public string Crew { get; set; }
//     
//     // Holding details
//     // public int Quantity { get; set; }
//     // public decimal AveragePrice { get; set; }
//     // public decimal CurrentPrice { get; set; }
//     // public decimal TotalInvested { get; set; }
//     // public decimal CurrentValue { get; set; }
//     // public decimal GainLoss { get; set; }
//     // public decimal GainLossPercentage { get; set; }
// }

/*
🎯 WHAT EACH MODEL DOES:

Portfolio: Database entity for user stock holdings
Trade: Database entity for trade transactions
BuyOrderDto: Data for buy requests from frontend
SellOrderDto: Data for sell requests from frontend
TradeResultDto: Response data after trade execution
PortfolioDto: Complete portfolio data for frontend
PortfolioHoldingDto: Individual stock holding data

🚀 C# MODEL CONCEPTS:

1. Classes and Properties - Object structure
2. Data Annotations - Validation attributes
3. Enums - Fixed set of values
4. Nullable types (decimal?) - Optional values
5. Collections (List<T>) - Multiple items
6. Navigation properties - Entity relationships

📚 ENTITY FRAMEWORK CONCEPTS:

1. [Table] - Maps class to database table
2. [Key] - Primary key designation
3. [Required] - Not null constraint
4. [Range] - Value range validation
5. [Column] - Database column configuration
6. Navigation properties - Foreign key relationships

🔧 VALIDATION ATTRIBUTES:

1. [Required] - Field must have value
2. [Range] - Numeric range validation
3. [StringLength] - Text length limits
4. [EmailAddress] - Email format validation
5. [RegularExpression] - Pattern matching
6. Custom validation attributes

NEXT FILE AFTER THIS: Create Trading Service (Business Logic)! 🚀
*/
