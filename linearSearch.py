

#   linear search alghoritma adalah sebuah algoritma pencarian yang mencari suatu data dari index pertama dan linear ke index selanjutnya

#   linear search alghoritm:

#     1. buat function yang mengambil input array, index, limit dari perulangan, target data yang _DispatchArity
    
#     2. deifinisikan percabangan sebagai flag batas pengulangan 

#     3. apabila array[index] ! = target maka akan muncul index +1 

#     4. apabila array[index] == target maka print index ke {index}


#   mendefinisikan sebuah fungsi input arguments
def linearSearch(arr,i,lim,target):
    



    #   mendefinisikan percabangan: apabila panjang data array kurang dari 1, maka algoritma linear search tidak dapat diterapkan   
    if len(arr) < 1 :
        return print("data tidak sesuai dan tidak bisa digunakan")

    #   mendefinisikan percabangan : apabila i = len(arr) return exit
    if lim == i :
        return print("data tidak ditemukan")    
    #   mendefinisikan percabangan : apabila panjang data array lebih dari 1, maka algoritma linear search dapat diterapkan 
    if len(arr) >1 :
        #   mendefinisikan percabangan : apabila data arr[i] == target maka akan return function dan berenti
        if arr[i] == target :
            return print(f"data yang diinginkan {target} berada pada index {arr[i]} ")

        #   mendefiniskan percabangan : apabila arr[i] != target maka akan memanggil kembali function return 

        elif arr[i] != target :
            #   memanggil kembali function secara recursive
            return linearSearch(arr,i+1,lim,target)


#   mendefinisikan sebuah array : LIST
arr = [1,2,3,4,5,6,7,8,9,10]
#   mendefinisikan vairable yang akan dicari di dalam LIST
target = 4
#   mendefiniskan panjang array : LIST
lim = len(arr) 
#   mendefinisikan vaariable awal pengulan recursivve "  i   "
i = 0
#   memanggil function: trigger function
linearSearch(arr,i,lim,target)



def func (arr,target):
    for i in arr:
        if i == target:
            return print(f"target berada di index{i}")

func([1,2,3,4,5,6,7,8],7)
