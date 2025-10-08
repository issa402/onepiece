/*
🏴‍☠️ USER SERVICE - AUTHENTICATION CONTROLLER BLUEPRINT
Your mission: Create user authentication and management system with JWT tokens

WHAT YOU'RE BUILDING:
- User registration and login endpoints
- JWT token generation and validation
- Password hashing and security
- User profile management
- Account balance management
- Role-based access control

LEARNING OBJECTIVES:
- JWT (JSON Web Token) authentication
- Password hashing with BCrypt
- C# security best practices
- Claims-based authentication
- Middleware and authorization
- Secure API design patterns
*/

// TODO 1: USING STATEMENTS
// Add these using statements:
// using Microsoft.AspNetCore.Mvc;
// using Microsoft.AspNetCore.Authorization;
// using Microsoft.IdentityModel.Tokens;
// using System.IdentityModel.Tokens.Jwt;
// using System.Security.Claims;
// using System.Text;
// using BCrypt.Net;
// using UserService.Models;
// using UserService.Services;
// using UserService.DTOs;

// WRITE YOUR USING STATEMENTS HERE:


// TODO 2: CONTROLLER CLASS DECLARATION
// namespace UserService.Controllers
// {
//     [ApiController]
//     [Route("api/[controller]")]
//     public class AuthController : ControllerBase
//     {
//         // Dependency injection fields
//         // private readonly IUserService _userService;
//         // private readonly IConfiguration _configuration;
//         // private readonly ILogger<AuthController> _logger;
//         
//         // Constructor for dependency injection
//         // public AuthController(IUserService userService, ...)
//     }
// }

// TODO 3: USER REGISTRATION ENDPOINT
// [HttpPost("register")]
// public async Task<ActionResult<AuthResponseDto>> Register([FromBody] RegisterDto registerDto)
// {
//     // Validate registration data
//     // Check if username/email already exists
//     // Hash the password using BCrypt
//     // Create new user in database
//     // Generate JWT token for new user
//     // Return user info and token
// }

// TODO 4: USER LOGIN ENDPOINT
// [HttpPost("login")]
// public async Task<ActionResult<AuthResponseDto>> Login([FromBody] LoginDto loginDto)
// {
//     // Find user by username or email
//     // Verify password using BCrypt
//     // Check if user account is active
//     // Generate JWT token
//     // Update last login timestamp
//     // Return user info and token
// }

// TODO 5: REFRESH TOKEN ENDPOINT
// [HttpPost("refresh")]
// public async Task<ActionResult<AuthResponseDto>> RefreshToken([FromBody] RefreshTokenDto refreshDto)
// {
//     // Validate refresh token
//     // Check if token is expired
//     // Generate new access token
//     // Optionally rotate refresh token
//     // Return new tokens
// }

// TODO 6: LOGOUT ENDPOINT
// [HttpPost("logout")]
// [Authorize]
// public async Task<ActionResult> Logout()
// {
//     // Get user ID from JWT claims
//     // Invalidate refresh tokens
//     // Add token to blacklist (optional)
//     // Log logout event
//     // Return success response
// }

// TODO 7: GET USER PROFILE ENDPOINT
// [HttpGet("profile")]
// [Authorize]
// public async Task<ActionResult<UserProfileDto>> GetProfile()
// {
//     // Get user ID from JWT claims
//     // Retrieve user profile from database
//     // Return user profile data (without sensitive info)
// }

// TODO 8: UPDATE USER PROFILE ENDPOINT
// [HttpPut("profile")]
// [Authorize]
// public async Task<ActionResult<UserProfileDto>> UpdateProfile([FromBody] UpdateProfileDto updateDto)
// {
//     // Get user ID from JWT claims
//     // Validate update data
//     // Update user profile in database
//     // Return updated profile
// }

// TODO 9: CHANGE PASSWORD ENDPOINT
// [HttpPost("change-password")]
// [Authorize]
// public async Task<ActionResult> ChangePassword([FromBody] ChangePasswordDto changePasswordDto)
// {
//     // Get user ID from JWT claims
//     // Verify current password
//     // Validate new password strength
//     // Hash new password
//     // Update password in database
//     // Invalidate all existing tokens (optional)
//     // Return success response
// }

// TODO 10: GET USER BALANCE ENDPOINT
// [HttpGet("balance")]
// [Authorize]
// public async Task<ActionResult<BalanceDto>> GetBalance()
// {
//     // Get user ID from JWT claims
//     // Retrieve current balance from database
//     // Return balance information
// }

// TODO 11: UPDATE USER BALANCE ENDPOINT (Internal)
// [HttpPost("balance/update")]
// [Authorize(Roles = "System")]
// public async Task<ActionResult> UpdateBalance([FromBody] UpdateBalanceDto updateDto)
// {
//     // Validate system authorization
//     // Update user balance (for trading operations)
//     // Log balance change
//     // Return success response
// }

// TODO 12: VALIDATE TOKEN ENDPOINT (Internal)
// [HttpPost("validate-token")]
// public async Task<ActionResult<TokenValidationDto>> ValidateToken([FromBody] ValidateTokenDto tokenDto)
// {
//     // Parse and validate JWT token
//     // Check token expiration
//     // Verify token signature
//     // Return validation result with user claims
// }

// TODO 13: JWT TOKEN GENERATION METHOD
// private string GenerateJwtToken(User user)
// {
//     // Create JWT security token handler
//     // Define token claims (user ID, username, roles, etc.)
//     // Set token expiration time
//     // Sign token with secret key
//     // Return token string
// }

// TODO 14: PASSWORD VALIDATION METHOD
// private bool ValidatePassword(string password)
// {
//     // Check minimum length (8 characters)
//     // Require at least one uppercase letter
//     // Require at least one lowercase letter
//     // Require at least one number
//     // Require at least one special character
//     // Return validation result
// }

/*
🎯 WHAT EACH ENDPOINT DOES:

Register: Creates new user accounts with password hashing
Login: Authenticates users and returns JWT tokens
RefreshToken: Generates new access tokens
Logout: Invalidates user sessions
GetProfile: Returns user profile information
UpdateProfile: Updates user profile data
ChangePassword: Allows users to change passwords
GetBalance: Returns user's account balance
UpdateBalance: Updates balance (for trading operations)
ValidateToken: Validates JWT tokens (internal use)

🚀 JWT AUTHENTICATION CONCEPTS:

1. JWT Structure - Header.Payload.Signature
2. Claims - User information in token
3. Token expiration - Security through time limits
4. Token signing - Cryptographic verification
5. Bearer token - Authorization header format
6. Refresh tokens - Long-term authentication

📚 SECURITY CONCEPTS:

1. Password hashing - BCrypt for secure storage
2. Salt and pepper - Additional password security
3. Token blacklisting - Invalidate compromised tokens
4. Rate limiting - Prevent brute force attacks
5. Input validation - Prevent injection attacks
6. HTTPS only - Secure transmission

🔧 C# SECURITY FEATURES:

1. [Authorize] attribute - Require authentication
2. Claims-based authorization - Role and permission checks
3. Data annotations - Input validation
4. Secure configuration - Environment variables
5. Logging and monitoring - Security event tracking

AUTHENTICATION FLOW:
1. User registers/logs in
2. Server validates credentials
3. Server generates JWT token
4. Client stores token
5. Client sends token in Authorization header
6. Server validates token on each request

NEXT FILE AFTER THIS: Create User Models and DTOs! 🚀
*/
