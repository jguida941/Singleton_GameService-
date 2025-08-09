# Singleton_GameService
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-ff6a00?style=flat-square&labelColor=0a0a0a)](LICENSE)
![Language](https://img.shields.io/badge/Java-8%2B-ff6a00?style=flat-square&labelColor=0a0a0a)
![Pattern](https://img.shields.io/badge/Pattern-Singleton-ff6a00?style=flat-square&labelColor=0a0a0a)
![Type](https://img.shields.io/badge/App-Command--line-ff6a00?style=flat-square&labelColor=0a0a0a)
![Build](https://img.shields.io/badge/Build-javac-ff6a00?style=flat-square&labelColor=0a0a0a)
![Artifact](https://img.shields.io/badge/JAR-Executable-ff6a00?style=flat-square&labelColor=0a0a0a)
![UML](https://img.shields.io/badge/UML-Included-ff6a00?style=flat-square&labelColor=0a0a0a)
![Extras](https://img.shields.io/badge/Extras-PyQt6%20%7C%20Jupyter-ff6a00?style=flat-square&labelColor=0a0a0a)

- A basic Java project demonstrating the Singleton design pattern. 
- This is a simple command-line app that initializes game data and verifies singleton behavior in `GameService`.
- Note: This contains additional PyQt6/Jupiter Notebooks components; this release is for hashcode-based singleton checks.

## Project Summary

It showcases:
- **The Singleton Pattern in Java**
- **Object-oriented design (`Game`, `Player`, `Team`)**
- **Command-line app architecture**
- **How to compile and package a JAR file with a manifest**

## Implementation Details

I completed the following requirements for this project:

1. **Unique Game and Team Names**: Implemented uniqueness checks for game and team names to prevent duplicates, allowing users to check if a name is already in use.

2. **Iterator Pattern**: Used the iterator pattern in the `addGame()`, `getGame()`, `addTeam()`, and `addPlayer()` methods to search for existing entities before creating new ones.

3. **Entity Base Class**: Created an abstract `Entity` class that holds common attributes and behaviors as shown in the UML diagram.

4. **Class Inheritance**: Refactored the `Game`, `Team`, and `Player` classes to inherit from the `Entity` class.

5. **Unique Names**: Implemented functionality to ensure every team and player has a unique name by searching for the supplied name prior to adding a new instance.

6. **Best Practices**: Applied industry standard best practices including appropriate naming conventions and in-line comments that describe the functionality.

## Sample Output

```
>>> Singleton GameService instance CREATED

About to test initializing game data...
Game [id=1, name=Game #1]
Game [id=2, name=Game #2]
Team [id=1, name=Team Alpha]
  Players:
    Player [id=1, name=Justin]
Player [id=1, name=Justin]
Team [id=2, name=Team Beta]
  Players:
    Player [id=2, name=John]
Player [id=2, name=John]

About to test the singleton...
service1 hashcode: 225534817
service2 hashcode: 225534817
service1 and service2 point to the same instance? true
```

## Memory Management
![Memory Management Diagram](https://github.com/user-attachments/assets/ff7615c1-7c4b-4d48-9b9d-45b775c9f63b)

## Software Engineering Principles

This project demonstrates several key software engineering principles:

### Singleton Design Pattern

I implemented the Singleton pattern in `GameService` to ensure only one instance exists throughout the application lifecycle. 
### This is **critical** for:

1. **Resource Management**: Prevents redundant instances consuming memory
2. **State Consistency**: Maintains a single source of truth for game data
3. **Global Access**: Provides controlled access to shared resources

### Iterator Pattern Implementation

The project also uses **Java's built-in Iterator pattern** through enhanced for loops to:
- **Safely traverse** collections of games, teams, and players
- **Prevent duplicate entries** by checking existing records
- **Implement clean, readable code that follows best practices**

### What I Added

I enhanced the original codebase by:
- **Implementing proper encapsulation** with private fields and accessors
- **Adding comprehensive documentation** with JavaDoc comments
- **Creating a clean singleton implementation** with lazy instantiation
- **Building a complete, runnable JAR** with proper manifest configuration
- **Added Team and Player functionality** to demonstrate the entity hierarchy
- **Implemented toString methods** for all classes to provide readable output

### TODO:
- **Ensuring thread safety considerations in the singleton design.** This is a work in progress.

---

### Project Structure
**Note I have many PyQt/Jupiter Notebooks I am working on in this version feel free to ignore or run them. Need to update file tree completly

```
Singleton_GameService/
├── src/com/gamingroom/
│   ├── Entity.java          # Base abstract class
│   ├── Game.java            # Game class extending Entity
│   ├── GameService.java     # Singleton service class
│   ├── Player.java          # Player class extending Entity
│   ├── ProgramDriver.java   # Main driver class
│   ├── SingletonTester.java # Tests singleton behavior
│   └── Team.java            # Team class extending Entity
├── Ptqt6/                   # PyQt6 visualizers and launchers
│   ├── start_visualizer.py              # ONE-CLICK LAUNCHER (START HERE!)
│   ├── RUN_VISUALIZER.command           # macOS double-click launcher
│   ├── launcher.html                    # Advanced HTML interface
│   ├── launcher_backend.py              # Backend server for HTML
│   ├── singleton_flowchart_complete.py  # Architecture visualizer
│   ├── singleton_visualizer_integrated.py # Code analyzer
│   └── README_SINGLETON_VISUALIZER.md   # Detailed documentation
├── bin/                     # Compiled .class files
├── manifest.txt             # Defines main class
├── GamingRoom.jar           # Final runnable JAR
├── README.md
├── LICENSE                  # MIT License for educational use
├── .gitignore
├── CS 230 Project One Milestone UML.png
└── CS 230 Project One Milestone Tasks.png
```

---

### Interactive Visualizers Suite (PyQt6)

This project includes a comprehensive suite of interactive visualizers to help understand the Singleton pattern:

#### Quick Start - One Command!

```bash
# Install PyQt6 (one-time setup)
pip install PyQt6

# Run the complete visualizer suite with one command!
cd Ptqt6
python start_visualizer.py
```

This launches:
-  Backend server automatically
- Beautiful HTML interface in your browser
- All launch buttons working instantly
- No manual server setup needed!

#### Alternative Launch Methods

**For macOS Users:**
```bash
# Double-click method
open Ptqt6/RUN_VISUALIZER.command
# Or in Finder, just double-click RUN_VISUALIZER.command
```

**Manual Methods:**
```bash
# Method 1: Simple Python GUI launcher
python Ptqt6/launcher.py

# Method 2: Backend + HTML (two steps)
python Ptqt6/launcher_backend.py
# Then open http://localhost:8080/launcher.html

# Method 3: Direct execution
python Ptqt6/singleton_flowchart_complete.py
python Ptqt6/singleton_visualizer_integrated.py
```

#### What's Included

1. **Animated Flowchart Visualizer**
   - Step-by-step singleton pattern animation
   - Interactive speed controls
   - Visual representation of getInstance() flow

2. **Architecture Explorer**
   - Complete Entity hierarchy visualization
   - GameService architecture overview
   - Three animation modes: Full, Singleton-only, Entity-only

3. **Code Analyzer**
   - Line-by-line Java code analysis
   - Pattern detection and explanation
   - Memory management visualization

4. **Java Runtime**
   - Launches the actual Java application
   - Shows singleton verification via hashcodes
   - Opens in terminal for clear output

**TODO List:**
- Add zoom functionality to flowchart visualizers
- Fix code analyzer to provide line-by-line explanations
- Complete integration of all visualizers into unified launcher
- Update PyQt6 documentation

See `Ptqt6/README_SINGLETON_VISUALIZER.md` for detailed documentation.

---

### How to Run the Java Application

The compiled JAR file has been tested and runs correctly.

**Run from project directory:**
```bash
java -jar GamingRoom.jar
```

**Or from Downloads folder:**
```bash
java -jar ~/Downloads/GamingRoom.jar
```

## How to Build from Source

**FIRST:** Navigate to the project directory

cd /path/to/Singleton_GameService

**Replace /path/to/ with where you extracted the ZIP or cloned it.**


**Step 1:** Create output directory

mkdir -p bin

**Step 2:** Compile Java source files

javac -d bin src/com/gamingroom/*.java

**Step 3:** Create the executable JAR with main class specified

jar -cfe GamingRoom.jar com.gamingroom.ProgramDriver -C bin .

**Run it**

java -jar GamingRoom.jar

## Key Concept: Singleton Pattern

The Singleton pattern ensures that only one instance of the GameService class is ever created.
All calls to GameService.getInstance() return the same object reference.

Why it matters:
- Prevents duplication of logic/state
- Enables global access to shared services
-  Ensures consistent game state management

### Real-world Applications

The Singleton pattern is widely used in:
- Database connection pools
- Configuration managers
- Logging services
- Cache implementations
- Thread pools



## License

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

This project is for educational use only, created as a school project for CS 230 at SNHU.

Copyright © 2025 Justin Guida

