from tkinter import Tk, Canvas
from create_server import create_server
from ball import Ball
from paddle import Paddle


def startGame(event):
    myBall.startGame(root, serverPaddle, opponentPaddle,
                     serverWaterLevel, opponentWaterLevel)

if __name__ == '__main__':
    # Creating root
    root = Tk()

    # Creating title
    root.title("ajinzrathod")

    # Restricting to resize window in both X and Y direction
    root.resizable(False, False)

    # Bring our window in front of all windows
    root.wm_attributes("-topmost", 1)

    # Declaring Height and width of root canvas
    myCanvasW = 500
    myCanvasH = 500

    # Creating Canvas (bd is for border)
    myCanvas = Canvas(root, width=myCanvasW, height=myCanvasH,
                      bd=0, highlightthickness=0)

    # Packing canvas
    myCanvas.pack()

    # Updating
    root.update()

    # Creating Ball
    myBall = Ball(myCanvas, "#ff0000")

    # Creating Paddle
    opponentPaddle = Paddle(myCanvas, "#ffff00",
                            paddleW=100, paddleH=20, yAxisPos=1/5)

    # The paddle we create last will be assign keys
    serverPaddle = Paddle(myCanvas, "#ffff00",
                          paddleW=100, paddleH=20, yAxisPos=4/5)

    # Creating Water for server
    serverWaterLevel = myCanvasH - 20
    myCanvas.create_rectangle(1, serverWaterLevel,
                              myCanvasW - 1, myCanvasH - 1,
                              fill="#1eafed")

    # Creating Water for opponent
    opponentWaterLevel = 20
    myCanvas.create_rectangle(1, 1, myCanvasW - 1, 20, fill="#1eafed")

    create_server(1246, opponentPaddle)

    # Moving clock for first time
    myCanvas.bind_all('<s>', startGame)

    # Showing window till user does'nt close it
    root.mainloop()
