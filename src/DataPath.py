import CSVfunction as csv

import os
dirname = os.path.dirname(__file__)


def data_path(dir:str):
    '''
    Membuat fungsi datapath untuk mempermudah mencari data
    '''
    # data path
    user_data_path =  os.path.join(dirname, f'../{dir}/user.csv')
    monster_data_path =  os.path.join(dirname, f'../{dir}/monster.csv')
    monster_shop_path =  os.path.join(dirname, f'../{dir}/monster_shop.csv')
    item_shop_path =  os.path.join(dirname, f'../{dir}/item_shop.csv')
    monster_inventory_path =  os.path.join(dirname, f'../{dir}/monster_inventory.csv')
    item_inventory_path =  os.path.join(dirname, f'../{dir}/item_inventory.csv')
    potion_data_path = os.path.join(dirname, f'../data/_06_Potion.csv')
    
    # read data as list of dictionary
    monster_shop_data = csv.read_csv(monster_shop_path)
    item_shop_data = csv.read_csv(item_shop_path)
    user_data = csv.read_csv(user_data_path)
    monster_inventory_data = csv.read_csv(monster_inventory_path)
    item_inventory = csv.read_csv(item_inventory_path)
    monster_data = csv.read_csv(monster_data_path)
    potion_data = csv.read_csv(potion_data_path)
    return monster_shop_data , item_shop_data , potion_data,  monster_inventory_data , item_inventory , monster_data, user_data 