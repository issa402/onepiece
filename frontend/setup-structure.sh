#!/bin/bash

# Create folders
mkdir -p src/components/{Dashboard,Characters,Portfolio,Trading,Auth}
mkdir -p src/contexts

# Create files
touch src/components/Dashboard/Dashboard.tsx
touch src/components/Characters/CharacterDetail.tsx
touch src/components/Portfolio/Portfolio.tsx
touch src/components/Trading/Trading.tsx
touch src/components/Auth/Login.tsx
touch src/components/Auth/Register.tsx
touch src/contexts/AuthContext.tsx
touch src/contexts/ApiContext.tsx
