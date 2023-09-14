from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        base_dir = "/Users/jeffcompas/PythonStuff/python-projects"
        
        
        if self.path == '/favicon.ico':
            # Open the favicon.ico file
            with open(base_dir +'/favicon.ico', 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'image/x-icon')
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            f = open(base_dir+self.path, "r")
            contents = f.read()
        
            self.wfile.write(bytes(contents,"utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    