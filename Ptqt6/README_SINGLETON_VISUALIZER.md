# Singleton Pattern Visualizer

This application provides an interactive visualization of the Singleton design pattern implementation in Java. It's designed as an educational tool for students to understand how the Singleton pattern works, with a focus on the GameService implementation.

## Features

1. **Interactive Flowchart**: Visual representation of the Singleton pattern flow
2. **Code Viewer**: Browse through the actual Java code implementing the pattern
3. **Explanation Tab**: Detailed explanation of the Singleton pattern concepts

## Key Concepts Visualized

- Private constructor preventing external instantiation
- Static instance variable holding the single instance
- Public static getInstance() method for controlled access
- HashCode verification proving singleton behavior

## Requirements

- Python 3.6+
- PyQt6

## Installation

1. Install PyQt6:
```bash
pip install PyQt6
```

2. Run the application:
```bash
python singleton_visualizer.py
```

## Understanding the Visualizer

### Flowchart Tab
The flowchart shows two parallel processes:
- Left side: How the GameService singleton is created and accessed
- Right side: How the SingletonTester verifies that only one instance exists

### Code Viewer Tab
View the actual Java code for:
- GameService: The singleton implementation
- SingletonTester: Code that verifies the singleton behavior
- ProgramDriver: The main application entry point
- Game: A class managed by the GameService

### Explanation Tab
Provides a detailed explanation of:
- What the Singleton pattern is
- Key components of the pattern
- Benefits of using Singleton
- How hashCode() verifies the singleton behavior

## How the Singleton Pattern Works

1. The application starts in ProgramDriver.main()
2. GameService.getInstance() is called
3. If instance == null, a new GameService is created
4. If instance != null, the existing instance is returned
5. SingletonTester gets two references to the singleton
6. Both references have the same hashcode, proving they point to the same object in memory

## Educational Value

This visualizer helps students understand:
- How the Singleton pattern is implemented in Java
- Why the pattern is useful for centralized resource management
- How to verify that a singleton is working correctly
- The role of hashCode() in object identity verification 