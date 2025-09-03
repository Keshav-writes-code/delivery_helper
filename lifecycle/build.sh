#!/bin/bash

# Store the original directory
ORIGINAL_DIR=$(pwd)

echo "🚀 Starting build process..."

# Navigate to frontend directory
echo "📁 Changing to frontend directory..."
cd delivery_helper_app/frontend/

# Build frontend assets
echo "🔨 Building frontend assets with Bun..."
bun run build

# Return to project root
echo "📁 Returning to project root..."
cd ../../

# RUn Tailwind Build
uv run manage.py tailwind build

# Run collectstatic with no input prompt
echo "📦 Collecting static files..."
uv run manage.py collectstatic --noinput

echo "✅ Build and collect complete!"

# Return to the original directory (in case script was called from elsewhere)
cd "$ORIGINAL_DIR"
