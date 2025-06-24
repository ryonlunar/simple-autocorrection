import CSVfunction
import os
dirname = os.path.dirname(__file__)
from GameState import game_state

def validate_username(username: str)->bool:
    '''
    Memvalidasi username
    '''
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-0123456789")
    for char in username:
        if char not in valid_characters:
            return False
    return True

def choose_monster(monster_data: list[str],username:str):
    '''
    Memilih monster
    '''
    print('Silahkan pilih salah satu monster sebagai monster awalmu.')
    for monster in monster_data:
        print(f"{monster['id']}. {monster['type']}")
    
    ids = []
    for monster in monster_data:
        ids.append(int(monster['id'])) 
    while True:
        try:
            monster_id = int(input('Monster pilihanmu: '))
            break
        except ValueError:
            print('Input anda salah! Ulangi!')
    
    if monster_id in ids:
        print(f"Selamat datang agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster_data[monster_id-1]['type']}!")
        return monster_id
    
    else: 
        print('Monster pilihan anda tidak ada, silahkan pilih kembali.')
        return choose_monster(monster_data, username)
    
    
def check_register(username: str, password:str, user_data:list[dict])->tuple[str,str]:
    '''
    Meregister username dan memvalidasinya
    '''
    if not validate_username(username):
        print('Username hanya boleh berisi alfabet, angka, underscore, dan strip!')
        username = False
        password = False
        return username , password
    for data in user_data:
        if username == data['username']:
            print(f'Username {username} sudah terpakai, silahkan gunakan username lain!')
            username = False
            password = False
            return username , password
    return username , password

def user_input(user_data:list[dict]):
    '''
    Input username dan password user
    '''
    username = input('Masukkan username: ')
    password = input('Masukkan password: ')
    return check_register(username,password,user_data)
    
def register_page(game_state: int, username:str, monster_data:list[dict], monster_inventory:list[dict], user_data:list[dict]):
    '''
    Membuat laman register untuk user
    '''
    if game_state == 0:
        username, password = user_input(user_data)
        if username:
            monster_id = choose_monster(monster_data, username)
            user_data.append({'id': str(len(user_data)+1),'username':username,'password':password,'role':'agent','oc':f'0'})
            monster_inventory.append({'user_id': str(len(user_data)),'monster_id':f'{monster_id}','level':'1'})
            # CSVfunction.write_csv(user_data_path, f'{len(user_data)+1};{username};{password};agent;{0}\n')
            # CSVfunction.write_csv(monster_inventory_path,f'{len(user_data)+1};{monster_id};{1}\n')
            game_state = 1
            return username , game_state
        else:
            return username , game_state
    else:
        print(f'Register gagal!\nAnda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan register!')
        return username , game_state


if __name__ == '__main__':
    # print(game_state)
    register_page(game_state,'bimo') 
    

