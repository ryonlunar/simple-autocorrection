import os
dirname = os.path.dirname(__file__)
import CSVfunction as csv
import DataPath as dp
import time

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(1)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')
    

def shop_currency_page(username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict], monster_inventory_data :list[dict], item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict] ):
    '''
    Membuat fitur shop dalam game dengan fungsi ini sebagai page pertamanya
    
    '''
    print('Irrasshaimase! Selamat datang di SHOP!!')
    cmd = input('Pilih aksi (lihat/beli/keluar): ')
    # user id
    for data in user_data:
        if username == data['username']:
            user_id = data['id'] 
                
    # item shop data
    if cmd == 'lihat':
        return lihat(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    elif cmd == 'beli':
        return beli(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id)
    elif cmd == 'keluar':
        print(f'Selamat tinggal {username}! Sampai bertemu lagi.')
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)

####################################################### FUNGSI UNTUK MELIHAT DATA #######################################################
def lihat(username:str, monster_shop_data:list[dict] , item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data:list[dict] , item_inventory :list[dict], monster_data:list[dict] , user_data:list[dict]):
    '''
    Membuat fungsi untuk melihat item apa saja yang dijual
    '''
    cmd = input('Mau lihat apa? (monster/potion)?: ')          
    if cmd == 'monster':
        lihat_monster(monster_shop_data, monster_data)
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    elif cmd == 'potion':
        item_shop_list = item_shop_arr(item_shop_data,potion_data)
        lihat_potion(item_shop_list)
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data , user_data )
    else:
        print('Perintah anda salah! Ulangi perintah anda.')
        delay()
        return lihat(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , )
####################################################### FUNGSI UNTUK MELIHAT DATA #######################################################        


####################################################### FUNGSI UNTUK MEMBELI #######################################################
def beli(username:str, monster_shop_data :list[dict], item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data :list[dict], item_inventory :list[dict] , monster_data :list[dict], user_data :list[dict], user_id:str):
    '''
    Membuat fungsi untuk membeli item atau monster yang dijual
    '''
    for data in user_data:
        if username == data['username']:
            coin = data['oc']
            
    print(f'Jumlah O.W.C.A coin mu sekarang {coin}')
    print()
    
    cmd = input('Mau beli apa? (monster/potion): ')
    if cmd == 'monster':
        beli_monster(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id, coin)
    elif cmd == 'potion':
        beli_potion(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data , user_id, coin)
    else:
        print('Perintah anda salah! Ulangi perintah anda!')
        return beli(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data ,user_id)
    
###################### MEMBELI MONSTER ########################
def beli_monster(username:str, monster_shop_data :list[dict] , item_shop_data :list[dict], potion_data:list[dict], monster_inventory_data :list[dict], item_inventory:list[dict] , monster_data:list[dict] , user_data:list[dict] ,user_id:str, coin:str):
    '''
    Membuat fungsi untuk membeli monster yang dijual
    '''
    coin = int(coin)
    ids_list = []
    for data in monster_shop_data:
        ids_list.append(data['monster_id'])
    monster_id = input('Masukkan monster id: ')
    if monster_id not in ids_list:
        print('Id tidak tersedia, silahkan coba id yang lain.')
        delay()
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    for data in monster_data:
        for subdata in monster_shop_data:
            if monster_id == data['id']:
                monster_type = data['type']
                monster_cost = int(subdata['price'])
                monster_stock = int(subdata['stock'])
    for data in monster_inventory_data:
        if monster_id == data['monster_id'] and user_id == data['user_id'] :
            print(f'Monster{monster_type}, sudah ada dalam inventory-mu! Pembelian dibatalkan.')
            return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
        
    if monster_stock == 0:
        print('Stock monster sudah habis, silahkan pilih yang lain')
    
    elif monster_cost > coin :
        print('OC-mu tidak cukup')
    
    else:
        monster_inventory_data.append({'user_id': user_id,'monster_id':monster_id,'level': '1'})
        print(f'Berhasil membeli item {monster_type}. Item sudah masuk ke inventory-mu!')
        for subdata in monster_shop_data:
            if monster_id == subdata['monster_id']:
                subdata['stock'] = str(monster_stock-1)
        for data in user_data:
            if user_id == data['id']:
                data['oc'] = str(coin-monster_cost)
                
    return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
###################### MEMBELI MONSTER ########################


###################### MEMBELI POTION ########################
def beli_potion(username:str, monster_shop_data:list[dict] , item_shop_data:list[dict] , potion_data:list[dict], monster_inventory_data:list[dict] , item_inventory :list[dict], monster_data :list[dict], user_data :list[dict],user_id:str, coin:str):
    '''
    Membuat fungsi untuk membeli item/potion yang dijual
    '''
    coin = int(coin)
    ids_list = []
    for data in item_shop_data:
        for subdata in potion_data:
            if data['type'] == subdata['potion_name']:
                ids_list.append(subdata['id'])
            
    item_id = input('Masukkan id potion: ')
    if item_id not in ids_list:
        print('Id tidak tersedia, silahkan coba id yang lain.')
        delay()
        return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)
    while True:
        try:
            qty = int(input('Masukkan jumlah: '))
            if qty > 0:
                break
            else:
                print('Input harus bilangan positif dan lebih dari 0!')
        except ValueError:
            print('Input harus berupa bilangan bulat! Ulangi')
    for data in potion_data:
        for subdata in item_shop_data:
            if item_id == data['id'] and data['potion_name'] == subdata['type']:
                item_type = subdata['type']
                item_cost = int(subdata['price'])
                item_stock = int(subdata['stock'])
                
    if item_stock == 0:
        print('Stock item sudah habis, silahkan pilih yang lain')
    
    elif item_cost*qty > coin :
        print('OC-mu tidak cukup')
    elif qty>item_stock:
        print('Kuantitas barang tidak mencukupi, silahkan ulangi')
    else:
        print(f'Berhasil membeli item: {qty} {item_type}. Item sudah masuk ke inventory-mu!')
        for subdata in item_shop_data:
            if item_type == subdata['type']:
                subdata['stock'] = str(item_stock-qty)
        for data in user_data:
            if user_id == data['id']:
                data['oc'] = str(coin-(qty*item_cost))
        temp = []
        for data in item_inventory:
            if user_id == data['user_id'] and item_type == data['type']:
                data['quantity'] = str(int(data['quantity'])+qty)
                temp.append(data['type'])
                
        if not temp:
            item_inventory.append({'user_id': str(user_id), 'type':str(item_type), 'quantity':str(qty)})
    
    delay()
    return shop_currency_page(username, monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)   
###################### MEMBELI POTION ########################
####################################################### FUNGSI UNTUK MEMBELI #######################################################

############################################### OTHER UTILITIES ###############################################################
def count_char_max(data_list:list[dict[str,str]], kolom:str, header:str):
    '''
    Fungsi untuk mengetahui karakter maksimal dalam kolom
    '''
    char_max = len(header)
    for i in range(len(data_list)):
        if len(data_list[i][kolom]) > char_max:
            char_max = len(data_list[i][kolom])
    return char_max

def lihat_monster(monster_shop_data:list[dict], monster_data:list[dict]):
    '''
    Fungsi untuk melihat monster
    '''
    list_of_len = [count_char_max(monster_shop_data, 'monster_id', 'ID'),
                    count_char_max(monster_data, 'type', 'Name/Type'),
                    count_char_max(monster_data, 'atk_power', 'ATK Power'),
                    count_char_max(monster_data, 'def_power', 'DEF Power'),
                    count_char_max(monster_data, 'hp', 'HP'),
                    count_char_max(monster_shop_data,'stock', 'Stok'),
                    count_char_max(monster_shop_data, 'price', 'Harga')]
    
    print(f"{'ID':<{list_of_len[0]}} | {'Name/Type':<{list_of_len[1]}} | {'ATK Power':<{list_of_len[2]}} | {'DEF Power':<{list_of_len[3]}} | {'HP':<{list_of_len[4]}} | {'Stok':<{list_of_len[5]}} | {'Harga':<{list_of_len[6]}}")
    print("-"*60)
    for data in monster_shop_data :
        for subdata in monster_data:
            if subdata['id'] == data['monster_id']:
                print(f"{subdata['id']:<{list_of_len[0]}} | {subdata['type']:<{list_of_len[1]}} | {subdata['atk_power']:<{list_of_len[2]}} | {subdata['def_power']:<{list_of_len[3]}} | {subdata['hp']:<{list_of_len[4]}} | {data['stock']:<{list_of_len[5]}} | {data['price']}")

def lihat_potion(item_shop_list:list[dict]):
    '''
    Fungsi untuk melihat potion/item
    '''
    list_of_len = [count_char_max(item_shop_list, 'id', 'ID'),
                    count_char_max(item_shop_list, 'type', 'Name/Type'),
                    count_char_max(item_shop_list,'stock', 'Stok'),
                    count_char_max(item_shop_list, 'price', 'Harga')]
    
    print(f"{'ID':<{list_of_len[0]}} | {'Name/Type':<{list_of_len[1]}} | {'Stok':<{list_of_len[2]}} | {'Harga':<{list_of_len[3]}}")
    print("-"*40)
    for data in item_shop_list :
        print(f"{data['id']:<{list_of_len[0]}} | {data['type']:<{list_of_len[1]}} | {data['stock']:<{list_of_len[2]}} | {data['price']:<{list_of_len[3]}}")

def item_shop_arr(item_shop_data:list[dict],potion_data:list[dict]):
    '''
    Membuat list item yang terdapat dalam shop beserta id-nya
    '''
    item_shop_list = []
    for data in potion_data:
            for subdata in item_shop_data:
                if data['potion_name'] == subdata['type']:
                    item_shop_list.append({'id': data['id'],'type': subdata['type'], 'stock': subdata['stock'],'price': subdata['price']})
    return item_shop_list
        
############################################### OTHER UTILITIES ###############################################################

if __name__ == '__main__':
    monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data = dp.data_path('data')
    #  = pi.player_inventory('Asep_Spakbor', user_data , monster_inventory_data , item_inventory , monster_data)
    shop_currency_page('bimo', monster_shop_data , item_shop_data , potion_data, monster_inventory_data , item_inventory , monster_data , user_data)