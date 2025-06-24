import CSVfunction as csv
import os
dirname = os.path.dirname(__file__)
from GameState import game_state,username,is_admin

def check_input(username: str, password:str,user_data:list[dict])->bool:
    '''
    Mengecek input dari user
    '''
    is_admin = False
    for data in user_data:
        if username == data['username']:
            if password == data['password']:
                print(f'Selamat datang, Agent {username}!\nMasukkan command "help" untuk daftar command yang dapat kamu panggil.')
                game_state = 1
                if 'admin' == data['role']:
                    is_admin = True
                    game_state = 0
                return  game_state , is_admin , username
            else:
                print('Password salah!')
                game_state = 0
                username = ''
                return  game_state , is_admin , username
    print('Username tidak terdaftar !')
    game_state = 0
    username = ''
    return  game_state , is_admin , username
        
def user_login(data:list[dict]):
    '''
    Membuat fungsi login untuk menerima input dari user
    '''
    username = str(input('Username: '))
    password = str(input('Password: '))
    
    return check_input(username,password,data)


def login_page(game_state: int,username:str,user_data:list[dict])->int:
    '''
    Membuat lama login untuk user
    '''
    if game_state == 0:
        return user_login(user_data)
    else:
        print(f'Login gagal!\nAnda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali!')
        return game_state , is_admin , username
    
if __name__ == '__main__' :
    # username , password = user_login()
    # print(username)
    # print(user_data)
    print(is_admin)
    print(game_state)
    login_page(game_state,'bimo')
    print(game_state)
    print(is_admin)