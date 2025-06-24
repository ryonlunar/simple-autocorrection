import CSVfunction as csv
import DataPath as dp
import PlayerInventory
import os
dirname = os.path.dirname(__file__)

def print_monster(cnt:int,monster:dict)->None:
    '''
    Mengeprint monster
    '''
    name = monster['type']
    level = monster['level']
    hp = atribute_by_level(int(monster['hp']),int(monster['level']))
    print(f"{cnt}.Monster       (Name: {name}, Lvl: {level}, HP: {hp})")


def print_potion(cnt:int,potion:dict)->None:
    '''
    Mengeprint potion
    '''
    potion_type = potion['type']
    quantity = potion['quantity']
    print(f"{cnt}.Potion        (Type: {potion_type}, Qty: {quantity})")

def print_monster_ball(cnt:int,monster_ball:dict)->None:
    '''
    Mengeprint monster ball
    '''
    quantity = monster_ball['quantity']
    print(f"{cnt}.Monster Ball  (Qty: {quantity})")

def display_inventory(player_inventory:list[dict],coin:int)->list[dict]:
    '''
    Menampilkan inventory user di layar
    '''
    # print(player_inventory) 
    print(f'Jumlah O.W.C.A Coin-mu sekarang {coin}\n')
    for index, item in enumerate(player_inventory, start=1):
        if 'id' in item:
            print_monster(index,item)
        elif 'quantity' in item: 
            if item['type'] != 'monster ball':
                print_potion(index,item)
            else:
                print_monster_ball(index,item)
    print()
    return print_details_by_id(player_inventory)
                    

def print_monster_details(monster:dict)->None:
    '''
    Mengeprint detail monster
    '''
    print("Monster")
    print(f"Name      : {monster['type']}")
    print(f"ATK Power : {atribute_by_level(int(monster['atk_power']),int(monster['level']))}")
    print(f"DEF Power : {atribute_by_level(int(monster['def_power']),int(monster['level']))}")
    print(f"HP        : {atribute_by_level(int(monster['hp']),int(monster['level']))}")
    print(f"Level     : {monster['level']}")


# Function to print potion details
def print_potion_details(potion:dict)->None:
    '''
    Mengeprint detail potion atau monster ball
    '''
    if potion['type'] != 'Monster Ball':
        print("Potion")
    else:
        print('Monster Balls')
    print(f"Type      : {potion['type']}")
    print(f"Quantity  : {potion['quantity']}")


def print_details_by_id(data:dict)->None:
    '''
    Mengeprint detail item yang terdapat dalam inventory player
    '''
    while True:
        print('!Input "back" untuk kembali!')
        item_id = input("Ketikkan id untuk menampilkan detail item:\n>>> ")
        ids = []
        for i in range(1,len(data)+1):
            ids.append(str(i))
        if item_id == 'back':
            return None
        elif item_id in ids:
            for index, item in enumerate(data, start=1):
                if index == int(item_id):
                    if 'id' in item:
                        print_monster_details(item)
                    elif 'quantity' in item:
                        print_potion_details(item)
        else:
            print('Id item tidak ada di inventory, gunakan Id lain.')

def atribute_by_level(atribute:int, level:int):
    if level > 1:
        atribute = atribute + round(level * atribute * 0.1)
    return atribute
    
if __name__ == '__main__' :
    monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path('data')
    player_inventory , coin = PlayerInventory.player_inventory('Asep_Spakbor', user_data , monster_inventory_data , item_inventory , monster_data)
    print(player_inventory)
    display_inventory(player_inventory,coin)
    
    