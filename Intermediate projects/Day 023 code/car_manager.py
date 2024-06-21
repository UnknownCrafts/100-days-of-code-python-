from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.carspeed = STARTING_MOVE_DISTANCE * -1
        self.hideturtle()
        self.car_threshold = 25
        self.cars = []
        self.total_cars = 0
        for i in range(self.car_threshold):
            self.generateCars()
    
    def generateCars(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(random.randint(310, 1200), random.randint(-240, 260))
        self.cars.append(car)
        self.total_cars += 1
        
    def movementCheck(self, turtle):
        for car in self.cars:
            car.forward(self.carspeed)
            if car.xcor() < -320:
                car.goto(random.randint(310, 1200), random.randint(-240, 260))
            if car.distance(turtle) < 24:
                return True
    
    def increase_speed(self):
        
        self.carspeed -= MOVE_INCREMENT
             
        
