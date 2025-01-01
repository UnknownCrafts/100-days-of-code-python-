import random
from turtle import Turtle
from alien import Alien

INIT_ALIEN_POSES = ["Marker", "alien0_pose1.gif", "alien1_pose1.gif", "alien2_pose1.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
ALIEN_ROW_SPACING = 50


class AlienManager(Turtle):
    
    def __init__(self, aliens_per_row=5):
        super().__init__()
        self.alien_speed = STARTING_MOVE_DISTANCE * -1
        self.hideturtle()
        self.aliens_per_row = aliens_per_row
        self.aliens = []
        self.total_aliens = 0
        self.xmove = 10
        self.ymove = -10
        self.starting_tile_position = (-350, 10)
        self.left_marker = None
        self.right_marker = None
        
        for pose in INIT_ALIEN_POSES:
            if pose == "Marker":
                self.left_marker = Alien(position=self.starting_tile_position)
                
                self.right_marker = Alien(position=(-110, 210))
                
                self.aliens.append(self.left_marker)
                self.aliens.append(self.right_marker)
            
            elif pose != "alien2_pose1.gif":
                for i in range(2):
                    for i in range(self.aliens_per_row):
                        self.generateAliens(position=self.starting_tile_position, pose=pose)
                        self.starting_tile_position = (self.starting_tile_position[0] + 60, self.starting_tile_position[1])
                    self.starting_tile_position = (-350, self.starting_tile_position[1] + ALIEN_ROW_SPACING)
            else:
                for i in range(self.aliens_per_row):
                    self.generateAliens(position=self.starting_tile_position, pose=pose)
                    self.starting_tile_position = (self.starting_tile_position[0] + 60, self.starting_tile_position[1])
                self.starting_tile_position = (-350, self.starting_tile_position[1] + ALIEN_ROW_SPACING)
        
        self.real_aliens_len = self.total_aliens + 2
    
    def generateAliens(self, position, pose):
        alien = Alien(pose=pose, position=position)
        self.aliens.append(alien)
        self.total_aliens += 1
        
    def movementCheck(self, player):
        rm_alien_index = None
        player_hit = False
        alien_hit = False
        
        if self.left_marker.ycor() < -250:
            return True
        
        can_move_down = False
        if self.left_marker.xcor() < -360 or self.right_marker.xcor() > 360:
            self.xmove *= -1
            can_move_down = True

        for i in range (self.real_aliens_len):
            alien = self.aliens[i]
            
            if can_move_down:
                alien.goto(alien.xcor() + self.xmove, alien.ycor() + self.ymove)
            else:
                alien.goto(alien.xcor() + self.xmove, alien.ycor())
            
            if alien.bullet_shot:
                bullet_check = alien.updateBulletPos(player, player.bullet)
                if bullet_check != None:
                    if bullet_check[1] == True:
                        player_hit = True
                    if bullet_check[0] == True:
                        player.resetBullet()
                
            elif alien.bullet_shot == False and random.randint(1, 1000) == 2:
                alien.shoot()
            
            current_alien_pose = alien.shape()
            
            if current_alien_pose != "classic":
                if alien.distance(player.bullet) < 24:
                    alien.goto(1000,1000)
                    player.resetBullet()
                    rm_alien_index = i
                    self.total_aliens -= 1
                    self.real_aliens_len -= 1
                    
                elif alien.distance(player) < 24:
                    player_hit = True
                
                # Change the alien pose on each movement update
                if current_alien_pose == "alien0_pose1.gif":
                    alien.shape("alien0_pose2.gif")
                    continue
                elif current_alien_pose == "alien0_pose2.gif":
                    alien.shape("alien0_pose1.gif")
                    continue
                    
                if current_alien_pose == "alien1_pose1.gif":
                    alien.shape("alien1_pose2.gif")
                    continue
                elif current_alien_pose == "alien1_pose2.gif":
                    alien.shape("alien1_pose1.gif")
                    continue
                    
                if current_alien_pose == "alien2_pose1.gif":
                    alien.shape("alien2_pose2.gif")
                elif current_alien_pose == "alien2_pose2.gif":
                    alien.shape("alien2_pose1.gif")
        
        if rm_alien_index != None:
            self.aliens.pop(rm_alien_index)
            alien_hit = True
        
        return (alien_hit, player_hit)
    
    def aliensRemaining(self):
        
        return self.total_aliens
             
        
