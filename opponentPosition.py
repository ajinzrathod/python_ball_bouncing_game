def recieveMsgs(conn, opponentPaddle):
    while True:
        data = conn.recv(1024)
        if not data:
            continue

        data = data.decode("utf-8")

        # l = left
        if data == "l":
            opponentPaddle.turn_left(None)

        # r = right
        elif data == 'r':
            opponentPaddle.turn_right(None)

        else:
            continue


if __name__ == '__main__':
    pass
