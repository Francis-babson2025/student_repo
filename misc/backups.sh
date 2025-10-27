#!/bin/bash

# --- Configuration ---
BACKUP_DIR="D:/babson2025/backups"   # Windows folder to store backups
repos=('python-rsail' 'python-sam')  # Add all student repos here

# --- Make sure backup folder exists ---
mkdir -p "$BACKUP_DIR"
cd "$BACKUP_DIR" || { echo "Cannot access backup folder"; exit 1; }

# --- Loop over all repos ---
for REPO in "${repos[@]}"; do
    if [ -d "$REPO" ]; then
        echo "Updating existing repo: $REPO"
        cd "$REPO" || continue
        git fetch origin
        git reset --hard origin/main
        cd ..
    else
        echo "Cloning new repo: $REPO"
        git clone "https://github.com/babson-org/$REPO.git"
    fi
done

echo "Backup complete!"



