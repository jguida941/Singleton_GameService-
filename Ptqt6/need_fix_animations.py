import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                           QGraphicsScene, QGraphicsView, QGraphicsRectItem,
                           QGraphicsTextItem, QGraphicsLineItem, QGraphicsEllipseItem,
                           QPushButton, QSlider, QLabel, QCheckBox, QGroupBox,
                           QGraphicsPolygonItem, QGraphicsPathItem)
from PyQt6.QtGui import (QBrush, QColor, QPen, QFont, QPainter, QPolygonF,
                       QPainterPath, QLinearGradient, QRadialGradient)
from PyQt6.QtCore import (QRectF, Qt, QPointF, QTimer, pyqtSignal,
                        QSequentialAnimationGroup, QParallelAnimationGroup,
                        pyqtProperty, QLineF)

class FlowchartNode(QGraphicsRectItem):
    """Enhanced flowchart node with animations"""
    def __init__(self, text, x, y, width=200, height=60, node_type="process"):
        super().__init__(QRectF(x, y, width, height))
        
        self.node_type = node_type
        self.is_active = False
        
        # Set style based on node type
        self.set_node_style(node_type)
        
        # Add text
        self.text_item = QGraphicsTextItem(text, self)
        self.text_item.setDefaultTextColor(QColor("white"))
        font = QFont("Arial", 10)
        self.text_item.setFont(font)
        
        # Center text
        text_rect = self.text_item.boundingRect()
        text_x = x + (width - text_rect.width()) / 2
        text_y = y + (height - text_rect.height()) / 2
        self.text_item.setPos(text_x, text_y)
        
        # For animation
        self._glow_effect = None
        
    def set_node_style(self, node_type):
        """Set visual style based on node type"""
        if node_type == "start":
            self.setBrush(QBrush(QColor("#2ecc71")))
            self.setPen(QPen(QColor("#27ae60"), 2))
        elif node_type == "decision":
            self.setBrush(QBrush(QColor("#3498db")))
            self.setPen(QPen(QColor("#2980b9"), 2))
        elif node_type == "process":
            self.setBrush(QBrush(QColor("#34495e")))
            self.setPen(QPen(QColor("#2c3e50"), 2))
        elif node_type == "singleton":
            self.setBrush(QBrush(QColor("#e74c3c")))
            self.setPen(QPen(QColor("#c0392b"), 2))
        elif node_type == "end":
            self.setBrush(QBrush(QColor("#95a5a6")))
            self.setPen(QPen(QColor("#7f8c8d"), 2))
    
    def activate(self):
        """Activate node with glow effect"""
        self.is_active = True
        # Create glow effect
        pen = QPen(QColor("#fff"), 4)
        pen.setStyle(Qt.PenStyle.DashLine)
        self.setPen(pen)
        
    def deactivate(self):
        """Deactivate node"""
        self.is_active = False
        self.set_node_style(self.node_type)

class FlowchartArrow(QGraphicsLineItem):
    """Animated arrow between nodes"""
    def __init__(self, start_node, end_node, label="", arrow_type="straight"):
        super().__init__()
        
        self.start_node = start_node
        self.end_node = end_node
        self.label = label
        self.arrow_type = arrow_type
        
        # Set line style
        self.setPen(QPen(QColor("#666"), 2))
        
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

class AnimatedFlowchartWidget(QWidget):
    """Widget containing the animated flowchart"""
    def __init__(self):
        super().__init__()
        self.nodes = {}
        self.arrows = []
        self.animation_group = None
        self.current_step = 0
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Control panel
        controls_group = QGroupBox("Animation Controls")
        controls_layout = QHBoxLayout()
        
        self.play_btn = QPushButton("Play Full Animation")
        self.play_btn.clicked.connect(self.play_full_animation)
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
        self.scene.setSceneRect(0, 0, 1000, 800)
        
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        layout.addWidget(self.view)
        
        # Status label
        self.status_label = QLabel("Ready to animate singleton pattern flow")
        self.status_label.setStyleSheet("font-size: 12px; color: #888;")
        layout.addWidget(self.status_label)
        
        self.setLayout(layout)
        
        # Create the flowchart
        self.create_flowchart()
        
    def create_flowchart(self):
        """Create the complete singleton pattern flowchart"""
        # Main flow nodes
        self.nodes['start'] = FlowchartNode("Program Start", 400, 20, node_type="start")
        self.nodes['main'] = FlowchartNode("ProgramDriver.main()", 350, 100, node_type="process")
        self.nodes['get_instance'] = FlowchartNode("GameService.getInstance()", 350, 180, node_type="singleton")
        self.nodes['check_null'] = FlowchartNode("instance == null?", 350, 260, node_type="decision")
        self.nodes['create_new'] = FlowchartNode("Create new GameService()", 150, 360, node_type="singleton")
        self.nodes['return_existing'] = FlowchartNode("Return existing instance", 550, 360, node_type="process")
        self.nodes['instance_ready'] = FlowchartNode("Instance Ready", 350, 460, node_type="process")
        
        # Singleton test flow nodes
        self.nodes['test_start'] = FlowchartNode("SingletonTester", 750, 100, node_type="process")
        self.nodes['get_service1'] = FlowchartNode("service1 = getInstance()", 750, 180, node_type="singleton")
        self.nodes['get_service2'] = FlowchartNode("service2 = getInstance()", 750, 260, node_type="singleton")
        self.nodes['compare'] = FlowchartNode("Compare hashCodes", 750, 340, node_type="process")
        self.nodes['verify'] = FlowchartNode("Verify same instance", 750, 420, node_type="process")
        self.nodes['result'] = FlowchartNode("Display: Same instance!", 750, 500, node_type="end")
        
        # Add all nodes to scene
        for node in self.nodes.values():
            self.scene.addItem(node)
        
        # Create arrows
        self.arrows.append(FlowchartArrow(self.nodes['start'], self.nodes['main']))
        self.arrows.append(FlowchartArrow(self.nodes['main'], self.nodes['get_instance']))
        self.arrows.append(FlowchartArrow(self.nodes['get_instance'], self.nodes['check_null']))
        self.arrows.append(FlowchartArrow(self.nodes['check_null'], self.nodes['create_new'], "Yes"))
        self.arrows.append(FlowchartArrow(self.nodes['check_null'], self.nodes['return_existing'], "No"))
        self.arrows.append(FlowchartArrow(self.nodes['create_new'], self.nodes['instance_ready']))
        self.arrows.append(FlowchartArrow(self.nodes['return_existing'], self.nodes['instance_ready']))
        
        # Test flow arrows
        self.arrows.append(FlowchartArrow(self.nodes['test_start'], self.nodes['get_service1']))
        self.arrows.append(FlowchartArrow(self.nodes['get_service1'], self.nodes['get_service2']))
        self.arrows.append(FlowchartArrow(self.nodes['get_service2'], self.nodes['compare']))
        self.arrows.append(FlowchartArrow(self.nodes['compare'], self.nodes['verify']))
        self.arrows.append(FlowchartArrow(self.nodes['verify'], self.nodes['result']))
        
        # Add arrows to scene
        for arrow in self.arrows:
            self.scene.addItem(arrow)
        
        # Add explanatory text
        explanation = QGraphicsTextItem(
            "This flowchart demonstrates how the Singleton pattern ensures only one instance of GameService exists.\n"
            "The left flow shows initial creation, while the right flow proves both references point to the same instance."
        )
        explanation.setPos(50, 600)
        explanation.setDefaultTextColor(QColor("#888"))
        explanation.setFont(QFont("Arial", 10))
        self.scene.addItem(explanation)
    
    def play_full_animation(self):
        """Play the complete animation sequence"""
        self.reset_animation()
        
        # Define animation sequence
        self.animation_sequence = [
            ("start", "Starting program execution"),
            ("main", "Entering main method"),
            ("get_instance", "Calling getInstance() - first time"),
            ("check_null", "Checking if instance exists"),
            ("create_new", "Instance is null, creating new GameService"),
            ("instance_ready", "Singleton instance created and ready"),
            ("test_start", "Starting singleton test"),
            ("get_service1", "Getting first reference to GameService"),
            ("check_null", "Instance already exists"),
            ("return_existing", "Returning existing instance"),
            ("get_service2", "Getting second reference to GameService"),
            ("compare", "Comparing hashCodes of both references"),
            ("verify", "Verifying both references point to same object"),
            ("result", "Test complete: Singleton verified!")
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
                
                # Animate arrow if applicable
                if self.current_step > 0:
                    self.animate_arrow_for_step(self.current_step)
            
            self.current_step += 1
        else:
            # Animation complete
            self.animation_timer.stop()
            self.play_btn.setEnabled(True)
            self.status_label.setText("Animation complete!")
            
            if self.loop_check.isChecked():
                QTimer.singleShot(1000, self.play_full_animation)
    
    def animate_arrow_for_step(self, step):
        """Animate the appropriate arrow for the current step"""
        # Map steps to arrow indices
        arrow_map = {
            1: 0,  # start -> main
            2: 1,  # main -> getInstance
            3: 2,  # getInstance -> check_null
            4: 3,  # check_null -> create_new
            5: 5,  # create_new -> instance_ready
            6: 7,  # test_start -> get_service1
            7: 2,  # getInstance -> check_null (again)
            8: 4,  # check_null -> return_existing
            9: 8,  # get_service1 -> get_service2
            10: 9, # get_service2 -> compare
            11: 10, # compare -> verify
            12: 11  # verify -> result
        }
        
        if step in arrow_map:
            arrow_index = arrow_map[step]
            if arrow_index < len(self.arrows):
                self.arrows[arrow_index].animate_flow()
    
    def next_step(self):
        """Execute next step manually"""
        if not hasattr(self, 'animation_sequence'):
            self.animation_sequence = [
                ("start", "Starting program execution"),
                ("main", "Entering main method"),
                # ... (same as in play_full_animation)
            ]
            self.current_step = 0
        
        if self.current_step < len(self.animation_sequence):
            node_name, description = self.animation_sequence[self.current_step]
            
            if node_name in self.nodes:
                self.nodes[node_name].activate()
                self.status_label.setText(f"Step {self.current_step + 1}: {description}")
                
                if self.current_step > 0:
                    self.animate_arrow_for_step(self.current_step)
            
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
        self.status_label.setText("Ready to animate singleton pattern flow")

def test_animated_flowchart():
    """Test the animated flowchart independently"""
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
    """)
    
    # Create and show widget
    flowchart = AnimatedFlowchartWidget()
    flowchart.setWindowTitle("Animated Flowchart - Singleton Pattern")
    flowchart.resize(1200, 800)
    flowchart.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    test_animated_flowchart()