from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def getWoolState(color):
    if color == "pink":
        blockState = 6
    elif color == "blue":
        blockState = 11
    elif color == "lime":
        blockState = 5
    else:
        blockState = 7
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
