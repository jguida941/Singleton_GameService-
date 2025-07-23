#!/usr/bin/env python3
"""
Backend launcher for Singleton Pattern Visualizer Suite
Handles launching of PyQt6 applications and Java JAR
"""

import os
import sys
import subprocess
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import webbrowser
import time

class LauncherHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler for launching applications"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/launch':
            # Get the app to launch from query parameters
            params = parse_qs(parsed_path.query)
            app = params.get('app', [''])[0]
            
            # Launch the appropriate application
            success = self.launch_app(app)
            
            # Send response
            self.send_response(200 if success else 500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'success': success,
                'app': app,
                'message': f'{"Launched" if success else "Failed to launch"} {app}'
            }
            self.wfile.write(json.dumps(response).encode())
            
        else:
            # Serve static files
            super().do_GET()
    
    def launch_app(self, app_name):
        """Launch the specified application"""
        try:
            # Get the directory where this script is located
            base_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(base_dir)
            
            if app_name == 'flowchart':
                # Launch animated flowchart
                subprocess.Popen([sys.executable, os.path.join(base_dir, 'singleton_flowchart_complete.py')])
                return True
                
            elif app_name == 'architecture':
                # Launch architecture explorer (same app, different mode could be added)
                subprocess.Popen([sys.executable, os.path.join(base_dir, 'singleton_flowchart_complete.py')])
                return True
                
            elif app_name == 'analyzer':
                # Launch code analyzer
                subprocess.Popen([sys.executable, os.path.join(base_dir, 'singleton_visualizer_integrated.py')])
                return True
                
            elif app_name == 'java':
                # Launch Java application in terminal
                jar_path = os.path.join(parent_dir, 'GamingRoom.jar')
                if sys.platform == 'darwin':  # macOS
                    # Open in Terminal app
                    apple_script = f'''
                    tell application "Terminal"
                        activate
                        do script "cd '{parent_dir}' && java -jar GamingRoom.jar; echo; echo 'Press any key to close...'; read -n 1"
                    end tell
                    '''
                    subprocess.Popen(['osascript', '-e', apple_script])
                elif sys.platform == 'win32':  # Windows
                    subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', 'java', '-jar', jar_path])
                else:  # Linux
                    subprocess.Popen(['gnome-terminal', '--', 'java', '-jar', jar_path])
                return True
                
            else:
                print(f"Unknown app: {app_name}")
                return False
                
        except Exception as e:
            print(f"Error launching {app_name}: {e}")
            return False

def start_server(port=8080):
    """Start the HTTP server"""
    # Change to the Ptqt6 directory to serve files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    server = HTTPServer(('localhost', port), LauncherHandler)
    print(f"Server started at http://localhost:{port}")
    print("Opening launcher in browser...")
    
    # Open the launcher in browser after a short delay
    def open_browser():
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}/launcher.html')
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start serving
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()

if __name__ == '__main__':
    print("Starting Singleton Pattern Visualizer Launcher...")
    print("Press Ctrl+C to stop the server")
    start_server()