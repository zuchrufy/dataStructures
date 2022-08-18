# queue data structure adalah sebuah data structure yang memungkinkan sebuah data berjalan seperti antrian


# prinsip queue adalah first in first out (FIFO) yang mana berarti;

#         bahwa setiap proses akan menyelesaikan data y ang pertama kali masuk dan mengeluarkan inputan data yang pertama kali masuk 


# contoh pseudocode dari queue

#         1. bentuk sebuah array data [1,2,3,4,5]
#         2. maka yang akan dikeluarkan pertama kali adalah index array[0]
        


#   basic operation dari queue :

basic_operation = {

    "enqueue" : "menambahkan element pada akhir dari queue",

    "dequeue" : "menghilangkan atau mengeluarkan item dari depan queue",

    "isEmpty" : "memeriksa apakah queueu kosong atau tidak",

    "isFull"  : "untuk mengecek apakah queue penuh atau tidak",

    "peek"    : "mengambil value didepan queue tanpa menghilangkan indexnya"

}

#   working flow of queue:
    #   2 pointers FRONT and REAR
    #   FRONT : melacak element pertama dari queue
    #   REAR  : melacak element terakhir dari queue
    #   menginisialisasikan , FRONT and REAR berniali -1 

#   enqueue operation flow:
    #   periksa apakah queueu isFull
    #   untuk elemen pertama set value front == 0
    #   naikan value REAR index dengan + 1
    #   tambahkan elemen baru di posisi rear

#   dequeue operation flow:
    #   memeriksa apa queue kosong atau tidak 
    #   return value FRONT
    #   naikan value FRONT index by 1
    #   for the last elment, reset the values of FRONT and REAR to -1


class Queue:
    def __init__(self):
        self.queue = []
        
    
    def enqueu(self, item):
        self.queue.append(item)

    def isEmpty(self):
        return len(self.queue)-1 == -1

            
    def dequeue(self):
        if self.enqueu(self):
           return None
        return self.queue.pop(0) 

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.qeueu)       

queue = Queue()

for i in range(0,16):
    queue.enqueu(i)
queue.display()

for i in range(0,12):
    queue.dequeue()
queue.display()