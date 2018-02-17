"""

HOW TO PLAY:
------------

    (1) --> set CREATIVE mode

        >gamemode 1 WoodieWooJr
        11:14:22 [INFO] CONSOLE: Set WoodieWooJr's game mode to CREATIVE mode

    (2) --> add a sword to inventory

    (3) --> set SURVIVAL mode

        >gamemode 0 WoodieWooJr
        11:14:17 [INFO] CONSOLE: Set WoodieWooJr's game mode to SURVIVAL mode

    (4) --> start python script and play :)

        PYTHONPATH=/Users/josejimenez/Documents/minecraft/minecraft-adventures/MyAdventures python game.py

"""


import time
import thread

import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
from mcpi.vec3 import Vec3

from platform.moving_platform import PlaneBorder, Platformer


# level
LEVELS = 3
TIMEOUTS = [3000, 250, 200] # [30,25,20]

# arena
ARENAX = 20
ARENAZ = 30
ARENAY = 3

# river
RIVERWIDTH = 20
RIVERZ = 4

# platform
PLATFORM_BLOCK_SIZE = 1
NUMBER_BLOCKS = 200
PLATFORM_SLEEP_TIME = 0.05



#Create the Arena
def createArena(pos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()
    
    #Create the floor
    mc.setBlocks(pos.x - 1 , pos.y, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y - 3, pos.z + ARENAZ + 1,
                 block.GRASS.id)

    #Create the walls on the outside of the arena
    mc.setBlocks(pos.x - 1, pos.y + 1, pos.z - 1,
                 pos.x + ARENAX + 1, pos.y + ARENAY, pos.z + ARENAZ + 1,
                 block.GLASS.id)
    mc.setBlocks(pos.x, pos.y + 1, pos.z,
                 pos.x + ARENAX, pos.y + ARENAY, pos.z + ARENAZ,
                 block.AIR.id)

#The River
def theRiver(arenaPos, riverZPos):
    #create connection to minecraft
    mc = minecraft.Minecraft.create()
    
    #create the river
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.AIR.id)
    #fill with water
    mc.setBlocks(arenaPos.x, arenaPos.y - 2, arenaPos.z + riverZPos,
                 arenaPos.x + ARENAX, arenaPos.y - 2, arenaPos.z + riverZPos + RIVERWIDTH - 1,
                 block.WATER.id)

    return [tuple(sorted([arenaPos.x - 1, arenaPos.x + ARENAX + 1])),
            tuple(sorted([arenaPos.z + riverZPos - 1, arenaPos.z + riverZPos + RIVERWIDTH]))]

def the_platform(xz=None):
    block_id = block.WOOD_PLANKS.id
    plane = PlaneBorder(x=xz[0], z=xz[1])
    platform = Platformer(number_blocks=NUMBER_BLOCKS, block_size=PLATFORM_BLOCK_SIZE, plane=plane)

    #create the platform shapes
    platform_shapes = []
    for pos in platform.get_block_positions():
        block_pos = Vec3(pos[0], arenaPos.y, pos[1])
        platform_blocks = []
        for x in range(PLATFORM_BLOCK_SIZE):
            for z in range(PLATFORM_BLOCK_SIZE):
                platform_blocks.append(minecraftstuff.ShapeBlock(x, 0, z, block_id))
        platform_shape = minecraftstuff.MinecraftShape(mc, block_pos, platform_blocks)
        platform_shapes.append(platform_shape)

    #move the platforms
    while not levelComplete:
        platform.move_blocks()
        directions = platform.get_block_directions()
        for i in range(len(directions)):
            platform_shapes[i].moveBy(directions[i][0], 0, directions[i][1])
            time.sleep(PLATFORM_SLEEP_TIME)


#Main program
#create minecraft object
mc = minecraft.Minecraft.create()

#create the gameOver flag
gameOver = False

#arena pos
arenaPos = mc.player.getTilePos()

#build the arena
createArena(arenaPos)

#create the river
xz = theRiver(arenaPos, RIVERZ)


#set level and points
level = 0
points = 0

#game loop, while not game over
while not gameOver:
    #position the player at the start of the arena
    mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)

    #start the clock
    start = time.time()

    #set the level complete flag
    levelComplete = False

    thread.start_new_thread(the_platform, (xz, ))

    #level loop
    sec_done = set()
    while not gameOver and not levelComplete:
        #sleep for a bit
        time.sleep(0.1)

        #get the players position
        pos = mc.player.getTilePos()
        
        #has player fallen down
        if pos.y < arenaPos.y:
            #put them back to the start
            mc.player.setPos(arenaPos.x + 1, arenaPos.y + 1, arenaPos.z + 1)
            
        #has the player got to the end of the arena and got all the diamonds?
        if pos.z == arenaPos.z + ARENAZ:
            levelComplete = True

        #has the time expired
        secondsLeft = TIMEOUTS[level] - (time.time() - start)
        secondsLeft_int = int(secondsLeft)
        if secondsLeft_int not in sec_done and (secondsLeft < 10 or secondsLeft_int % 5 == 0):
            mc.postToChat("Seconds remaining: {}".format(str(secondsLeft_int)))
            sec_done.add(secondsLeft_int)
        if secondsLeft < 0:
            gameOver = True
            mc.postToChat("Out of time...")

    #level complete?
    if levelComplete:
        level = level + 1
        if level == LEVELS:
            gameOver = True
            mc.postToChat("Congratulations - All levels complete")

#its game over
mc.postToChat("Game Over - Points = " + str(points))
