import sys
import os
import time
import _15_Save as save

def game_exit(username:str, user:list[dict], item_inventories:list[dict], item_shop:list[dict], monster:list[dict], monster_shop:list[dict], monster_inventory:list[dict]):
    '''
    Fungsi untuk keluar dari game
    '''
    exit_input = input('Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ').lower()
    if exit_input != 'y' and exit_input!='n':
        print('Input anda salah, ulangi')
        return game_exit(username, user, item_inventories, item_shop, monster, monster_shop, monster_inventory)
    elif exit_input == 'y':
        save.save(user, item_inventories, item_shop, monster, monster_shop, monster_inventory)
        print(f'Selamat tinggal agent {username}!')
        time.sleep(3)
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix/Linux/Mac
            os.system('clear')
        sys.exit()
    elif exit_input == 'n':
        print(f'Selamat tinggal agent {username}!')
        time.sleep(3)
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Unix/Linux/Mac
            os.system('clear')
        sys.exit()

if __name__ == '__main__' :
    game_exit('bimo')