#!/usr/bin/env python3
"""Simple static server for Hive Landing Page"""
import http.server
import os
import socket

PORT = int(os.environ.get('PORT', 9999))
DIR = os.path.dirname(os.path.abspath(__file__))

class HiveHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")

if __name__ == '__main__':
    os.chdir(DIR)
    # Find an available port
    port = PORT
    for attempt in range(20):
        try:
            httpd = http.server.HTTPServer(('0.0.0.0', port), HiveHandler)
            print(f"🐝 Hive Landing Server running on port {port}")
            print(f"   Open: http://localhost:{port}")
            httpd.serve_forever()
            break
        except OSError:
            port += 1
            if port > 10000:
                print("❌ Could not find available port")
                sys.exit(1)
