class Character:

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def sleep(self):
        print('you put ' + self.name + ' to sleep')

class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print(self.name + ' hugs you back')


if __name__ == '__main__':
    dave = Enemy('Dave', 'A smelly zombie')
    dave.describe()
    dave.set_conversation('I am Dave and i will eat you')
    dave.talk()

    # Set a weakness
    dave.set_weakness("cheese")

    # Fight with dave
    print("What will you fight with?")
    fight_with = input()
    dave.fight(fight_with)
