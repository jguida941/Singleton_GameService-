import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                           QComboBox, QTextEdit, QGroupBox, QLabel, QSplitter,
                           QPushButton, QTextBrowser)
from PyQt6.QtGui import QFont, QTextCharFormat, QColor, QSyntaxHighlighter, QTextCursor
from PyQt6.QtCore import Qt, QRegularExpression

class JavaSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []
        
        # Keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(86, 156, 214))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "abstract", "assert", "boolean", "break", "byte", "case", "catch",
            "char", "class", "const", "continue", "default", "do", "double",
            "else", "enum", "extends", "final", "finally", "float", "for",
            "goto", "if", "implements", "import", "instanceof", "int", "interface",
            "long", "native", "new", "package", "private", "protected", "public",
            "return", "short", "static", "strictfp", "super", "switch", "synchronized",
            "this", "throw", "throws", "transient", "try", "void", "volatile", "while"
        ]
        for keyword in keywords:
            pattern = QRegularExpression(f"\\b{keyword}\\b")
            self.highlighting_rules.append((pattern, keyword_format))
        
        # Class names
        class_format = QTextCharFormat()
        class_format.setForeground(QColor(78, 201, 176))
        self.highlighting_rules.append((QRegularExpression("\\b[A-Z][A-Za-z0-9_]*\\b"), class_format))
        
        # Comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(106, 153, 85))
        self.highlighting_rules.append((QRegularExpression("//[^\n]*"), comment_format))
        
        # Multi-line comments
        self.multiline_comment_format = QTextCharFormat()
        self.multiline_comment_format.setForeground(QColor(106, 153, 85))
        
        # Strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(206, 145, 120))
        self.highlighting_rules.append((QRegularExpression("\".*\""), string_format))
        
        # Numbers
        number_format = QTextCharFormat()
        number_format.setForeground(QColor(181, 206, 168))
        self.highlighting_rules.append((QRegularExpression("\\b[0-9]+\\b"), number_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

class CodeAnalyzerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.project_path = "/Users/jguida941/Downloads/Singleton_GameService--main-2/src/com/gamingroom"
        self.current_file = None
        self.current_content = []
        self.init_ui()
        self.init_code_analysis()
    
    def init_ui(self):
        main_layout = QHBoxLayout()
        
        # Left panel - Code viewer
        left_panel = QVBoxLayout()
        
        # File selector
        file_selector_layout = QHBoxLayout()
        file_selector_layout.addWidget(QLabel("Select File:"))
        
        self.file_selector = QComboBox()
        self.file_selector.addItems([
            "Entity.java",
            "GameService.java",
            "Game.java",
            "Team.java",
            "Player.java",
            "SingletonTester.java",
            "ProgramDriver.java"
        ])
        self.file_selector.currentTextChanged.connect(self.load_file)
        file_selector_layout.addWidget(self.file_selector)
        
        self.reload_btn = QPushButton("Reload")
        self.reload_btn.clicked.connect(self.reload_current_file)
        file_selector_layout.addWidget(self.reload_btn)
        
        left_panel.addLayout(file_selector_layout)
        
        # Code editor
        self.code_editor = QTextEdit()
        self.code_editor.setReadOnly(True)
        self.code_editor.setFont(QFont("Consolas", 10))
        self.code_editor.cursorPositionChanged.connect(self.analyze_current_line)
        
        # Syntax highlighter
        self.highlighter = JavaSyntaxHighlighter(self.code_editor.document())
        
        left_panel.addWidget(self.code_editor)
        
        # Right panel - Analysis
        right_panel = QVBoxLayout()
        
        # Current line info
        line_info_group = QGroupBox("Current Line Information")
        line_info_layout = QVBoxLayout()
        
        self.line_label = QLabel("Line: -")
        self.line_label.setStyleSheet("font-weight: bold; font-size: 14px; color: #4a90e2;")
        line_info_layout.addWidget(self.line_label)
        
        self.current_line_text = QTextEdit()
        self.current_line_text.setReadOnly(True)
        self.current_line_text.setMaximumHeight(60)
        self.current_line_text.setFont(QFont("Consolas", 9))
        line_info_layout.addWidget(self.current_line_text)
        
        line_info_group.setLayout(line_info_layout)
        right_panel.addWidget(line_info_group)
        
        # Explanation
        explanation_group = QGroupBox("Code Explanation")
        explanation_layout = QVBoxLayout()
        
        self.explanation_text = QTextBrowser()
        self.explanation_text.setOpenExternalLinks(False)
        explanation_layout.addWidget(self.explanation_text)
        
        explanation_group.setLayout(explanation_layout)
        right_panel.addWidget(explanation_group)
        
        # Memory impact
        memory_group = QGroupBox("Memory Impact Analysis")
        memory_layout = QVBoxLayout()
        
        self.memory_text = QTextEdit()
        self.memory_text.setReadOnly(True)
        self.memory_text.setMaximumHeight(120)
        memory_layout.addWidget(self.memory_text)
        
        memory_group.setLayout(memory_layout)
        right_panel.addWidget(memory_group)
        
        # Design pattern
        pattern_group = QGroupBox("Design Pattern & Complexity")
        pattern_layout = QVBoxLayout()
        
        self.pattern_text = QTextEdit()
        self.pattern_text.setReadOnly(True)
        self.pattern_text.setMaximumHeight(120)
        pattern_layout.addWidget(self.pattern_text)
        
        pattern_group.setLayout(pattern_layout)
        right_panel.addWidget(pattern_group)
        
        # Create splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        left_widget = QWidget()
        left_widget.setLayout(left_panel)
        splitter.addWidget(left_widget)
        
        right_widget = QWidget()
        right_widget.setLayout(right_panel)
        splitter.addWidget(right_widget)
        
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 1)
        
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)
        
        # Load first file
        self.load_file("Entity.java")
    
    def init_code_analysis(self):
        """Initialize comprehensive code analysis database"""
        self.code_analysis = {
            "Entity.java": {
                1: {
                    "line": "package com.gamingroom;",
                    "explanation": "Package declaration defines the namespace for this class. All classes in this package can access each other's package-private members.",
                    "memory": "No runtime memory impact. Package info stored in class metadata.",
                    "pattern": "Package organization pattern for namespace management.",
                    "complexity": "O(1) - Compile-time directive"
                },
                11: {
                    "line": "public abstract class Entity {",
                    "explanation": "Declares Entity as an abstract class. Abstract classes cannot be instantiated directly - they serve as base classes for inheritance. The 'public' modifier means this class is accessible from any package.",
                    "memory": "Class metadata stored in method area/metaspace. No instance memory since abstract classes cannot be instantiated.",
                    "pattern": "Template Method Pattern - Defines structure that subclasses must follow.",
                    "complexity": "O(1) - Class declaration"
                },
                14: {
                    "line": "private long id;",
                    "explanation": "Private instance field storing unique identifier. 'long' is a 64-bit primitive type. Private access ensures encapsulation - only accessible within this class.",
                    "memory": "8 bytes per instance in heap memory. Stored inline within object memory layout.",
                    "pattern": "Encapsulation - Information hiding principle of OOP.",
                    "complexity": "O(1) - Direct memory access"
                },
                16: {
                    "line": "private String name;",
                    "explanation": "Private instance field storing entity name. String is a reference type, so this stores a reference (pointer) to the actual String object.",
                    "memory": "8 bytes for reference (64-bit JVM) + String object size (varies based on content).",
                    "pattern": "Encapsulation - Private field with public getter.",
                    "complexity": "O(1) - Reference storage"
                },
                19: {
                    "line": "public Entity(long id, String name) {",
                    "explanation": "Public constructor that requires both id and name. This ensures every Entity has these values from creation - no Entity can exist without them.",
                    "memory": "Stack frame allocated during construction. Parameters passed: 8 bytes (long) + 8 bytes (String reference).",
                    "pattern": "Constructor pattern - Ensures valid initial state.",
                    "complexity": "O(1) - Simple assignment"
                },
                20: {
                    "line": "this.id = id;",
                    "explanation": "Assigns constructor parameter 'id' to instance field 'id'. The 'this' keyword distinguishes the instance field from the parameter of the same name.",
                    "memory": "Direct write to object's heap memory location. No additional allocation.",
                    "pattern": "Standard initialization pattern.",
                    "complexity": "O(1) - Direct assignment"
                },
                25: {
                    "line": "public long getId() {",
                    "explanation": "Public getter method providing read-only access to the private id field. Follows JavaBean naming convention (get + FieldName).",
                    "memory": "No memory allocation. Returns primitive directly from object memory.",
                    "pattern": "Getter pattern - Controlled access to private data.",
                    "complexity": "O(1) - Direct field access"
                },
                30: {
                    "line": "public String getName() {",
                    "explanation": "Public getter for name field. Returns the String reference, not a copy, so caller could modify the String if it were mutable (but Strings are immutable in Java).",
                    "memory": "No allocation. Returns existing reference (8 bytes).",
                    "pattern": "Getter pattern - Encapsulation.",
                    "complexity": "O(1) - Direct reference return"
                },
                43: {
                    "line": "public String toString() {",
                    "explanation": "Overrides Object.toString() to provide meaningful string representation. The @Override annotation ensures this correctly overrides the parent method.",
                    "memory": "Creates new String objects during concatenation. Temporary StringBuilder used internally.",
                    "pattern": "Override pattern - Polymorphic behavior.",
                    "complexity": "O(n) - String concatenation"
                },
                44: {
                    "line": "return getClass().getSimpleName() + \" [id=\" + id + \", name=\" + name + \"]\";",
                    "explanation": "Uses reflection (getClass()) to get actual runtime type, then getSimpleName() for class name without package. This ensures subclasses show their actual type, not 'Entity'.",
                    "memory": "Creates multiple temporary String objects. Each + operation may create new String. Total: ~100-200 bytes temporary.",
                    "pattern": "Polymorphism - Method returns actual subclass type.",
                    "complexity": "O(n) - Multiple string concatenations"
                }
            },
            "GameService.java": {
                11: {
                    "line": "public class GameService {",
                    "explanation": "Public class declaration for GameService. This will implement the Singleton pattern to ensure only one instance exists.",
                    "memory": "Class metadata in metaspace. Static fields allocated when class loads.",
                    "pattern": "Singleton Pattern implementation class.",
                    "complexity": "O(1) - Class declaration"
                },
                19: {
                    "line": "private static GameService instance = null;",
                    "explanation": "Static field holding the single instance. Initialized to null for lazy initialization. 'static' means this belongs to the class, not instances.",
                    "memory": "8 bytes in method area/metaspace. Shared across all class users.",
                    "pattern": "Singleton Pattern - Instance holder with lazy initialization.",
                    "complexity": "O(1) - Static field"
                },
                22: {
                    "line": "private static List<Game> games = new ArrayList<Game>();",
                    "explanation": "Static list to store all games. ArrayList provides dynamic sizing. Initial capacity is 10 by default.",
                    "memory": "ArrayList object (~48 bytes) + backing array (10 * 8 bytes initially) in heap.",
                    "pattern": "Singleton Pattern - Centralized storage.",
                    "complexity": "O(1) - Initialization"
                },
                31: {
                    "line": "private GameService() {",
                    "explanation": "Private constructor is KEY to Singleton pattern. Prevents external code from creating instances with 'new GameService()'.",
                    "memory": "No direct memory impact - prevents allocation.",
                    "pattern": "Singleton Pattern - Access control through private constructor.",
                    "complexity": "O(1) - Empty constructor"
                },
                42: {
                    "line": "public static GameService getInstance() {",
                    "explanation": "Static factory method - the ONLY way to get GameService instance. Being static, it can be called without an instance.",
                    "memory": "No instance memory. Method in method area.",
                    "pattern": "Singleton Pattern - Global access point.",
                    "complexity": "O(1) - Method declaration"
                },
                43: {
                    "line": "if (instance == null) {",
                    "explanation": "Lazy initialization check. Instance created only on first access, not at class load time. Saves memory if never used.",
                    "memory": "Simple null check - no allocation.",
                    "pattern": "Singleton Pattern - Lazy initialization.",
                    "complexity": "O(1) - Comparison"
                },
                44: {
                    "line": "instance = new GameService();",
                    "explanation": "Creates the singleton instance. This line executes ONLY ONCE in application lifetime, on first getInstance() call.",
                    "memory": "Allocates GameService object (~32-48 bytes) in heap.",
                    "pattern": "Singleton Pattern - Single instance creation.",
                    "complexity": "O(1) - Object allocation"
                },
                47: {
                    "line": "return instance;",
                    "explanation": "Returns the singleton instance. All callers get the same object reference.",
                    "memory": "Returns existing reference - no allocation.",
                    "pattern": "Singleton Pattern - Shared instance.",
                    "complexity": "O(1) - Return"
                },
                100: {
                    "line": "return ++nextGameId;",
                    "explanation": "Pre-increment operator: increments first, then returns new value. Ensures unique sequential IDs. Thread-unsafe in current form.",
                    "memory": "Modifies static long field (8 bytes).",
                    "pattern": "ID Generation Pattern - Sequential unique IDs.",
                    "complexity": "O(1) - Increment and return"
                }
            },
            "Game.java": {
                20: {
                    "line": "public class Game extends Entity {",
                    "explanation": "Game inherits from Entity, gaining id and name fields plus their methods. 'extends' creates IS-A relationship: Game IS-A Entity.",
                    "memory": "Inherits Entity's fields (16 bytes) plus own fields. Virtual method table for polymorphism.",
                    "pattern": "Inheritance - Extending abstract base class.",
                    "complexity": "O(1) - Class declaration"
                },
                23: {
                    "line": "private List<Team> teams = new ArrayList<Team>();",
                    "explanation": "Composition relationship: Game HAS-A list of Teams. ArrayList allows dynamic team addition/removal.",
                    "memory": "8 bytes (reference) + ArrayList object + backing array in heap.",
                    "pattern": "Composition Pattern - Game contains Teams.",
                    "complexity": "O(1) - Initialization"
                },
                27: {
                    "line": "super(id, name);",
                    "explanation": "Calls Entity's constructor. Must be first statement in constructor. Passes id and name up to parent for initialization.",
                    "memory": "Reuses parent's initialization - no extra allocation.",
                    "pattern": "Constructor chaining - Inheritance pattern.",
                    "complexity": "O(1) - Parent constructor call"
                },
                44: {
                    "line": "public Team addTeam(String name) {",
                    "explanation": "Factory method for creating teams. Enforces uniqueness by name within this game.",
                    "memory": "May allocate new Team object if not found.",
                    "pattern": "Factory Method Pattern within aggregate.",
                    "complexity": "O(n) - Linear search through teams"
                },
                46: {
                    "line": "if (team.getName().equalsIgnoreCase(name)) {",
                    "explanation": "Case-insensitive comparison prevents duplicate teams. 'Team1' and 'team1' are considered the same.",
                    "memory": "Temporary lowercase strings created for comparison.",
                    "pattern": "Uniqueness constraint enforcement.",
                    "complexity": "O(k) - String comparison, k = string length"
                },
                53: {
                    "line": "Team team = new Team(GameService.getInstance().getNextTeamId(), name);",
                    "explanation": "Creates new Team with globally unique ID. Demonstrates Singleton usage - gets ID from single GameService instance.",
                    "memory": "Allocates new Team object + gets GameService reference.",
                    "pattern": "Factory + Singleton collaboration.",
                    "complexity": "O(1) - Object creation"
                }
            },
            "Team.java": {
                12: {
                    "line": "public class Team extends Entity {",
                    "explanation": "Team inherits from Entity, gaining id and name. Continues the hierarchy: Entity <- Game <- Team <- Player.",
                    "memory": "Inherits 16 bytes from Entity + own fields.",
                    "pattern": "Inheritance hierarchy - Template pattern.",
                    "complexity": "O(1) - Class declaration"
                },
                15: {
                    "line": "private List<Player> players = new ArrayList<>();",
                    "explanation": "Composition: Team HAS-A list of Players. Diamond operator <> infers type from declaration.",
                    "memory": "8 bytes reference + ArrayList allocation.",
                    "pattern": "Composition Pattern - Aggregation.",
                    "complexity": "O(1) - Initialization"
                },
                18: {
                    "line": "super(id, name);",
                    "explanation": "Delegates to Entity constructor for base initialization. Ensures Entity's contract is fulfilled.",
                    "memory": "No additional allocation - reuses parent logic.",
                    "pattern": "Constructor chaining.",
                    "complexity": "O(1) - Super call"
                },
                35: {
                    "line": "Player player = new Player(GameService.getInstance().getNextPlayerId(), name);",
                    "explanation": "Creates Player with globally unique ID from GameService singleton. Shows cross-hierarchy singleton usage.",
                    "memory": "New Player object + singleton reference.",
                    "pattern": "Factory + Singleton pattern.",
                    "complexity": "O(1) - Object creation"
                }
            },
            "Player.java": {
                15: {
                    "line": "public class Player extends Entity {",
                    "explanation": "Player is the leaf node in hierarchy. Simplest entity - just inherits from Entity without adding fields.",
                    "memory": "Only Entity's 16 bytes - no additional fields.",
                    "pattern": "Inheritance - Leaf node in hierarchy.",
                    "complexity": "O(1) - Class declaration"
                },
                20: {
                    "line": "public Player(long id, String name) {",
                    "explanation": "Simple constructor that delegates everything to Entity. Player adds no additional state.",
                    "memory": "Stack frame during construction only.",
                    "pattern": "Constructor delegation.",
                    "complexity": "O(1) - Constructor"
                },
                26: {
                    "line": "return \"Player [id=\" + getId() + \", name=\" + getName() + \"]\";",
                    "explanation": "Custom toString() using getters instead of direct field access (fields are private in parent).",
                    "memory": "String concatenation creates temporary objects.",
                    "pattern": "Method override for custom representation.",
                    "complexity": "O(n) - String concatenation"
                }
            }
        }
    
    def load_file(self, filename):
        """Load and display file content with line numbers"""
        self.current_file = filename
        file_path = os.path.join(self.project_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                self.current_content = content.split('\n')
            
            # Add line numbers
            numbered_lines = []
            for i, line in enumerate(self.current_content, 1):
                numbered_lines.append(f"{i:4d} | {line}")
            
            self.code_editor.setPlainText('\n'.join(numbered_lines))
            
            # Reset analysis panel
            self.line_label.setText(f"File: {filename}")
            self.current_line_text.clear()
            self.explanation_text.clear()
            self.memory_text.clear()
            self.pattern_text.clear()
            
        except FileNotFoundError:
            self.code_editor.setPlainText(f"Error: Could not find file {file_path}")
            self.current_content = []
        except Exception as e:
            self.code_editor.setPlainText(f"Error loading file: {str(e)}")
            self.current_content = []
    
    def reload_current_file(self):
        """Reload the current file"""
        if self.current_file:
            self.load_file(self.current_file)
    
    def analyze_current_line(self):
        """Analyze the line where cursor is positioned"""
        cursor = self.code_editor.textCursor()
        block_number = cursor.blockNumber()
        
        # Get the actual line number (remove line number prefix)
        current_text = cursor.block().text()
        if ' | ' in current_text:
            try:
                line_num = int(current_text.split(' | ')[0].strip())
                line_content = current_text.split(' | ', 1)[1] if ' | ' in current_text else ""
                
                self.line_label.setText(f"Line: {line_num}")
                self.current_line_text.setPlainText(line_content)
                
                # Check if we have analysis for this line
                if hasattr(self, 'code_analysis') and self.current_file in self.code_analysis:
                    file_analysis = self.code_analysis[self.current_file]
                    if line_num in file_analysis:
                        analysis = file_analysis[line_num]
                        
                        # Update all analysis panels
                        self.explanation_text.setHtml(f"<p style='color: #cccccc;'>{analysis['explanation']}</p>")
                        self.memory_text.setPlainText(analysis['memory'])
                        self.pattern_text.setPlainText(f"Pattern: {analysis['pattern']}\nComplexity: {analysis['complexity']}")
                        
                        # Highlight the current line
                        self.highlight_current_line(block_number)
                    else:
                        self.show_default_message()
                else:
                    self.show_default_message()
            except ValueError:
                self.show_default_message()
        else:
            self.show_default_message()
    
    def highlight_current_line(self, block_number):
        """Highlight the current line in the editor"""
        # Clear previous highlights
        cursor = self.code_editor.textCursor()
        cursor.select(QTextCursor.SelectionType.Document)
        cursor.setCharFormat(QTextCharFormat())
        cursor.clearSelection()
        
        # Highlight current line
        cursor = self.code_editor.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        for _ in range(block_number):
            cursor.movePosition(QTextCursor.MoveOperation.NextBlock)
        
        cursor.select(QTextCursor.SelectionType.LineUnderCursor)
        
        highlight_format = QTextCharFormat()
        highlight_format.setBackground(QColor(50, 50, 80))
        cursor.setCharFormat(highlight_format)
    
    def show_default_message(self):
        """Show default message when no analysis is available"""
        self.explanation_text.setHtml(
            "<p style='color: #888;'><i>Click on a line with analysis available to see detailed explanation.</i></p>"
        )
        self.memory_text.setPlainText("Memory analysis will appear here when you select an analyzed line.")
        self.pattern_text.setPlainText("Design pattern and complexity information will appear here.")

def test_code_analyzer():
    """Test the code analyzer widget independently"""
    app = QApplication(sys.argv)
    
    # Set dark theme
    app.setStyleSheet("""
        QWidget {
            background-color: #2a2a2a;
            color: #cccccc;
        }
        QGroupBox {
            border: 1px solid #444;
            border-radius: 4px;
            margin-top: 8px;
            padding-top: 8px;
            font-weight: bold;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            left: 10px;
            padding: 0 5px 0 5px;
        }
        QTextEdit, QTextBrowser {
            background-color: #1e1e1e;
            border: 1px solid #444;
            border-radius: 4px;
        }
        QComboBox {
            background-color: #333;
            border: 1px solid #444;
            padding: 5px;
        }
        QPushButton {
            background-color: #4a90e2;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #5ba0f2;
        }
    """)
    
    # Create and show widget
    analyzer = CodeAnalyzerWidget()
    analyzer.setWindowTitle("Code Analyzer - Debug Test")
    analyzer.resize(1200, 800)
    analyzer.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    test_code_analyzer()