from turtle import Turtle

COLORS = ["yellow", "green", "orange", "red"]


class TileManager(Turtle):
    
    def __init__(self, tiles_per_row=13):
        super().__init__()
        self.hideturtle()
        self.tiles_per_row = tiles_per_row
        self.total_tiles = 0
        self.tiles = []
        self.starting_tile_position = (-360, 10)
        
        for color in COLORS:
            for i in range(2):
                for i in range(self.tiles_per_row):
                    self.generateTiles(position=self.starting_tile_position, color=color)
                    self.starting_tile_position = (self.starting_tile_position[0] + 60, self.starting_tile_position[1])
                self.starting_tile_position = (-360, self.starting_tile_position[1] + 30)
    
    def generateTiles(self, position, color):
        tile = Turtle()
        tile.color(color)
        tile.shape("square")
        tile.shapesize(stretch_wid=1, stretch_len=2)
        tile.penup()
        tile.goto(position)
        self.tiles.append(tile)
        self.total_tiles += 1
        
    def tileCollisionCheck(self, ball):
        for tile in self.tiles:
            if tile.distance(ball) < 24:
                tile.goto(800, 800)
                self.total_tiles -= 1
                tile_color = tile.color()[0]
                ball.bounce()
                
                if tile_color == "yellow":
                    return (1, self.total_tiles)
                elif tile_color == "green":
                    return (3, self.total_tiles)
                elif tile_color == "orange":
                    return (5, self.total_tiles)
                elif tile_color == "red":
                    return (7, self.total_tiles)
    
    def get_total_tiles(self):
        return self.total_tiles
        
