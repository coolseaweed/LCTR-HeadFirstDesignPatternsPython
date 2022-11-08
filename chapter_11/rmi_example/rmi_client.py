from datetime import datetime

import Pyro4
import sys
# server = Pyro4.Proxy(f"PYRONAME:mess.server")

# server_ip = "localhost"
# server = Pyro4.core.Proxy(f"PYRO:chat@{server_ip}:9090")


def start_chatting(server):
    text = ''
    while (text != 'exit'):
        text = input("... ")
        now = datetime.now()
        server.send_message(text)
        print(f'sent at {now:%H:%M:%S} \n')


if __name__ == '__main__':
    try:
        url = sys.argv[1]
        server = Pyro4.core.Proxy(f"{url}")
        start_chatting(server)
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
