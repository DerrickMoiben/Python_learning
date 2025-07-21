

class Room():
    def __init__(self, direction, exit, item):
        self.direction = direction
        self.exit = exit
        self.item = item
        
        
        
    def go_direction(self):
        direction = {
            '1':'North',
            '2':'South',
            '3':'East',
            '4':'West'
        }
        roomit = int(input('Select the room you would like to enter 1, 2, 3, 4: '))
        if roomit == 1:
            print(f'You have entred the {direction["1"]}')
        elif roomit == 2:
            print(f'You have entered the {direction["2"]}')
        elif roomit == 3:
            print(f'You have entered the {direction["3"]}')
        elif roomit == 4:
            print(f'You have entere the {direction["4"]}')
        else:
            print(f'You have entered the wrong chooice recheck and  enter again please ')
            
    def add_item():
        inventory = []
        item = input('What do you want to add to you inventory: ')
        inventory.append(item)
        print(f'Your Inventory is this {inventory}')
            
    
