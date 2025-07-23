#!/usr/bin/env python3
"""
Launch script for the Singleton Pattern Visualizer
Ensures all dependencies are available and runs the main application
"""

import sys
import subprocess
import os

def check_pyqt6():
    """Check if PyQt6 is installed"""
    try:
        import PyQt6
        print("✓ PyQt6 is installed")
        return True
    except ImportError:
        print("✗ PyQt6 is not installed")
        return False

def install_pyqt6():
    """Attempt to install PyQt6"""
    print("\nWould you like to install PyQt6? (y/n): ", end="")
    response = input().strip().lower()
    
    if response == 'y':
        print("Installing PyQt6...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6"])
            print("✓ PyQt6 installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("✗ Failed to install PyQt6")
            print("Please install manually with: pip install PyQt6")
            return False
    return False

def run_application():
    """Run the main application"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Try integrated version first
    integrated_path = os.path.join(script_dir, "singleton_visualizer_integrated.py")
    if os.path.exists(integrated_path):
        print("\nLaunching Singleton Pattern Visualizer...")
        subprocess.run([sys.executable, integrated_path])
    else:
        print(f"Error: Could not find {integrated_path}")
        print("\nAvailable test options:")
        print("1. Test Code Analyzer: python code_analyzer_fixed.py")
        print("2. Test Flowchart: python animated_flowchart_fixed.py")
        print("3. Test All Components: python test_all_components.py")

def main():
    print("=" * 50)
    print("Singleton Pattern Visualizer - Launch Script")
    print("=" * 50)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 6):
        print("✗ Python 3.6 or higher is required")
        sys.exit(1)
    
    # Check PyQt6
    if not check_pyqt6():
        if not install_pyqt6():
            print("\nCannot run without PyQt6. Exiting.")
            sys.exit(1)
    
    # Run the application
    run_application()

if __name__ == "__main__":
    main()