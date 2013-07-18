import BaseHTTPServer
from LavenDistanceNoParallel import distance
import re
import QueryMaster
HOST_NAME = 'localhost' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 5123 # Maybe set this to 9000
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
	def do_GET(s):
		s.send_response(200)
		s.send_header("Content-type", "text/html")
		s.end_headers()
		query=s.path.lstrip("/")
		query=query.split("+")
		query=" ".join(query)
		result=QueryMaster.returnResult(query)
		s.wfile.write(result)
def main():
	server_class = BaseHTTPServer.HTTPServer
	httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
if __name__ == '__main__':
	main()
