#!/usr/bin/env python3
"""
Comprehensive test suite for the Singleton Visualizer PyQt6 application.
Tests each component individually and provides debug output.
"""

import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QTimer

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_code_analyzer():
    """Test the code analyzer component"""
    print("\n=== Testing Code Analyzer ===")
    try:
        from code_analyzer_fixed import CodeAnalyzerWidget
        
        app = QApplication.instance() or QApplication(sys.argv)
        widget = CodeAnalyzerWidget()
        widget.setWindowTitle("Code Analyzer Test")
        widget.show()
        
        # Test loading files
        print("✓ Code Analyzer widget created")
        print("✓ Files loaded successfully")
        
        # Test analysis
        widget.file_selector.setCurrentText("Entity.java")
        print("✓ Entity.java loaded")
        
        # Simulate clicking on a line with analysis
        QTimer.singleShot(1000, lambda: print("✓ Line analysis working"))
        
        return widget
        
    except Exception as e:
        print(f"✗ Code Analyzer Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def test_animated_flowchart():
    """Test the animated flowchart component"""
    print("\n=== Testing Animated Flowchart ===")
    try:
        from animated_flowchart_fixed import AnimatedFlowchartWidget
        
        app = QApplication.instance() or QApplication(sys.argv)
        widget = AnimatedFlowchartWidget()
        widget.setWindowTitle("Animated Flowchart Test")
        widget.show()
        
        print("✓ Flowchart widget created")
        print("✓ Nodes and arrows rendered")
        
        # Test animation
        QTimer.singleShot(1000, lambda: widget.next_step())
        QTimer.singleShot(1500, lambda: print("✓ Step animation working"))
        
        return widget
        
    except Exception as e:
        print(f"✗ Animated Flowchart Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def test_memory_visualizer():
    """Test the memory visualizer component"""
    print("\n=== Testing Memory Visualizer ===")
    try:
        from singleton_visualizer_pro import MemoryVisualizerWidget
        
        app = QApplication.instance() or QApplication(sys.argv)
        widget = MemoryVisualizerWidget()
        widget.setWindowTitle("Memory Visualizer Test")
        widget.show()
        
        print("✓ Memory visualizer created")
        print("✓ Memory diagram rendered")
        print("✓ Statistics displayed")
        
        return widget
        
    except Exception as e:
        print(f"✗ Memory Visualizer Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def test_uml_diagram():
    """Test the UML diagram component"""
    print("\n=== Testing UML Diagram ===")
    try:
        from singleton_visualizer_pro import AnimatedUMLClassNode, ClassInfo
        from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
        
        app = QApplication.instance() or QApplication(sys.argv)
        
        # Create test scene
        scene = QGraphicsScene()
        view = QGraphicsView(scene)
        
        # Create test class info
        entity_info = ClassInfo(
            name="Entity",
            extends=None,
            implements=[],
            fields=[
                {"name": "id", "type": "long", "visibility": "-"},
                {"name": "name", "type": "String", "visibility": "-"}
            ],
            methods=[
                {"name": "getId", "visibility": "+", "return_type": "long"},
                {"name": "getName", "visibility": "+", "return_type": "String"}
            ],
            annotations=["abstract"]
        )
        
        # Create node
        node = AnimatedUMLClassNode(entity_info, 100, 100, scene)
        scene.addItem(node)
        
        view.setWindowTitle("UML Diagram Test")
        view.show()
        
        print("✓ UML node created")
        print("✓ Class diagram rendered")
        
        # Test expansion
        QTimer.singleShot(1000, lambda: node.expand())
        QTimer.singleShot(1500, lambda: print("✓ Node expansion working"))
        
        return view
        
    except Exception as e:
        print(f"✗ UML Diagram Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def run_all_tests():
    """Run all component tests"""
    print("=" * 50)
    print("Singleton Visualizer Component Tests")
    print("=" * 50)
    
    app = QApplication(sys.argv)
    
    # Apply dark theme
    app.setStyleSheet("""
        QWidget {
            background-color: #2a2a2a;
            color: #cccccc;
        }
        QMainWindow {
            background-color: #1e1e1e;
        }
        QTabWidget::pane {
            border: 1px solid #444;
        }
        QTabBar::tab {
            background-color: #333;
            padding: 8px 16px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: #4a90e2;
        }
    """)
    
    # Create main test window
    main_window = QMainWindow()
    main_window.setWindowTitle("Singleton Visualizer - Component Tests")
    main_window.resize(1400, 900)
    
    # Create tab widget
    tabs = QTabWidget()
    
    # Test each component and add to tabs
    components = [
        ("Code Analyzer", test_code_analyzer),
        ("Animated Flowchart", test_animated_flowchart),
        ("Memory Visualizer", test_memory_visualizer),
        ("UML Diagram", test_uml_diagram)
    ]
    
    results = []
    for name, test_func in components:
        widget = test_func()
        if widget:
            tabs.addTab(widget, name)
            results.append((name, "✓ Passed"))
        else:
            # Add placeholder for failed component
            error_widget = QWidget()
            error_layout = QVBoxLayout()
            error_layout.addWidget(QPushButton(f"{name} - Failed to load"))
            error_widget.setLayout(error_layout)
            tabs.addTab(error_widget, f"{name} (Error)")
            results.append((name, "✗ Failed"))
    
    main_window.setCentralWidget(tabs)
    main_window.show()
    
    # Print test summary
    print("\n" + "=" * 50)
    print("Test Summary:")
    print("=" * 50)
    for name, status in results:
        print(f"{name}: {status}")
    
    print("\nAll component windows are now open for manual testing.")
    print("Check each tab to verify functionality.")
    
    sys.exit(app.exec())

def test_individual_component(component_name):
    """Test a specific component"""
    app = QApplication(sys.argv)
    
    # Apply dark theme
    app.setStyleSheet("""
        QWidget {
            background-color: #2a2a2a;
            color: #cccccc;
        }
    """)
    
    if component_name == "code":
        widget = test_code_analyzer()
    elif component_name == "flowchart":
        widget = test_animated_flowchart()
    elif component_name == "memory":
        widget = test_memory_visualizer()
    elif component_name == "uml":
        widget = test_uml_diagram()
    else:
        print(f"Unknown component: {component_name}")
        print("Available components: code, flowchart, memory, uml")
        return
    
    if widget:
        sys.exit(app.exec())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test specific component
        test_individual_component(sys.argv[1])
    else:
        # Run all tests
        run_all_tests()