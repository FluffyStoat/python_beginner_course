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
import socket
from typing import Optional
import time
import requests
from requests import Response

HOST: str = '10.10.149.102'  # Standard loopback interface address (localhost)
PORT: int = 3010  # Port to listen on (non-privileged ports are > 1023)
URL: str = f'http://{HOST}:{PORT}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def main():
    response: Response = requests.get(URL, headers=headers)
    print(f'{response.text}')

    found: Optional = re.compile('":([0-9]+)"').search(response.text)
    if found:
        start_port = int(found.group(1))
        print(f"start_port: {start_port}")

        next_port: int = start_port

        while True:
            time.sleep(1)
            resp: Response = requests.get(f'http://{HOST}:{next_port}', headers=headers)

            if resp.text == 'STOP':
                break

            command: [str] = resp.text.split()
            print(f'command: {command[0]} {command[1]} {command[2]}')
            if command[0] == 'minus':
                start_port = start_port - int(command[1])
            elif command[0] == 'add':
                start_port = start_port + int(command[1])
            elif command[0] == 'divide':
                start_port = start_port + int(command[1])

            next_port = int(command[2])
            print(f"result = {start_port}")
            print(f"{next_port}")

    else:
        print("NOT_FOUND")


if __name__ == "__main__":
    main()
