// Jest setup file for One Piece Trading Platform

// Extend Jest matchers
expect.extend({
  toBeValidCharacter(received) {
    const pass = received && 
                 typeof received.id === 'string' &&
                 typeof received.name === 'string' &&
                 typeof received.bounty === 'number' &&
                 typeof received.crew === 'string' &&
                 Array.isArray(received.haki) &&
                 typeof received.isActive === 'boolean';
    
    if (pass) {
      return {
        message: () => `expected ${JSON.stringify(received)} not to be a valid character`,
        pass: true,
      };
    } else {
      return {
        message: () => `expected ${JSON.stringify(received)} to be a valid character`,
        pass: false,
      };
    }
  },
});

// Global test setup
beforeAll(() => {
  console.log('🏴‍☠️ Starting One Piece Trading Platform Tests...');
});

afterAll(() => {
  console.log('🎉 All tests completed!');
});

// Mock console methods for cleaner test output
global.console = {
  ...console,
  // Uncomment to suppress logs during tests
  // log: jest.fn(),
  // info: jest.fn(),
  // warn: jest.fn(),
  // error: jest.fn(),
};
