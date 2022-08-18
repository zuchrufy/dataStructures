    #   stack merupakan sebuah data structure yang menggunakan prinsip LIFO (last in first out)
# 
    #   ilustrasi dari last in first out :
# 
        #   bayangkan ada sebuah tumpukan piring, piring pertama yang ditumpuk terletak paling bawah.
         
        #   sedangkan, piring terakhir yang diletakan berada pada tumpukan paling atas.

        #   dan apabila kita ingin mengambil sebuah piring pasti piring yang terakhir diletakan yang akan pertama diambil, karena posisinya yang berada diatas tumpukan



asic_element_dari_stack_adalah = {
    "push"      :   "untuk menaruh element kedalam stack",
    
    "pop"       :   "untuk mengeluarkan element dalam stack",
    
    "isempty"   :   "untuk melihat apakah stack kosong",
    
    "isfull"    :   "untuk melihat apakah stack penuh",
    
    "peek"      :   "untuk melihat element stack paling atas tanpa mengambil data "
    }

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#   stack alghoritma :
        #   sebuah penunjuk yang didefinisikan  TOP digunakan untuk melihat element teratas stack

        #   ketika membuat sebuah stack kita akan membuat value stack tersebut -1, agar kita bisa mengecek apakah stack kosong dengan mengomparisi TOP == -1 itu berarti nilai top berada pada dasar stack

        #   ketika melakukan push kita akan menaikan nilai TOP dan menaruh data baru dalam tumpukan stack pada posisi TOP

        #   ketika melakukan pop kita akan mengurangi value TOP 

        #   sebelum melakukan push kita harus melihat apakah stack sudah penuh

        #   apabila melakukan pop kita harus mengecek apakah stack sudah kosong


#___________________________________________ CODE IMPLEMENTATION OF STACK VALUE_________________________________________________________________________________


    #   untuk membuat list tempat menampung stack
def stack():
    stack = []
    return stack

#   untuk mengecek apakah stack kosong 
def isempty(stack):
    return len(stack) -1 == -1


#   tempat mengecek apakah stack penuh
def isfull(stack):
    return len(stack)-1 == 16 

#   tempat untuk menaruh data di stack
def push(stack, item):
    if isfull(stack):
        return print("maaf stack sudah penuh")
    stack.append(item)
    return print("stack pushed " + item)

#   tempat untuk mengeluarkan stack
def pop(stack):
    if isempty(stack):
        return print("stack sudah kosong")
    return stack.pop()

 
stack = stack()
for i in range(0,17):
    push(stack,str(i))



#   contoh program menggunakan stack 
#   membentuk reverse word



def create_stack():
    stack = []
    return stack
#   untuk memasukan stack
def pushStack(stack,kalimat):
    stack[:0] = kalimat
    return stack

def dibalik_kalimat(stack,new_stack):
    for i in range(0,len(stack)):
        stackPoped = stack.pop()

        new_stack.append(stackPoped)
    return new_stack
    
stack = create_stack()
reversed_stack = create_stack()

isi_stack = pushStack(stack,"jupri")

stack_dibalik = dibalik_kalimat(isi_stack,reversed_stack)

print(stack_dibalik)
