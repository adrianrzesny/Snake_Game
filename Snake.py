from Direction import Direction
from Segment import Segment
import pygame
import copy

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        #The original image of the head
        self.original_picture = pygame.image.load("images/head.png")
        #Auxiliary image used when changing directions
        self.image = pygame.transform.rotate(self.original_picture, 0)
        #Head coordinates
        self.rect = self.image.get_rect(center=(12*32-16, 9*32-16))
        self.direction = Direction.UP
        self.new_direction = Direction.UP

        self.last_position = self.rect
        self.add_segment = False
        self.segments = []        

    def change_direction(self, direction):
        is_change = True

        if direction == Direction.UP and self.direction == Direction.DOWN:
            is_change = False
            
        if direction == Direction.DOWN and self.direction == Direction.UP:
            is_change = False
            
        if direction == Direction.RIGHT and self.direction == Direction.LEFT:
            is_change = False
            
        if direction == Direction.LEFT and self.direction == Direction.RIGHT:
            is_change = False
            
        if is_change:
            self.new_direction = direction  

    def update(self):
        self.direction = self.new_direction
        self.image = pygame.transform.rotate(self.original_picture, (self.direction.value*-90))

        #Update position 
        self.last_position = copy.deepcopy(self.rect)
        if self.direction == Direction.UP:
            self.rect.move_ip(0, -32)
            
        if self.direction == Direction.RIGHT:
            self.rect.move_ip(32, 0)
            
        if self.direction == Direction.LEFT:
            self.rect.move_ip(-32, 0)
            
        if self.direction == Direction.DOWN:
            self.rect.move_ip(0, 32)
            
        for i in range(len(self.segments)):
            if i==0:
                self.segments[i].move(self.last_position)
            else:
                self.segments[i].move(self.segments[i-1].last_position)
                            
        #Add new segment
        if self.add_segment:
            new_segment = Segment()
            new_position = None

            if len(self.segments) > 0:
                new_position = copy.deepcopy(self.segments[-1].position)
            else:
                new_position = copy.deepcopy(self.last_position)
                new_segment.position = new_position
                
            self.segments.append(new_segment)
            self.add_segment = False
                    

    def draw_segments(self, screen):
        for segment in self.segments:
            screen.blit(segment.image, segment.position)                   

    def collect_bonus(self):
        self.add_segment = True        

    def check_collision(self):
        #Tail bite
        for segment in self.segments:
            if self.rect.topleft == segment.position.topleft:
                return True
        #Going off screen
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True
        return False

    

