import DataPath as dp
import time
import os
        
def monster_not_in_shop(monster_shop_data:list[dict], monster_data:list[dict]):
    '''
    Membuat list untuk monster yang tidak ada dalam shop
    '''
    monster_not_in_shop_list = []
    id_monster_in_shop = []
    for data in monster_shop_data:
        id_monster_in_shop.append(data['monster_id'])
        
    for data in monster_data:
        if data['id'] not in id_monster_in_shop:
            monster_not_in_shop_list.append(data)
            
    return monster_not_in_shop_list

def item_not_in_shop(item_shop:list[dict]):
    '''
    Membuat list item yang tidak ada dalam shop
    '''
    item_list = ['healing', 'resilience', 'strength']
    item_type_in_shop = []

    for data in item_shop:
        item_type_in_shop.append(data['type'])    
    item_not_in_shop_list = [item for item in item_list if item not in item_type_in_shop]
    
    return item_not_in_shop_list

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


def tampilan_awal(username:str, item_shop:list[dict], monster_shop_data:list[dict], monster_data:list[dict], potion_data:list[dict]):
    '''
    Memberikan tampilan awal ketika admin pertama kali masuk ke shop management
    '''
    print(f"Halo {username}, Selamat datang kembali!")
    print("-~"*22)
    print("Terdapat beberapa pilihan aksi :")
    
    return memilih(username, item_shop, monster_shop_data, monster_data, potion_data)

def memilih(username:str, item_shop_data:list[dict], monster_shop_data:list[dict], monster_data:list[dict], potion_data:list[dict]):
    '''
    Menu untuk memilih opsi dalam shop management
    '''
    monster_not_in_shop_list = monster_not_in_shop(monster_shop_data,monster_data)
    item_not_in_shop_list = item_not_in_shop(item_shop_data)
    item_shop_list = item_shop_arr(item_shop_data, potion_data)
    
    print("[1] lihat, [2] tambah, [3] ubah, [4] hapus, [5] keluar ")
    pilihan = input("Mau pilih aksi yang mana? : ")
    
    if pilihan=="lihat" or pilihan=="1" : ############### MENU LIHAT #################
        validasi = False 
        while validasi == False :
            jenis = input("Mau lihat apa? (monster/potion) : ")
            if jenis=="monster" :
                validasi == True
                delay()
                lihat_monster(monster_shop_data, monster_data)
                break
            elif jenis=="potion" :
                validasi == True
                delay()
                lihat_potion(item_shop_list)
                break
            else : 
                validasi == False 
                print("Ups, Pilih antara monster atau potion!")
                print(". . .")

    elif pilihan=="tambah" or pilihan=="2" : ############### MENU TAMBAH #################
        validasi = False 
        while validasi == False :
            jenis = input("Mau tambah apa? (monster/potion) : ")
            if jenis=="monster" :
                validasi = True
                if len(monster_not_in_shop_list)>0:
                    delay()
                    tambah_monster(monster_not_in_shop_list, monster_shop_data, monster_data)
                else:
                    print('Semua monster telah ada di shop.')
                    delay()
                break
            elif jenis=="potion" :
                validasi = True
                if len(item_not_in_shop_list)>0:
                    delay()
                    tambah_potion(item_not_in_shop_list, item_shop_list, item_shop_data, potion_data)
                else:
                    print('Semua item telah berada di shop.')
                    delay()
                break
            else : 
                validasi = False 
                print("Ups, Pilih antara monster atau potion!")
                print(". . .")
                

    elif pilihan=="ubah" or pilihan=="3" : ############### MENU UBAH #################
        validasi = False 
        while validasi == False :
            jenis = input("Mau ubah apa? (monster/potion) : ")
            if jenis=="monster" :
                validasi = True 
                if len(monster_shop_data)>0:
                    delay()
                    ubah_monster(monster_shop_data, monster_data)
                else:
                    print('Tidak bisa mengubah, data tidak ada')
                    delay()
                break
                    
            elif jenis=="potion" :
                validasi = True 
                if len(item_shop_list)>0:
                    delay()
                    ubah_potion(item_shop_list, item_shop_data)
                else:
                    print('Tidak bisa mengubah, data tidak ada')
                    delay()
                break
            else : 
                validasi = False 
                print("Ups, Pilih antara monster atau potion!")
                print(". . .")
            
    elif pilihan=="hapus" or pilihan=="4" : ############### MENU HAPUS #################
        validasi = False 
        while validasi == False :
            jenis = input("Mau hapus apa? (monster/potion) : ")
            if jenis=="monster" :
                validasi = True 
                if len(monster_shop_data)>0:
                    delay()
                    monster_shop_data = hapus_monster(monster_shop_data, monster_data)
                else:
                    print('Tidak bisa menghapus, data tidak ada')
                    delay()
                break
                    
            elif jenis=="potion" :
                validasi = True
                if len(item_shop_list)>0:
                    delay()
                    item_shop_data = hapus_potion(item_shop_list, item_shop_data)
                else:
                    print('Tidak bisa menghapus, data tidak ada')
                    delay()
                break
            else : 
                validasi = False 
                print("Ups, Pilih antara monster atau potion!")
                print(". . .")
                
    elif pilihan=="keluar" or pilihan=="5" : ############### MENU KELUAR #################
        keluar(username)
        return
    else:
        print('Input anda salah! Ulangi.')
        delay()
        return memilih(username, item_shop_data, monster_shop_data, monster_data, potion_data)
    
    return memilih(username, item_shop_data, monster_shop_data, monster_data, potion_data)

################################################## FUNGSI UNTUK MELIHAT DATA #########################################################

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
        
################################################## FUNGSI UNTUK MELIHAT DATA #########################################################


################################################## FUNGSI UNTUK MENAMBAH DATA #########################################################
def tambah_monster(monster_not_in_shop_list:list[dict], monster_shop_data:list[dict], monster_data:list[dict]):
    '''
    Fungsi untuk menambah monster
    '''
    list_of_len = [count_char_max(monster_shop_data, 'monster_id', 'ID'),
                    count_char_max(monster_data, 'type', 'Name/Type'),
                    count_char_max(monster_data, 'atk_power', 'ATK Power'),
                    count_char_max(monster_data, 'def_power', 'DEF Power'),
                    count_char_max(monster_data, 'hp', 'HP')]
    
    print("Memuat data Monster yang belum ada di shop")
    print(f"{'ID':<{list_of_len[0]}} | {'Name/Type':<{list_of_len[1]}} | {'ATK Power':<{list_of_len[2]}} | {'DEF Power':<{list_of_len[3]}} | {'HP':<{list_of_len[4]}}")
    print("-"*50)
    for data in monster_not_in_shop_list :
        print(f"{data['id']:<{list_of_len[0]}} | {data['type']:<{list_of_len[1]}} | {data['atk_power']:<{list_of_len[2]}} | {data['def_power']:<{list_of_len[3]}} | {data['hp']:<{list_of_len[4]}}")
    
    ids_list = []
    for data in monster_not_in_shop_list:
        ids_list.append(data['id'])
        
    monster_id = get_numeric_input("Masukkan id monster yang ingin ditambah ke dalam shop : ")
    
    if monster_id not in ids_list:
        print('Tidak tersedia id tersebut, pilih id yang lain.')
        delay()
        return tambah_monster(monster_not_in_shop_list, monster_shop_data, monster_data)
    
    stok_baru = get_numeric_input("Masukkan stok baru monster : ")
    harga_baru = get_numeric_input("Masukkan harga baru monster : ")

    monster_shop_data.append({'monster_id': monster_id, 'stock': stok_baru, 'price': harga_baru})
    sort_data(monster_shop_data,'monster_id')
    
    for data in monster_data:
        if data['id'] == monster_id:
            nama = data['type']
            
    print(f"Proses menambahkan {nama} ke dalam shop telah berhasil!")


def tambah_potion(item_not_in_shop_list:list[dict], item_shop_list:list[dict], item_shop_data, potion_data:list[dict]):
    '''
    Fungsi untuk menambah potion
    '''
    list_of_len = [count_char_max(item_shop_list, 'id', 'ID'),
                    count_char_max(item_shop_list, 'type', 'Name/Type')]
    ids_list = []
    print("Memuat data Potion yang belum ada di shop")
    print(f"{'ID':<{list_of_len[0]}} | {'Name/Type':<{list_of_len[1]}}")
    for data in item_not_in_shop_list :
        for subdata in potion_data:
            if subdata['potion_name'] == data:
                print(f"{subdata['id']:<{list_of_len[0]}} | {subdata['potion_name']:<{list_of_len[1]}}")
                ids_list.append(subdata['id'])
    
    Id = get_numeric_input("Masukkan id potion yang ingin ditambahkan ke dalam shop : ")
    
    if Id not in ids_list:
        print('Tidak tersedia id tersebut, silahkan pilih id yang lain.')
        delay()
        return tambah_potion(item_not_in_shop_list, item_shop_list, item_shop_data, potion_data)
    
    stok_baru = get_numeric_input("Masukkan stok baru potion : ")
    harga_baru = get_numeric_input("Masukkan harga baru potion : ")
    
    for data in potion_data:
        if data['id'] == Id:
            nama_item = data['potion_name']
            
    item_shop_data.append({'type': nama_item, 'stock': stok_baru, 'price': harga_baru})
    print(f"Proses menambahkan {nama_item} ke dalam shop telah berhasil!")

################################################## FUNGSI UNTUK MENAMBAH DATA #########################################################



################################################## FUNGSI UNTUK MENGUBAH DATA #########################################################
def ubah_monster(monster_shop_data:list[dict], monster_data:list[dict]):
    '''
    Fungsi untuk mengubah monster
    '''
    print("Memuat keadaan Monster saat ini...")
    
    lihat_monster(monster_shop_data, monster_data)
    
    ids_list = []
    for data in monster_shop_data:
        ids_list.append(data['monster_id'])
        
    Id = get_numeric_input("Masukkan id monster yang ingin diubah : ")
    
    if Id not in ids_list:
        print('Tidak tersedia id tersebut, pilih id yang lain')
        delay()
        return ubah_monster(monster_shop_data, monster_data)

    stok_baru = get_numeric_input_boleh_kosong("Masukkan stok baru monster : ", allow_empty=True)
    harga_baru = get_numeric_input_boleh_kosong("Masukkan harga baru monster : ", allow_empty=True)

    if stok_baru != "" and harga_baru != "" :
        for subdata in monster_shop_data:
            if subdata['monster_id'] == Id:
                subdata['stock'] = str(stok_baru)
                subdata['price'] = str(harga_baru)
        
        for data in monster_data:
            if data['id'] == Id:
                nama = data['type']
                
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dengan stok baru berjumlah ", stok_baru, " dan harga baru ", harga_baru)

    elif harga_baru != "" :
        for subdata in monster_shop_data:
            if subdata['monster_id'] == Id:
                subdata['price'] = str(harga_baru)
        
        for data in monster_data:
            if data['id'] == Id:
                nama = data['type']
                
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dengan harga baru ", harga_baru)

    elif stok_baru != "":
        for subdata in monster_shop_data:
            if subdata['monster_id'] == Id:
                subdata['stock'] = str(stok_baru)
        
        for data in monster_data:
            if data['id'] == Id:
                nama = data['type']
                
        print("Pembaharuan data berhasil dilakukan pada monster ", nama, " dengan stok baru ", stok_baru)
    else:
        print('Tidak ada perubahan')
    delay()

def ubah_potion(item_shop_list:list[dict],item_shop_data:list[dict]) :
    '''
    Fungsi untuk mengubah potion
    '''
    
    lihat_potion(item_shop_list)
    
    ids_list = []
    for data in item_shop_list:
        ids_list.append(data['id'])
        
    Id = get_numeric_input("Urutan ke berapa yang ingin diganti? : ")
    
    if Id not in ids_list:
        print('Tidak tersedia id tersebut, pilih id yang lain')
        delay()
        return ubah_potion(item_shop_list,item_shop_data)
    
    stok_baru = get_numeric_input_boleh_kosong("Masukkan stok baru potion : ", allow_empty=True)
    harga_baru = get_numeric_input_boleh_kosong("Masukkan harga baru potion : ", allow_empty=True)

    if stok_baru != "" and harga_baru != "" :
        for data in item_shop_list:
            if data['id'] == Id:
                name_potion = data['type']
                for subdata in item_shop_data:
                    if name_potion == subdata['type']:
                        nama_potion = subdata['type']
                        subdata['stock'] = str(stok_baru)
                        subdata['price'] = str(harga_baru)
                
        print("Pembaharuan data berhasil dilakukan pada potion jenis ", nama_potion, " dengan stok baru berjumlah ", stok_baru, " dan harga baru ", harga_baru)

    elif harga_baru != "" :
        for data in item_shop_list:
            if data['id'] == Id:
                name_potion = data['type']
                for subdata in item_shop_data:
                    if name_potion == subdata['type']:
                        nama_potion = subdata['type']
                        subdata['price'] = str(harga_baru)
        print("Pembaharuan data berhasil dilakukan pada potion jenis ", nama_potion, " dengan harga baru ", harga_baru)

    elif stok_baru != "" :
        for data in item_shop_list:
            if data['id'] == Id:
                name_potion = data['type']
                for subdata in item_shop_data:
                    if name_potion == subdata['type']:
                        nama_potion = subdata['type']
                        subdata['stock'] = str(stok_baru)
                    
        print("Pembaharuan data berhasil dilakukan pada monster ", nama_potion, " dengan stok baru ", stok_baru)
    
    else:
        print('Tidak ada perubahan')
    delay()
################################################## FUNGSI UNTUK MENGUBAH DATA ######################################################### 



################################################## FUNGSI UNTUK MENGHAPUS DATA #########################################################         
def hapus_monster(monster_shop_data:list[dict], monster_data:list[dict]): 
    '''
    Fungsi untuk menghapus monster
    '''
    lihat_monster(monster_shop_data, monster_data)

    ids_list = []
    for data in monster_shop_data:
        ids_list.append(data['monster_id'])
        
    Id = get_numeric_input("Pilih ID monster yang ingin dihapus : ")
    
    if Id not in ids_list:
        print('Tidak tersedia id tersebut, pilih id yang lain.')
        delay()
        return hapus_monster(monster_shop_data, monster_data)
    
    for data in monster_shop_data:
        for subdata in monster_data:
            if data['monster_id'] == Id and subdata['id'] == Id:
                type_monster = subdata['type']
                id_monster = subdata['id']

    yes_no = input(f"Anda yakin ingin menghapus {type_monster} dari shop? (y/n) : ").lower()
    if yes_no == "y" :
        monster_shop_data_update = []
        for data in monster_shop_data:
            if data['monster_id'] != id_monster:
                monster_shop_data_update.append(data)
        
        monster_shop_data = monster_shop_data_update
        print(f"Done, {type_monster} telah berhasil dihapus dari shop.")
        delay()
        return monster_shop_data
        
    elif yes_no == "n" :
        print(f"{type_monster} dibatalkan untuk dihapus dari shop.")
        delay()
    else:
        print('Input anda salah, ulangi!')
        delay()
        return hapus_monster(monster_shop_data, monster_data)

def hapus_potion(item_shop_list:list[dict], item_shop_data:list[dict]):
    '''
    Fungsi untuk menghapus potion
    '''
    lihat_potion(item_shop_list)
    
    ids_list = []
    for data in item_shop_list:
        ids_list.append(data['id'])

    Id = get_numeric_input("Pilih ID potion yang ingin dihapus : ")
    
    if Id not in ids_list:
        print('Tidak tersedia id tersebut, pilih id yang lain.')
        delay()
        return hapus_monster(monster_shop_data, monster_data)

    for data in item_shop_list:
        if data['id'] == str(Id):
            type_potion = data['type']

    yes_no = input(f"Anda yakin ingin menghapus {type_potion} dari shop? (y/n) : ").lower()
    if yes_no == "y" :
        item_shop_data_update = []
        for data in item_shop_data:
            if data['type'] != type_potion:
                item_shop_data_update.append(data)

        item_shop_data = item_shop_data_update
        print(f"Done, {type_potion} telah berhasil dihapus dari shop.")
        delay()
        return item_shop_data

    elif yes_no == "n" :
        print(f"{type_potion} dibatalkan untuk dihapus dari shop.")
        delay()
    else:
        print('Input anda salah, ulangi!')
        delay()
        return hapus_potion(item_shop_list, item_shop_data)
################################################## FUNGSI UNTUK MENGHAPUS DATA ######################################################### 




################################################## FUNGSI UNTUK KELUAR ######################################################### 
def keluar(username:str) :
    '''
    Fungsi untuk keluar dari shop management
    '''
    print(f"Sampai jumpa lagi, {username}...")
    delay()
    return 
################################################## FUNGSI UNTUK KELUAR ######################################################### 



################################################## OTHER UTILITIES ######################################################### 
def count_char_max(data_list:list[dict[str,str]], kolom:str, header:str):
    '''
    Fungsi untuk mengetahui karakter maksimal dalam kolom
    '''
    char_max = len(header)
    for i in range(len(data_list)):
        if len(data_list[i][kolom]) > char_max:
            char_max = len(data_list[i][kolom])
    return char_max

def sort_data(data:list[dict],sortby:str):
    '''
    Mengurutkan data sesuai urutannya
    '''
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(data[j][sortby]) > int(data[j+1][sortby]):
                data[j], data[j+1] = data[j+1], data[j]
def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(1)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

def get_numeric_input(prompt:str):
    '''
    Fungsi untuk mengecek apakah input merupakan valid integer atau tidak
    '''
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return str(value)
            else:
                print('Input harus berupa bilangan positif! Ulangi!')
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def get_numeric_input_boleh_kosong(prompt: str, allow_empty: bool = False)-> str :
    '''
    Fungsi untuk mengecek apakah input merupakan valid integer atau tidak.
    Jika allow_empty bernilai True, input kosong juga dianggap valid.
    '''
    while True:
        user_input = input(prompt)
        if allow_empty and user_input == "":
            return user_input
        try:
            value = int(user_input)
            if value >= 0:
                return str(value)
            else:
                print('Input harus berupa bilangan positif! Ulangi')
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

################################################## OTHER UTILITIES #########################################################

if __name__ == '__main__':
    monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path('data')
    tampilan_awal('Asep_Spakbor',item_shop_data, monster_shop_data, monster_data, potion_data)
    