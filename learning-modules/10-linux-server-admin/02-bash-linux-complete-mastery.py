"""
🐧 LINUX & BASH COMPLETE MASTERY - FROM ZERO TO EXPERT
═══════════════════════════════════════════════════════════

This is EVERYTHING you need to know about Linux and Bash to be
comfortable on any server without a GUI. Companies want engineers
who can SSH into a production server at 3am and fix shit.

═══════════════════════════════════════════════════════════
🏗️ PART 1: UNDERSTANDING THE ARCHITECTURE
═══════════════════════════════════════════════════════════

THE LAYERS OF A COMPUTER (Top to Bottom):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│  YOU (typing commands)                                   │
├─────────────────────────────────────────────────────────┤
│  SHELL (bash, zsh, fish) - Interprets your commands     │
├─────────────────────────────────────────────────────────┤
│  SYSTEM UTILITIES (ls, cat, grep) - Programs that do    │
│  specific tasks                                          │
├─────────────────────────────────────────────────────────┤
│  LINUX KERNEL - The brain of the OS, talks to hardware  │
├─────────────────────────────────────────────────────────┤
│  HARDWARE (CPU, RAM, Disk, Network Card)                │
└─────────────────────────────────────────────────────────┘

WHAT IS LINUX?
━━━━━━━━━━━━━━
Linux is the KERNEL - the core software that:
- Manages CPU time between programs (process scheduling)
- Manages RAM (memory allocation)
- Manages disk access (file systems)
- Manages network communication
- Manages device drivers (hardware communication)
- Provides security and permissions

Linux was created by Linus Torvalds in 1991. It's open source,
meaning anyone can see and modify the code.

WHAT IS A LINUX DISTRIBUTION (DISTRO)?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A distro = Linux kernel + package manager + default software + config

Common Distros:
┌────────────────┬─────────────────────────────────────────────┐
│ DISTRO         │ USE CASE                                    │
├────────────────┼─────────────────────────────────────────────┤
│ Ubuntu         │ Desktop, beginners, servers (you're on this)│
│ Debian         │ Stable servers, Ubuntu is based on this     │
│ CentOS/RHEL    │ Enterprise servers, banks, corporations     │
│ Fedora         │ Cutting edge, Red Hat testing ground        │
│ Arch           │ Advanced users, minimal, you build it       │
│ Alpine         │ Docker containers, tiny size (5MB)          │
│ Amazon Linux   │ AWS EC2 instances                           │
└────────────────┴─────────────────────────────────────────────┘

WHAT IS A SHELL?
━━━━━━━━━━━━━━━━
A shell is a program that:
1. Shows you a prompt (like: user@machine:~$ )
2. Reads what you type
3. Interprets the command
4. Asks the kernel to execute it
5. Shows you the output

It's called a "shell" because it's the outer layer around the kernel.

WHAT IS BASH?
━━━━━━━━━━━━━
Bash = "Bourne Again Shell" (a pun on "born again" and Stephen Bourne
who created the original sh shell)

Bash is the most common shell. When you open Terminal on Ubuntu,
you're running bash. It's both:
1. An interactive command interpreter (you type, it runs)
2. A scripting language (you write .sh files, it runs them)

OTHER SHELLS:
┌─────────┬────────────────────────────────────────────────────┐
│ SHELL   │ DESCRIPTION                                        │
├─────────┼────────────────────────────────────────────────────┤
│ sh      │ Original Bourne shell, basic, POSIX compliant      │
│ bash    │ Most common, what you should learn first           │
│ zsh     │ Bash++ with better autocomplete (Mac default now)  │
│ fish    │ Friendly, auto-suggestions, not POSIX compliant    │
│ dash    │ Minimal, fast, used for system scripts             │
│ ksh     │ Korn shell, popular in enterprise Unix             │
└─────────┴────────────────────────────────────────────────────┘

You only need to learn Bash. If a company uses zsh, you'll adapt
in hours because it's 95% the same syntax.

HOW TO CHECK YOUR SHELL:
"""

# Run this in your terminal:
# echo $SHELL
# Output: /bin/bash (or /usr/bin/bash or /bin/zsh)

# To see all available shells on your system:
# cat /etc/shells

# To temporarily switch to another shell:
# zsh    # switches to zsh
# exit   # goes back to previous shell

# To permanently change your default shell:
# chsh -s /bin/zsh

"""
═══════════════════════════════════════════════════════════
🏗️ PART 2: THE LINUX FILE SYSTEM - EVERYTHING IS A FILE
═══════════════════════════════════════════════════════════

In Linux, EVERYTHING is represented as a file:
- Regular files (text, binary, images)
- Directories (special files that list other files)
- Devices (your hard drive is /dev/sda)
- Processes (info in /proc)
- Network sockets
- Pipes for communication

THE DIRECTORY STRUCTURE:
━━━━━━━━━━━━━━━━━━━━━━━━
"""

LINUX_FILESYSTEM = """
/                   # ROOT - the top of everything
├── bin/            # Essential binaries (ls, cat, cp, mv, rm)
├── sbin/           # System binaries (init, shutdown, ifconfig)
├── boot/           # Boot loader files (kernel, grub)
├── dev/            # Device files
│   ├── sda         # First hard drive
│   ├── sda1        # First partition of first drive
│   ├── null        # Black hole - discards anything written
│   ├── zero        # Infinite zeros
│   ├── random      # Random numbers
│   └── tty         # Terminal devices
├── etc/            # Configuration files (like Windows Registry)
│   ├── passwd      # User accounts
│   ├── shadow      # Encrypted passwords
│   ├── hosts       # Local DNS
│   ├── fstab       # Filesystem mount config
│   ├── ssh/        # SSH server config
│   ├── nginx/      # Nginx config
│   └── systemd/    # Service definitions
├── home/           # User home directories
│   └── iscjmz/     # YOUR home directory
├── lib/            # Shared libraries (.so files, like .dll)
├── media/          # Mount point for removable media (USB)
├── mnt/            # Mount point for temporary mounts
├── opt/            # Optional software (third party apps)
├── proc/           # Virtual filesystem for process info
│   ├── cpuinfo     # CPU information
│   ├── meminfo     # Memory information
│   └── [PID]/      # Info about process with that ID
├── root/           # Root user's home directory
├── run/            # Runtime data (PIDs, sockets)
├── srv/            # Service data (web servers, ftp)
├── sys/            # System information (hardware, kernel)
├── tmp/            # Temporary files (cleared on reboot)
├── usr/            # User programs and data
│   ├── bin/        # User binaries
│   ├── lib/        # User libraries
│   ├── local/      # Locally compiled software
│   └── share/      # Shared data (docs, icons)
└── var/            # Variable data
    ├── log/        # LOG FILES - very important!
    ├── cache/      # Application cache
    ├── mail/       # Email storage
    └── www/        # Web server files
"""

"""
IMPORTANT PATHS TO KNOW:
━━━━━━━━━━━━━━━━━━━━━━━━

~           = Your home directory (/home/iscjmz)
.           = Current directory
..          = Parent directory
/           = Root directory (top of filesystem)
/etc        = Configuration files
/var/log    = Log files (check here when debugging)
/tmp        = Temporary files
/dev/null   = Discard output (black hole)

PATH TYPES:
━━━━━━━━━━━
Absolute path: Starts from root /
  Example: /home/iscjmz/onepiece/README.md

Relative path: Starts from current directory
  Example: ./README.md or ../other-folder/file.txt

═══════════════════════════════════════════════════════════
🏗️ PART 3: ESSENTIAL BASH COMMANDS - NAVIGATION
═══════════════════════════════════════════════════════════

COMMAND STRUCTURE:
━━━━━━━━━━━━━━━━━━
command [options] [arguments]

Example: ls -la /home
         │   │   │
         │   │   └── argument (what to operate on)
         │   └────── options (modify behavior)
         └────────── command

Options usually start with:
-  (single dash, short form):  -l -a or combined: -la
-- (double dash, long form):   --all --long

NAVIGATION COMMANDS:
━━━━━━━━━━━━━━━━━━━━
"""

# pwd - Print Working Directory (where am I?)
# -----------------------------------------
# pwd
# Output: /home/iscjmz/onepiece

# cd - Change Directory
# -----------------------------------------
# cd /home              # Go to absolute path
# cd onepiece           # Go to relative path (inside current dir)
# cd ..                 # Go up one level
# cd ../..              # Go up two levels
# cd ~                  # Go to home directory (same as cd with no args)
# cd -                  # Go to previous directory (toggle)
# cd /                  # Go to root

# ls - List directory contents
# -----------------------------------------
# ls                    # List files in current directory
# ls /var/log           # List files in specific directory
# ls -l                 # Long format (permissions, owner, size, date)
# ls -a                 # Show hidden files (starting with .)
# ls -la                # Long format + hidden files (MOST COMMON)
# ls -lh                # Human readable sizes (1K, 2M, 3G)
# ls -lt                # Sort by modification time (newest first)
# ls -ltr               # Sort by time, reversed (oldest first)
# ls -lS                # Sort by size (largest first)
# ls -R                 # Recursive (list subdirectories too)
# ls -d */              # List only directories

"""
UNDERSTANDING ls -l OUTPUT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━

drwxr-xr-x  5  iscjmz  iscjmz  4096  Nov 27 10:00  onepiece
│└┬┘└┬┘└┬┘  │    │       │      │        │          │
│ │  │  │   │    │       │      │        │          └── Filename
│ │  │  │   │    │       │      │        └── Modification date
│ │  │  │   │    │       │      └── Size in bytes
│ │  │  │   │    │       └── Group owner
│ │  │  │   │    └── User owner
│ │  │  │   └── Number of hard links
│ │  │  └── Others permissions (r-x = read, execute)
│ │  └── Group permissions (r-x = read, execute)
│ └── User permissions (rwx = read, write, execute)
└── File type: d=directory, -=file, l=symlink

PERMISSIONS EXPLAINED:
━━━━━━━━━━━━━━━━━━━━━━
r = read    (4)  - Can view file contents / list directory
w = write   (2)  - Can modify file / create files in directory
x = execute (1)  - Can run file / can cd into directory

Examples:
rwx = 4+2+1 = 7 (full access)
rw- = 4+2+0 = 6 (read and write)
r-x = 4+0+1 = 5 (read and execute)
r-- = 4+0+0 = 4 (read only)
--- = 0+0+0 = 0 (no access)

chmod 755 file = rwxr-xr-x (owner full, others read+execute)
chmod 644 file = rw-r--r-- (owner read+write, others read only)
chmod 600 file = rw------- (owner read+write, others nothing)

═══════════════════════════════════════════════════════════
🏗️ PART 4: FILE OPERATIONS
═══════════════════════════════════════════════════════════
"""

# touch - Create empty file or update timestamp
# -----------------------------------------
# touch newfile.txt               # Create empty file
# touch file1.txt file2.txt       # Create multiple files
# touch -m existingfile.txt       # Update modification time only

# mkdir - Make directory
# -----------------------------------------
# mkdir newdir                    # Create directory
# mkdir -p parent/child/grandchild  # Create nested dirs (-p = parents)
# mkdir -m 755 securedir          # Create with specific permissions

# cp - Copy files/directories
# -----------------------------------------
# cp source.txt dest.txt          # Copy file
# cp file.txt /path/to/           # Copy to directory (keeps name)
# cp -r sourcedir destdir         # Copy directory recursively
# cp -i file.txt dest/            # Interactive (ask before overwrite)
# cp -v file.txt dest/            # Verbose (show what's happening)
# cp -p file.txt dest/            # Preserve permissions and timestamps

# mv - Move or rename files/directories
# -----------------------------------------
# mv oldname.txt newname.txt      # Rename file
# mv file.txt /path/to/           # Move file
# mv file.txt /path/to/newname.txt  # Move and rename
# mv -i file.txt dest/            # Interactive (ask before overwrite)
# mv -v file.txt dest/            # Verbose

# rm - Remove files/directories (DANGEROUS - NO TRASH BIN!)
# -----------------------------------------
# rm file.txt                     # Remove file
# rm file1.txt file2.txt          # Remove multiple files
# rm -r directory/                # Remove directory recursively
# rm -f file.txt                  # Force (no confirmation, ignore errors)
# rm -rf directory/               # Force recursive (DANGEROUS!)
# rm -i file.txt                  # Interactive (confirm each file)
# rm -v file.txt                  # Verbose

# NEVER RUN: rm -rf /  (deletes EVERYTHING)
# NEVER RUN: rm -rf ~  (deletes your entire home directory)

# ln - Create links
# -----------------------------------------
# ln -s /path/to/original symlink   # Create symbolic link (shortcut)
# ln original hardlink              # Create hard link
# Symbolic links are like shortcuts in Windows
# Hard links are like multiple names for the same file

"""
═══════════════════════════════════════════════════════════
🏗️ PART 5: VIEWING AND EDITING FILES
═══════════════════════════════════════════════════════════
"""

# cat - Concatenate and display file contents
# -----------------------------------------
# cat file.txt                    # Display entire file
# cat file1.txt file2.txt         # Display multiple files
# cat -n file.txt                 # Show line numbers
# cat > newfile.txt               # Create file (type content, Ctrl+D to save)
# cat >> file.txt                 # Append to file

# less - View file with pagination (BETTER for large files)
# -----------------------------------------
# less file.txt
# Navigation in less:
#   Space or f     = Forward one page
#   b              = Back one page
#   /pattern       = Search forward
#   ?pattern       = Search backward
#   n              = Next search result
#   N              = Previous search result
#   g              = Go to beginning
#   G              = Go to end
#   q              = Quit
#   h              = Help

# more - Simpler pagination (less is better)
# -----------------------------------------
# more file.txt                   # Basic pagination

# head - View first lines of file
# -----------------------------------------
# head file.txt                   # First 10 lines (default)
# head -n 20 file.txt             # First 20 lines
# head -n -5 file.txt             # All except last 5 lines
# head -c 100 file.txt            # First 100 bytes

# tail - View last lines of file (CRUCIAL for logs!)
# -----------------------------------------
# tail file.txt                   # Last 10 lines (default)
# tail -n 20 file.txt             # Last 20 lines
# tail -n +5 file.txt             # All lines starting from line 5
# tail -f file.txt                # FOLLOW - watch file in real-time (logs!)
# tail -F file.txt                # Follow even if file rotates
# tail -f -n 100 file.txt         # Show last 100 then follow

# wc - Word count
# -----------------------------------------
# wc file.txt                     # Lines, words, characters
# wc -l file.txt                  # Count lines only
# wc -w file.txt                  # Count words only
# wc -c file.txt                  # Count bytes
# wc -m file.txt                  # Count characters

"""
TEXT EDITORS IN TERMINAL:
━━━━━━━━━━━━━━━━━━━━━━━━━

1. nano - Easiest for beginners
   nano file.txt
   - Ctrl+O = Save
   - Ctrl+X = Exit
   - Ctrl+K = Cut line
   - Ctrl+U = Paste
   - Ctrl+W = Search

2. vim - Most powerful, steep learning curve
   vim file.txt
   Two modes: Command mode and Insert mode

   START IN COMMAND MODE:
   - i        = Enter insert mode (type text)
   - Esc      = Exit insert mode, back to command
   - :w       = Save
   - :q       = Quit
   - :wq      = Save and quit
   - :q!      = Quit without saving
   - dd       = Delete line
   - yy       = Copy line
   - p        = Paste
   - /pattern = Search
   - u        = Undo
   - Ctrl+r   = Redo

3. vi - Original vim (on older systems)
   Same as vim but fewer features

═══════════════════════════════════════════════════════════
🏗️ PART 6: SEARCHING AND FILTERING
═══════════════════════════════════════════════════════════
"""

# grep - Search for patterns in files (INCREDIBLY USEFUL)
# -----------------------------------------
# grep "error" file.txt                   # Find lines containing "error"
# grep -i "error" file.txt                # Case insensitive
# grep -r "error" /var/log/               # Recursive search in directory
# grep -n "error" file.txt                # Show line numbers
# grep -v "error" file.txt                # Invert (lines NOT containing)
# grep -c "error" file.txt                # Count matches
# grep -l "error" *.txt                   # List files containing pattern
# grep -w "error" file.txt                # Match whole word only
# grep -A 3 "error" file.txt              # Show 3 lines After match
# grep -B 3 "error" file.txt              # Show 3 lines Before match
# grep -C 3 "error" file.txt              # Show 3 lines Context (before+after)
# grep -E "error|warning" file.txt        # Extended regex (OR)
# grep "^Start" file.txt                  # Lines starting with "Start"
# grep "end$" file.txt                    # Lines ending with "end"

# find - Find files in directory tree
# -----------------------------------------
# find /path -name "filename"             # Find by exact name
# find /path -name "*.txt"                # Find by pattern
# find /path -iname "*.TXT"               # Case insensitive
# find /path -type f                      # Find files only
# find /path -type d                      # Find directories only
# find /path -size +100M                  # Files larger than 100MB
# find /path -size -1k                    # Files smaller than 1KB
# find /path -mtime -7                    # Modified in last 7 days
# find /path -mtime +30                   # Modified more than 30 days ago
# find /path -user root                   # Find files owned by root
# find /path -perm 755                    # Find by permission
# find /path -name "*.log" -delete        # Find and delete (CAREFUL!)
# find /path -name "*.txt" -exec cat {} \;  # Find and execute command

# locate - Fast file search (uses database, run updatedb first)
# -----------------------------------------
# locate filename                         # Quick search
# sudo updatedb                           # Update the database

# which - Find location of command
# -----------------------------------------
# which python                            # /usr/bin/python
# which ls                                # /bin/ls

# whereis - Find binary, source, manual
# -----------------------------------------
# whereis python                          # binary, source, man locations

"""
═══════════════════════════════════════════════════════════
🏗️ PART 7: PIPING AND REDIRECTION - POWER OF UNIX
═══════════════════════════════════════════════════════════

The real power of Linux comes from chaining commands together.
Each command does ONE thing well, then you combine them.

STANDARD STREAMS:
━━━━━━━━━━━━━━━━━
stdin  (0) = Standard Input  - where command reads from
stdout (1) = Standard Output - where command writes output
stderr (2) = Standard Error  - where command writes errors
"""

# REDIRECTION:
# -----------------------------------------
# command > file          # Redirect stdout to file (OVERWRITES)
# command >> file         # Redirect stdout to file (APPENDS)
# command 2> file         # Redirect stderr to file
# command 2>&1            # Redirect stderr to stdout
# command > file 2>&1     # Redirect both stdout and stderr to file
# command &> file         # Same as above (bash shortcut)
# command < file          # Read stdin from file

# Examples:
# ls -la > listing.txt                    # Save directory listing
# echo "new line" >> file.txt             # Append to file
# python script.py 2> errors.log          # Save only errors
# python script.py > output.log 2>&1      # Save all output
# command > /dev/null 2>&1                # Discard ALL output (silent)

# PIPING (|) - Send output of one command to input of another
# -----------------------------------------
# command1 | command2                     # Pipe stdout to next command

# Examples:
# ls -la | less                           # Paginate long listing
# cat file.txt | grep "error"             # Same as grep "error" file.txt
# history | grep "git"                    # Find git commands in history
# ps aux | grep python                    # Find python processes
# cat /var/log/syslog | grep error | tail -20   # Last 20 errors
# find . -name "*.py" | wc -l             # Count Python files
# ls -la | awk '{print $9}'               # Print only filenames
# cat file.txt | sort | uniq              # Sort and remove duplicates
# du -sh * | sort -h                      # Sort directories by size

"""
COMMON PIPE COMBINATIONS FOR SERVER WORK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# Find most common errors in log:
# cat /var/log/app.log | grep ERROR | sort | uniq -c | sort -rn | head -10

# Find largest files:
# du -ah /var | sort -rh | head -20

# Count requests by IP (from access log):
# cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Watch log for specific pattern:
# tail -f /var/log/app.log | grep --line-buffered "ERROR"

# Find and kill process:
# ps aux | grep python | awk '{print $2}' | xargs kill

"""
═══════════════════════════════════════════════════════════
🏗️ PART 8: PROCESS MANAGEMENT - SERVER ESSENTIALS
═══════════════════════════════════════════════════════════
"""

# ps - Process status
# -----------------------------------------
# ps                      # Your processes in current terminal
# ps aux                  # ALL processes (a=all users, u=user format, x=no terminal)
# ps -ef                  # Full format (alternative to aux)
# ps aux | grep nginx     # Find nginx processes
# ps -p 1234              # Show specific process by PID

"""
ps aux OUTPUT EXPLAINED:
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1  33832  4512 ?        Ss   Nov26   0:02 /sbin/init

USER    = Process owner
PID     = Process ID (unique identifier)
%CPU    = CPU usage percentage
%MEM    = Memory usage percentage
VSZ     = Virtual memory size
RSS     = Resident memory (actual RAM used)
TTY     = Terminal (? means no terminal)
STAT    = Status (S=sleeping, R=running, Z=zombie, T=stopped)
START   = When process started
TIME    = CPU time consumed
COMMAND = Command that started the process
"""

# top - Live process monitor (like Task Manager)
# -----------------------------------------
# top
# Inside top:
#   q        = Quit
#   k        = Kill process (enter PID)
#   M        = Sort by memory
#   P        = Sort by CPU
#   c        = Show full command
#   1        = Show per-CPU stats
#   h        = Help

# htop - Better top (may need to install: sudo apt install htop)
# -----------------------------------------
# htop
# More colorful, easier to use, scroll with arrow keys

# kill - Send signal to process
# -----------------------------------------
# kill 1234               # Send SIGTERM (graceful shutdown)
# kill -9 1234            # Send SIGKILL (force kill, use as last resort)
# kill -15 1234           # Same as kill 1234 (SIGTERM)
# kill -HUP 1234          # Send SIGHUP (reload config)
# killall nginx           # Kill all processes with name
# pkill -f "python app"   # Kill by pattern match

# Common Signals:
# SIGTERM (15) = Please terminate (graceful)
# SIGKILL (9)  = Die immediately (cannot be caught)
# SIGHUP  (1)  = Hangup, often used to reload config
# SIGINT  (2)  = Interrupt (Ctrl+C)
# SIGSTOP (19) = Pause process
# SIGCONT (18) = Continue paused process

# jobs, bg, fg - Background/foreground processes
# -----------------------------------------
# command &               # Run command in background
# Ctrl+Z                  # Suspend current process
# jobs                    # List background jobs
# bg                      # Resume suspended job in background
# fg                      # Bring background job to foreground
# fg %1                   # Bring job 1 to foreground

# nohup - Keep running after logout
# -----------------------------------------
# nohup long_process.sh &          # Run in background, survives logout
# nohup command > output.log 2>&1 &  # With logging

# screen/tmux - Terminal multiplexer (ESSENTIAL for servers)
# -----------------------------------------
# screen                  # Start new screen session
# screen -S myname        # Start named session
# screen -ls              # List sessions
# screen -r myname        # Reattach to session
# Inside screen:
#   Ctrl+a d      = Detach (leaves running)
#   Ctrl+a c      = New window
#   Ctrl+a n      = Next window
#   Ctrl+a "      = List windows

# tmux (more modern alternative to screen)
# tmux                    # Start new session
# tmux new -s myname      # Start named session
# tmux ls                 # List sessions
# tmux attach -t myname   # Attach to session
# Inside tmux:
#   Ctrl+b d      = Detach
#   Ctrl+b c      = New window
#   Ctrl+b n      = Next window
#   Ctrl+b %      = Split vertical
#   Ctrl+b "      = Split horizontal

"""
═══════════════════════════════════════════════════════════
🏗️ PART 9: SYSTEM INFORMATION AND MONITORING
═══════════════════════════════════════════════════════════
"""

# System info
# -----------------------------------------
# uname -a                # All system info
# uname -r                # Kernel version
# hostname                # Machine hostname
# uptime                  # How long system running, load average
# whoami                  # Current username
# id                      # User ID, group IDs
# date                    # Current date/time
# cal                     # Calendar

# Memory
# -----------------------------------------
# free -h                 # Memory usage (human readable)
# free -m                 # Memory in MB
# cat /proc/meminfo       # Detailed memory info
# vmstat 1                # Virtual memory stats every second

# Disk
# -----------------------------------------
# df -h                   # Disk space usage (human readable)
# df -i                   # Inode usage
# du -sh *                # Size of items in current directory
# du -sh /var/log         # Size of specific directory
# du -ah /var | sort -rh | head -20   # Largest files/dirs
# lsblk                   # List block devices (disks)
# fdisk -l                # Disk partitions (need sudo)

# CPU
# -----------------------------------------
# cat /proc/cpuinfo       # CPU information
# lscpu                   # CPU architecture info
# nproc                   # Number of processors

# Network
# -----------------------------------------
# ip addr                 # IP addresses (modern)
# ifconfig                # IP addresses (older, may need net-tools)
# ip route                # Routing table
# netstat -tulpn          # Open ports and listening services
# ss -tulpn               # Modern replacement for netstat
# ping google.com         # Test connectivity
# traceroute google.com   # Trace network path
# curl ifconfig.me        # Get public IP
# dig google.com          # DNS lookup
# nslookup google.com     # DNS lookup (older)
# host google.com         # DNS lookup (simple)

"""
═══════════════════════════════════════════════════════════
🏗️ PART 10: SSH - CONNECTING TO REMOTE SERVERS
═══════════════════════════════════════════════════════════

SSH (Secure Shell) is how you connect to remote servers.
This is THE skill companies want - being comfortable on remote servers.
"""

# Basic SSH
# -----------------------------------------
# ssh user@hostname                       # Connect to server
# ssh user@192.168.1.100                  # Connect by IP
# ssh -p 2222 user@server                 # Connect on different port
# exit                                    # Disconnect

# SSH Keys (more secure than passwords)
# -----------------------------------------
# ssh-keygen -t ed25519 -C "your@email.com"  # Generate key pair
# ssh-keygen -t rsa -b 4096                  # RSA alternative
# Files created:
#   ~/.ssh/id_ed25519      = Private key (NEVER share!)
#   ~/.ssh/id_ed25519.pub  = Public key (put on servers)

# ssh-copy-id user@server                 # Copy public key to server
# Now you can login without password!

# SSH Config (make life easier)
# Create ~/.ssh/config:
"""

SSH_CONFIG_EXAMPLE = """
# ~/.ssh/config

Host prod
    HostName 192.168.1.100
    User deploy
    Port 22
    IdentityFile ~/.ssh/id_ed25519

Host staging
    HostName 192.168.1.101
    User deploy

Host dev-*
    User developer
    IdentityFile ~/.ssh/dev_key

# Now you can just type: ssh prod
"""

"""
# SCP - Copy files over SSH
# -----------------------------------------
# scp file.txt user@server:/path/         # Upload file
# scp user@server:/path/file.txt .        # Download file
# scp -r folder/ user@server:/path/       # Upload folder recursively
# scp -P 2222 file.txt user@server:/path/ # Different port

# rsync - Better file sync (only transfers changes)
# -----------------------------------------
# rsync -avz folder/ user@server:/path/   # Sync folder
# rsync -avz --delete folder/ user@server:/path/  # Sync and delete removed files
# -a = archive (preserves permissions, timestamps)
# -v = verbose
# -z = compress during transfer

# SSH Port Forwarding (Tunnels)
# -----------------------------------------
# ssh -L 8080:localhost:80 user@server    # Local port forward
# Access server's port 80 at localhost:8080

# ssh -R 8080:localhost:80 user@server    # Remote port forward
# Server can access your port 80 at its localhost:8080

# ssh -D 1080 user@server                 # SOCKS proxy
# Route traffic through server

═══════════════════════════════════════════════════════════
🏗️ PART 11: SERVICE MANAGEMENT - SYSTEMD
═══════════════════════════════════════════════════════════

systemd is the service manager on modern Linux (Ubuntu, CentOS 7+, etc).
Services are background processes that run on the server.
"""

# systemctl - Control services
# -----------------------------------------
# systemctl status nginx              # Check service status
# systemctl start nginx               # Start service
# systemctl stop nginx                # Stop service
# systemctl restart nginx             # Restart service
# systemctl reload nginx              # Reload config without restart
# systemctl enable nginx              # Start on boot
# systemctl disable nginx             # Don't start on boot
# systemctl is-active nginx           # Check if running
# systemctl is-enabled nginx          # Check if enabled on boot
# systemctl list-units --type=service # List all services
# systemctl list-units --failed       # List failed services

# journalctl - View service logs
# -----------------------------------------
# journalctl                          # All logs
# journalctl -u nginx                 # Logs for specific service
# journalctl -u nginx -f              # Follow logs (like tail -f)
# journalctl -u nginx --since "1 hour ago"   # Recent logs
# journalctl -u nginx --since "2024-01-01"   # Logs since date
# journalctl -u nginx -n 100          # Last 100 lines
# journalctl -xe                      # Recent errors with explanations
# journalctl --disk-usage             # How much space logs take
# journalctl --vacuum-size=500M       # Reduce log size to 500MB

"""
CREATING A SYSTEMD SERVICE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create file: /etc/systemd/system/myapp.service
"""

SYSTEMD_SERVICE_EXAMPLE = """
[Unit]
Description=My Python Application
After=network.target

[Service]
Type=simple
User=deploy
WorkingDirectory=/home/deploy/myapp
Environment=NODE_ENV=production
ExecStart=/usr/bin/python3 /home/deploy/myapp/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target

# After creating the file:
# sudo systemctl daemon-reload        # Reload systemd
# sudo systemctl enable myapp         # Enable on boot
# sudo systemctl start myapp          # Start now
"""

"""
═══════════════════════════════════════════════════════════
🏗️ PART 12: USER AND PERMISSION MANAGEMENT
═══════════════════════════════════════════════════════════
"""

# User management
# -----------------------------------------
# whoami                              # Current user
# id                                  # User/group IDs
# users                               # Logged in users
# who                                 # Who is logged in
# w                                   # Who is logged in + what doing
# last                                # Login history

# sudo - Run as root
# -----------------------------------------
# sudo command                        # Run single command as root
# sudo -i                             # Login as root
# sudo -u otheruser command           # Run as different user
# sudo su -                           # Switch to root user

# Creating users
# -----------------------------------------
# sudo useradd username               # Create user (basic)
# sudo useradd -m -s /bin/bash username   # Create with home dir and shell
# sudo passwd username                # Set password
# sudo adduser username               # Interactive user creation (Debian)
# sudo usermod -aG groupname username # Add user to group
# sudo userdel username               # Delete user
# sudo userdel -r username            # Delete user and home dir

# Groups
# -----------------------------------------
# groups                              # Your groups
# groups username                     # User's groups
# sudo groupadd groupname             # Create group
# sudo groupdel groupname             # Delete group

# File permissions
# -----------------------------------------
# chmod 755 file                      # Set permissions (numeric)
# chmod u+x file                      # Add execute for user
# chmod g-w file                      # Remove write for group
# chmod o-rwx file                    # Remove all for others
# chmod +x file                       # Add execute for all
# chmod -R 755 directory/             # Recursive

# Ownership
# -----------------------------------------
# chown user file                     # Change owner
# chown user:group file               # Change owner and group
# chown -R user:group directory/      # Recursive
# chgrp group file                    # Change group only

"""
═══════════════════════════════════════════════════════════
🏗️ PART 13: LOG FILES - DEBUGGING SERVERS
═══════════════════════════════════════════════════════════

When something breaks on a server, LOGS ARE YOUR BEST FRIEND.
This is what companies mean by "debugging skills".
"""

# Common log locations
LOG_LOCATIONS = """
/var/log/syslog          # Main system log (Ubuntu/Debian)
/var/log/messages        # Main system log (CentOS/RHEL)
/var/log/auth.log        # Authentication (login attempts, sudo)
/var/log/kern.log        # Kernel messages
/var/log/dmesg           # Boot messages
/var/log/nginx/          # Nginx logs
/var/log/apache2/        # Apache logs
/var/log/mysql/          # MySQL logs
/var/log/postgresql/     # PostgreSQL logs
/var/log/cron            # Cron job logs
~/.pm2/logs/             # PM2 logs (Node.js)
"""

# Log viewing commands
# -----------------------------------------
# tail -f /var/log/syslog             # Follow system log
# tail -f /var/log/nginx/error.log    # Follow nginx errors
# less /var/log/syslog                # Browse log
# grep "error" /var/log/syslog        # Find errors
# grep -i "fail" /var/log/auth.log    # Find failed logins
# zcat /var/log/syslog.1.gz | grep error   # Search compressed logs
# journalctl -u nginx -f              # Follow systemd service logs

"""
REAL DEBUGGING WORKFLOW:
━━━━━━━━━━━━━━━━━━━━━━━━

1. Check if service is running:
   systemctl status myservice

2. Check recent service logs:
   journalctl -u myservice -n 50

3. Check system logs around the time of issue:
   grep "Mar 27 14:3" /var/log/syslog

4. Check application logs:
   tail -f /var/log/myapp/error.log

5. Check if port is listening:
   ss -tulpn | grep 8080

6. Check disk space:
   df -h

7. Check memory:
   free -h

8. Check running processes:
   ps aux | grep myapp

═══════════════════════════════════════════════════════════
🏗️ PART 14: PACKAGE MANAGEMENT
═══════════════════════════════════════════════════════════
"""

# APT (Ubuntu/Debian)
# -----------------------------------------
# sudo apt update                     # Update package lists
# sudo apt upgrade                    # Upgrade installed packages
# sudo apt install nginx              # Install package
# sudo apt remove nginx               # Remove package
# sudo apt purge nginx                # Remove package + config
# sudo apt autoremove                 # Remove unused dependencies
# apt search nginx                    # Search for packages
# apt show nginx                      # Show package info
# dpkg -l                             # List installed packages
# dpkg -L nginx                       # List files installed by package

# YUM/DNF (CentOS/RHEL/Fedora)
# -----------------------------------------
# sudo yum update                     # Update packages
# sudo yum install nginx              # Install
# sudo yum remove nginx               # Remove
# yum search nginx                    # Search
# rpm -qa                             # List installed packages
# DNF is the newer version of YUM, same commands

"""
═══════════════════════════════════════════════════════════
🏗️ PART 15: BASH SCRIPTING BASICS
═══════════════════════════════════════════════════════════

Bash scripts automate repetitive tasks. File extension: .sh
First line should be: #!/bin/bash (called "shebang")
"""

BASH_SCRIPT_EXAMPLE = """
#!/bin/bash
# This is a comment

# Variables (NO SPACES around =)
NAME="World"
COUNT=5

# Use variables with $
echo "Hello, $NAME"
echo "Count is: ${COUNT}"

# Command substitution
DATE=$(date +%Y-%m-%d)
FILES=$(ls -1 | wc -l)
echo "Today is $DATE, there are $FILES files"

# Arguments
# $0 = script name
# $1, $2, etc = arguments
# $# = number of arguments
# $@ = all arguments
echo "Script: $0"
echo "First arg: $1"
echo "All args: $@"

# Conditionals
if [ "$1" = "hello" ]; then
    echo "You said hello!"
elif [ "$1" = "bye" ]; then
    echo "Goodbye!"
else
    echo "Unknown command"
fi

# Numeric comparison
if [ $COUNT -gt 3 ]; then
    echo "Count is greater than 3"
fi
# -eq (equal), -ne (not equal)
# -gt (greater than), -ge (greater or equal)
# -lt (less than), -le (less or equal)

# String comparison
if [ -z "$NAME" ]; then
    echo "NAME is empty"
fi
if [ -n "$NAME" ]; then
    echo "NAME is not empty"
fi

# File tests
if [ -f "/path/file" ]; then
    echo "File exists"
fi
if [ -d "/path/dir" ]; then
    echo "Directory exists"
fi
# -e exists, -f is file, -d is directory
# -r readable, -w writable, -x executable

# Loops
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

for file in *.txt; do
    echo "Processing $file"
done

for i in {1..10}; do
    echo $i
done

# While loop
COUNT=0
while [ $COUNT -lt 5 ]; do
    echo "Count: $COUNT"
    COUNT=$((COUNT + 1))
done

# Functions
greet() {
    local name=$1  # local variable
    echo "Hello, $name!"
}
greet "Alice"

# Exit codes
# 0 = success, anything else = failure
exit 0
"""

# Running scripts
# -----------------------------------------
# chmod +x script.sh                  # Make executable
# ./script.sh                         # Run script
# bash script.sh                      # Run with bash explicitly
# ./script.sh arg1 arg2               # Run with arguments

"""
═══════════════════════════════════════════════════════════
🏗️ PART 16: ENVIRONMENT VARIABLES
═══════════════════════════════════════════════════════════
"""

# View environment variables
# -----------------------------------------
# env                                 # All environment variables
# echo $PATH                          # Specific variable
# echo $HOME                          # Home directory
# echo $USER                          # Current user
# echo $SHELL                         # Current shell
# echo $PWD                           # Current directory

# Important variables
# PATH = Where shell looks for commands (colon-separated directories)
# HOME = Home directory
# USER = Current username
# SHELL = Default shell
# LANG = Language/locale
# EDITOR = Default text editor
# TERM = Terminal type

# Setting variables
# -----------------------------------------
# VAR="value"                         # Set for current shell only
# export VAR="value"                  # Set for current shell + child processes
# unset VAR                           # Remove variable

# Permanent variables (add to these files):
# ~/.bashrc         # For interactive bash shells
# ~/.bash_profile   # For login shells
# ~/.profile        # For all shells
# /etc/environment  # System-wide

# Example: Add to PATH
# export PATH="$PATH:/opt/myprogram/bin"

"""
═══════════════════════════════════════════════════════════
🏗️ PART 17: NETWORKING COMMANDS
═══════════════════════════════════════════════════════════
"""

# curl - Transfer data from/to server (HTTP client)
# -----------------------------------------
# curl https://api.example.com        # GET request
# curl -I https://example.com         # Headers only
# curl -X POST https://api.example.com  # POST request
# curl -X POST -d "data=value" URL    # POST with data
# curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' URL
# curl -o file.zip URL                # Save to file
# curl -O URL                         # Save with remote filename
# curl -L URL                         # Follow redirects
# curl -v URL                         # Verbose (debug)
# curl -u user:pass URL               # Basic auth

# wget - Download files
# -----------------------------------------
# wget URL                            # Download file
# wget -O filename URL                # Download with different name
# wget -c URL                         # Continue interrupted download
# wget -r URL                         # Recursive download

# Network diagnostics
# -----------------------------------------
# ping host                           # Test connectivity
# ping -c 5 host                      # Send 5 pings only
# traceroute host                     # Trace network path
# mtr host                            # Better traceroute (continuous)
# dig domain                          # DNS lookup
# dig +short domain                   # Just the IP
# nslookup domain                     # DNS lookup (older)
# host domain                         # Simple DNS lookup

# Port and connection checking
# -----------------------------------------
# netstat -tulpn                      # All listening ports
# ss -tulpn                           # Same (modern)
# lsof -i :8080                       # What's using port 8080
# telnet host 80                      # Test TCP connection
# nc -zv host 80                      # Test TCP connection (netcat)

"""
═══════════════════════════════════════════════════════════
🏗️ PART 18: REAL-WORLD SCENARIOS
═══════════════════════════════════════════════════════════

These are the situations you'll face on production servers.
"""

SCENARIO_1 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 1: Website is down, find out why
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. SSH into server
ssh deploy@production-server

# 2. Check if web server is running
systemctl status nginx
# If not running, check why:
journalctl -u nginx -n 50

# 3. Check if app is running
systemctl status myapp
# Or for Node.js:
pm2 status

# 4. Check if port is listening
ss -tulpn | grep 80
ss -tulpn | grep 3000

# 5. Check recent error logs
tail -n 100 /var/log/nginx/error.log
tail -n 100 /var/log/myapp/error.log

# 6. Check disk space (logs can fill disk)
df -h

# 7. Check memory
free -h

# 8. Check if database is running
systemctl status postgresql
systemctl status mysql

# 9. Try restarting services
sudo systemctl restart nginx
sudo systemctl restart myapp
"""

SCENARIO_2 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 2: Server is slow, diagnose
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. Check system load
uptime
# Load average > number of CPUs = overloaded

# 2. Check what's using CPU
top
# Press 'P' to sort by CPU
# Or use htop for better view

# 3. Check memory usage
free -h
# If swap is heavily used, you're low on RAM

# 4. Check disk I/O
iostat -x 1 5
# High await time = disk bottleneck

# 5. Check which process is using most memory
ps aux --sort=-%mem | head -10

# 6. Check which process is using most CPU
ps aux --sort=-%cpu | head -10

# 7. Check for zombie processes
ps aux | grep Z

# 8. Check disk usage
df -h
du -sh /var/* | sort -rh | head -10

# 9. Check network connections
ss -s  # Summary of connections
ss -tulpn | wc -l  # Count listening ports
"""

SCENARIO_3 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 3: Deploy new code to server
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. SSH to server
ssh deploy@production

# 2. Go to app directory
cd /home/deploy/myapp

# 3. Pull latest code
git fetch origin
git checkout main
git pull origin main

# 4. Install dependencies
# Python:
pip install -r requirements.txt
# Node.js:
npm install

# 5. Run database migrations if needed
# Django:
python manage.py migrate
# Node.js:
npm run migrate

# 6. Build if needed
npm run build

# 7. Restart application
sudo systemctl restart myapp
# Or for PM2:
pm2 restart all

# 8. Check it's running
systemctl status myapp
curl localhost:3000/health

# 9. Check logs for errors
tail -f /var/log/myapp/error.log
"""

SCENARIO_4 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 4: Find and kill runaway process
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. Find the process using lots of CPU
top
# Note the PID

# 2. Get more info about it
ps aux | grep PID
lsof -p PID  # Files it has open

# 3. Try graceful termination first
kill PID
# Wait a few seconds

# 4. If still running, force kill
kill -9 PID

# 5. If you know the process name
pkill -f "python badly_written_script.py"

# 6. To kill all processes by a user (CAREFUL)
pkill -u baduser
"""

SCENARIO_5 = """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SCENARIO 5: Disk is full
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# 1. Check disk usage
df -h

# 2. Find largest directories
du -sh /* 2>/dev/null | sort -rh | head -10
du -sh /var/* | sort -rh | head -10
du -sh /var/log/* | sort -rh | head -10

# 3. Find large files
find / -type f -size +100M 2>/dev/null | head -20

# 4. Clean package cache
# Ubuntu:
sudo apt clean
# CentOS:
sudo yum clean all

# 5. Clear old logs
sudo journalctl --vacuum-size=500M
# Or manually:
sudo truncate -s 0 /var/log/largelogfile.log

# 6. Remove old kernels (Ubuntu)
sudo apt autoremove

# 7. Clear temp files
sudo rm -rf /tmp/*
"""

"""
═══════════════════════════════════════════════════════════
🏗️ PART 19: ESSENTIAL KEYBOARD SHORTCUTS
═══════════════════════════════════════════════════════════

These work in bash and most shells:
"""

KEYBOARD_SHORTCUTS = """
NAVIGATION:
Ctrl + A        Move cursor to beginning of line
Ctrl + E        Move cursor to end of line
Ctrl + B        Move cursor back one character
Ctrl + F        Move cursor forward one character
Alt + B         Move cursor back one word
Alt + F         Move cursor forward one word

EDITING:
Ctrl + U        Cut everything before cursor
Ctrl + K        Cut everything after cursor
Ctrl + W        Cut word before cursor
Ctrl + Y        Paste what was cut
Ctrl + L        Clear screen (like 'clear' command)

HISTORY:
Ctrl + R        Search command history (SUPER USEFUL)
Ctrl + P        Previous command (same as Up arrow)
Ctrl + N        Next command (same as Down arrow)
!!              Repeat last command
!$              Last argument of previous command
!*              All arguments of previous command
!git            Run last command starting with 'git'

PROCESS CONTROL:
Ctrl + C        Kill current process
Ctrl + Z        Suspend current process
Ctrl + D        Exit shell (EOF)

TAB:
Tab             Auto-complete commands/filenames
Tab Tab         Show all possible completions
"""

"""
═══════════════════════════════════════════════════════════
🏗️ PART 20: THE PROFESSIONAL CHECKLIST
═══════════════════════════════════════════════════════════

If you can do all of these, you have the Linux skills companies want:
"""

SKILL_CHECKLIST = """
NAVIGATION & FILES:
[ ] Navigate filesystem without thinking (cd, ls, pwd)
[ ] Create, copy, move, delete files and directories
[ ] Understand file permissions and change them
[ ] Use tab completion efficiently

VIEWING & EDITING:
[ ] View file contents (cat, less, head, tail)
[ ] Edit files in vim or nano
[ ] Follow log files in real-time (tail -f)
[ ] Search for text in files (grep)

PIPING & REDIRECTION:
[ ] Chain commands with pipes
[ ] Redirect output to files
[ ] Use common combinations (grep | sort | uniq)

PROCESSES:
[ ] Find running processes (ps, top, htop)
[ ] Kill processes
[ ] Run processes in background
[ ] Use screen or tmux for persistent sessions

SYSTEM MONITORING:
[ ] Check CPU, memory, disk usage
[ ] Find what's consuming resources
[ ] Read and understand system logs

SSH:
[ ] Connect to remote servers
[ ] Use SSH keys instead of passwords
[ ] Copy files between servers (scp, rsync)
[ ] Create SSH config for easy connections

SERVICES:
[ ] Start/stop/restart services
[ ] Check service status
[ ] View service logs
[ ] Create basic systemd services

SCRIPTING:
[ ] Write basic bash scripts
[ ] Use variables, loops, conditionals
[ ] Automate repetitive tasks

PACKAGE MANAGEMENT:
[ ] Install/remove software
[ ] Update system packages

TROUBLESHOOTING:
[ ] SSH in when website is down
[ ] Check logs to find errors
[ ] Diagnose slow server
[ ] Clear disk space
[ ] Restart services properly
"""

print("""
═══════════════════════════════════════════════════════════
🎯 CONCLUSION: HOW TO ACTUALLY GET GOOD
═══════════════════════════════════════════════════════════

1. USE THE TERMINAL DAILY
   - Force yourself to use command line instead of GUI
   - Every time you're about to click, ask "can I do this in terminal?"

2. GET A CHEAP VPS
   - DigitalOcean, Linode, Vultr - $5/month
   - Practice SSHing in, setting up services, breaking and fixing things

3. BREAK THINGS ON PURPOSE
   - Kill processes, fill up disk, mess with configs
   - Learn to fix what you broke

4. SET UP YOUR OWN PROJECTS
   - Deploy a website to a VPS
   - Set up nginx, SSL, systemd services
   - Real experience > reading

5. READ MAN PAGES
   - man ls, man grep, man ssh
   - They're dry but complete

Companies don't care if you memorized 100 commands.
They care if you can SSH into a server at 3am and fix
their broken production system without panicking.

That confidence comes from practice, not memorization.
═══════════════════════════════════════════════════════════
""")

