class Paddle:
    def __init__(self, myCanvas, color, paddleW, paddleH, yAxisPos):
        """
        consider there are 5 points in  Y-Axis,
        if we give 4/5 in `yAxisPos`,
        Paddle we positioned at 4th place
        + ------------- +
        | 1 .           |
        | 2 .           |
        | 3 .           |
        | 4 . <--- Here |
        | 5 .           |
        + --------------+
        Points on Y-Axis can be dynamic.
        Thus, paddle Initial Pos will be -> (canvas_height * yAxisPos)
        """
        self.canvas = myCanvas
        self.id = myCanvas.create_rectangle(0, 0, paddleW, paddleH, fill=color)

        # Getting height and width of current window
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

        # Horizontal Scroll
        self.x = 0

        # Centering from width and setting height as per yAxisPos
        self.canvas.move(self.id,
                         (self.canvas_width//2) - paddleW // 2,
                         ((int(self.canvas_height * yAxisPos)) - (paddleH//2)))

        # Binding Arrow Keys
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self, moveL, moveR):
        # Getting Paddle Postition
        paddlePostion = self.canvas.coords(self.id)

        # If Paddle is on extreme Left, restrict furthur moving
        if (paddlePostion[0] <= 0) and (moveL is True):
            return

        # If Paddle is on extreme Right, restrict furthur moving
        elif (paddlePostion[2] >= self.canvas_width) and (moveR is True):
            return

        self.canvas.move(self.id, self.x, 0)

    def turn_left(self, event):
        # to move on negative X-Axis
        self.x = -20
        self.draw(moveL=True, moveR=False)

    def turn_right(self, event):
        # to move on Positive X-Axis
        self.x = 20
        self.draw(moveL=False, moveR=True)
