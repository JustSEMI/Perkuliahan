def rekursif(data):
    if len(data) == 0:
        return data
    else:
        return data[-1] + rekursif(data[:-1])   
string = input("Masukan data string: ")
print(rekursif(string))