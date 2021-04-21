import socket
from threading import Thread
from opponentPosition import recieveMsgs


def create_server(PORT, opponentPaddle):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((socket.gethostname(), PORT))

    s.listen(1)
    conn, addr = s.accept()

    print(f"Connected with {addr}")

    t1 = Thread(target=recieveMsgs, args=(conn, opponentPaddle))
    t1.start()


if __name__ == '__main__':
    pass
