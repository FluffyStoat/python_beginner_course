import base64


def main():
    with open("encoded_flag.txt", "r") as file:
        msg = file.readline()
        flag_bytes = msg.encode('ascii')

        for i in range(5):
            flag_bytes = base64.b16decode(flag_bytes)

        for i in range(5):
            flag_bytes = base64.b32decode(flag_bytes)

        for i in range(5):
            flag_bytes = base64.b64decode(flag_bytes)

        print(f"flag = {flag_bytes}")


if __name__ == "__main__":
    main()
