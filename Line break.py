from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
width = 10
height = 12
length = 13
block = 103
mc.setBlocks(pos.x, pos.y, pos.z,
             pos.x + width, pos.y + height, pos.z + length, block)
