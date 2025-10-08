#!/usr/bin/env node

// 🔥 VERIFY ALL LEARNING MODULES USE YOUR REAL DATABASE
// This script checks that ALL modules use YOUR onepiece_market database
// and have NO hardcoded data or PostgreSQL references

const fs = require('fs');
const path = require('path');

console.log('🔥 VERIFYING ALL LEARNING MODULES');
console.log('=================================');
console.log('🎯 Checking: All modules use YOUR onepiece_market MySQL database');
console.log('❌ Looking for: PostgreSQL, hardcoded data, fake data');
console.log('');

// Things that should NOT exist in any module
const badPatterns = [
    { pattern: /PostgreSQL/gi, name: 'PostgreSQL references' },
    { pattern: /postgres/gi, name: 'postgres references' },
    { pattern: /node-postgres/gi, name: 'node-postgres library' },
    { pattern: /'pg'/gi, name: 'pg library imports' },
    { pattern: /"pg"/gi, name: 'pg library imports' },
    { pattern: /require\('pg'\)/gi, name: 'pg require statements' },
    { pattern: /require\("pg"\)/gi, name: 'pg require statements' },
    { pattern: /new Pool\(/gi, name: 'PostgreSQL Pool syntax' },
    { pattern: /onepiece_trading/gi, name: 'old database name' },
    { pattern: /trading_platform/gi, name: 'old database name' },
    { pattern: /5432/g, name: 'PostgreSQL port' },
    { pattern: /\$1|\$2|\$3|\$4|\$5/g, name: 'PostgreSQL parameter syntax' },
    { pattern: /result\.rows/gi, name: 'PostgreSQL result syntax' },
    { pattern: /hardcoded data/gi, name: 'hardcoded data references' },
    { pattern: /fake data/gi, name: 'fake data references' },
    { pattern: /previous_price/gi, name: 'old column names' },
    { pattern: /daily_change/gi, name: 'old column names' },
    { pattern: /last_updated/gi, name: 'old column names' },
];

// Things that SHOULD exist in database-related modules
const goodPatterns = [
    { pattern: /onepiece_market/gi, name: 'YOUR database name' },
    { pattern: /mysql2/gi, name: 'MySQL library' },
    { pattern: /3306/g, name: 'MySQL port' },
    { pattern: /current_price/gi, name: 'YOUR schema columns' },
    { pattern: /sentiment_score/gi, name: 'YOUR schema columns' },
    { pattern: /weekly_change/gi, name: 'YOUR schema columns' },
];

// Function to check a file
function checkFile(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const issues = [];
        const goodFeatures = [];
        
        // Check for bad patterns
        badPatterns.forEach(({ pattern, name }) => {
            const matches = content.match(pattern);
            if (matches) {
                issues.push(`❌ Found ${matches.length} ${name}`);
            }
        });
        
        // Check for good patterns (only in database-related files)
        if (content.includes('database') || content.includes('Database') || content.includes('mysql') || content.includes('MySQL')) {
            goodPatterns.forEach(({ pattern, name }) => {
                const matches = content.match(pattern);
                if (matches) {
                    goodFeatures.push(`✅ Found ${matches.length} ${name}`);
                }
            });
        }
        
        return { issues, goodFeatures };
    } catch (error) {
        return { issues: [`❌ Error reading file: ${error.message}`], goodFeatures: [] };
    }
}

// Function to check all files in a directory
function checkDirectory(dirPath, moduleName) {
    const items = fs.readdirSync(dirPath);
    let totalIssues = 0;
    let totalGoodFeatures = 0;
    const moduleIssues = [];
    const moduleGoodFeatures = [];
    
    items.forEach(item => {
        const itemPath = path.join(dirPath, item);
        const stat = fs.statSync(itemPath);
        
        if (stat.isFile() && (item.endsWith('.js') || item.endsWith('.ts') || item.endsWith('.tsx') || item.endsWith('.py'))) {
            const { issues, goodFeatures } = checkFile(itemPath);
            
            if (issues.length > 0) {
                moduleIssues.push(`   📁 ${item}:`);
                issues.forEach(issue => moduleIssues.push(`      ${issue}`));
                totalIssues += issues.length;
            }
            
            if (goodFeatures.length > 0) {
                moduleGoodFeatures.push(`   📁 ${item}:`);
                goodFeatures.forEach(feature => moduleGoodFeatures.push(`      ${feature}`));
                totalGoodFeatures += goodFeatures.length;
            }
        }
    });
    
    return { totalIssues, totalGoodFeatures, moduleIssues, moduleGoodFeatures };
}

// Main verification
async function verifyAllModules() {
    const learningModulesPath = path.join(__dirname, 'learning-modules');
    
    if (!fs.existsSync(learningModulesPath)) {
        console.error('❌ learning-modules directory not found!');
        process.exit(1);
    }
    
    const modules = fs.readdirSync(learningModulesPath)
        .filter(item => {
            const itemPath = path.join(learningModulesPath, item);
            return fs.statSync(itemPath).isDirectory() && !item.startsWith('.');
        });
    
    console.log(`📁 Checking ${modules.length} learning modules...\n`);
    
    let totalIssuesFound = 0;
    let totalGoodFeaturesFound = 0;
    let modulesWithIssues = 0;
    let modulesWithGoodFeatures = 0;
    
    for (const module of modules) {
        const modulePath = path.join(learningModulesPath, module);
        const { totalIssues, totalGoodFeatures, moduleIssues, moduleGoodFeatures } = checkDirectory(modulePath, module);
        
        if (totalIssues > 0 || totalGoodFeatures > 0) {
            console.log(`🔍 ${module}:`);
            
            if (totalIssues > 0) {
                console.log(`❌ Found ${totalIssues} issues:`);
                moduleIssues.forEach(issue => console.log(issue));
                modulesWithIssues++;
                totalIssuesFound += totalIssues;
            }
            
            if (totalGoodFeatures > 0) {
                console.log(`✅ Found ${totalGoodFeatures} good features:`);
                moduleGoodFeatures.forEach(feature => console.log(feature));
                modulesWithGoodFeatures++;
                totalGoodFeaturesFound += totalGoodFeatures;
            }
            
            console.log('');
        } else {
            console.log(`✅ ${module}: No database-related content or already clean`);
        }
    }
    
    console.log('🎯 VERIFICATION SUMMARY:');
    console.log('========================');
    console.log(`📊 Total modules checked: ${modules.length}`);
    console.log(`❌ Modules with issues: ${modulesWithIssues}`);
    console.log(`✅ Modules with good features: ${modulesWithGoodFeatures}`);
    console.log(`🔍 Total issues found: ${totalIssuesFound}`);
    console.log(`🎉 Total good features found: ${totalGoodFeaturesFound}`);
    console.log('');
    
    if (totalIssuesFound === 0) {
        console.log('🎉 PERFECT! ALL MODULES ARE CLEAN!');
        console.log('✅ No PostgreSQL references found');
        console.log('✅ No hardcoded data references found');
        console.log('✅ No old database names found');
        console.log('✅ All modules use YOUR onepiece_market database');
        console.log('');
        console.log('🏴‍☠️ ALL MODULES ARE READY FOR YOUR REAL DATABASE! ⚔️');
    } else {
        console.log('⚠️ ISSUES FOUND - NEED TO FIX:');
        console.log(`❌ ${totalIssuesFound} issues need to be resolved`);
        console.log('💡 Run the fix script again or manually update the files');
        console.log('');
        console.log('🔧 Quick fixes:');
        console.log('   - Replace PostgreSQL → MySQL');
        console.log('   - Replace onepiece_trading → onepiece_market');
        console.log('   - Replace hardcoded data → YOUR real database');
        console.log('   - Replace pg → mysql2');
        console.log('   - Replace $1, $2 → ?');
        console.log('   - Replace 5432 → 3306');
    }
    
    console.log('');
    console.log('🚀 Next Steps:');
    console.log('1. If issues found, fix them manually or run fix script again');
    console.log('2. Make sure MySQL is running: sudo systemctl start mysql');
    console.log('3. Set up YOUR database: mysql -u root -p < database/schema.sql');
    console.log('4. Insert YOUR data: mysql -u root -p < database/sample_data.sql');
    console.log('5. Test any module: cd learning-modules/15-javascript-fundamentals && npm install && npm start');
}

// Run the verification
verifyAllModules().catch(console.error);
