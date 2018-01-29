from mcpi.minecraft from Minecraft
mc = Minecraft.create()

Beach = (28.6, 2.0, 7,7)
Forest = (95.4, 2.0, 48.9)
Ocean = (26.4, 0.0, 117.6)

choice = " "
while choice != "exit"
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        
