import os
import time
dirname = os.path.dirname(__file__)
import DataPath as dp

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(1)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
    
# monster_list=[]
def laboratory(username:str, monster_inventory_data:list[dict] , user_data:list[dict] , monster_data:list[dict]):
    '''
    Membuat fitur shop dalam game dengan fungsi ini sebagai page utamanya
    
    '''
    # user id
    for name in user_data:
        if username == name['username']:
            user_id = name['id']
            coin=int(name['oc'])
            

    print(f'Selamat datang di laboratory {username}!!')
    print('Tekan 0 untuk kembali ke menu utama.')
    monster_list = display_monster_inventory(user_id,monster_inventory_data, monster_data)
    display_upgrade_price()
    try:
        monster_id = int(input("Pilih monster: "))
        if 1 <= monster_id <= len(monster_list):
            selected_monster = monster_list[monster_id - 1]
            monster_id, monster_name, level = selected_monster
            level = int(level)
            price= level_price(level)
            if level >= 5:
                print('Maaf,monster yang Anda pilih sudah memiliki level maksimum')
                delay()
                return laboratory(username, monster_inventory_data , user_data , monster_data)
            else:
                level_up = level + 1
                print(f"{monster_name} akan di upgrade ke level {level_up}.") 
                confirm = input("Lanjutkan upgrade (Y/N): ").lower()
                if confirm == 'y':
                    if coin >= price:
                        coin -= price
                        level = level_up
                        print(f"Selamat, {monster_name} berhasil di-upgrade ke level {level_up} !")
                        print(f"Jumlah O.W.C.A. Coin kamu sekarang {coin}.")
                        # Update jumlah coin
                        for user in user_data:
                            if user['id'] == user_id:
                                user['oc'] = str(coin)  
                        # Update data level 
                        for monster in monster_inventory_data:
                            if monster['user_id'] == user_id and monster['monster_id'] == monster_id:
                                monster['level'] = str(level)
                        delay()
                        return laboratory(username, monster_inventory_data , user_data , monster_data)
                        
                    else:
                        print("Maaf, Anda tidak memiliki cukup O.W.C.A. Coin untuk melakukan upgrade.")
                elif confirm == 'n':
                    print("Upgrade monster dibatalkan.")
                else:
                    print('Masukkan tidak valid')
                    delay()
                    return laboratory(username, monster_inventory_data , user_data , monster_data)
        elif monster_id == 0:
            print('Terimakasih telah berkunjung! Sampai bertemu kembali!')
            delay()
        else:
            print("Tidak ada monster tersebut")
            delay()
            return laboratory(username, monster_inventory_data , user_data , monster_data)
    except:
        print('Input harus berupa bilangan bulat')
        delay()
        return laboratory(username, monster_inventory_data , user_data , monster_data)
    
def level_price (level : int)-> int:
    """
    fungsi untuk menentukan harga upgrade ke level berikutny
    """
    if level == 1:
        price = 300
    elif level == 2:
        price = 500
    elif level == 3:
        price = 800
    elif level == 4:
        price = 1000
    elif level >= 5:
        price = 9999
    return price
    
def display_monster_inventory(user_id : str, monster_inventory_data:list[dict], monster_data:list[dict])->str:
    '''
    Fungsi untuk menampilkan inventaris monster.
    '''
    print("============ MONSTER LIST ============")
    index = 1
    
    monster_list = []
    temp = [{'id': monster['id'], 'type': monster['type'], 'atk_power': monster['atk_power'], 'def_power': monster['def_power'], 'hp': monster['hp']} for monster in monster_data]
    
    for data in monster_inventory_data:
        if user_id == data['user_id']:
            level = int(data['level'])
            monster_id = data['monster_id']
            for subdata in temp:
                if monster_id == subdata['id']:
                    monster_name = subdata['type']
                    print(f"{index}. {monster_name} (Level: {level})")
                    monster_list.append((monster_id, monster_name, level))
                    index += 1
                    
    return monster_list

def display_upgrade_price():
    '''
    Fungsi untuk menampilkan harga upgrade monster.
    '''
    print("============ UPGRADE PRICE ============")
    print("1. Level 1 -> Level 2: 300 OC")
    print("2. Level 2 -> Level 3: 500 OC")
    print("3. Level 3 -> Level 4: 800 OC")
    print("4. Level 4 -> Level 5: 1000 OC")
    
if __name__ =='__main__':
    monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data, user_data = dp.data_path('data')
    laboratory('Asep_Spakbor', monster_inventory_data , user_data , monster_data)
