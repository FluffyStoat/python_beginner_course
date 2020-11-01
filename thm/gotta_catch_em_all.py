# You need to write a script that connects to this webserver on the correct port, do an operation on a number
# and then move onto the next port. Start your original number at 0.
#
# The format is: operation, number, next port.
#
# For example the website might display, add 900 3212 which would be: add 900 and move onto port 3212.
#
# Then if it was minus 212 3499, you'd minus 212 (from the previous number which was 900) and move onto the next
# port 3499
#
# Do this until you the page response is STOP (or you hit port 9765).
#
# Each port is also only live for 4 seconds. After that it goes to the next port. You might have to wait until
# port 1337 becomes live again...
#
# Go to: http://<machines_ip>:3010 to start...
#
# General Approach(it's best to do this using the sockets library in Python):
#
# Create a socket in Python using the sockets library
# Connect to the port
# Send an operation
# View response and continue
import re
from typing import Optional

import socket

import requests
from requests import Response

HOST: str = '10.10.56.146'  # Standard loopback interface address (localhost)
PORT: int = 3010  # Port to listen on (non-privileged ports are > 1023)
URL: str = f'http://{HOST}:{PORT}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def main():
    response: Response = requests.get(URL, headers=headers)
    print(f'{response.text}')

    result: Optional = re.compile(':([0-9]+)').search(response.text)
    start_port: str = result.group(1)
    print(start_port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((f"{HOST}", PORT))
        # s.sendall(b"GET / HTTP/1.1\r\nAccept: text/html\r\n\r\n")
        s.sendall(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")

        data: str = str(s.recv(4048), 'utf-8')
        print(f"data: {data}")

        optional: Optional = re.compile('":([0-9]+)').search(data)
        p: str = optional.group(1)

        print(f"port: {p}")


if __name__ == "__main__":
    main()
