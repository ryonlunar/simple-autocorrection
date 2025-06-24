from GameState import game_state

def logout(game_state: int,is_admin:bool)->bool:
    '''
    User akan logout dari permainan dan perlu login kembali
    '''
    if game_state == 1 or is_admin:
        print('Anda telah logout!')
        game_state = 0
        is_admin = False
        return game_state , is_admin
    else:
        print('Logout gagal!')
        print('Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout!')
        return game_state , is_admin

if __name__== '__main__':
    logout(1)
    print(game_state)