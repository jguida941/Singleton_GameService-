# Updated UML Diagram - Singleton GameService with Entity Hierarchy
**TODO: Fix text not fitting in box**

```mermaid
classDiagram
    %% Abstract Entity class
    class Entity {
        <<abstract>>
        -long id
        -String name
        +Entity(long id, String name)
        +long getId()
        +String getName()
        +String toString()
    }

    %% Singleton GameService
    class GameService {
        <<singleton>>
        -static GameService instance
        -List~Game~ games
        -long nextGameId
        -long nextTeamId
        -long nextPlayerId
        -GameService()
        +static GameService getInstance()
        +Game addGame(String name)
        +Game getGame(long id)
        +long getNextGameId()
        +long getNextTeamId()
        +long getNextPlayerId()
    }

    %% Game class
    class Game {
        -List~Team~ teams
        +Game(long id, String name)
        +Team addTeam(String name)
        +List~Team~ getTeams()
        +String toString()
    }

    %% Team class
    class Team {
        -List~Player~ players
        +Team(long id, String name)
        +Player addPlayer(String name)
        +List~Player~ getPlayers()
        +String toString()
    }

    %% Player class
    class Player {
        +Player(long id, String name)
        +String toString()
    }

    %% Main driver classes
    class ProgramDriver {
        +static void main(String[] args)
    }

    class SingletonTester {
        +void testSingleton()
    }

    %% Inheritance relationships
    Entity <|-- Game : extends
    Entity <|-- Team : extends
    Entity <|-- Player : extends

    %% Composition relationships
    GameService "1" *-- "0..*" Game : manages
    Game "1" *-- "0..*" Team : contains
    Team "1" *-- "0..*" Player : contains

    %% Dependencies
    ProgramDriver ..> GameService : uses
    SingletonTester ..> GameService : tests
    Game ..> GameService : uses getInstance()
    Team ..> GameService : uses getInstance()

    %% Notes on relationships
    note for GameService "Singleton Pattern:\n- Private constructor\n- Static instance\n- getInstance() method"
    
    note for Entity "Abstract Base Class:\n- Common fields (id, name)\n- Shared behavior\n- Cannot be instantiated"
```

## Key Design Patterns and Relationships:

1. **Singleton Pattern**: GameService ensures only one instance exists
2. **Inheritance Hierarchy**: Entity is the abstract base class for Game, Team, and Player
3. **Composition**: 
   - GameService manages multiple Games
   - Each Game contains multiple Teams
   - Each Team contains multiple Players
4. **ID Management**: GameService centrally manages unique IDs for all entities

## Class Responsibilities:

- **Entity**: Abstract base providing id and name fields for all game objects
- **GameService**: Singleton managing all games and providing unique IDs
- **Game**: Represents a game session with teams
- **Team**: Represents a team with players
- **Player**: Represents an individual player
- **ProgramDriver**: Main entry point demonstrating the system
- **SingletonTester**: Tests the singleton pattern implementation
