# Singleton Pattern Visualizer

This application provides multiple interactive visualizations of the Singleton design pattern implementation in Java, with a focus on the GameService and Entity hierarchy. It's designed as an educational tool for students to understand how design patterns work together.

## Available Visualizations

### 1. Complete Architecture Visualizer (`singleton_flowchart_complete.py`)
- **Full program flow** with Entity hierarchy and Singleton pattern
- **Three animation modes**: Full flow, Singleton only, Entity hierarchy only
- **Interactive controls**: Play, step-through, speed control, and loop
- Shows relationships between Entity, Game, Team, and Player classes
- Demonstrates how GameService manages all instances with unique IDs

### 2. Animated Flowchart (`need_fix_animations.py`)
- **Fixed animation system** using QTimer instead of QPropertyAnimation
- Step-by-step visualization of singleton creation and verification
- Visual flow indicators showing data movement

### 3. Integrated Visualizer (`singleton_visualizer_integrated.py`)
- **Multi-tab interface**: Flowchart, Code Viewer, and Explanation tabs
- **Code browser**: View actual Java source files
- **Educational explanations**: Detailed pattern descriptions

### 4. Working Code Visualizer (`working_code_viz.py`)
- Alternative implementation with stable animations
- Focus on code structure visualization

## Key Concepts Visualized

- **Entity Inheritance**: Abstract base class for Game, Team, and Player
- **Singleton Pattern**: GameService as the single instance manager
- **ID Management**: Centralized unique ID generation
- **Collection Management**: Lists of games, teams, and players
- **Pattern Verification**: How SingletonTester proves the pattern works

## Requirements

- Python 3.6+
- PyQt6

## Installation

1. Install PyQt6:
```bash
pip install PyQt6
```

2. Run the visualizers:
```bash
# For the complete architecture view:
python singleton_flowchart_complete.py

# For the animated singleton flow:
python need_fix_animations.py

# For the integrated multi-tab view:
python singleton_visualizer_integrated.py

# For the working code visualizer:
python working_code_viz.py
```

## Understanding the Architecture

### Complete Flow
The complete architecture visualizer shows:
- **Entity Hierarchy** (left): Base Entity class and its subclasses
- **Main Flow** (center): Program execution and singleton creation
- **Operations** (right): How games, teams, and players are managed
- **Verification** (bottom): SingletonTester proving the pattern works

### Animation Modes
1. **Full Program Flow**: Shows entire system from Entity classes to singleton verification
2. **Singleton Pattern Only**: Focuses on getInstance() and instance management
3. **Entity Hierarchy Only**: Shows how Game, Team, and Player inherit from Entity

### Code Structure
```
Entity (Abstract)
├── Game (contains List<Team>)
├── Team (contains List<Player>)
└── Player

GameService (Singleton)
├── games: List<Game>
├── gameId, teamId, playerId (counters)
└── getInstance() method
```

## How the Complete System Works

1. **Entity Base Class**: Provides id and name fields for all game objects
2. **GameService Singleton**: 
   - Controls creation of all game objects
   - Manages unique ID generation
   - Stores all games in a central list
3. **Object Creation Flow**:
   - addGame() checks for duplicates, creates with unique ID
   - Game.addTeam() uses GameService for team IDs
   - Team.addPlayer() uses GameService for player IDs
4. **Verification**: SingletonTester proves only one GameService exists

## Animation Controls

- **Play Animation**: Runs the complete sequence automatically
- **Next Step**: Manual step-through for detailed study
- **Speed Slider**: Control animation speed (1-10)
- **Loop**: Continuously repeat the animation
- **Mode Selector**: Choose which aspect to focus on

## Educational Value

These visualizers help students understand:
- **Design Pattern Integration**: How Singleton and inheritance work together
- **Object Relationships**: Visual representation of class hierarchies
- **ID Management**: Why centralized ID generation prevents conflicts
- **Pattern Verification**: How to test that patterns work correctly
- **Real-world Application**: GameService as a practical example

## Troubleshooting

If animations aren't working:
1. Ensure PyQt6 is properly installed
2. Check Python version (3.6+ required)
3. Try the alternative visualizers if one has issues
4. The `need_fix_animations.py` file has been updated to fix QPropertyAnimation errors 