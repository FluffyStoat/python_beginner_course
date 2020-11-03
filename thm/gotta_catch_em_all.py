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
import time
from typing import Optional
import requests
from requests import Response

HOST: str = '10.10.127.201'  # Standard loopback interface address (localhost)
PORT: int = 3010  # Port to listen on (non-privileged ports are > 1023)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def parse_command(cmd: str, amount: float) -> (int, int):
    command: [str] = cmd.split()

    print(f'command: {command[0]} {command[1]} {command[2]}')

    if command[0] == 'minus':
        amount = amount - int(command[1])
    elif command[0] == 'add':
        amount = amount + int(command[1])
    elif command[0] == 'divide':
        amount = amount / float(command[1])
    elif command[0] == 'multiply':
        amount = amount * int(command[1])

    next_port: int = int(command[2])
    print(f'amount: {amount}')

    return amount, next_port


def main():
    response: Response = requests.get(f'http://{HOST}:{PORT}', headers=headers)
    response.close()
    print(f'{response.text}')
    time.sleep(1)

    found: Optional = re.compile('":([0-9]+)"').search(response.text)
    if found:
        start_port = int(found.group(1))
        print(f"start_port: {start_port}")

        first_response: Response = requests.get(f'http://{HOST}:{start_port}')
        first_response.close()
        cmd: str = first_response.text
        time.sleep(1)

        print(f"first_command: {cmd}")

        parsed_command: [str] = parse_command(first_response.text, 0.0)

        print(f"parsed_command[0]: {parsed_command[0]} parsed_command[1]: {parsed_command[1]}")

        amount: float = parsed_command[0]
        next_port: int = parsed_command[1]

        while cmd != "STOP" or next_port != 9765:
            try:
                time.sleep(10)
                cmd_response: Response = requests.get(f'http://{HOST}:{next_port}')
                cmd_response.close()
                cmd = cmd_response.text
                print(f"resp: {cmd_response.text}")

                new_cmd: [str] = parse_command(cmd, amount)
                amount = new_cmd[0]
                next_port = new_cmd[1]
            except requests.exceptions.ConnectionError:
                print("Connection error")
                raise

        # while cmd != "STOP" or next_port != 9765:
        #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #         s.connect((HOST, next_port))
        #         s.send(f"{amount}".encode("Utf-8"))
        #         data = s.recv(1024)
        #         print(f'Data: {repr(data)}')




    else:
        print("NOT_FOUND")


if __name__ == "__main__":
    main()