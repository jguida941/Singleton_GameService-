# Complete System Flowchart - GameService Application

```mermaid
flowchart TB
    %% Entry Points
    Start1[ProgramDriver.main] --> GetService1[GameService.getInstance]
    Start2[SingletonTester.testSingleton] --> GetService2[GameService.getInstance]
    
    %% Singleton Check
    GetService1 --> SingletonCheck{instance == null?}
    GetService2 --> SingletonCheck
    
    SingletonCheck -->|Yes| CreateNew[Create new GameService]
    SingletonCheck -->|No| ReturnExisting[Return existing instance]
    
    CreateNew --> InitService[Initialize:\n- games = new ArrayList\n- nextGameId = 1\n- nextTeamId = 1\n- nextPlayerId = 1]
    InitService --> ReturnExisting
    
    %% Main Program Flow
    ReturnExisting --> ServiceReady[GameService Ready]
    
    %% Add Game Flow
    ServiceReady --> AddGame[service.addGame"Game Name"]
    AddGame --> CheckDuplicate1{Game name exists?}
    CheckDuplicate1 -->|Yes| ReturnExistingGame[Return existing Game]
    CheckDuplicate1 -->|No| CreateGame[Create new Game:\n- id = getNextGameId\n- Extends Entity]
    
    CreateGame --> IncrementGameId[nextGameId++]
    IncrementGameId --> AddToList1[Add to games list]
    AddToList1 --> ReturnGame[Return Game instance]
    
    %% Add Team Flow
    ReturnGame --> AddTeam[game.addTeam"Team Name"]
    ReturnExistingGame --> AddTeam
    AddTeam --> CheckDuplicate2{Team name exists\nin this game?}
    CheckDuplicate2 -->|Yes| ReturnExistingTeam[Return existing Team]
    CheckDuplicate2 -->|No| CreateTeam[Create new Team:\n- id = service.getNextTeamId\n- Extends Entity]
    
    CreateTeam --> GetServiceForId1[GameService.getInstance]
    GetServiceForId1 --> IncrementTeamId[nextTeamId++]
    IncrementTeamId --> AddToList2[Add to teams list]
    AddToList2 --> ReturnTeam[Return Team instance]
    
    %% Add Player Flow
    ReturnTeam --> AddPlayer[team.addPlayer"Player Name"]
    ReturnExistingTeam --> AddPlayer
    AddPlayer --> CheckDuplicate3{Player name exists\nin this team?}
    CheckDuplicate3 -->|Yes| ReturnExistingPlayer[Return existing Player]
    CheckDuplicate3 -->|No| CreatePlayer[Create new Player:\n- id = service.getNextPlayerId\n- Extends Entity]
    
    CreatePlayer --> GetServiceForId2[GameService.getInstance]
    GetServiceForId2 --> IncrementPlayerId[nextPlayerId++]
    IncrementPlayerId --> AddToList3[Add to players list]
    AddToList3 --> ReturnPlayer[Return Player instance]
    
    %% Entity Inheritance
    ReturnPlayer --> DisplayInfo[Display using toString]
    ReturnExistingPlayer --> DisplayInfo
    
    %% Singleton Test Flow
    ServiceReady --> TestFlow[SingletonTester Flow]
    TestFlow --> GetFirst[service1 = getInstance]
    GetFirst --> GetSecond[service2 = getInstance]
    GetSecond --> CompareHash[Compare hashCodes]
    CompareHash --> VerifySame[Verify service1 == service2]
    VerifySame --> TestResult[Display: Same instance!]
    
    %% Style
    classDef singleton fill:#f9f,stroke:#333,stroke-width:4px
    classDef entity fill:#bbf,stroke:#333,stroke-width:2px
    classDef check fill:#ffd,stroke:#333,stroke-width:2px
    
    class GameService,CreateNew,InitService,ServiceReady singleton
    class CreateGame,CreateTeam,CreatePlayer entity
    class SingletonCheck,CheckDuplicate1,CheckDuplicate2,CheckDuplicate3 check
```

## Key Flow Elements:

### 1. Singleton Pattern Implementation
- Both entry points (ProgramDriver and SingletonTester) use getInstance()
- Singleton check ensures only one GameService instance exists
- All ID generation goes through the single GameService instance

### 2. Entity Hierarchy Usage
- Game, Team, and Player all extend Entity
- Each inherits id and name fields
- All use super constructor to initialize Entity fields

### 3. Duplicate Prevention
- At each level (Game, Team, Player), names are checked for duplicates
- Case-insensitive comparison used
- Existing objects returned if found

### 4. ID Management Flow
- GameService maintains separate counters for each entity type
- IDs are incremented after each new entity creation
- All entities must request IDs from GameService.getInstance()

### 5. Hierarchical Structure
- GameService → Games → Teams → Players
- Each level maintains a list of its children
- Navigation possible through getter methods