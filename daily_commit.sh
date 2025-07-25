#!/bin/bash

# Define variables
REPO_PATH=$(pwd)  # Replace with the path to your repo
COMMIT_MESSAGE="Updating README"  # You can change this message
BRANCH_NAME="main"  # Replace with your branch name (could be 'master' or any other)

# Change to the repo directory
cd $REPO_PATH

# Pull the latest changes to avoid conflicts
git pull origin $BRANCH_NAME

# Update a file (we'll create a simple file that changes every time)
echo "Commit at $(date)" >> daily_commit.txt  # This file will have the current timestamp

# Stage the changes
git add daily_commit.txt  # Only add the modified file (you can add more files if needed)

# Commit with a message
git commit -m

# Push the commit to GitHub
git push origin $BRANCH_NAME

