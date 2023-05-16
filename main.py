import pygame
from sys import exit
from random import randint

from Player import Player
from Headshot import Headshot
from Enemy import Enemy

scene1_dialogue = [
    ["Charalampost", "Philostrate", "I have a good feeling about this election."],
    ["Charalampost", "Vasiliki", "Can you get me some water and a snack please?"],
    ["Charalampost", "Nobody", "Okay, everyone attention please!"],
    ["Charalampost", "Nobody", "The election ends tomorrow so I need everyone on their best behavior."],
    ["Philostrate", "Charalampost", "Excuse me, sir. I just got word of a disturbance downstairs."],
    ["Philostrate", "Charalampost", "I think we should go check it out."],
]
scene2_dialogue = [
    ["Charalampost", "Nobody", "[Screaming and shattering glass]"],
    ["Charalampost", "Nobody", "Who are all of these people? What is going on!!"],
    ["Charalampost", "Nobody", "Oh no! I am outnumbered. How do I defend myself from all of these people?"],
]
battle_dialogue = [
    ["Charalampost", "Nobody", "[Charalampost is injured.]"],
    ["Bobina", "Charalampost", "Charalampost! Get away from him!"],
    ["Charalampost", "Bobina", "Thank you Vasaliki, you saved me!"],
    ["Charalampost", "Philostrate", "Philostrate? What are you doing here?"],
    ["Philostrate", "Charalampost", "I heard you were in trouble, I am here to help!"],
    ["Philostrate", "Charalampost", "*Breathing Heavilty*"],
    ["Philostrate", "Charalampost", "Charalampost… I am so proud of you, son."],
    ["Charalampost", "Philostrate", "Son??? What are you talking about?"],
    ["Philostrate", "Charalampost", "I’m sorry I kept this from you. It was for your own safety."],
    ["Philostrate", "Charalampost", "*Dies*"],
]
scene31_dialogue = [
    ["Bobina", "Nobody", "And our new prime minister is… Charalampost!"],
    ["Charalampost", "Nobody", "[Gets on stage and is handed the trophy]"],
    ["Bobina", "Nobody", "Do you have any words for your supporters?"],
    ["Charalampost", "Nobody", "As some of you may have heard, there has been some chaos on the back-end of this campaign."],
    ["Charalampost", "Charalampost", "Thank you all for continuing to support me throughout this confusion and I hope to not let you down."],
    ["Charalampost", "Charalampost", "And a special thanks to Bobina and Philostrate,"],
    ["Charalampost", "Charalampost", "two members of my team who got me through this campaign."],
    ["Charalampost", "Charalampost", "[You successfully helped Charalampost defeat his rioters and win the election!]"],
]
scene32_dialogue = [
    ["Bobina", "Nobody", "And our new prime minister is… Charalampost!"],
    ["Charalampost", "Nobody", "I have some news."],
    ["Charalampost", "Nobody", "I am grievanced to report to you all that"],
    ["Charalampost", "Nobody", "I am unable to fufill the position of prime minister."],
    ["Charalampost", "Nobody", "While I am honored for the support my campaign has received,"],
    ["Charalampost", "Nobody", "I am dealing with personal issues behind the scene."],
    ["Charalampost", "Nobody", "Thus, I appoint a member of my team to assume my position, Vasaliki."],
    ["Bobina", "Nobody", "Thank you all. I am honored to be your first female prime minister"],
    ["Bobina", "Nobody", "and I promise to uphold the goal’s of my boss, Charalampost’s, campaign."],
    ["Charalampost", "Nobody", "[While you have successfully helped Charalampost defeat the rioters,"],
    ["Charalampost", "Nobody", "he was unable to fufill the role and someone from his team took his position.]"],
]
scene33_dialogue = [
    ["Bobina", "Nobody", "And our new prime minister is… Charalampost!"],
    ["Charalampost", "Nobody", "[Gets on stage and is handed the trophy]"],
    ["Charalampost", "Nobody", "Thank you to everyone who has supported me throughout this campaign."],
    ["Charalampost", "Nobody", "Nonetheless, I am disheartened to inform you that after dealing with the dark side"],
    ["Charalampost", "Nobody", "of the world of politics, I feel as though my team is not fit for this position."],
    ["Charalampost", "Nobody", "Therefore, I shall step down as prime minister and hand the role to my opposing candidate."],
    ["Charalampost", "Nobody", "[Charalampost walks off stage and the audience booes.]"],
    ["Bobina", "Nobody", "[While you have helped Charalampost defeat the rioters, the Poster Design "],
    ["Bobina", "Nobody", "wasn't good enough he was ultimately unable to become prime minister, "],
    ["Bobina", "Nobody", "making the efforts be a waste.] "],
]

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('The Campaign')
MAX_FRAME_RATE = 60
clock = pygame.time.Clock()
game_scene = "intro"
game_state = "battle"
text_index = 0

# Battle
player = pygame.sprite.GroupSingle()
object_ = Player()
object_.rect.midbottom = (200,300)
player.add(object_)

# Battle
enemy = pygame.sprite.GroupSingle()
object_ = Player()
object_.rect.midbottom = (200,300)
player.add(object_)

# Backdrop 
intro_surface = pygame.transform.scale(pygame.image.load('graphics/backdrops/Intro_Background.jpg').convert(), (800,400))
scene1_surface = pygame.transform.scale(pygame.image.load('graphics/backdrops/Scene1.jpg').convert(), (800,400))
scene2_surface = pygame.transform.scale(pygame.image.load('graphics/backdrops/Scene2.jpg').convert(), (800,400))
battle_surface = pygame.transform.scale(pygame.image.load('graphics/backdrops/Battle_Ground.png').convert(), (800,400))
scene3_surface = pygame.transform.scale(pygame.image.load('graphics/backdrops/Scene3.jpg').convert(), (800,400))
sky_surface = pygame.image.load('graphics/backdrops/Sky.png').convert()
ground_surface = pygame.image.load('graphics/backdrops/ground.png').convert()


# Talk
butler = pygame.sprite.GroupSingle()
object_ = Headshot("graphics/Butler_Head.png", "right")
object_.rect.bottomright = (800,400)
butler.add(object_)

chara = pygame.sprite.GroupSingle()
object_ = Headshot("graphics/Charalampost_Head.png", "left")
object_.rect.bottomleft = (0,400)
chara.add(object_)

bob = pygame.sprite.GroupSingle()
object_ = Headshot("graphics/Bobina_Headshot.png", "left")
object_.rect.bottomleft = (0,400)
bob.add(object_)

headshots = {
    "Charalampost": chara,
    "Philostrate": butler,
    "Vasiliki": bob,
    "Bobina": bob,
    "Nobody": None
}

enemy_group = pygame.sprite.Group()
death_count = 0

# Setup of gray rectangle that sits over game
IMAGE = pygame.Surface((800, 400), pygame.SRCALPHA)
pygame.draw.rect(IMAGE, pygame.Color('black'), pygame.Rect(0, 0, 800, 400),)
alpha_surface = pygame.Surface(IMAGE.get_size(), pygame.SRCALPHA)
alpha_surface.fill((255, 255, 255, 220))
IMAGE.blit(alpha_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
fh_surface = pygame.image.load('graphics/Full_Heart.png').convert_alpha()
hh_surface = pygame.image.load('graphics/Half_Heart.png').convert_alpha()
eh_surface = pygame.image.load('graphics/Empty_Heart.png').convert_alpha()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1500)
count = 0
        
def home_screen():
    screen.blit(intro_surface,(0,0))
    my_font = pygame.font.SysFont('Comic Sans MS', 60)
    text_surface = my_font.render('The Campaign', False, (255, 255, 255))
    screen.blit(text_surface, (200,0))   
    keys = pygame.key.get_pressed()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    other = my_font.render('Atul, Emily, Yash, Priyanka', False, (255, 255, 255))
    screen.blit(other, (200,300))   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        global game_scene
        game_scene = "1"
 
def scene_1():
    screen.blit(scene1_surface,(0,0))

    global text_index

    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global scene1_dialogue
        headshots[scene1_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{scene1_dialogue[text_index][0]}: {scene1_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 
        

    elif game_state == "battle":    
        player.draw(screen)
        player.update()

def scene_2():
    screen.blit(scene2_surface,(0,0))
    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global scene2_dialogue
        headshots[scene2_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{scene2_dialogue[text_index][0]}: {scene2_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 

    elif game_state == "battle":    
        player.draw(screen)
        player.update()

def fight():
    screen.blit(battle_surface,(0,0))
    global game_scene
    global enemy_group
    global game_state
    global text_index
    print(text_index)

    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global battle_dialogue
        headshots[battle_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{battle_dialogue[text_index][0]}: {battle_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 

    elif game_state == "battle":
        global count
        enemy_group.draw(screen)
        enemy_group.update()
        player.draw(screen)
        player.update()
        count += 1
        print(count)
        if count > 500:
            text_index = 2
            game_state = "talk"
        if pygame.sprite.spritecollide(player.sprite,enemy_group,False):
            enemy_group.empty()
            game_state = "talk"
            count = 0
            global death_count
            game_scene = "2"

def judge():
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    my_font = pygame.font.SysFont('Times New Roman', 40)
    text_surface = my_font.render(f'Design Team, how did you do?', False, (255, 0, 0))
    text_surface_rect = text_surface.get_rect(midbottom = (400,200))
    screen.blit(text_surface, text_surface_rect) 

def scene_31():
    screen.blit(scene3_surface,(0,0))
    player.draw(screen)
    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global scene31_dialogue
        headshots[scene31_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{scene31_dialogue[text_index][0]}: {scene31_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 

    elif game_state == "battle":    
        player.draw(screen)
        player.update()

def scene_32():
    screen.blit(scene3_surface,(0,0))
    player.draw(screen)
    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global scene32_dialogue
        headshots[scene32_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{scene32_dialogue[text_index][0]}: {scene32_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 

    elif game_state == "battle":    
        player.draw(screen)
        player.update()

def scene_33():
    screen.blit(scene3_surface,(0,0))
    player.draw(screen)
    if game_state == "talk":
        screen.blit(IMAGE, (0, 0))
        global headshots
        global scene33_dialogue
        headshots[scene33_dialogue[text_index][0]].draw(screen)
        # if headshots[scene1_dialogue[text_index][1]] != None:
        #     headshots[scene1_dialogue[text_index][1]].draw(screen)
        my_font = pygame.font.SysFont('Times New Roman', 20)
        text_surface = my_font.render(f'{scene33_dialogue[text_index][0]}: {scene33_dialogue[text_index][2]}', False, (255, 255, 255))
        text_surface_rect = text_surface.get_rect(midbottom = (400,100))
        screen.blit(text_surface, text_surface_rect) 

    elif game_state == "battle":    
        player.draw(screen)
        player.update()

def ending_screen():
    screen.blit(intro_surface,(0,0))
    my_font = pygame.font.SysFont('Comic Sans MS', 60)
    text_surface = my_font.render('The Campaign', False, (255, 255, 255))
    screen.blit(text_surface, (200,0))   
    my_font = pygame.font.SysFont('Times New Roman', 60)
    text_surface = my_font.render(f'The End', False, (255, 0, 0))
    text_surface_rect = text_surface.get_rect(midbottom = (550,200))
    screen.blit(text_surface, text_surface_rect) 

# Main game loop
while True:
    for event in pygame.event.get():
        # Handling of quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                if game_state == "talk":      
                    game_state = "battle"
                elif game_state == "battle":      
                    game_state = "talk"
            if event.key == pygame.K_k:
                death_count = 100  
        if event.type == enemy_timer and game_scene == "battle":
            enemy_group.add(Enemy())

        if event.type == pygame.KEYUP and game_state == "talk":
            if event.key == pygame.K_SPACE:
                if game_scene == "1":
                    if text_index < len(scene1_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "2"
                        text_index = 0
                        game_state = "battle" 
                if game_scene == "2":
                    if text_index < len(scene2_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "battle"
                        text_index = 0
                        game_state = "battle"
                if game_scene == "battle":
                    if text_index < len(battle_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "judge"
                        text_index = 0
                        game_state = "battle"
                if game_scene == "3-1":
                    if text_index < len(scene31_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "end"
                if game_scene == "3-2":
                    if text_index < len(scene32_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "end"
                if game_scene == "3-3":
                    if text_index < len(scene33_dialogue)-1:
                        text_index += 1
                    else:
                        game_scene = "end"
            if event.key == pygame.K_RETURN and game_scene == "end":
                pygame.quit()
                exit()
        if event.type == pygame.KEYUP and game_scene == "judge":
            if event.key == pygame.K_a:
                game_scene = "3-1"
            elif event.key == pygame.K_b:
                game_scene = "3-2"
            elif event.key == pygame.K_c:
                game_scene = "3-3"
            


    if game_scene == "intro":
        home_screen()
    if game_scene == "1":
        scene_1()
    if game_scene == "2":
        scene_2()
    if game_scene == "battle":
        fight()
    if game_scene == "judge":
        judge()
    if game_scene == "3-1":
        scene_31()
    if game_scene == "3-2":
        scene_32()
    if game_scene == "3-3":
        scene_33()
    if game_scene == "end":
        ending_screen()

    
    # Default updates
    pygame.display.update()
    clock.tick(MAX_FRAME_RATE)

