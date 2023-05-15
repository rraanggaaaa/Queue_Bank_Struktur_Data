class Customer:  # Membuat kelas bernama Customer
    def __init__(self, number, name): 
        self.number = number  # Inisialisasi atribut nomor dengan nilai yang diberikan
        self.name = name  # Inisialisasi atribut nama dengan nilai yang diberikan

class Queue:  # Membuat kelas bernama Queue
    def __init__(self):  
        self.items = []  # Membuat atribut list kosong untuk menyimpan elemen Queue

    def is_empty(self):  # Mengembalikan True jika Queue kosong, False jika sebaliknya
        return len(self.items) == 0

    def enqueue(self, customer):  # Menambahkan customer ke dalam Queue
        self.items.append(customer)

    def dequeue(self):  # Menghapus dan mengembalikan customer pertama dari Queue
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):  # Mengembalikan jumlah customer dalam Queue
        return len(self.items)

    def display_queue(self):  # Menampilkan nomor Queue dan nama customer dalam Queue
        if self.is_empty():
            print("Queue kosong.")
        else:
            print("Queue saat ini:")
            for customer in self.items:
                print(f"Nomor Queue: {customer.number}, Nama: {customer.name}")

queue = Queue()  # Membuat objek Queue menggunakan kelas Queue

while True:  # Loop utama
    print("\n","="*30)
    print("Sistem Queue Teller Bank")
    print("="*30,"\n")
    print("1. Tambahkan Queue")
    print("2. Panggil Queue")
    print("3. Jumlah Queue Saat Ini")
    print("4. Keluar")
    print("="*30,"\n")

    choice = input("Pilih opsi: ")  # Menerima input opsi dari pengguna
    print("="*30,"\n")

    if choice == "1":  # Opsi 1: Tambahkan Queue
        number = input("Masukkan nomor Queue: ")  # Menerima nomor Queue dari pengguna
        name = input("Masukkan nama: ")  # Menerima nama dari pengguna
        customer = Customer(number, name)  # Membuat objek customer menggunakan kelas Customer
        queue.enqueue(customer)  # Menambahkan customer ke dalam Queue
        print(f"Queue dengan nomor {number} dan nama {name} telah ditambahkan.")
        print("="*30,"\n")

    elif choice == "2":  # Opsi 2: Panggil Queue
        if queue.is_empty():
            print("Tidak ada Queue yang tersedia.")
            print("="*30,"\n")
        else:
            customer = queue.dequeue()  # Menghapus dan mengembalikan customer pertama dari Queue
            print(f"Queue dengan nomor {customer.number} dan nama {customer.name} dipanggil.")
            print("="*30,"\n")

    elif choice == "3":  # Opsi 3: Jumlah Queue Saat Ini
        print(f"Jumlah Queue saat ini:{queue.size()}")
        print("="*30,"\n")
        queue.display_queue()
        
    elif choice == "4":  # Opsi 4: Keluar
        print("Terima kasih. Program selesai.")
        print("="*30,"\n")
        break

    else:  # Opsi tidak valid
        print("Pilihan tidak valid. Silakan coba lagi.")
