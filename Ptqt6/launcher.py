#!/usr/bin/env python3
"""
Simple launcher for Singleton Pattern Visualizer Suite
Opens a GUI with buttons to launch each visualizer
"""

import sys
import os
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

class SingletonLauncher:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Singleton Pattern Visualizer Launcher")
        self.root.geometry("600x500")
        
        # Set dark theme colors
        self.bg_color = "#1a1a1a"
        self.fg_color = "#ffffff"
        self.button_bg = "#ff6600"
        self.button_hover = "#ff8833"
        
        self.root.configure(bg=self.bg_color)
        
        # Get base directory
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.dirname(self.base_dir)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="SINGLETON PATTERN VISUALIZER",
            font=("Arial", 24, "bold"),
            fg=self.button_bg,
            bg=self.bg_color
        )
        title.pack(pady=20)
        
        subtitle = tk.Label(
            self.root,
            text="Choose a visualizer to launch:",
            font=("Arial", 14),
            fg=self.fg_color,
            bg=self.bg_color
        )
        subtitle.pack(pady=10)
        
        # Create buttons
        buttons_data = [
            ("Animated Flowchart", "View step-by-step singleton pattern animations", self.launch_flowchart),
            ("Architecture Explorer", "Explore complete Entity hierarchy and GameService", self.launch_architecture),
            ("Code Analyzer", "Deep dive into Java implementation with analysis", self.launch_analyzer),
            ("Java Runtime", "Run the actual Singleton GameService implementation", self.launch_java),
            ("Open HTML Launcher", "Open the advanced HTML launcher interface", self.open_html_launcher)
        ]
        
        for btn_text, desc_text, command in buttons_data:
            frame = tk.Frame(self.root, bg=self.bg_color)
            frame.pack(pady=10, padx=40, fill="x")
            
            btn = tk.Button(
                frame,
                text=btn_text,
                command=command,
                font=("Arial", 12, "bold"),
                fg="white",
                bg=self.button_bg,
                activebackground=self.button_hover,
                activeforeground="white",
                relief="flat",
                height=2,
                cursor="hand2"
            )
            btn.pack(fill="x")
            
            desc = tk.Label(
                frame,
                text=desc_text,
                font=("Arial", 10),
                fg="#cccccc",
                bg=self.bg_color
            )
            desc.pack(pady=(5, 0))
    
    def launch_flowchart(self):
        """Launch animated flowchart visualizer"""
        try:
            script_path = os.path.join(self.base_dir, 'singleton_flowchart_complete.py')
            subprocess.Popen([sys.executable, script_path])
            self.show_status("Launched Animated Flowchart!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch flowchart: {e}")
    
    def launch_architecture(self):
        """Launch architecture explorer"""
        try:
            # For now, using the same flowchart app
            script_path = os.path.join(self.base_dir, 'singleton_flowchart_complete.py')
            subprocess.Popen([sys.executable, script_path])
            self.show_status("Launched Architecture Explorer!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch architecture: {e}")
    
    def launch_analyzer(self):
        """Launch code analyzer"""
        try:
            script_path = os.path.join(self.base_dir, 'singleton_visualizer_integrated.py')
            subprocess.Popen([sys.executable, script_path])
            self.show_status("Launched Code Analyzer!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch analyzer: {e}")
    
    def launch_java(self):
        """Launch Java application in terminal"""
        try:
            jar_path = os.path.join(self.parent_dir, 'GamingRoom.jar')
            
            if sys.platform == 'darwin':  # macOS
                apple_script = f'''
                tell application "Terminal"
                    activate
                    do script "cd '{self.parent_dir}' && java -jar GamingRoom.jar; echo; echo 'Press any key to close...'; read -n 1"
                end tell
                '''
                subprocess.Popen(['osascript', '-e', apple_script])
            elif sys.platform == 'win32':  # Windows
                subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', f'cd /d "{self.parent_dir}" && java -jar GamingRoom.jar && pause'])
            else:  # Linux
                subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'cd "{self.parent_dir}" && java -jar GamingRoom.jar; read -p "Press any key to close..."'])
            
            self.show_status("Launched Java Runtime in Terminal!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Java app: {e}")
    
    def open_html_launcher(self):
        """Open the HTML launcher in browser"""
        try:
            html_path = os.path.join(self.base_dir, 'launcher.html')
            webbrowser.open(f'file://{html_path}')
            self.show_status("Opened HTML Launcher in Browser!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open HTML launcher: {e}")
    
    def show_status(self, message):
        """Show status message"""
        status_label = tk.Label(
            self.root,
            text=message,
            font=("Arial", 10),
            fg="#00ff00",
            bg=self.bg_color
        )
        status_label.pack(side="bottom", pady=10)
        
        # Remove after 3 seconds
        self.root.after(3000, status_label.destroy)
    
    def run(self):
        """Run the launcher"""
        self.root.mainloop()

if __name__ == '__main__':
    launcher = SingletonLauncher()
    launcher.run()