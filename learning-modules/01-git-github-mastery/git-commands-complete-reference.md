# 🚀 COMPLETE GIT COMMANDS REFERENCE - ALL COMMANDS EXPLAINED

## 🎯 BASIC GIT COMMANDS

### **Repository Initialization & Cloning**
```bash
# Initialize new repository
git init
git init --bare  # Create bare repository
git init --template=<template_directory>

# Clone repositories
git clone <url>
git clone <url> <directory>
git clone --depth 1 <url>  # Shallow clone
git clone --branch <branch> <url>
git clone --recursive <url>  # Clone with submodules
```

### **Configuration**
```bash
# Global configuration
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global merge.tool vimdiff

# Local configuration
git config user.name "Project Name"
git config user.email "project@example.com"

# List all configurations
git config --list
git config --global --list
git config --local --list

# Aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'
```

## 🔧 FILE OPERATIONS

### **Adding & Staging**
```bash
# Add files to staging
git add <file>
git add .  # Add all files
git add -A  # Add all files including deleted
git add -u  # Add only modified files
git add -p  # Interactive staging
git add -i  # Interactive mode

# Remove files
git rm <file>
git rm --cached <file>  # Remove from staging only
git rm -r <directory>
git rm --dry-run <file>  # Preview removal

# Move/rename files
git mv <old_name> <new_name>
```

### **Status & Differences**
```bash
# Check status
git status
git status -s  # Short format
git status --porcelain  # Machine-readable format

# View differences
git diff  # Working directory vs staging
git diff --staged  # Staging vs last commit
git diff HEAD  # Working directory vs last commit
git diff <commit1> <commit2>
git diff --name-only
git diff --stat
git diff --word-diff
```

## 📝 COMMIT OPERATIONS

### **Basic Commits**
```bash
# Commit changes
git commit -m "Commit message"
git commit -am "Add and commit"
git commit --amend  # Modify last commit
git commit --amend --no-edit  # Amend without changing message
git commit -v  # Verbose commit (show diff)

# Empty commits
git commit --allow-empty -m "Empty commit"

# Commit with specific date
git commit --date="2023-01-01 12:00:00" -m "Message"
```

### **Advanced Commit Operations**
```bash
# Interactive commits
git commit -p  # Patch mode
git add -p && git commit  # Interactive staging and commit

# Commit templates
git config --global commit.template ~/.gitmessage.txt

# GPG signing
git commit -S -m "Signed commit"
git config --global commit.gpgsign true
```

## 🌿 BRANCHING & MERGING

### **Branch Operations**
```bash
# List branches
git branch  # Local branches
git branch -r  # Remote branches
git branch -a  # All branches
git branch -v  # Verbose (with last commit)
git branch --merged  # Merged branches
git branch --no-merged  # Unmerged branches

# Create branches
git branch <branch_name>
git branch <branch_name> <commit>
git checkout -b <branch_name>  # Create and switch
git switch -c <branch_name>  # New syntax

# Switch branches
git checkout <branch_name>
git switch <branch_name>  # New syntax
git checkout -  # Switch to previous branch

# Delete branches
git branch -d <branch_name>  # Safe delete
git branch -D <branch_name>  # Force delete
git push origin --delete <branch_name>  # Delete remote branch

# Rename branches
git branch -m <old_name> <new_name>
git branch -M <new_name>  # Rename current branch
```

### **Merging**
```bash
# Merge branches
git merge <branch_name>
git merge --no-ff <branch_name>  # No fast-forward
git merge --squash <branch_name>  # Squash merge
git merge --strategy=ours <branch_name>
git merge --strategy-option=theirs <branch_name>

# Abort merge
git merge --abort

# Continue merge after resolving conflicts
git merge --continue
```

## 🌐 REMOTE OPERATIONS

### **Remote Management**
```bash
# List remotes
git remote
git remote -v  # Verbose
git remote show origin

# Add remotes
git remote add <name> <url>
git remote add upstream <url>

# Remove remotes
git remote remove <name>
git remote rm <name>

# Rename remotes
git remote rename <old_name> <new_name>

# Change remote URL
git remote set-url origin <new_url>
```

### **Fetch, Pull, Push**
```bash
# Fetch changes
git fetch
git fetch origin
git fetch --all
git fetch --prune  # Remove deleted remote branches

# Pull changes
git pull
git pull origin main
git pull --rebase  # Rebase instead of merge
git pull --ff-only  # Fast-forward only

# Push changes
git push
git push origin main
git push -u origin main  # Set upstream
git push --all  # Push all branches
git push --tags  # Push tags
git push --force  # Force push (dangerous)
git push --force-with-lease  # Safer force push
```

## 📚 HISTORY & LOGGING

### **Log Commands**
```bash
# Basic log
git log
git log --oneline  # Compact format
git log --graph  # ASCII graph
git log --all  # All branches
git log --decorate  # Show refs

# Advanced log formatting
git log --pretty=format:"%h %an %ar - %s"
git log --pretty=oneline
git log --pretty=short
git log --pretty=full
git log --pretty=fuller

# Log filtering
git log -n 5  # Last 5 commits
git log --since="2 weeks ago"
git log --until="2023-01-01"
git log --author="John Doe"
git log --grep="bug fix"
git log --all --grep="feature"

# File-specific log
git log <file>
git log --follow <file>  # Follow renames
git log -p <file>  # Show patches
git log --stat <file>  # Show stats
```

### **Show & Blame**
```bash
# Show commit details
git show <commit>
git show --name-only <commit>
git show --stat <commit>

# Blame (line-by-line history)
git blame <file>
git blame -L 10,20 <file>  # Specific lines
git blame -w <file>  # Ignore whitespace
```

## 🔄 REBASE & RESET

### **Rebase Operations**
```bash
# Basic rebase
git rebase <branch>
git rebase origin/main

# Interactive rebase
git rebase -i HEAD~3  # Last 3 commits
git rebase -i <commit>

# Rebase options during interactive mode:
# pick = use commit
# reword = use commit, but edit message
# edit = use commit, but stop for amending
# squash = use commit, but meld into previous
# fixup = like squash, but discard message
# drop = remove commit

# Continue/abort rebase
git rebase --continue
git rebase --abort
git rebase --skip
```

### **Reset Operations**
```bash
# Soft reset (keep changes staged)
git reset --soft HEAD~1

# Mixed reset (default - unstage changes)
git reset HEAD~1
git reset --mixed HEAD~1

# Hard reset (discard all changes)
git reset --hard HEAD~1
git reset --hard origin/main

# Reset specific files
git reset HEAD <file>
git reset --hard HEAD <file>
```

## 🍒 CHERRY-PICK & STASH

### **Cherry-pick**
```bash
# Cherry-pick commits
git cherry-pick <commit>
git cherry-pick <commit1> <commit2>
git cherry-pick <commit1>..<commit2>

# Cherry-pick options
git cherry-pick --no-commit <commit>  # Don't auto-commit
git cherry-pick -x <commit>  # Add source commit info
git cherry-pick --continue
git cherry-pick --abort
```

### **Stash Operations**
```bash
# Stash changes
git stash
git stash push -m "Work in progress"
git stash -u  # Include untracked files
git stash -a  # Include all files

# List stashes
git stash list
git stash show
git stash show -p  # Show patch

# Apply stashes
git stash apply
git stash apply stash@{2}
git stash pop  # Apply and remove
git stash pop stash@{2}

# Manage stashes
git stash drop stash@{2}
git stash clear  # Remove all stashes
git stash branch <branch> stash@{2}
```

## 🏷️ TAGS & RELEASES

### **Tag Operations**
```bash
# List tags
git tag
git tag -l "v1.*"  # Pattern matching

# Create tags
git tag <tagname>  # Lightweight tag
git tag -a <tagname> -m "Tag message"  # Annotated tag
git tag -a <tagname> <commit>  # Tag specific commit

# Show tag info
git show <tagname>

# Delete tags
git tag -d <tagname>  # Local
git push origin --delete <tagname>  # Remote

# Push tags
git push origin <tagname>
git push origin --tags  # All tags
```

## 🔍 SEARCH & DEBUGGING

### **Search Commands**
```bash
# Search in files
git grep "search term"
git grep -n "search term"  # Show line numbers
git grep -i "search term"  # Case insensitive
git grep -w "search term"  # Whole word

# Search in history
git log -S "search term"  # Pickaxe search
git log -G "regex pattern"  # Regex search
git log --grep="commit message search"
```

### **Debugging**
```bash
# Bisect (binary search for bugs)
git bisect start
git bisect bad  # Current commit is bad
git bisect good <commit>  # Known good commit
git bisect reset  # End bisect session

# Reflog (reference log)
git reflog
git reflog show HEAD
git reflog show <branch>

# Fsck (file system check)
git fsck
git fsck --full
```

## 🔧 ADVANCED OPERATIONS

### **Submodules**
```bash
# Add submodule
git submodule add <url> <path>

# Initialize submodules
git submodule init
git submodule update
git submodule update --init --recursive

# Update submodules
git submodule update --remote
git submodule foreach git pull origin main

# Remove submodule
git submodule deinit <path>
git rm <path>
```

### **Worktrees**
```bash
# Add worktree
git worktree add <path> <branch>
git worktree add ../feature-branch feature

# List worktrees
git worktree list

# Remove worktree
git worktree remove <path>
git worktree prune
```

### **Clean Operations**
```bash
# Clean untracked files
git clean -n  # Dry run
git clean -f  # Force clean
git clean -fd  # Clean files and directories
git clean -fx  # Clean ignored files too
```

## 🛠️ MAINTENANCE & OPTIMIZATION

### **Repository Maintenance**
```bash
# Garbage collection
git gc
git gc --aggressive
git gc --auto

# Prune operations
git prune
git remote prune origin

# Verify repository
git fsck --full
git count-objects -v

# Repack repository
git repack -ad
```

### **Configuration & Hooks**
```bash
# Hook management
ls .git/hooks/
chmod +x .git/hooks/pre-commit

# Archive repository
git archive --format=zip HEAD > project.zip
git archive --format=tar.gz --prefix=project/ HEAD > project.tar.gz
```

This complete reference covers ALL Git commands from basic to advanced level! 🚀
