# Singleton_GameService
#I Did more then expected and added some features of my own ive decided im gonna focus on the the single and the rest of the patters to expand mya architecure an desugn kniwkedgge, nit I dont have the words for it yet,

- A basic Java project demonstrating the Singleton design pattern. 
- This is a simple command-line app that initializes game data and verifies singleton behavior in `GameService`.

## Project Summary

This project was created for **CS 230** as a milestone assignment.

It showcases:
- **The Singleton Pattern in Java**
- **Object-oriented design (`Game`, `Player`, `Team`)**
- **Command-line app architecture**
- **How to compile and package a JAR file with a manifest**

## Memory Management
<img width="506" height="280" alt="Screenshot 2025-07-13 at 7 41 31 AM" src="https://github.com/user-attachments/assets/ff7615c1-7c4b-4d48-9b9d-45b775c9f63b" />

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

### TODO:
- **Ensuring thread safety considerations in the singleton design.** This is a work in progress.

---

### Project Structure

```
Singleton_GameService/
├── src/com/gamingroom/
│   ├── Game.java
│   ├── GameService.java
│   ├── Player.java
│   ├── ProgramDriver.java
│   ├── SingletonTester.java
│   └── Team.java
├── bin/                      # Compiled .class files
├── manifest.txt              # Defines main class
├── GameApp.jar               # Final runnable JAR
├── README.md
├── LICENSE                   # MIT License for educational use
├── .gitignore
├── CS 230 Project One Milestone UML.png
└── CS 230 Project One Milestone Tasks.png
```

---

### How to Run

If you downloaded the compiled `GameApp.jar`:

 **Run it from the terminal:**

```bash
java -jar GameApp.jar
```

**Or, if downloaded from GitHub:**

```bash
java -jar ~/Downloads/GameApp.jar
```

## How to Build from Source

**FIRST:** Navigate to the project directory

cd /path/to/Singleton_GameService--main-3

**Replace /path/to/ with where you extracted the ZIP or cloned it.**


**Step 1:** Create output directory

mkdir -p bin

**Step 2:** Compile Java source files

javac -d bin src/com/gamingroom/*.java

**Step 3:** Create the manifest file

echo "Main-Class: com.gamingroom.ProgramDriver" > manifest.txt

**Step 4:** Package into a runnable JAR

jar cfm GameApp.jar manifest.txt -C bin .

**Run it**

java -jar GameApp.jar

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

