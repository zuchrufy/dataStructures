    #   stack merupakan sebuah data structure yang menggunakan prinsip LIFO (last in first out)
# 
    #   ilustrasi dari last in first out :
# 
        #   bayangkan ada sebuah tumpukan piring, piring pertama yang ditumpuk terletak paling bawah.
         
        #   sedangkan, piring terakhir yang diletakan berada pada tumpukan paling atas.

        #   dan apabila kita ingin mengambil sebuah piring pasti piring yang terakhir diletakan yang akan pertama diambil, karena posisinya yang berada diatas tumpukan



basic_element_dari_stack_adalah = {
    "push":"untuk menaruh element kedalam stack",
    "pop":"untuk mengeluarkan element dalam stack",
    "isempty":"untuk melihat apakah stack kosong",
    "isfull":"untuk melihat apakah stack penuh",
    "peek":"untuk melihat element stack paling atas tanpa mengambil data "
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

def stack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) -1 == -1


def isfull(stack):
    return len(stack)-1 == 16 

def push(stack, item):
    if isfull(stack):
        return print("maaf stack sudah penuh")
    stack.append(item)
    return print("stack pushed " + item)

def pop(stack):
    if isempty(stack):
        return print("stack sudah kosong")
    return print(stack[-1:])



stack = stack()
for i in range(0,17):
    push(stack,str(i))
print(stack)