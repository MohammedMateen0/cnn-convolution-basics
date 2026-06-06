class BoundingBox:
    def __init__(
            self,
            x1,
            y1,
            x2,
            y2,
            score=1.0
    ):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.score=score

    @property
    def width(self):
        return self.x2-self.x1
        
    @property
    def height(self):
        return self.y1-self.y2
        
    @property
    def area(self):
        return (
                self.width *
                self.height
            )