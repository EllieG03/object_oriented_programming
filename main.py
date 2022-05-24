from room import Room
from items import Item
from character import Enemy, Friend

kitchen = Room('kitchen')
kitchen.set_description('A dank and dirty room buzzing with flies')
# kitchen.describe()

ballroom = Room('ballroom')
ballroom.set_description('A vast room with a shiny wooden floor; huge candlesticks guard the entrance')

dining_hall = Room('dining hall')
dining_hall.set_description('A large room with ornate golden decorations on each wall')

kitchen.link_room(dining_hall, 'south')
# the link only goes one way, so it only links the kitchen to the dining hall right now
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')
# dining_hall.get_link_details()

dave = Enemy('Dave', 'A smelly zombie')
dave.set_conversation('I am Dave and i will eat your brain')
dave.set_weakness('cheese')

emily = Friend('Emily', 'A friendly skeleton')
emily.set_conversation('Hello, fancy seeing you here')

dining_hall.set_character(dave)
ballroom.set_character(emily)


current_room = kitchen
dead = False
while dead == False:
    current_room.get_link_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input('> ')
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == 'fight':
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print('what will you fight with? ')
            weapon = input()
            if inhabitant.fight(weapon) == True:
                print('you won the fight!')
                current_room.set_character(None)
            else:
                print('oh no, you lost the fight.')
                print('looks like its the end of the game for you!')
                dead = True
        else:
            print('There is no one to fight with')
    elif command == 'hug':
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print('i dont think that is a safe idea')
            else:
                inhabitant.hug()
        else:
            print('there is no one to hug :(')





