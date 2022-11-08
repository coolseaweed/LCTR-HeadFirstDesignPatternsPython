from datetime import datetime

import Pyro4


@Pyro4.expose
class Chat(object):
    def send_message(self, text):
        now = datetime.now()
        print(f'{text} - received at {now:%H:%M:%S} \n')


def start_server():
    # Pyro4.Daemon.serveSimple({
    #     Chat: "chat",
    # }, host="0.0.0.0", port=9090, ns=False, verbose=True)
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    for i in range(3):
        chat_obj = Chat()

        uri = daemon.register(chat_obj, f"chat_{i}")
        print(uri, "??")
        ns.register('mess.server', str(uri))
    print(f'Ready to listen')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
