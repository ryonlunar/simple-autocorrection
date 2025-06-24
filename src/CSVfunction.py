def head_csv(data: list[str])->list[str]:
    """
    Mengambil head dari list of list dalam csv
    """
    header = []
    for i in range(len(data[0])):
        header.append(data[0][i])
    return header

def list_of_dicts(head: list[str],data: list[str])->list[dict[str]]:
    """
    Membuat list of dictionary
    """
    list_of_dicts = []
    for inner_list in data:
        row_dict = {}
        for i, value in enumerate(inner_list):
            row_dict[head[i]] = value
        list_of_dicts.append(row_dict)
    return list_of_dicts

def data_csv(data: list[str])->list[str]:
    """
    Membuat data tanpa head
    """  
    datas = []
    for i in range(1,len(data)):
        datas.append(data[i])
    return datas

def read_csv(file_path: str)->list[dict[str]]:
    """
    Membaca file csv menjadi list of dictionarry
    """
    array = []
    temp = ''
    data_temp = []
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char != ';' and char != '\n':
                    temp += char
                else:
                    data_temp.append(temp)
                    temp = ''
            array.append(data_temp)
            data_temp = []
            
    head = head_csv(array)
    # print(head)
    array_data = data_csv(array)
    # print(array_data)
    data = list_of_dicts(head, array_data)
    return data
 

def write_csv(file_path: str,data: str)->str:
    """ 
    Menuliskan data ke file csv
    """
    with open(file_path, 'a') as csvfile:
        csvfile.write(data)
        
def join_array(data:list[str])->str:
    """ 
    Menggabungkan kembali list of dictionarry menjadi format csv
    """
    csv = ''
    keys = list(data[0].keys())
    for i in range(len(keys)):
        if i == len(keys)-1:
            csv+=keys[i]
            csv+='\n'
        else:
            csv+=keys[i]
            csv+=';'

    for i in range(len(data)):
        values = list(data[i].values())
        for j in range(len(keys)):
            if j == (len(keys)-1):
                csv+=values[j]
                csv += '\n'
            else:
                csv+=values[j]
                csv+=';'
    return csv

def generate_id(data:list[str])->int:
    num_id = len(data)
    # for i in range(len(data)):
    #     if num_id == data[i][0]:
    #         return generate_id(data)
    return num_id
    
if __name__ == '__main__':
    data = read_csv(r'if1210-2024-tubes-k02-i\data\user.csv')
    print(data)
    print(join_array(data))
    
