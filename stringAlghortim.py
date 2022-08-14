# tower of hanoi solution with dive and conquer alghorithm

from reprlib import recursive_repr


# alghoritm
# 1. buat function dengan parameter :
#     1.1 n sebagai jumlah berapa kali recursive atau looping sesuai tower yang diinginkan
#     1.2 parameter tower of hanoi string maupun integer, array maupun string biasa
# 2. buat percabangan batasan looping atau recursive
# 3. buat logika perpindahan tower1, ke tower c melalui tower b sebagai hash tower



def towerHanoi(n,tower1,tower2,tower3):
    if n == 1:
        print(f"kubik 1 {tower1} pindah ke tower 1")
        return 
    
    
    
