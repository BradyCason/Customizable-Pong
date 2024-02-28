import pygame
import sys
import pygame.font
from pygame.sprite import Sprite
from random import randint
import time
pygame.init()

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Pong")
        self.bg_color = (230,230,230)
        self.game_active = False
        self.left_is_player = True
        self.right_is_player = True
        self.left_speed = 1.5
        self.right_speed = 1.5
        self.right_score = 0
        self.left_score = 0
        self.right_target_score = 5
        self.left_target_score = 5
        self.right_height = 300
        self.left_height = 300
        self.right_color = (0,0,0)
        self.left_color = (0,0,0)
        self.ball_color = (0,0,0)
        self.ball_increase_speed = 0.5
        self.difficulty = "Normal"
        self.ball_size = 20
        
    def reset_settings(self):
        self.right_score = 0
        self.left_score = 0
        self.game_active = False

class LeftPlayer(Sprite):
    def __init__(self, s):
        super(LeftPlayer, self)
        self.width = 30
        self.height = s.left_height
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.left = 20
        self.rect.centery = s.screen_height / 2
        self.y_holder = self.rect.centery
        self.color = (0,0,0)
        self.moving_up = False
        self.moving_down = False
        
    def draw_player(self, s):
        self.color = s.left_color
        self.height = s.left_height
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        if self.moving_up and self.rect.top > 0:
            self.y_holder -= float(s.left_speed)
            self.rect.centery = self.y_holder
        if self.moving_down and self.rect.bottom < s.screen_height:
            self.y_holder += float(s.left_speed)
            self.rect.centery = self.y_holder
        pygame.draw.rect(s.screen, self.color, self.rect)
        
    def move_player(self, s, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.moving_up = True
            if event.key == pygame.K_s:
                self.moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.moving_up = False
            if event.key == pygame.K_s:
                self.moving_down = False
    
    def move_computer(self, s):
        if self.rect.centery < s.ball.rect.centery:
            self.moving_down = True
            self.moving_up = False
        elif self.rect.centery > s.ball.rect.centery:
            self.moving_up = True
            self.moving_down = False
        else:
            self.moving_down = False
            self.moving_up = False

class RightPlayer(Sprite):
    def __init__(self, s):
        super(RightPlayer, self)
        self.width = 30
        self.height = s.right_height
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.right = s.screen_width - 20
        self.rect.centery = s.screen_height / 2
        self.y_holder = self.rect.centery
        self.color = (0,0,0)
        self.moving_up = False
        self.moving_down = False
        
    def draw_player(self, s):
        self.color = s.right_color
        self.height = s.right_height
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        if self.moving_up and self.rect.top > 0:
            self.y_holder -= float(s.right_speed)
            self.rect.centery = self.y_holder
        if self.moving_down and self.rect.bottom < s.screen_height:
            self.y_holder += float(s.right_speed)
            self.rect.centery = self.y_holder
        pygame.draw.rect(s.screen, self.color, self.rect)
        
    def move_player(self, s, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moving_up = True
            if event.key == pygame.K_DOWN:
                self.moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.moving_up = False
            if event.key == pygame.K_DOWN:
                self.moving_down = False
    
    def move_computer(self, s):
        if self.rect.centery < s.ball.rect.centery:
            self.moving_down = True
            self.moving_up = False
        elif self.rect.centery > s.ball.rect.centery:
            self.moving_up = True
            self.moving_down = False
        else:
            self.moving_down = False
            self.moving_up = False

class Ball(Sprite):
    def __init__(self, s):
        super(Ball, self)
        self.width = s.ball_size
        self.height = s.ball_size
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = s.screen_width / 2
        self.rect.centery = s.screen_height / 2
        self.x_holder = self.rect.centerx
        self.y_holder = self.rect.centery
        self.color = (0,0,0)
        self.speedy_increaser = 0
        if s.difficulty == "Easy":
            self.speedx = 0.25
        if s.difficulty == "Normal":
            self.speedx = 0.5
        if s.difficulty == "Hard":
            self.speedx = 1
        if s.difficulty == "Pro":
            self.speedx = 1.5
        
        self.directionx = randint(1,2)
        if self.directionx == 1:
            self.directionx = -1
        elif self.directionx == 2:
            self.directionx == 1
            
        self.directiony = randint(1,2)
        if self.directiony == 1:
            self.directiony = -1
        elif self.directiony == 2:
            self.directiony == 1
            
        self.speedy = randint(1,5)
        if self.speedy == 1:
            self.speedy = 0.5
        if self.speedy == 2:
            self.speedy = 0.75
        if self.speedy == 3:
            self.speedy = 1
        if self.speedy == 4:
            self.speedy = 1.25
        if self.speedy == 5:
            self.speedy = 1.5
        
    def draw_ball(self, s):
        self.width = s.ball_size
        self.height = s.ball_size
        self.rect = pygame.Rect(self.rect.x,self.rect.y, self.width, self.height)
        self.color = s.ball_color
        pygame.draw.rect(s.screen, self.color, self.rect)
        
    def move_ball(self, s):
        if self.rect.top <= 0:
            self.directiony = 1
        if self.rect.bottom >= s.screen_height:
            self.directiony = -1
        
        if self.rect.right <= 0:
            ball_hit_left(s)
        if self.rect.left >= s.screen_width:
            ball_hit_right(s)
            
        if self.rect.colliderect(s.left_player.rect):
            self.directionx = 1
            self.speedx += s.ball_increase_speed
            self.speedy_increaser += 0.1
            if s.difficulty != "Easy":
                self.speedy = randint(1,5)
                if self.speedy == 1:
                    self.speedy = 0.5 + self.speedy_increaser
                if self.speedy == 2:
                    self.speedy = 0.75 + self.speedy_increaser
                if self.speedy == 3:
                    self.speedy = 1 + self.speedy_increaser
                if self.speedy == 4:
                    self.speedy = 1.25 + self.speedy_increaser
                if self.speedy == 5:
                    self.speedy = 1.5 + self.speedy_increaser
            
                self.directiony = randint(1,2)
                if self.directiony == 1:
                    self.directiony = -1
                elif self.directiony == 2:
                    self.directiony == 1
            
        if self.rect.colliderect(s.right_player.rect):
            self.directionx = -1
            self.speedx += s.ball_increase_speed
            self.speedy_increaser += 0.1
            if s.difficulty != "Easy":
                self.speedy = randint(1,5)
                if self.speedy == 1:
                    self.speedy = 0.5 + self.speedy_increaser
                if self.speedy == 2:
                    self.speedy = 0.75 + self.speedy_increaser
                if self.speedy == 3:
                    self.speedy = 1 + self.speedy_increaser
                if self.speedy == 4:
                    self.speedy = 1.25 + self.speedy_increaser
                if self.speedy == 5:
                    self.speedy = 1.5 + self.speedy_increaser
            
                self.directiony = randint(1,2)
                if self.directiony == 1:
                    self.directiony = -1
                elif self.directiony == 2:
                    self.directiony == 1
            else:
                self.speedy += self.speedy_increaser
        
        self.x_holder += float(self.directionx * self.speedx)
        self.rect.centerx = self.x_holder
        self.y_holder += float(self.directiony * self.speedy)
        self.rect.centery = self.y_holder

class Button():
    def __init__(self, s, msg, x=600, y=750, font_size=48, text_color=(255,255,255), button_color=(0,255,0)):
        self.screen_rect = s.screen.get_rect()
        self.width, self.height = 270, 50
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, font_size)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.prep_msg(msg)
        
    def prep_msg(self, msg):
        self.msg = msg
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self, s):
        s.screen.fill(self.button_color, self.rect)
        s.screen.blit(self.msg_image, self.msg_image_rect)

def check_if_game_over(s):
    if s.right_score >= s.right_target_score:
        s.font = pygame.font.Font(None, 150)
        if s.right_is_player:
            s.winner_text = s.font.render('Right Player Wins!', False, s.right_color)
        else:
            s.winner_text = s.font.render('Right Computer Wins!', False, s.right_color)
        s.screen.blit(s.winner_text,(150,300))
        pygame.display.flip()
        time.sleep(3)
        s.reset_settings()
    if s.left_score >= s.left_target_score:
        s.font = pygame.font.Font(None, 150)
        if s.left_is_player:
            s.winner_text = s.font.render('Left Player Wins!', False, s.left_color)
        else:
            s.winner_text = s.font.render('Left Computer Wins!', False, s.left_color)
        s.screen.blit(s.winner_text,(150,300))
        pygame.display.flip()
        time.sleep(3)
        s.reset_settings()

def ball_hit_left(s):
    s.ball.__init__(s)
    s.right_score += 1
    s.right_player.__init__(s)
    s.left_player.__init__(s)

def ball_hit_right(s):
    s.ball.__init__(s)
    s.left_score += 1
    s.right_player.__init__(s)
    s.left_player.__init__(s)

def change_active_variables(s):
    if s.difficulty == "Easy":
        s.ball_increase_speed = 0.2
    if s.difficulty == "Medium":
        s.ball_increase_speed = 0.25
    if s.difficulty == "Hard":
        s.ball_increase_speed = 0.75
    if s.difficulty == "Pro":
        s.ball_increase_speed = 1

def draw_score(s):
    if s.left_is_player:
        s.left_text = s.font.render(('Left Player Score: ' + str(s.left_score)), False, s.left_player.color)
    else:
        s.left_text = s.font.render(('Left Computer Score: ' + str(s.left_score)), False, s.left_player.color)
    if s.right_is_player:
        s.right_text = s.font.render(('Right Player Score: ' + str(s.right_score)), False, s.right_player.color)
    else:
        s.right_text = s.font.render(('Right Computer Score: ' + str(s.right_score)), False, s.right_player.color)
    s.font = pygame.font.Font(None, 50)
    s.screen.blit(s.left_text,(100,10))
    s.screen.blit(s.right_text,(700,10))

def check_inactive_button_presses(s, mouse_x, mouse_y):
    if s.left_player_or_computer_button.rect.collidepoint(mouse_x, mouse_y):
        if s.left_is_player:
            s.left_is_player = False
        else:
            s.left_is_player = True
    if s.right_player_or_computer_button.rect.collidepoint(mouse_x, mouse_y):
        if s.right_is_player:
            s.right_is_player = False
        else:
            s.right_is_player = True
    
    if s.right_color_button.rect.collidepoint(mouse_x, mouse_y):
        c1 = randint(0,255)
        c2 = randint(0,255)
        c3 = randint(0,255)
        s.right_color_button.button_color = (c1, c2, c3)
        s.right_color = (c1, c2, c3)
        s.right_color_button.button_color = s.right_color
        s.right_color_button.prep_msg(s.right_color_button.msg)
        
    if s.left_color_button.rect.collidepoint(mouse_x, mouse_y):
        c1 = randint(0,255)
        c2 = randint(0,255)
        c3 = randint(0,255)
        s.left_color_button.button_color = (c1, c2, c3)
        s.left_color = (c1, c2, c3)
        s.left_color_button.button_color = s.left_color
        s.left_color_button.prep_msg(s.left_color_button.msg)
        
    if s.right_target_score_button.rect.collidepoint(mouse_x, mouse_y):
        if s.right_target_score == 1:
            s.right_target_score = 2
        elif s.right_target_score == 2:
            s.right_target_score = 3
        elif s.right_target_score == 3:
            s.right_target_score = 4
        elif s.right_target_score == 4:
            s.right_target_score = 5
        elif s.right_target_score == 5:
            s.right_target_score = 10
        elif s.right_target_score == 10:
            s.right_target_score = 25
        elif s.right_target_score == 25:
            s.right_target_score = 1
        
        s.right_target_score_button.msg = "Target Score: " + str(s.right_target_score)
        s.right_target_score_button.prep_msg(s.right_target_score_button.msg)
        
    if s.left_target_score_button.rect.collidepoint(mouse_x, mouse_y):
        if s.left_target_score == 1:
            s.left_target_score = 2
        elif s.left_target_score == 2:
            s.left_target_score = 3
        elif s.left_target_score == 3:
            s.left_target_score = 4
        elif s.left_target_score == 4:
            s.left_target_score = 5
        elif s.left_target_score == 5:
            s.left_target_score = 10
        elif s.left_target_score == 10:
            s.left_target_score = 25
        elif s.left_target_score == 25:
            s.left_target_score = 1
        
        s.left_target_score_button.msg = "Target Score: " + str(s.left_target_score)
        s.left_target_score_button.prep_msg(s.left_target_score_button.msg)
        
    if s.right_speed_button.rect.collidepoint(mouse_x, mouse_y):
        if s.right_speed == 0.5:
            s.right_speed = 1
            s.right_speed_button.msg = "Speed: Slow"
        elif s.right_speed == 1:
            s.right_speed = 1.5
            s.right_speed_button.msg = "Speed: Normal"
        elif s.right_speed == 1.5:
            s.right_speed = 2
            s.right_speed_button.msg = "Speed: Quick"
        elif s.right_speed == 2:
            s.right_speed = 3
            s.right_speed_button.msg = "Speed: Fast"
        elif s.right_speed == 3:
            s.right_speed = 6
            s.right_speed_button.msg = "Speed: Zooming"
        elif s.right_speed == 6:
            s.right_speed = 0.5
            s.right_speed_button.msg = "Speed: Sloooow"
        
        s.right_speed_button.prep_msg(s.right_speed_button.msg)
        
    if s.left_speed_button.rect.collidepoint(mouse_x, mouse_y):
        if s.left_speed == 0.5:
            s.left_speed = 1
            s.left_speed_button.msg = "Speed: Slow"
        elif s.left_speed == 1:
            s.left_speed = 1.5
            s.left_speed_button.msg = "Speed: Normal"
        elif s.left_speed == 1.5:
            s.left_speed = 2
            s.left_speed_button.msg = "Speed: Quick"
        elif s.left_speed == 2:
            s.left_speed = 3
            s.left_speed_button.msg = "Speed: Fast"
        elif s.left_speed == 3:
            s.left_speed = 6
            s.left_speed_button.msg = "Speed: Zooming"
        elif s.left_speed == 6:
            s.left_speed = 0.5
            s.left_speed_button.msg = "Speed: Sloooow"
        
        s.left_speed_button.prep_msg(s.left_speed_button.msg)
        
    if s.right_length_button.rect.collidepoint(mouse_x, mouse_y):
        if s.right_height == 20:
            s.right_height = 100
            s.right_player.rect.height = s.right_height
            s.right_player.rect.centery = s.screen_rect.centery
            s.right_length_button.msg = "Length: Small"
        elif s.right_height == 100:
            s.right_height = 300
            s.right_player.rect.height = s.right_height
            s.right_player.rect.centery = s.screen_rect.centery
            s.right_length_button.msg = "Length: Normal"
        elif s.right_height == 300:
            s.right_height = 500
            s.right_player.rect.height = s.right_height
            s.right_player.rect.centery = s.screen_rect.centery
            s.right_length_button.msg = "Length: Long"
        elif s.right_height == 500:
            s.right_height = 800
            s.right_player.rect.height = s.right_height
            s.right_player.rect.centery = s.screen_rect.centery
            s.right_length_button.msg = "Length: Unfair"
        elif s.right_height == 800:
            s.right_height = 20
            s.right_player.rect.height = s.right_height
            s.right_player.rect.centery = s.screen_rect.centery
            s.right_length_button.msg = "Length: Tiny"
        
        s.right_length_button.prep_msg(s.right_length_button.msg)
        
    if s.left_length_button.rect.collidepoint(mouse_x, mouse_y):
        if s.left_height == 20:
            s.left_height = 100
            s.left_player.rect.height = s.left_height
            s.left_player.rect.centery = s.screen_rect.centery
            s.left_length_button.msg = "Length: Small"
        elif s.left_height == 100:
            s.left_height = 300
            s.left_player.rect.height = s.left_height
            s.left_player.rect.centery = s.screen_rect.centery
            s.left_length_button.msg = "Length: Normal"
        elif s.left_height == 300:
            s.left_height = 500
            s.left_player.rect.height = s.left_height
            s.left_player.rect.centery = s.screen_rect.centery
            s.left_length_button.msg = "Length: Long"
        elif s.left_height == 500:
            s.left_height = 800
            s.left_player.rect.height = s.left_height
            s.left_player.rect.centery = s.screen_rect.centery
            s.left_length_button.msg = "Length: Unfair"
        elif s.left_height == 800:
            s.left_height = 20
            s.left_player.rect.height = s.left_height
            s.left_player.rect.centery = s.screen_rect.centery
            s.left_length_button.msg = "Length: Tiny"
        
        s.left_length_button.prep_msg(s.left_length_button.msg)
    
    if s.ball_color_button.rect.collidepoint(mouse_x, mouse_y):
        c1 = randint(0,255)
        c2 = randint(0,255)
        c3 = randint(0,255)
        s.ball_color_button.button_color = (c1, c2, c3)
        s.ball_color = (c1, c2, c3)
        s.ball_color_button.button_color = s.ball_color
        s.ball_color_button.prep_msg(s.ball_color_button.msg)
        
    if s.background_color_button.rect.collidepoint(mouse_x, mouse_y):
        c1 = randint(0,255)
        c2 = randint(0,255)
        c3 = randint(0,255)
        s.background_color_button.button_color = (c1, c2, c3)
        s.bg_color = (c1, c2, c3)
        s.background_color_button.button_color = s.bg_color
        s.background_color_button.prep_msg(s.background_color_button.msg)
        
    if s.difficulty_button.rect.collidepoint(mouse_x, mouse_y):
        if s.difficulty == "Easy":
            s.difficulty = "Normal"
            s.ball.speedx = 0.5
        elif s.difficulty == "Normal":
            s.difficulty = "Hard"
            s.ball.speedx = 1
        elif s.difficulty == "Hard":
            s.difficulty = "Pro"
            s.ball.speedx = 1.5
        elif s.difficulty == "Pro":
            s.difficulty = "Easy"
            s.ball.speedx = 0.25
        s.difficulty_button.msg = "Level: " + s.difficulty
        s.difficulty_button.prep_msg(s.difficulty_button.msg)
        
    if s.ball_size_button.rect.collidepoint(mouse_x, mouse_y):
        if s.ball_size == 10:
            s.ball_size = 20
            s.ball_size_button.msg = "Ball: Normal"
        elif s.ball_size == 20:
            s.ball_size = 40
            s.ball_size_button.msg = "Ball: Large"
        elif s.ball_size == 40:
            s.ball_size = 80
            s.ball_size_button.msg = "Ball: Huge"
        elif s.ball_size == 80:
            s.ball_size = 10
            s.ball_size_button.msg = "Ball: Small"
        s.ball_size_button.prep_msg(s.ball_size_button.msg)

def draw_inactive_words(s):
    s.font = pygame.font.Font(None, 80)
    s.left_text = s.font.render('Left', False, (0,0,0))
    s.right_text = s.font.render('Right', False, (0,0,0))
    s.screen.blit(s.left_text,(200,10))
    s.screen.blit(s.right_text,(880,10))
    
    if s.left_is_player:
        s.left_player_or_computer_button.prep_msg("Player")
    else:
        s.left_player_or_computer_button.prep_msg("Computer")
    if s.right_is_player:
        s.right_player_or_computer_button.prep_msg("Player")
    else:
        s.right_player_or_computer_button.prep_msg("Computer")
    s.left_player_or_computer_button.draw_button(s)
    s.right_player_or_computer_button.draw_button(s)
    
    s.left_color_button.draw_button(s)
    s.right_color_button.draw_button(s)
    s.left_target_score_button.draw_button(s)
    s.right_target_score_button.draw_button(s)
    s.left_speed_button.draw_button(s)
    s.right_speed_button.draw_button(s)
    s.left_length_button.draw_button(s)
    s.right_length_button.draw_button(s)
    s.ball_color_button.draw_button(s)
    s.background_color_button.draw_button(s)
    s.ball_size_button.draw_button(s)
    s.difficulty_button.draw_button(s)
    
def check_play_button(s, mouse_x, mouse_y):
    if s.play_button.rect.collidepoint(mouse_x, mouse_y):
        s.game_active = True

def check_for_input(s):
    for event in pygame.event.get():
        s.left_player.move_player(s, event)
        s.right_player.move_player(s, event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_inactive_button_presses(s, mouse_x, mouse_y)
            check_play_button(s, mouse_x, mouse_y)

def non_active_game_loop(s):
    s.play_button.draw_button(s)
    draw_inactive_words(s)

def active_game_loop(s):
    change_active_variables(s)
    
    s.screen.fill(s.bg_color)
    if not s.left_is_player:
        s.left_player.move_computer(s)
    s.left_player.draw_player(s)
    if not s.right_is_player:
        s.right_player.move_computer(s)
    s.right_player.draw_player(s)
    
    s.ball.move_ball(s)
    s.ball.draw_ball(s)
    
    draw_score(s)
    check_if_game_over(s)

def run_game():
    s = Settings()
    s.left_player = LeftPlayer(s)
    s.right_player = RightPlayer(s)
    s.ball = Ball(s)
    
    s.play_button = Button(s, "Play", font_size=60)
    s.left_player_or_computer_button = Button(s, "Player", x=250, y=150, font_size=48, button_color=(30,30,30))
    s.right_player_or_computer_button = Button(s, "Player", x=950, y=150, font_size=48, button_color=(30,30,30))
    s.left_color_button = Button(s, "Color", x=250, y=250, font_size=48, button_color=(0,0,0))
    s.right_color_button = Button(s, "Color", x=950, y=250, font_size=48, button_color=(0,0,0))
    s.left_target_score_button = Button(s, "Target Score: 5", x=250, y=350, font_size=48, button_color=(0,0,0))
    s.right_target_score_button = Button(s, "Target Score: 5", x=950, y=350, font_size=48, button_color=(0,0,0))
    s.left_speed_button = Button(s, "Speed: Normal", x=250, y=450, font_size=48, button_color=(0,0,0))
    s.right_speed_button = Button(s, "Speed: Normal", x=950, y=450, font_size=48, button_color=(0,0,0))
    s.left_length_button = Button(s, "Length: Normal", x=250, y=550, font_size=48, button_color=(0,0,0))
    s.right_length_button = Button(s, "Length: Normal", x=950, y=550, font_size=48, button_color=(0,0,0))
    
    s.background_color_button = Button(s, "BG Color", x=600, y=150, font_size=48, button_color=(0,0,0))
    s.ball_color_button = Button(s, "Ball Color", x=600, y=250, font_size=48, button_color=(0,0,0))
    s.ball_size_button = Button(s, "Ball: Normal", x=600, y=350, font_size=48, button_color=(0,0,0))
    s.difficulty_button = Button(s, "Level: Normal", x=600, y=450, font_size=48, button_color=(0,0,0))
    
    while True:
        s.screen.fill((230,230,230))
        check_for_input(s)
        
        if s.game_active:
            active_game_loop(s)
        else:
            non_active_game_loop(s)
    
        pygame.display.flip()

run_game()
