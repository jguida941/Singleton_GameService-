import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                           QGraphicsScene, QGraphicsView, QGraphicsRectItem,
                           QGraphicsTextItem, QGraphicsLineItem, QGraphicsEllipseItem,
                           QPushButton, QSlider, QLabel, QCheckBox, QGroupBox,
                           QGraphicsPolygonItem, QGraphicsPathItem, QComboBox)
from PyQt6.QtGui import (QBrush, QColor, QPen, QFont, QPainter, QPolygonF,
                       QPainterPath, QLinearGradient, QRadialGradient)
from PyQt6.QtCore import (QRectF, Qt, QPointF, QTimer, QLineF)

class FlowchartNode(QGraphicsRectItem):
    """Enhanced flowchart node with animations and different shapes"""
    def __init__(self, text, x, y, width=200, height=60, node_type="process", shape="rect"):
        super().__init__(QRectF(x, y, width, height))
        
        self.node_type = node_type
        self.shape = shape
        self.is_active = False
        self.original_brush = None
        self.original_pen = None
        
        # Set style based on node type
        self.set_node_style(node_type)
        
        # Add text
        self.text_item = QGraphicsTextItem(text, self)
        self.text_item.setDefaultTextColor(QColor("white"))
        font = QFont("Arial", 9 if len(text) > 30 else 10)
        self.text_item.setFont(font)
        
        # Center text
        text_rect = self.text_item.boundingRect()
        text_x = x + (width - text_rect.width()) / 2
        text_y = y + (height - text_rect.height()) / 2
        self.text_item.setPos(text_x, text_y)
        
    def set_node_style(self, node_type):
        """Set visual style based on node type"""
        if node_type == "start":
            brush = QBrush(QColor("#2ecc71"))
            pen = QPen(QColor("#27ae60"), 2)
        elif node_type == "decision":
            brush = QBrush(QColor("#3498db"))
            pen = QPen(QColor("#2980b9"), 2)
        elif node_type == "process":
            brush = QBrush(QColor("#34495e"))
            pen = QPen(QColor("#2c3e50"), 2)
        elif node_type == "singleton":
            brush = QBrush(QColor("#e74c3c"))
            pen = QPen(QColor("#c0392b"), 2)
        elif node_type == "entity":
            brush = QBrush(QColor("#9b59b6"))
            pen = QPen(QColor("#8e44ad"), 2)
        elif node_type == "collection":
            brush = QBrush(QColor("#f39c12"))
            pen = QPen(QColor("#d68910"), 2)
        elif node_type == "end":
            brush = QBrush(QColor("#95a5a6"))
            pen = QPen(QColor("#7f8c8d"), 2)
        else:
            brush = QBrush(QColor("#34495e"))
            pen = QPen(QColor("#2c3e50"), 2)
            
        self.setBrush(brush)
        self.setPen(pen)
        self.original_brush = brush
        self.original_pen = pen
    
    def activate(self):
        """Activate node with glow effect"""
        self.is_active = True
        # Create glow effect
        glow_color = QColor(self.original_brush.color())
        glow_color.setAlpha(200)
        self.setBrush(QBrush(glow_color))
        pen = QPen(QColor("#fff"), 4)
        pen.setStyle(Qt.PenStyle.DashLine)
        self.setPen(pen)
        
    def deactivate(self):
        """Deactivate node"""
        self.is_active = False
        self.setBrush(self.original_brush)
        self.setPen(self.original_pen)

class FlowchartArrow(QGraphicsLineItem):
    """Animated arrow between nodes"""
    def __init__(self, start_node, end_node, label="", arrow_type="straight", style="solid"):
        super().__init__()
        
        self.start_node = start_node
        self.end_node = end_node
        self.label = label
        self.arrow_type = arrow_type
        
        # Set line style
        pen = QPen(QColor("#666"), 2)
        if style == "dashed":
            pen.setStyle(Qt.PenStyle.DashLine)
        elif style == "dotted":
            pen.setStyle(Qt.PenStyle.DotLine)
        self.setPen(pen)
        
        # Create arrow head
        self.arrow_head = QGraphicsPolygonItem(self)
        self.arrow_head.setBrush(QBrush(QColor("#666")))
        
        # Create label if provided
        if label:
            self.label_item = QGraphicsTextItem(label, self)
            self.label_item.setDefaultTextColor(QColor("#888"))
            self.label_item.setFont(QFont("Arial", 9))
        
        self.update_position()
        
    def update_position(self):
        """Update arrow position based on connected nodes"""
        start_rect = self.start_node.rect()
        end_rect = self.end_node.rect()
        
        # Calculate connection points
        start_point = QPointF(
            start_rect.x() + start_rect.width() / 2,
            start_rect.y() + start_rect.height()
        )
        end_point = QPointF(
            end_rect.x() + end_rect.width() / 2,
            end_rect.y()
        )
        
        # Set line
        self.setLine(QLineF(start_point, end_point))
        
        # Update arrow head
        self.update_arrow_head()
        
        # Update label position
        if hasattr(self, 'label_item'):
            mid_point = QPointF(
                (start_point.x() + end_point.x()) / 2,
                (start_point.y() + end_point.y()) / 2
            )
            self.label_item.setPos(mid_point.x() + 10, mid_point.y() - 10)
    
    def update_arrow_head(self):
        """Update arrow head polygon"""
        line = self.line()
        angle = line.angle()
        
        # Arrow head size
        arrow_length = 12
        arrow_degrees = 25
        
        # Calculate arrow points
        end_point = line.p2()
        
        # Convert angle to radians
        import math
        angle_rad = math.radians(angle)
        
        # Calculate arrow wings
        wing1_angle = math.radians(angle - 180 - arrow_degrees)
        wing2_angle = math.radians(angle - 180 + arrow_degrees)
        
        point1 = end_point
        point2 = QPointF(
            end_point.x() + arrow_length * math.cos(wing1_angle),
            end_point.y() + arrow_length * math.sin(wing1_angle)
        )
        point3 = QPointF(
            end_point.x() + arrow_length * math.cos(wing2_angle),
            end_point.y() + arrow_length * math.sin(wing2_angle)
        )
        
        # Create arrow polygon
        arrow_polygon = QPolygonF([point1, point2, point3])
        self.arrow_head.setPolygon(arrow_polygon)
    
    def animate_flow(self):
        """Animate data flow along the arrow"""
        # Create a small circle to represent data flow
        flow_item = QGraphicsEllipseItem(-5, -5, 10, 10)
        flow_item.setBrush(QBrush(QColor("#f39c12")))
        flow_item.setPen(QPen(Qt.PenStyle.NoPen))
        
        # Add to scene
        if self.scene():
            self.scene().addItem(flow_item)
            
            # Animate along the line
            line = self.line()
            
            # Create a timer to move the item along the path
            steps = 20
            current_step = 0
            
            def move_flow():
                nonlocal current_step
                if current_step <= steps:
                    t = current_step / steps
                    x = line.p1().x() + t * (line.p2().x() - line.p1().x())
                    y = line.p1().y() + t * (line.p2().y() - line.p1().y())
                    flow_item.setPos(x - 5, y - 5)
                    current_step += 1
                else:
                    timer.stop()
                    if self.scene():
                        self.scene().removeItem(flow_item)
            
            timer = QTimer()
            timer.timeout.connect(move_flow)
            timer.start(50)  # 50ms interval for smooth animation

class CompleteFlowchartWidget(QWidget):
    """Widget containing the complete singleton pattern flowchart with Entity hierarchy"""
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.arrows = []
        self.animation_group = None
        self.current_step = 0
        self.animation_mode = "full"  # full, singleton, entity
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Control panel
        controls_group = QGroupBox("Animation Controls")
        controls_layout = QHBoxLayout()
        
        # Animation mode selector
        controls_layout.addWidget(QLabel("Mode:"))
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Full Program Flow", "Singleton Pattern Only", "Entity Hierarchy Only"])
        self.mode_combo.currentTextChanged.connect(self.change_animation_mode)
        controls_layout.addWidget(self.mode_combo)
        
        self.play_btn = QPushButton("Play Animation")
        self.play_btn.clicked.connect(self.play_animation)
        controls_layout.addWidget(self.play_btn)
        
        self.step_btn = QPushButton("Next Step")
        self.step_btn.clicked.connect(self.next_step)
        controls_layout.addWidget(self.step_btn)
        
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_animation)
        controls_layout.addWidget(self.reset_btn)
        
        controls_layout.addWidget(QLabel("Speed:"))
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(10)
        self.speed_slider.setValue(5)
        self.speed_slider.setMaximumWidth(200)
        controls_layout.addWidget(self.speed_slider)
        
        self.loop_check = QCheckBox("Loop Animation")
        controls_layout.addWidget(self.loop_check)
        
        controls_layout.addStretch()
        controls_group.setLayout(controls_layout)
        layout.addWidget(controls_group)
        
        # Create scene and view
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 1500, 1200)
        
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        layout.addWidget(self.view)
        
        # Status label
        self.status_label = QLabel("Ready to animate complete GameService architecture")
        self.status_label.setStyleSheet("font-size: 12px; color: #888;")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
        # Create the complete flowchart
        self.create_complete_flowchart()
        
    def create_complete_flowchart(self):
        """Create the complete flowchart with Entity hierarchy and Singleton pattern"""
        # Clear existing items
        self.scene.clear()
        self.nodes.clear()
        self.arrows.clear()
        
        # Entity hierarchy nodes (left side) - increased vertical spacing
        self.nodes['entity_class'] = FlowchartNode("Entity (Abstract)\nid: long\nname: String", 50, 50, 200, 80, node_type="entity")
        self.nodes['game_class'] = FlowchartNode("Game extends Entity\nteams: List<Team>", 50, 200, 200, 80, node_type="entity")
        self.nodes['team_class'] = FlowchartNode("Team extends Entity\nplayers: List<Player>", 50, 350, 200, 80, node_type="entity")
        self.nodes['player_class'] = FlowchartNode("Player extends Entity", 50, 500, 200, 80, node_type="entity")
        
        # Main program flow nodes (center) - adjusted positions
        self.nodes['start'] = FlowchartNode("Program Start", 550, 50, node_type="start")
        self.nodes['main'] = FlowchartNode("ProgramDriver.main()", 500, 150, node_type="process")
        self.nodes['get_instance'] = FlowchartNode("GameService.getInstance()", 500, 250, node_type="singleton")
        self.nodes['check_null'] = FlowchartNode("instance == null?", 500, 350, node_type="decision")
        self.nodes['create_new'] = FlowchartNode("Create new GameService()", 300, 470, node_type="singleton")
        self.nodes['return_existing'] = FlowchartNode("Return existing instance", 700, 470, node_type="process")
        self.nodes['instance_ready'] = FlowchartNode("GameService Ready", 500, 590, node_type="process")
        
        # GameService operations (right side) - better spacing
        self.nodes['add_game'] = FlowchartNode("addGame(name)", 1000, 150, 180, 60, node_type="collection")
        self.nodes['check_game'] = FlowchartNode("Game exists?", 1000, 250, 180, 60, node_type="decision")
        self.nodes['create_game'] = FlowchartNode("new Game(id, name)", 850, 350, 180, 60, node_type="entity")
        self.nodes['return_game'] = FlowchartNode("Return existing", 1150, 350, 180, 60, node_type="process")
        self.nodes['add_team'] = FlowchartNode("game.addTeam(name)", 1000, 450, 180, 60, node_type="collection")
        self.nodes['add_player'] = FlowchartNode("team.addPlayer(name)", 1000, 550, 180, 60, node_type="collection")
        
        # SingletonTester flow (bottom) - adjusted spacing
        self.nodes['test_start'] = FlowchartNode("SingletonTester", 500, 700, node_type="process")
        self.nodes['get_service1'] = FlowchartNode("service1 = getInstance()", 300, 800, node_type="singleton")
        self.nodes['get_service2'] = FlowchartNode("service2 = getInstance()", 700, 800, node_type="singleton")
        self.nodes['compare'] = FlowchartNode("Compare instances", 500, 900, node_type="process")
        self.nodes['verify'] = FlowchartNode("Verify: Same instance!", 500, 1000, node_type="end")
        
        # Lists display nodes - moved to avoid overlap
        self.nodes['games_list'] = FlowchartNode("games: List<Game>", 1250, 50, 160, 60, node_type="collection")
        self.nodes['id_counters'] = FlowchartNode("ID Counters:\ngameId++\nteamId++\nplayerId++", 1250, 150, 160, 90, node_type="singleton")
        
        # Add all nodes to scene
        for node in self.nodes.values():
            self.scene.addItem(node)
        
        # Create arrows for Entity hierarchy
        self.arrows.append(FlowchartArrow(self.nodes['entity_class'], self.nodes['game_class'], "inherits", style="dashed"))
        self.arrows.append(FlowchartArrow(self.nodes['entity_class'], self.nodes['team_class'], "inherits", style="dashed"))
        self.arrows.append(FlowchartArrow(self.nodes['entity_class'], self.nodes['player_class'], "inherits", style="dashed"))
        self.arrows.append(FlowchartArrow(self.nodes['game_class'], self.nodes['team_class'], "contains"))
        self.arrows.append(FlowchartArrow(self.nodes['team_class'], self.nodes['player_class'], "contains"))
        
        # Main flow arrows
        self.arrows.append(FlowchartArrow(self.nodes['start'], self.nodes['main']))
        self.arrows.append(FlowchartArrow(self.nodes['main'], self.nodes['get_instance']))
        self.arrows.append(FlowchartArrow(self.nodes['get_instance'], self.nodes['check_null']))
        self.arrows.append(FlowchartArrow(self.nodes['check_null'], self.nodes['create_new'], "Yes"))
        self.arrows.append(FlowchartArrow(self.nodes['check_null'], self.nodes['return_existing'], "No"))
        self.arrows.append(FlowchartArrow(self.nodes['create_new'], self.nodes['instance_ready']))
        self.arrows.append(FlowchartArrow(self.nodes['return_existing'], self.nodes['instance_ready']))
        
        # GameService operations arrows
        self.arrows.append(FlowchartArrow(self.nodes['instance_ready'], self.nodes['add_game']))
        self.arrows.append(FlowchartArrow(self.nodes['add_game'], self.nodes['check_game']))
        self.arrows.append(FlowchartArrow(self.nodes['check_game'], self.nodes['create_game'], "No"))
        self.arrows.append(FlowchartArrow(self.nodes['check_game'], self.nodes['return_game'], "Yes"))
        self.arrows.append(FlowchartArrow(self.nodes['create_game'], self.nodes['add_team']))
        self.arrows.append(FlowchartArrow(self.nodes['return_game'], self.nodes['add_team']))
        self.arrows.append(FlowchartArrow(self.nodes['add_team'], self.nodes['add_player']))
        
        # Test flow arrows
        self.arrows.append(FlowchartArrow(self.nodes['instance_ready'], self.nodes['test_start']))
        self.arrows.append(FlowchartArrow(self.nodes['test_start'], self.nodes['get_service1']))
        self.arrows.append(FlowchartArrow(self.nodes['test_start'], self.nodes['get_service2']))
        self.arrows.append(FlowchartArrow(self.nodes['get_service1'], self.nodes['compare']))
        self.arrows.append(FlowchartArrow(self.nodes['get_service2'], self.nodes['compare']))
        self.arrows.append(FlowchartArrow(self.nodes['compare'], self.nodes['verify']))
        
        # GameService to lists arrows
        self.arrows.append(FlowchartArrow(self.nodes['create_game'], self.nodes['games_list'], "stores", style="dotted"))
        self.arrows.append(FlowchartArrow(self.nodes['get_instance'], self.nodes['id_counters'], "manages", style="dotted"))
        
        # Add arrows to scene
        for arrow in self.arrows:
            self.scene.addItem(arrow)
        
        # Add explanatory text
        explanation = QGraphicsTextItem(
            "Complete GameService Architecture:\n"
            "• Entity hierarchy provides base structure for all game objects\n"
            "• GameService singleton manages all game instances and ensures unique IDs\n"
            "• Each Game contains Teams, each Team contains Players\n"
            "• All IDs are centrally managed to prevent duplicates"
        )
        explanation.setPos(50, 1100)
        explanation.setDefaultTextColor(QColor("#888"))
        explanation.setFont(QFont("Arial", 10))
        self.scene.addItem(explanation)
    
    def change_animation_mode(self, mode_text):
        """Change animation mode based on selection"""
        if "Full" in mode_text:
            self.animation_mode = "full"
        elif "Singleton" in mode_text:
            self.animation_mode = "singleton"
        elif "Entity" in mode_text:
            self.animation_mode = "entity"
        self.reset_animation()
    
    def play_animation(self):
        """Play animation based on selected mode"""
        self.reset_animation()
        
        # Define animation sequences for different modes
        if self.animation_mode == "full":
            self.animation_sequence = [
                ("start", "Starting program execution"),
                ("main", "Entering ProgramDriver.main()"),
                ("entity_class", "Entity abstract class defines base structure"),
                ("game_class", "Game extends Entity with team list"),
                ("team_class", "Team extends Entity with player list"),
                ("player_class", "Player extends Entity"),
                ("get_instance", "Calling GameService.getInstance()"),
                ("check_null", "Checking if singleton instance exists"),
                ("create_new", "Creating new GameService instance"),
                ("id_counters", "Initializing ID counters"),
                ("instance_ready", "GameService singleton ready"),
                ("add_game", "Adding a new game"),
                ("check_game", "Checking if game already exists"),
                ("create_game", "Creating new Game with unique ID"),
                ("games_list", "Storing game in games list"),
                ("add_team", "Adding team to game"),
                ("add_player", "Adding player to team"),
                ("test_start", "Running singleton verification test"),
                ("get_service1", "Getting first GameService reference"),
                ("get_service2", "Getting second GameService reference"),
                ("compare", "Comparing both references"),
                ("verify", "Confirmed: Both references point to same instance!")
            ]
        elif self.animation_mode == "singleton":
            self.animation_sequence = [
                ("start", "Starting program execution"),
                ("main", "Entering main method"),
                ("get_instance", "Calling getInstance() - first time"),
                ("check_null", "Checking if instance exists"),
                ("create_new", "Instance is null, creating new GameService"),
                ("instance_ready", "Singleton instance created"),
                ("test_start", "Starting singleton test"),
                ("get_service1", "Getting first reference"),
                ("check_null", "Instance already exists"),
                ("return_existing", "Returning existing instance"),
                ("get_service2", "Getting second reference"),
                ("compare", "Comparing references"),
                ("verify", "Test complete: Singleton verified!")
            ]
        elif self.animation_mode == "entity":
            self.animation_sequence = [
                ("entity_class", "Entity abstract base class"),
                ("game_class", "Game extends Entity"),
                ("team_class", "Team extends Entity"),
                ("player_class", "Player extends Entity"),
                ("add_game", "Creating a game instance"),
                ("create_game", "New Game with unique ID from GameService"),
                ("add_team", "Adding teams to game"),
                ("add_player", "Adding players to team"),
                ("games_list", "All games stored in GameService")
            ]
        
        # Create timer for sequential animation
        self.animation_timer = QTimer()
        self.animation_timer.timeout.connect(self.animate_next_step)
        
        # Calculate interval based on speed slider
        interval = 2000 // self.speed_slider.value()
        self.animation_timer.start(interval)
        
        self.current_step = 0
        self.play_btn.setEnabled(False)
        
    def animate_next_step(self):
        """Animate the next step in sequence"""
        if self.current_step < len(self.animation_sequence):
            node_name, description = self.animation_sequence[self.current_step]
            
            # Activate node
            if node_name in self.nodes:
                self.nodes[node_name].activate()
                self.status_label.setText(f"Step {self.current_step + 1}: {description}")
                
                # Animate arrows if applicable
                if self.current_step > 0:
                    self.animate_arrows_for_step(self.current_step)
            
            self.current_step += 1
        else:
            # Animation complete
            self.animation_timer.stop()
            self.play_btn.setEnabled(True)
            self.status_label.setText("Animation complete!")
            
            if self.loop_check.isChecked():
                QTimer.singleShot(1000, self.play_animation)
    
    def animate_arrows_for_step(self, step):
        """Animate relevant arrows for the current step"""
        # This would need more complex mapping based on the animation mode
        # For now, we'll animate arrows connected to activated nodes
        pass
    
    def next_step(self):
        """Execute next step manually"""
        if not hasattr(self, 'animation_sequence'):
            self.play_animation()
            self.animation_timer.stop()
            return
        
        if self.current_step < len(self.animation_sequence):
            node_name, description = self.animation_sequence[self.current_step]
            
            if node_name in self.nodes:
                self.nodes[node_name].activate()
                self.status_label.setText(f"Step {self.current_step + 1}: {description}")
            
            self.current_step += 1
        else:
            self.status_label.setText("Animation complete - click Reset to start over")
    
    def reset_animation(self):
        """Reset all nodes and animations"""
        # Deactivate all nodes
        for node in self.nodes.values():
            node.deactivate()
        
        # Stop any running timers
        if hasattr(self, 'animation_timer'):
            self.animation_timer.stop()
        
        self.current_step = 0
        self.play_btn.setEnabled(True)
        self.status_label.setText("Ready to animate complete GameService architecture")

def main():
    """Run the complete flowchart application"""
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
        QGraphicsView {
            background-color: #1e1e1e;
            border: 1px solid #444;
        }
        QPushButton {
            background-color: #4a90e2;
            border: none;
            padding: 6px 12px;
            border-radius: 3px;
        }
        QPushButton:hover {
            background-color: #5ba0f2;
        }
        QPushButton:disabled {
            background-color: #555;
        }
        QSlider::groove:horizontal {
            height: 6px;
            background: #444;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #4a90e2;
            width: 14px;
            height: 14px;
            margin: -4px 0;
            border-radius: 7px;
        }
        QComboBox {
            background-color: #3a3a3a;
            border: 1px solid #555;
            padding: 4px;
            border-radius: 3px;
        }
        QComboBox::drop-down {
            border: none;
        }
        QComboBox::down-arrow {
            image: none;
            border-left: 4px solid transparent;
            border-right: 4px solid transparent;
            border-top: 6px solid #888;
            width: 0;
            height: 0;
            margin-right: 4px;
        }
    """)
    
    # Create and show widget
    flowchart = CompleteFlowchartWidget()
    flowchart.setWindowTitle("Complete GameService Architecture - Singleton Pattern with Entity Hierarchy")
    flowchart.resize(1500, 1100)
    flowchart.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()