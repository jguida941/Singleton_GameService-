#!/bin/bash
# Start the Singleton Pattern Visualizer Launcher

echo "Starting Singleton Pattern Visualizer Launcher..."
echo "The launcher will open in your default browser"
echo "Press Ctrl+C to stop the server"
echo ""

# Make sure we're in the right directory
cd "$(dirname "$0")"

# Start the Python backend server
python3 launcher_backend.py