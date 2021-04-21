import random


class Ball:
    def __init__(self, myCanvas, color):
        self.canvas = myCanvas

        # Creating Oval
        self.id = myCanvas.create_oval(0, 0, 15, 15, fill=color)
        """ (15 - 0) = 15
        Thus, the height and width of ball will be 15, 15 respectively
        Half of ball width be 15 // 2 = 7
        Half of ball height be 15 // 2 = 7
        """

        self.y = -1

        tpl = (-3, -2, -1, 1, 2, 3)
        # tpl = (0,)
        self.x = random.choice(tpl)

        # Getting height and width of current window
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def startGame(self,
                  root, serverPaddle, opponentPaddle,
                  serverWaterLevel, opponentWaterLevel):

        # Getting current co ordinates of Ball
        ballPos = self.canvas.coords(self.id)  # -> [x1, y1, x2, y2]

        # Getting Center of Canvas
        canvasCenterW = self.canvas_width // 2
        canvasCenterH = self.canvas_height // 2

        self.x = canvasCenterW - ballPos[2]
        self.y = canvasCenterH - ballPos[3]

        # Moving Ball to center
        self.canvas.move(self.id, (self.x)-7, (self.y)-7)

        tpl = (-3, -2, -1, 1, 2, 3)
        self.x = random.choice(tpl)
        self.y = -1

        self.clock(root,
                   serverPaddle, opponentPaddle,
                   serverWaterLevel, opponentWaterLevel)

    def draw(self, serverPaddle, opponentPaddle,
             serverWaterLevel, oppWaterLevel):

        # Moving ball up
        self.canvas.move(self.id, self.x, self.y)

        # Getting current co ordinates of Ball
        ballPos = self.canvas.coords(self.id)  # -> [x1, y1, x2, y2]

        # Getting current co ordinates of Paddles
        serverPaddlePos = self.canvas.coords(serverPaddle.id)
        oppPaddlePos = self.canvas.coords(opponentPaddle.id)

        # If Ball Reaches Extreme Left
        if ballPos[0] <= 0:
            self.x = abs(self.x)

        # If Ball Reaches Extreme Right
        elif ballPos[2] >= self.canvas_width:
            self.x = abs(self.x) * -1

        """In below line `else if` will not come.
        There is a possibility that ball reaches at extreme top and Left
        at same time"""
        # If Ball Reaches Extreme Top
        if ballPos[1] <= 0:
            self.y = 3

        # If Ball Touches Server's Water
        elif ballPos[3] >= serverWaterLevel:
            self.y = 0
            self.x = 0
            self.canvas.create_text(self.canvas_width // 2, 100, text="End")
            return True

        # If Ball Touches Opponent's Water
        elif ballPos[1] <= oppWaterLevel:
            self.y = 0
            self.x = 0
            self.canvas.create_text(self.canvas_width // 2, 100, text="End")
            return True

        # When Ball Touches Server's Paddle
        if ballPos[2] >= serverPaddlePos[0] and ballPos[0] <= serverPaddlePos[2]:
            if ballPos[3] >= serverPaddlePos[1] and ballPos[3] <= serverPaddlePos[3]:
                self.y = -3

        # When Ball Touches Opponent's Paddle
        if ballPos[2] >= oppPaddlePos[0] and ballPos[0] <= oppPaddlePos[2]:
            if ballPos[1] >= oppPaddlePos[1] and ballPos[1] <= oppPaddlePos[3]:
                self.y = 3

        return False

    # Forever Moving Ball
    def clock(self, root,
              serverPaddle, oppPaddle,
              serverWaterLevel, oppWaterLevel):

        losed = self.draw(serverPaddle, oppPaddle,
                          serverWaterLevel, oppWaterLevel)

        root.update_idletasks()
        """Calls all pending idle tasks, without processing any other events.
        This can be used to carry out geometry management
        and redraw widgets if necessary,
        without calling any callbacks."""

        if not losed:
            # After function name(self.clock), all are arguments
            root.after(10, self.clock, root,
                       serverPaddle, oppPaddle,
                       serverWaterLevel, oppWaterLevel)
