# 🎨 Singleton Pattern Visualizer Suite

A comprehensive educational tool for understanding the Singleton design pattern through interactive visualizations.

## 🚀 Quick Start

The easiest way to run the entire suite:

```bash
# One command to rule them all!
python start_visualizer.py
```

This will:
1. Start the backend server automatically
2. Open the fancy HTML launcher in your browser
3. Enable all launch buttons to work instantly

## 📁 File Structure

```
Ptqt6/
├── 🚀 Launchers
│   ├── start_visualizer.py          # Main launcher - starts server + opens HTML
│   ├── RUN_VISUALIZER.command       # macOS double-click launcher
│   ├── launcher.html                # Beautiful HTML interface with themes
│   ├── launcher_backend.py          # Backend server for button functionality
│   └── launcher.py                  # Simple Python GUI launcher
│
├── 🎯 Visualizers
│   ├── singleton_flowchart_complete.py    # Architecture & flow animations
│   ├── singleton_visualizer_integrated.py  # Code analyzer with tabs
│   └── working_code_viz.py                # Alternative visualizer
│
└── 📚 Documentation
    ├── README_SINGLETON_VISUALIZER.md      # This file
    └── UNIFICATION_PLAN.md                 # Development roadmap
```

## 🏃‍♂️ Running the Visualizers

### Method 1: One-Click Launch (Recommended)
```bash
cd Ptqt6
python start_visualizer.py
```

### Method 2: macOS Command File
```bash
# In Terminal
open RUN_VISUALIZER.command

# Or just double-click RUN_VISUALIZER.command in Finder
```

### Method 3: Manual Backend + HTML
```bash
# Terminal 1: Start backend
python launcher_backend.py

# Terminal 2: Open browser
open http://localhost:8080/launcher.html
```

### Method 4: Direct Execution
```bash
# Run individual visualizers
python singleton_flowchart_complete.py
python singleton_visualizer_integrated.py
```

## 🎯 Features

### 1. **Animated Flowchart** (`singleton_flowchart_complete.py`)
- **Interactive Animations**: Watch the Singleton pattern come to life
- **Speed Control**: Adjust animation speed from 0.5x to 3x
- **Three Modes**:
  - Full System Flow
  - Singleton Pattern Only
  - Entity Hierarchy Only
- **Visual Elements**:
  - getInstance() method flow
  - Singleton verification
  - Entity inheritance structure

### 2. **Code Analyzer** (`singleton_visualizer_integrated.py`)
- **Multi-Tab Interface**:
  - Code Browser: View Java source files
  - Flow Visualization: See the pattern in action
  - Explanations: Understand each component
- **Syntax Highlighting**: Color-coded Java code
- **Pattern Detection**: Identifies design patterns
- **Educational Notes**: Learn best practices

### 3. **HTML Launcher** (`launcher.html`)
- **Beautiful Interface**: 
  - Cyberpunk-inspired design
  - 5 color themes (Default, Cyberpunk, Matrix, Quantum, Neon)
  - Animated backgrounds and particles
- **System Monitor**: Real-time status updates
- **One-Click Launch**: All visualizers accessible from one place
- **Responsive Design**: Works on any screen size

### 4. **Java Runtime Integration**
- Launch the actual Java application
- See singleton verification in action
- Compare hashcodes to prove single instance

## 🛠️ Requirements

```bash
# Install PyQt6
pip install PyQt6

# Java (for running the JAR)
java --version  # Should be 8 or higher
```

## 🎨 HTML Launcher Themes

The HTML launcher includes 5 stunning themes:

1. **Default** (Orange/Cyan): Classic tech look
2. **Cyberpunk** (Pink/Green): Neon city vibes
3. **Matrix** (Green): Digital rain aesthetic
4. **Quantum** (Blue/Purple): Futuristic quantum computing
5. **Neon** (Magenta/Yellow): Bright and bold

Switch themes using the buttons in the top-right corner!

## 🔧 Troubleshooting

### Launch buttons not working?
- Make sure you ran `python start_visualizer.py` (not just opened the HTML)
- Check that port 8080 is not in use
- The server will auto-find an available port if needed

### PyQt6 not found?
```bash
pip install PyQt6
# or
pip3 install PyQt6
```

### Java app won't launch?
- Ensure Java is installed: `java --version`
- Check that `GamingRoom.jar` exists in the parent directory

### Port already in use?
The `start_visualizer.py` script automatically finds an available port!

## 📈 Future Enhancements

- [ ] Add zoom functionality to flowcharts
- [ ] Implement pattern complexity analysis
- [ ] Add more design pattern visualizers
- [ ] Create video export of animations
- [ ] Add collaborative features

## 🤝 Contributing

Feel free to contribute! Areas for improvement:
1. Additional visualizer modes
2. More design patterns
3. Enhanced animations
4. Performance optimizations

## 📝 License

This educational tool is part of the Singleton_GameService project.
Created for CS 230 at SNHU.

---

**Pro Tip**: For the best experience, use `python start_visualizer.py` - it handles everything automatically! 🚀