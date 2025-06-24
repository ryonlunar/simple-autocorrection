import DataPath as dp
import _00_LCG as lcg
import os
import math
import time
import sys , subprocess
import PlayerInventory as pi
dirname = os.path.dirname(__file__)

    
def arena(username:str, monster_data:list[dict], monster_inventory_data:list[dict], potion_data:list[dict], item_inventory:list[dict], user_data:list[dict]):
    
    player_inventory , coin = pi.player_inventory(username, user_data , monster_inventory_data , item_inventory , monster_data)

    print('Selamat datang di Arena !!!\n')
    print('Silahkan pilih monster yang anda ingin latih !!!\n')
    print('============ MONSTER LIST ============')

    monster_ids = []
    for index, data in enumerate(player_inventory, start=1):
        if 'id' in data:
            print(f'{index}. {data["type"]}, Level = {data["level"]}')
            monster_ids.append(str(index))
            
    # User memanggil monster
    user_monster_choice = input('Pilih monster untuk bertarung: ')

    # Looping terjadi apabila inputan user_monster_choice tidak sesuai dalam range
    while user_monster_choice not in monster_ids:
        print('''Pilihan monster tidak tersedia! Coba lagi!\n''')
        user_monster_choice = input('Pilih monster untuk bertarung: ')


    user_monster_choice_list = player_inventory[int(user_monster_choice)-1]
    user_monster_level = int(player_inventory[int(user_monster_choice)-1]['level'])
    
    user_monster_choice_name = user_monster_choice_list['type']
    user_monster_choice_attack_power = atribute_by_level(int(user_monster_choice_list['atk_power']), user_monster_level)
    user_monster_choice_defense_power = atribute_by_level(int(user_monster_choice_list['def_power']), user_monster_level)
    user_monster_choice_health_power = atribute_by_level(int(user_monster_choice_list['hp']), user_monster_level)
    user_monster_choice_health_power_max = atribute_by_level(int(user_monster_choice_list['hp']), user_monster_level)

    ## const
    strength_qty = 0
    resilience_qty = 0
    healing_qty = 0
    
    for data in player_inventory:
        if 'id' not in data:
            if data['type'] == 'strength':
                strength_qty = int(data['quantity'])
            if data['type'] == 'resilience':
                resilience_qty = int(data['quantity'])
            if data['type'] == 'healing':
                healing_qty = int(data['quantity'])

    for strength_ in potion_data:
        if strength_['potion_name'] == 'strength':
            strength_percentage = int(strength_['percentage'])
    for resilience_ in potion_data:
        if resilience_['potion_name'] == 'resilience':
            resilience_percentage = int(resilience_['percentage'])
    for healing_ in potion_data:
        if healing_['potion_name'] == 'resilience':
            healing_percentage = int(healing_['percentage'])

    # Insialisasi variabel untuk digunakan dalam loop
    over = False
    clear = False
    lose = False
    win = False
    total_attack_user = 0
    total_attack_enemy = 0
    turn_round = 1
    stage_round = 1
    oc_prize = 0

    while not clear:
        print(f'============ STAGE {stage_round} ============')
        
        rng_monster = lcg.LCG(0, len(monster_data)) # RNG mengasumsikan bahwa batas sebanyak baris dari list monster database

        monster_enemy = monster_data
        desired_monster_enemy = monster_enemy[rng_monster-1]
        level_monster_enemy = stage_round

        # Memilah nama, atk, def, dan health power monster musuh
        monster_enemy_name = desired_monster_enemy['type']
        attack_power_monster_enemy = atribute_by_level(int(desired_monster_enemy['atk_power']), level_monster_enemy)
        defense_power_monster_enemy = atribute_by_level(int(desired_monster_enemy['def_power']), level_monster_enemy)
        health_monster_enemy = atribute_by_level(int(desired_monster_enemy['hp']), level_monster_enemy)
        health_monster_enemy_max = atribute_by_level(int(desired_monster_enemy['hp']), level_monster_enemy)

        print(f'''RAWRRR, Agent {username} mengeluarkan monster {user_monster_choice_name} !!!\n''')
        # Mengeluarkan ASCII art monster user
        print(r'''
           _/\----/\\   
          /         \\     /\\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \\  |  |
        /   `^^^^^'    \\ |  |
      ./  /|            \\|  |_
     /   / |         |\\__     /
     \\  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__

      ''')
        # Mengeluarkan deskripsi monster user
        print_hp_bar(user_monster_choice_name, user_monster_choice_health_power, user_monster_choice_health_power_max)
        print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
        
        print(f'''RAWRRR, Monster {monster_enemy_name} telah muncul !!!''')

        # Mengeluarkan ASCII art monster musuh
        print(r'''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

      ''')
        # Mengeluarkan deskripsi monster musuh
        print_hp_bar(monster_enemy_name, health_monster_enemy, health_monster_enemy_max)
        print(f'Name : {monster_enemy_name}\nATK Power : {attack_power_monster_enemy}\nDEF Power : {defense_power_monster_enemy}\nHP : {health_monster_enemy}\nLevel : {level_monster_enemy}\n')
        
        over = False
        while not over:
            # RNG user
            attack_user_rng = math.floor(lcg.LCG(30 * user_monster_choice_attack_power/100, 70 * user_monster_choice_attack_power/100))
            defense_user_rng = math.floor(lcg.LCG(0, defense_power_monster_enemy))
            reduced_attack_user = math.floor((100 - defense_user_rng) * attack_user_rng/100)

            # RNG musuh
            attack_enemy_rng = math.floor(lcg.LCG(30 * attack_power_monster_enemy/100, 70 * attack_power_monster_enemy/100))
            defense_enemy_rng = math.floor(lcg.LCG(0, user_monster_choice_defense_power))
            reduced_attack_enemy = math.floor((100 - defense_enemy_rng) * attack_enemy_rng/100)
            
            print(f'============ TURN {turn_round} ({user_monster_choice_name}) ============')
            print('============ USER TURN ============')
            print('''1. Attack\n2. Use Potion\n3. Quit\n''')
            while True:
                try:
                    user_choice = int(input('Pilih perintah: ')) # User memilih perintah
                    break
                except ValueError:
                    print('Input anda salah! Ulangi.')
            subprocess.run('cls', shell=True)
            
            if user_choice == 1: # Ketika user memilih untuk Attack
                health_monster_enemy = math.floor(health_monster_enemy - reduced_attack_user) # HP monster musuh berkurang oleh ATK monster user yg sudah ter-RNG
                total_attack_user += reduced_attack_user
                
                if health_monster_enemy <= 0: 
                    health_monster_enemy = 0 # Mengembalikan HP monster musuh yang tidak boleh kurang dari 0
                    win = True # Jika HP monster musuh sudah 0
                # delay()
                print(r'''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

      ''')

                print(f'SKADIDODOO, {user_monster_choice_name} menyerang {monster_enemy_name} !!!\n')
                print_hp_bar(monster_enemy_name, health_monster_enemy, health_monster_enemy_max)
                print(f'Name : {monster_enemy_name}\nATK Power : {attack_power_monster_enemy}\nDEF Power : {defense_power_monster_enemy}\nHP : {health_monster_enemy}\nLevel : {level_monster_enemy}\n')
                print(f'# Penjelasan: ATT: {attack_user_rng}, Reduced by: {defense_user_rng}, ATT Results: {reduced_attack_user}')
                
                # Jika menang
                if win:
                    print(f'Selamat anda mengalahkan monster {monster_enemy_name} !!!')
                    # Permainan selesai
                    over = True
                    clear = True
                    
                    break
                
                # Monster musuh gantian menyerang
                print(f'============ TURN {turn_round} ({monster_enemy_name}) ============')
                print('============ ENEMY TURN ============')
                user_monster_choice_health_power = math.floor(user_monster_choice_health_power - reduced_attack_enemy) # HP monster user berkurang oleh ATK monster user yg sudah ter-RNG
                total_attack_enemy += reduced_attack_enemy
                
                if user_monster_choice_health_power <= 0:
                    user_monster_choice_health_power = 0 # Mengembalikan HP monster user yang tidak boleh kurang dari 0
                    lose = True # Jika HP monster user sudah 0
                    
                # Deskripsi penyerangan dan dampak pada monster user
                print(r'''
           _/\----/\\   
          /         \\     /\\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \\  |  |
        /   `^^^^^'    \\ |  |
      ./  /|            \\|  |_
     /   / |         |\\__     /
     \\  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__

      ''')
                print(f'SKADLIDODOR, {monster_enemy_name} menyerang {user_monster_choice_name} !!!\n')
                print_hp_bar(user_monster_choice_name, user_monster_choice_health_power, user_monster_choice_health_power_max)
                print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                print(f'# Penjelasan: ATT: {attack_enemy_rng}, Reduced by: {defense_enemy_rng}, ATT Results: {reduced_attack_enemy}')
                
                # Jika kalah
                if lose:
                    print(f'Tidakkk, kamu telah dikalahkan oleh {monster_enemy_name} !!!')
                    # Permainan selesai
                    over = True 
                    clear = True
                turn_round += 1

            elif user_choice == 2: # Ketika user memilih potion
                print('============ POTION LIST ============')
                # Deskripsi potion yang tersedia
                print(f'''1. Strength Potion (Qty: {strength_qty}) - Increases ATK Power\n2. Resilience Potion (Qty: {resilience_qty}) - Increases DEF Power\n3. Healing Potion (Qty: {healing_qty}) - Restores Health\n4. Cancel''')
                
                while True:
                    try:
                        user_potion_choice = int(input('Pilih perintah: \n')) # User memilih potion atau cancel
                        break
                    except ValueError:
                        print('Input anda salah! Ulangi.')
                        
                if user_potion_choice == 1: # Jika user memilih potion strength
                    if strength_qty == 0: # Jika potion strength tidak tersedia
                        print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
                    else: # Jika potion strength tersedia
                        user_monster_choice_attack_power *= (strength_percentage + 100) / 100 # Attack power bertambah
                        strength_qty -= 1 # Ketersediaan potion berkurang 1
                        
                        # Deskripsi perubahan pada monster user
                        print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                        print(f'# Penjelasan: Attack power monster bertambah sebesar {strength_percentage}% menjadi: {user_monster_choice_attack_power}')
                                
                elif user_potion_choice == 2: # Jika user memilih potion resilience
                    if resilience_qty == 0: # Jika poton resilience tidak tersedia
                        print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
                    else: # Jika potion resilience tersedia
                        user_monster_choice_defense_power *= (resilience_percentage + 100) / 100
                        resilience_qty -= 1 # Ketersediaan potion berkurang 1
                        
                        # Deskripsi perubahan pada monster user
                        print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                        print(f'# Penjelasan: Defense power monster bertambah sebesar {resilience_percentage}% menjadi: {user_monster_choice_defense_power}')
                        
                elif user_potion_choice == 3: # Jika user memilih potion healing
                    if healing_qty == 0: # Jika potion healing tidak tersedia
                        print('Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!')
                    else: # Jika potion healing tersedia
                        user_monster_choice_health_power *= (healing_percentage + 100) / 100
                        healing_qty -= 1 
                                
                        # Deskripsi perubahan pada monster user
                        print(f'Name : {user_monster_choice_name}\nATK Power : {user_monster_choice_attack_power}\nDEF Power : {user_monster_choice_defense_power}\nHP : {user_monster_choice_health_power}\nLevel : {user_monster_level}\n')
                        print(f'# Penjelasan: Health power monster bertambah sebesar {healing_percentage}% menjadi: {user_monster_choice_health_power}')
                        
                    if user_monster_choice_health_power > user_monster_choice_health_power_max: # Jika HP monster user bertambah lebih dari maksimum HP-nya
                        user_monster_choice_health_power = user_monster_choice_health_power_max # HP monster user akan sama dengan HP monster maksimumnya
                        
                elif user_potion_choice == 4: # Jika user memilih cancel
                    over = False # Kembali looping 
                
                else: # Jika pilihan user tidak tersedia
                    print('Perintah yang diberikan tidak tersedia, coba ulangi!')

            elif user_choice == 3: # Jika user memilih Quit
                print('Anda berhasil kabur dari BATTLE !')
                lose = True
                clear = True
                break
            
            else: 
                print('Perintah yang diberikan tidak tersedia, coba ulangi!')
        
        if lose: # Jika kalah dalam battle di arena
            print(f'GAME OVER! Sesi latihan berakhir pada stage {stage_round}')
            print('============== STATS ==============')
            print(f'OC Prize : {oc_prize}\nJumlah stage : {stage_round}\nDamage diberikan : {math.floor(total_attack_user)}\nDamage diterima : {math.floor(total_attack_enemy)}\n')
            coin = int(coin)
            coin += oc_prize
            cmd = input('Tekan apapun untuk keluar: ')
            
        elif stage_round >= 5: # Jika stage telah selesai
            print('Selamat! Anda telah menyelesaikan semua stage')
            print('============== STATS ==============')
            print(f'OC Prize : {oc_prize}\nJumlah stage : {stage_round}\nDamage diberikan : {math.floor(total_attack_user)}\nDamage diterima : {math.floor(total_attack_enemy)}\n')
            coin = int(coin)
            coin += oc_prize
            clear = True
            cmd = input('Tekan apapun untuk keluar: ')
            
        elif win: # Jika menang dalam battle di arena
            print('Menuju ke stage berikutnya....')
            over = False
            clear = False
            lose = False
            win = False
            user_monster_choice_health_power = user_monster_choice_health_power_max
            health_monster_enemy = health_monster_enemy_max
            oc_prize += 30
            stage_round += 1
            turn_round = 1
            
        update_user_data(username, item_inventory, user_data, strength_qty, resilience_qty, healing_qty, coin)

def atribute_by_level(atribute:int, level:int):
    '''
    Menyesuaikan atribut monster berdasarkan level
    '''
    if level > 1:
        atribute = atribute + round(level * atribute * 0.1)
    return atribute

def update_user_data(username:str, item_inventory:list[dict], user_data:list[dict], qty_str:int, qty_res:int, qty_heal:int, coin:int):
    '''
    Update data dari user ketika setelah game
    '''
    for data in user_data:
        if username == data['username']:
            user_id = data['id']
            data['oc'] = str(coin)
    
    for data in item_inventory:
        if user_id == data['user_id']:
            if data['type'] == 'strength':
                data['quantity'] = str(qty_str)
            if data['type'] == 'resilience':
                data['quantity'] = str(qty_res)
            if data['type'] == 'healing':
                data['quantity'] = str(qty_heal)

def print_hp_bar(name:str, hp:int, max_hp:int, bar_length=50):
    """
    Mengeprint bar hp monster
    """   
    # Menghitung bar yang terisi
    filled_length = int(bar_length * hp / max_hp)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    # Print health bar
    print(f"{name} HP: [{bar}] {hp}/{max_hp}")
    
def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(3)
    if os.name == 'nt':  # Untuk Windows
        os.system('cls')
    else:  # Untuk Unix/Linux/Mac
        os.system('clear')

if __name__ == '__main__':
    monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path('data')
    arena('Asep_Spakbor',monster_data, monster_inventory_data, potion_data, item_inventory, user_data)