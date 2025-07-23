#!/usr/bin/env python3
"""
Singleton Pattern Visualizer - One-Click Launcher
Opens the fancy HTML interface with backend server running
"""

import os
import sys
import subprocess
import threading
import webbrowser
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class LauncherHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler for launching applications"""
    
    def log_message(self, format, *args):
        """Suppress console logging for cleaner output"""
        pass
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/launch':
            # Get the app to launch from query parameters
            params = parse_qs(parsed_path.query)
            app = params.get('app', [''])[0]
            
            # Special case for status check
            if app == 'status':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = {'success': True, 'status': 'running'}
                self.wfile.write(json.dumps(response).encode())
                return
            
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
            
            print(f"🚀 Launching {app_name}...")
            
            if app_name == 'flowchart':
                # Launch animated flowchart
                subprocess.Popen([sys.executable, os.path.join(base_dir, 'singleton_flowchart_complete.py')])
                return True
                
            elif app_name == 'architecture':
                # Launch architecture explorer
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

def main():
    """Main entry point"""
    print("""
╔═══════════════════════════════════════════════════════════════╗
║          SINGLETON PATTERN VISUALIZER SUITE                   ║
║                                                               ║
║  🎯 Starting backend server...                                ║
║  🌐 Opening fancy HTML interface...                           ║
║  ✨ All launch buttons will work automatically!              ║
║                                                               ║
║  Press Ctrl+C to stop the server                              ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    
    # Change to the Ptqt6 directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Start the server in a separate thread with automatic port finding
    port = 8080
    max_attempts = 10
    server = None
    
    for attempt in range(max_attempts):
        try:
            server = HTTPServer(('localhost', port), LauncherHandler)
            break
        except OSError as e:
            if e.errno == 48 and attempt < max_attempts - 1:  # Address already in use
                print(f"⚠️  Port {port} in use, trying port {port + 1}...")
                port += 1
            else:
                print(f"❌ Error: Could not find an available port after {max_attempts} attempts")
                print(f"   Last error: {e}")
                sys.exit(1)
    
    def run_server():
        server.serve_forever()
    
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()
    
    print(f"✅ Backend server running on http://localhost:{port}")
    
    # Open the fancy HTML launcher
    time.sleep(1)  # Give server time to start
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'launcher.html')
    webbrowser.open(f'file://{html_path}')
    
    print("✅ HTML interface opened in browser")
    print("\n📌 Keep this window open for the launch buttons to work!")
    print("📌 Press Ctrl+C when done to stop the server\n")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down server...")
        server.shutdown()
        print("✅ Server stopped. Goodbye!")

if __name__ == '__main__':
    main()