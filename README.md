# Singleton_GameService

- A basic Java project demonstrating the Singleton design pattern. 
- This is a simple command-line app that initializes game data and verifies singleton behavior in `GameService`.

## Project Summary

This project was created for **CS 230** as a milestone assignment.

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
<img width="506" height="280" alt="Screenshot 2025-07-13 at 7 41 31 AM" src="https://github.com/user-attachments/assets/ff7615c1-7c4b-4d48-9b9d-45b775c9f63b" />

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
├── Ptqt6/                   # PyQt6 visualizers
│   ├── singleton_flowchart_complete.py  # Complete architecture visualizer
│   ├── need_fix_animations.py           # Animated singleton flow
│   ├── singleton_visualizer_integrated.py # Multi-tab interface
│   ├── working_code_viz.py              # Alternative visualizer
│   └── README_SINGLETON_VISUALIZER.md   # PyQt6 documentation
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

### Interactive Visualizers (PyQt6)

This project includes interactive Python visualizers to help understand the Singleton pattern and Entity hierarchy:

1. **Complete Architecture Visualizer** (`Ptqt6/singleton_flowchart_complete.py`)
   - Shows the entire system architecture with Entity hierarchy
   - Three animation modes: Full flow, Singleton only, Entity hierarchy only
   - Interactive controls with speed adjustment

2. **Animated Singleton Flow** (`Ptqt6/need_fix_animations.py`)
   - Step-by-step animation of singleton creation
   - Visual flow indicators showing data movement

3. **Integrated Multi-tab Interface** (`Ptqt6/singleton_visualizer_integrated.py`)
   - Browse Java source code
   - View flowcharts and explanations
   - Educational tool for understanding patterns

To run the visualizers:
```bash
# Install PyQt6
pip install PyQt6

# Run the complete architecture visualizer
python Ptqt6/singleton_flowchart_complete.py
```

See `Ptqt6/README_SINGLETON_VISUALIZER.md` for detailed documentation.

---

### How to Run the Java Application

If you downloaded the compiled `GamingRoom.jar`:

 **Run it from the terminal:**

```bash
java -jar GamingRoom.jar
```

**Or, if downloaded from GitHub:**

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

---

##  License
#STILL A WORK IN PROGRESS
**Educational Use Only**
– Created as a school project for CS 230 at SNHU.

- This education and I dont need donwloads for forks at at this time.
Copyright © 2025 Justin Guida

