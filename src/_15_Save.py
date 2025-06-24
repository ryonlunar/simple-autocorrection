import CSVfunction as csv
import DataPath as dp
import os

def save(user:list[dict], item_inventories:list[dict], item_shop:list[dict], monster, monster_shop:list[dict], monster_inventory:list[dict]) -> None:
    """
    memeriksa apakah folder yang dimaksud sudah ada dan akan membuat folder baru jika belum serta menyimpan file csv ke folder tersebut
    """
    # Tentukan folder utama sebagai "data"
    parent_folder= "data"
    # Menerima data sebagai list atau dictionary
    folder = get_valid_input("Masukkan nama folder: ")
    folder = "data/" + folder
    print("Saving...")
    # Periksa apakah folder /data sudah ada
    if not os.path.exists(parent_folder):
        print("Membuat folder data")
        # Buat parent folder jika belum ada
        os.makedirs(parent_folder)
    # Periksa apakah folder sudah ada
    
    if not  os.path.exists(folder):
        print(f"Membuat folder {folder}.")
        # Buat folder baru
        os.makedirs(folder)

    # Simpan data
    data_save(folder, "user", user)
    data_save(folder, "item_inventory", item_inventories)
    data_save(folder, "item_shop", item_shop)
    data_save(folder, "monster", monster)
    data_save(folder, "monster_shop", monster_shop)
    data_save(folder, "monster_inventory", monster_inventory)

    print(f"Berhasil menyimpan data di folder {folder}!")


def data_save(path : str, file_name : str, data ) -> None:
    file_path = path + "/" + file_name + ".csv"
    """
    menyimpan data dari bentuk list of dictionaries menjadi csv di suatu folder
    """
    if file_name == "item_inventory":
        sort_data(data,'user_id')
    elif file_name == "monster":
        sort_data(data,'id')
    elif file_name == "monster_inventory":
        sort_data(data, 'user_id')
    elif file_name == "monster_shop":
        sort_data(data, 'monster_id')
    elif file_name == "user":
        sort_data(data, 'id')
        
    data = csv.join_array(data)
    
    with open(file_path, 'w') as csvfile:
        csvfile.write(data)
            
def sort_data(data:list[dict],sortby:str):
    '''
    Mengurutkan data sesuai urutannya
    '''
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(data[j][sortby]) > int(data[j+1][sortby]):
                data[j], data[j+1] = data[j+1], data[j]
                
def is_valid_name(name:str):
    '''
    Memastikan bahwa input nama folder merupakan nama yang valid
    '''
    forbidden_characters = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
    reserved_names = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
    ]
    if name in reserved_names:
        return False
    for char in forbidden_characters:
        if char in name:
            return False
    return True

def get_valid_input(prompt:str):
    '''
    Meminta user untuk memasukkan nama folder, jika salah maka akan meminta user untuk mengulangi
    '''
    while True:
        user_input = input(prompt)
        if is_valid_name(user_input):
            return user_input
        else:
            print("Input invalid, gunakan nama lain!")
            
if __name__ == "__main__":
    monster_shop_data , item_shop_data, potion_data, monster_inventory_data, item_inventory, monster_data, user_data = dp.data_path('data')
    save(user_data, item_inventory, item_shop_data, monster_data, monster_shop_data, monster_inventory_data)
    # save(users, item_inventories, item_shop, monster, monster_shop, monster_inventory)

