
def help_menu(username: str, is_admin: bool)->None:
    '''
    menampilkan menu help di game
    '''
    if username == '' and not is_admin:
        pretext = 'Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.'
        
        main_text =  '''
        1. Login: Masuk ke dalam akun yang sudah terdaftar
        2. Register: Membuat akun baru
        3. Exit: keluar dari game
        '''
    elif is_admin:
        pretext = 'Halo admin! Selamat datang di menu bantuan. Kala tak tau arah, menu inilah tujuan-mu'
        
        main_text = '''
            Untuk dapat mengakses menu admin, anda perlu memasukkan command spesial pada start menu
            asepspakbortheboss ~~~ merupakan kata kunci tersebut!
            
            Di dalam menu admin akan terdapat:
            1. Shop Management: Untuk mengubah data dalam shop
            2. Monster Management: Untuk mengubah data monster
        '''
    else:
        pretext = f'Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang'
        
        main_text = '''
            1. Logout: Keluar dari akun yang sedang digunakan
            2. Menu: Memasuki main menu dan mulai petualanganmu!
            
            Dalam menu terdapat beberapa hal yang dapat kamu akses:
            
            1. Inventory : Untuk mengakses item/monster apa yang kamu punya
            2. Battle : Suka tantangan? Lawan monster galak di sini!
            3. Arena : Tempat latihan menantang dengan stage tertentu!
            4. Laboratory : Upgrade monster-mu hingga ke level maksimal
            5. Shop : Beli monster/item untuk membantu petualangan-mu!
            
        '''
    print(pretext)   
    print(main_text)
    cmd = input('Tekan apapun untuk kembali: ')
    return None


    
if __name__ == '__main__':
    help_menu('')
    