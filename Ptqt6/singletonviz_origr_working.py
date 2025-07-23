from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, 
                           QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsTextItem,
                           QTabWidget, QPushButton, QTextEdit, QSplitter, QComboBox)
from PyQt6.QtGui import QBrush, QColor, QPen, QFont
from PyQt6.QtCore import QRectF, Qt, QPointF, QLineF
import sys

class FlowchartNode(QGraphicsRectItem):
    def __init__(self, text: str, x: float, y: float, width: float = 180, height: float = 50, color="#1e1e1e"):
        super().__init__(QRectF(x, y, width, height))
        self.setBrush(QBrush(QColor(color)))
        self.setPen(QPen(QColor("#888"), 2))

        label = QGraphicsTextItem(text, self)
        label.setDefaultTextColor(QColor("#fff"))
        font = QFont("Arial", 9)
        label.setFont(font)
        label.setTextWidth(width)
        
        # Center text in the box
        text_width = label.boundingRect().width()
        text_height = label.boundingRect().height()
        label.setPos(x + (width - text_width) / 2, y + (height - text_height) / 2)

class FlowchartArrow(QGraphicsRectItem):
    def __init__(self, start_node, end_node, text="", arrow_type="straight"):
        super().__init__()
        self.setPen(QPen(Qt.PenStyle.NoPen))  # Make the rectangle invisible
        
        # Create the arrow line
        start_x = start_node.rect().center().x()
        start_y = start_node.rect().bottom()
        end_x = end_node.rect().center().x()
        end_y = end_node.rect().top()
        
        # Create line
        line = QGraphicsTextItem(self)
        line.setPlainText("↓")  # Arrow symbol
        line.setDefaultTextColor(QColor("#888"))
        font = QFont("Arial", 14)
        line.setFont(font)
        
        # Position the arrow
        line.setPos(start_x - 5, (start_y + end_y) / 2 - 10)
        
        # Add text label if provided
        if text:
            label = QGraphicsTextItem(text, self)
            label.setDefaultTextColor(QColor("#888"))
            font = QFont("Arial", 8)
            label.setFont(font)
            label.setPos(start_x + 10, (start_y + end_y) / 2 - 10)

class CodeViewer(QWidget):
    def __init__(self, title, code):
        super().__init__()
        layout = QVBoxLayout(self)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        layout.addWidget(title_label)
        
        # Code display
        code_display = QTextEdit()
        code_display.setReadOnly(True)
        code_display.setPlainText(code)
        code_display.setStyleSheet("font-family: monospace; background-color: #f5f5f5;")
        layout.addWidget(code_display)
        
        self.setLayout(layout)

class SingletonFlowchartApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Singleton Pattern Visualizer")
        self.setGeometry(100, 100, 1200, 800)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        
        # Create tabs
        tabs = QTabWidget()
        
        # Tab 1: Flowchart
        flowchart_tab = QWidget()
        flowchart_layout = QVBoxLayout(flowchart_tab)
        
        # Create flowchart scene
        scene = QGraphicsScene()
        
        # Create nodes
        program_driver = FlowchartNode("ProgramDriver main()", 50, 30)
        get_instance1 = FlowchartNode("GameService.getInstance()", 50, 100)
        check_null = FlowchartNode("instance == null?", 50, 170)
        create_new = FlowchartNode("Create new GameService", 20, 240, color="#2a5d7c")
        return_existing = FlowchartNode("Return existing instance", 200, 240, color="#2a7c5d")
        
        # Singleton tester nodes
        tester = FlowchartNode("SingletonTester.testSingleton()", 400, 30)
        get_service1 = FlowchartNode("Get service1 = GameService.getInstance()", 400, 100)
        get_service2 = FlowchartNode("Get service2 = GameService.getInstance()", 400, 170)
        compare_hash = FlowchartNode("Compare hashCodes", 400, 240, color="#7c2a5d")
        display_hash = FlowchartNode("Display hashCode values", 400, 310)
        check_equal = FlowchartNode("Check if service1 == service2", 400, 380)
        display_result = FlowchartNode("Display verification result", 400, 450, color="#7c5d2a")
        
        # Add nodes to scene
        scene.addItem(program_driver)
        scene.addItem(get_instance1)
        scene.addItem(check_null)
        scene.addItem(create_new)
        scene.addItem(return_existing)
        scene.addItem(tester)
        scene.addItem(get_service1)
        scene.addItem(get_service2)
        scene.addItem(compare_hash)
        scene.addItem(display_hash)
        scene.addItem(check_equal)
        scene.addItem(display_result)
        
        # Add arrows
        scene.addItem(FlowchartArrow(program_driver, get_instance1))
        scene.addItem(FlowchartArrow(get_instance1, check_null))
        scene.addItem(FlowchartArrow(check_null, create_new, "Yes"))
        scene.addItem(FlowchartArrow(check_null, return_existing, "No"))
        
        scene.addItem(FlowchartArrow(tester, get_service1))
        scene.addItem(FlowchartArrow(get_service1, get_service2))
        scene.addItem(FlowchartArrow(get_service2, compare_hash))
        scene.addItem(FlowchartArrow(compare_hash, display_hash))
        scene.addItem(FlowchartArrow(display_hash, check_equal))
        scene.addItem(FlowchartArrow(check_equal, display_result))
        
        # Create view
        view = QGraphicsView(scene)
        flowchart_layout.addWidget(view)
        
        # Add explanation
        explanation = QLabel("This flowchart shows how the Singleton pattern works in the GameService class.")
        explanation.setWordWrap(True)
        flowchart_layout.addWidget(explanation)
        
        tabs.addTab(flowchart_tab, "Flowchart")
        
        # Tab 2: Code Viewer
        code_tab = QWidget()
        code_layout = QVBoxLayout(code_tab)
        
        # Create code selector
        code_selector = QComboBox()
        code_selector.addItems(["GameService", "SingletonTester", "ProgramDriver", "Game"])
        code_layout.addWidget(code_selector)
        
        # Create code display area
        code_stack = QVBoxLayout()
        
        # GameService code
        gameservice_code = """package com.gamingroom;

import java.util.ArrayList;
import java.util.List;

public class GameService {

    // Private constructor to prevent instantiation from outside the class
    private GameService() {
        // prevents instantiation from outside the class
    }

    // A list of the active games
    private static List<Game> games = new ArrayList<Game>();

    // Holds the next game identifier
    private static long nextGameId = 1;

    // Properly initialized singleton instance
    private static GameService instance = null;

    // Public accessor to retrieve the singleton instance
    public static GameService getInstance() {
        if (instance == null) {
            instance = new GameService();
            System.out.println(">>> Singleton GameService instance CREATED");
        }
        return instance;
    }
    
    // Other methods omitted for brevity
}"""
        
        # SingletonTester code
        singletontester_code = """package com.gamingroom;

public class SingletonTester {

    public void testSingleton() {
        
        System.out.println("\\nAbout to test the singleton...");
        
        // Local references to the singleton instance
        GameService service1 = GameService.getInstance();
        GameService service2 = GameService.getInstance();

        // Shows that both references point to same object in memory
        System.out.println("service1 hashcode: " + service1.hashCode());
        System.out.println("service2 hashcode: " + service2.hashCode());
        System.out.println("service1 and service2 point to the same instance? " + (service1 == service2));
        
        // Clean print using just one reference
        System.out.println("service (via service1) hashcode: " + service1.hashCode());
    }
}"""
        
        # ProgramDriver code
        programdriver_code = """package com.gamingroom;

public class ProgramDriver {
    
    public static void main(String[] args) {
        
        // Reference to the singleton instance
        GameService service = GameService.getInstance();
        
        System.out.println("\\nAbout to test initializing game data...");
        
        // Initialize with some game data
        Game game1 = service.addGame("Game #1");
        System.out.println(game1);
        Game game2 = service.addGame("Game #2");
        System.out.println(game2);
        
        // Use another class to prove there is only one instance
        SingletonTester tester = new SingletonTester();
        tester.testSingleton();
    }
}"""
        
        # Game code
        game_code = """package com.gamingroom;

public class Game {
    long id;
    String name;

    // Private constructor to prevent creating empty instances
    private Game() {
    }

    // Constructs a Game object with a unique ID and name
    public Game(long id, String name) {
        this();
        this.id = id;
        this.name = name;
    }

    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Game [id=" + id + ", name=" + name + "]";
    }
}"""
        
        # Create code viewer
        self.code_viewer = QTextEdit()
        self.code_viewer.setReadOnly(True)
        self.code_viewer.setStyleSheet("font-family: monospace; background-color: #f5f5f5;")
        self.code_viewer.setPlainText(gameservice_code)  # Default to GameService
        code_layout.addWidget(self.code_viewer)
        
        # Connect selector to code display
        def update_code(index):
            if index == 0:
                self.code_viewer.setPlainText(gameservice_code)
            elif index == 1:
                self.code_viewer.setPlainText(singletontester_code)
            elif index == 2:
                self.code_viewer.setPlainText(programdriver_code)
            elif index == 3:
                self.code_viewer.setPlainText(game_code)
        
        code_selector.currentIndexChanged.connect(update_code)
        
        tabs.addTab(code_tab, "Code Viewer")
        
        # Tab 3: Explanation
        explanation_tab = QWidget()
        explanation_layout = QVBoxLayout(explanation_tab)
        
        explanation_text = """# Singleton Pattern Explanation

## What is the Singleton Pattern?
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

## Key Components
1. Private constructor to prevent instantiation from outside the class
2. Private static instance variable to hold the single instance
3. Public static method to return the instance (creating it if necessary)

## Why Use Singleton?
- Memory Efficiency: Only one instance is created
- Centralized Control: Single point of access for management
- Consistency: All parts of the application work with the same instance

## Verifying with hashCode()
The hashCode method in Java returns an integer value representing the memory address of an object.
By comparing hashcodes, we can verify that two references point to the same object in memory.

## Implementation in GameService
- Private constructor prevents external instantiation
- Static instance variable holds the single instance
- getInstance() method creates the instance only once
- HashCode verification proves both references point to the same object"""
        
        explanation_display = QTextEdit()
        explanation_display.setReadOnly(True)
        explanation_display.setMarkdown(explanation_text)
        explanation_layout.addWidget(explanation_display)
        
        tabs.addTab(explanation_tab, "Explanation")
        
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SingletonFlowchartApp()
    window.show()
    sys.exit(app.exec()) 