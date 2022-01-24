benda = ["laptop","handphon","komputer"]

mencari_benda = input("cari benda yang yang di inginkan :")

x = 0
while x < len(benda):
    if benda[x].upper() == mencari_benda.upper():
        print("ditemukan pada index ke-",x)
        break
    print("bukan",benda[x])
    x += 1


    



    
    
    
    


