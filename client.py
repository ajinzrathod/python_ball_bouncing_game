import socket
from tkinter import Tk, Frame


def leftKey(event):
    msgToSend = "l"
    s.sendall(bytes(msgToSend, 'utf-8'))


def rightKey(event):
    msgToSend = "r"
    s.sendall(bytes(msgToSend, 'utf-8'))


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1246))

    root = Tk()

    frame = Frame(root, width=100, height=100)

    frame.bind('<Left>', leftKey)
    frame.bind('<Right>', rightKey)

    frame.focus_set()
    frame.pack()

    root.mainloop()
