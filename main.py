import pr_rileylink

import http.server

from itertools import zip_longest
from sys import stdin

PORT_NUMBER = 8999

# From itertools
def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

# Encode a word with the lights' radio encoding
def encode(word):
    o = "1111110001"
    for c in word:
        if c == '1':
            o += "001"
        else:
            o += "01"

    return bytes(int(''.join(group), 2) for group in grouper(8, o, '0'))

command_on = "1011100011010000"
command_off = "1011100011010001"

rl = pr_rileylink.RileyLink()

def send_packet(data):
    rl.send_packet(encode(data) + (b'\x00' * 10), 10, 10, 1)

g_state = b''

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global g_state
        if self.path == '/on':
            send_packet(command_on)
            g_state = b'on'
        elif self.path == '/off':
            send_packet(command_off)
            g_state = b'off'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(g_state)
        return

try:
    server = http.server.HTTPServer(('', PORT_NUMBER), handler)
    print('Started httpserver on port %d' % PORT_NUMBER)
    server.serve_forever()
except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
