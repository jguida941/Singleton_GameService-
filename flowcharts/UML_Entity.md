# Singleton GameService UML Diagram

This UML diagram illustrates the structure and relationships of the Singleton GameService implementation.
**TODO: Fix text fititng properly into boxes**

```mermaid
classDiagram
    class Entity {
        -long id
        -String name
        +Entity(long id, String name)
        +long getId()
        +String getName()
        +String toString()
    }
    
    class Game {
        -List~Team~ teams
        +Game(long id, String name)
        +Team addTeam(String name)
        +List~Team~ getTeams()
        +String toString()
    }
    
    class Team {
        -List~Player~ players
        +Team(long id, String name)
        +Player addPlayer(String name)
        +List~Player~ getPlayers()
        +String toString()
    }
    
    class Player {
        +Player(long id, String name)
        +String toString()
    }
    
    class GameService {
        -static GameService instance
        -static List~Game~ games
        -long nextGameId
        -long nextTeamId
        -long nextPlayerId
        -GameService()
        +static GameService getInstance()
        +long getNextPlayerId()
        +long getNextTeamId()
        +Game addGame(String name)
        +Game getGame(int index)
        +Game getGame(long id)
        +Game getGame(String name)
        +int getGameCount()
    }
    
    class ProgramDriver {
        +static void main(String[] args)
    }
    
    class SingletonTester {
        +void testSingleton()
    }
    
    Entity <|-- Game : extends
    Entity <|-- Team : extends
    Entity <|-- Player : extends
    
    Game *-- Team : contains
    Team *-- Player : contains
    
    GameService o-- Game : manages
    ProgramDriver --> GameService : uses
    SingletonTester --> GameService : tests
```

## Key Design Patterns

### Singleton Pattern
- Implemented in `GameService` class
- Ensures only one instance exists throughout the application
- Provides global access point via `getInstance()`

### Iterator Pattern
- Used in `addGame()`, `getGame()`, `addTeam()`, and `addPlayer()` methods
- Searches for existing entities before creating new ones
- Prevents duplicate entries

### Inheritance Hierarchy
- `Entity` serves as the base abstract class
- `Game`, `Team`, and `Player` inherit from `Entity`
- Common attributes (id, name) and behaviors (toString) are defined in the base class 
