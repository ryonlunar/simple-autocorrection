import CSVfunction as csv
import os
import time
import DataPath as dp
dirname = os.path.dirname(__file__)

def delay():
    '''
    Membuat delay pada screen dan clear screen di terminal
    '''
    time.sleep(0.5)
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix/Linux/Mac
        os.system('clear')

def tampilan_awal(monster_list:list[dict]):
    '''
    Membuat tampilan pertama kali ketika masuk ke Monster Management
    '''
    print("Selamat Datang Para Agen")
    print("Di sini adalah tempat database para monster.")
    print("-"*50)
    return pilihan_monster_management(monster_list)

def pilihan_monster_management(monster_list:list[dict]):
    '''
    Membuat fungsi untuk memilih dalam monster management
    '''
    print(". . .")
    print("[1] Tampilkan semua monster yang ada")
    print("[2] Tambahkan monster baru")
    print('[3] Untuk kembali ke menu admin')
    pil = input("Anda ingin pilih aksi mana (1/2/3)?: ")
    if pil=='1' :
        delay()
        lihat_monster(monster_list)
        return pilihan_monster_management(monster_list)
    elif pil=='2':
        return tambah_monster_baru(monster_list)
    elif pil=='3':
        print("Keluar dari Monster Management")
        print(". . .")
        return None
    else:
        print('Input anda salah, ulangi!')
        delay()
        return pilihan_monster_management(monster_list)
    
def cek_kesamaan_nama(monster_list:list[dict], nama:str):
    '''
    Mengecek nama yang sama dalam data
    '''
    for data in monster_list:
        if data['type']== nama:
            return True

    return False

def tambah_monster_baru(monster_list:list[dict]):
    '''
    Fungsi untuk menambah atribut monster baru
    '''
    print("... Proses pembuatan monster baru dimulai ...")    
    print()
    nama = input("Nama/Type Monster Baru : ")
    while cek_kesamaan_nama(monster_list, nama):
        print("Ups.. Nama Monster sudah terdaftar...")
        print("Silakan masukkan nama lain!")
        nama = input("Nama/Type Monster Baru : ")
    print()
    valid_int = set("0123456789")
    atk = input("ATK Power Monster Baru : ")
    while not all(char in valid_int for char in atk):
        print("ATK Power harus dalam angka yang bernilai positif...")
        print("Silakan coba lagi!")
        atk = input("ATK Power Monster Baru : ")
    Atk = int(atk)
    print()
    while True:
        try:
            defense = int(input("DEF Power Monster Baru (0-50) : "))
            if 0 <= defense <= 50:
                break 
            else:
                print("Def Power Monster harus bernilai 0-50...")
                print("Silakan coba lagi!")
        except ValueError:
            print("Input harus berupa bilangan bulat!")
    while True:
        try:
            hp = int(input("Nilai HP Monster Baru: "))
            if hp >= 0 :
                break 
            else:
                print("HP Monster harus bernilai bilangan positif")
                print("Silakan coba lagi!")
        except ValueError:
            print("Input harus berupa bilangan bulat!")
    
    monster_id = len(monster_list) + 1

    monster_baru = {'id':str(monster_id),'type':str(nama),'atk_power':str(Atk),'def_power':str(defense),'hp':str(hp)}
    
    print()
    return tambah_monster_ke_database(monster_list,monster_baru)
    
def tambah_monster_ke_database(monster_list:list[dict],monster_baru:dict):
    '''
    Fungsi untuk menambah monster baru ke dalam data base
    '''
    pilihan = input("Ingin menambahkan Monster baru ke database? (Y/N) : ")
    if pilihan.lower() == "y" :
        print("Monster baru berhasil ditambahkan ke database!")
        monster_list.append(monster_baru)
        return pilihan_monster_management(monster_list)
    elif pilihan.lower() == "n" :
        print("Monster baru gagal ditambahkan ke database!")
        return pilihan_monster_management(monster_list)
    else:
        print('Perintah anda salah, pilih (Y atau N)')
        return tambah_monster_ke_database(monster_list,monster_baru)
    
def count_char_max(data_list:list[dict[str,str]], kolom:str, header:str):
    '''
    Fungsi untuk mengetahui karakter maksimal dalam kolom
    '''
    char_max = len(header)
    for i in range(len(data_list)):
        if len(data_list[i][kolom]) > char_max:
            char_max = len(data_list[i][kolom])
    return char_max

def lihat_monster(monster_data:list[dict]):
    '''
    Fungsi untuk melihat monster
    '''
    list_of_len = [count_char_max(monster_data, 'id', 'ID'),
                    count_char_max(monster_data, 'type', 'Name/Type'),
                    count_char_max(monster_data, 'atk_power', 'ATK Power'),
                    count_char_max(monster_data, 'def_power', 'DEF Power'),
                    count_char_max(monster_data, 'hp', 'HP')]
    
    print("Memuat data Monster yang belum ada di shop")
    print(f"{'ID':<{list_of_len[0]}} | {'Name/Type':<{list_of_len[1]}} | {'ATK Power':<{list_of_len[2]}} | {'DEF Power':<{list_of_len[3]}} | {'HP':<{list_of_len[4]}}")
    print("-"*50)
    for data in monster_data :
        print(f"{data['id']:<{list_of_len[0]}} | {data['type']:<{list_of_len[1]}} | {data['atk_power']:<{list_of_len[2]}} | {data['def_power']:<{list_of_len[3]}} | {data['hp']:<{list_of_len[4]}}")

if __name__ == "__main__":
    monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data, user_data = dp.data_path('data')
    tampilan_awal(monster_data)