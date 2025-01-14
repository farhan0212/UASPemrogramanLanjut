
class Stack:
    def __init__(self, max_size=10): #Max stack menjadi 10 
        self.max_size = max_size
        self.top = -1
        self.data = [0] * self.max_size

    def is_full(self):
        return self.top == self.max_size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("Maaf, stack penuh")
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Data telah kosong!")
        else:
            print(f"Data yang terambil: {self.data[self.top]}")
            self.top -= 1

  
    # menu search untuk mencari data yang ada di stack
    def search(self, value): # membuat func search dengan parameter self dan value
        for i in range(self.top, -1, -1): # looping semua data yang ada di stack
            if self.data[i] == value: # kondisional jika data stack == value input 
                return i # maka return hasil value yang sesuai dengan data stack
        return -1 # jika tidak ditemukan maka hasilnya -1 atau false

    def print_stack(self):
        print("\nData yang terdapat dalam stack:")
        print("--------------------------------")
        if self.is_empty():
            print("Stack kosong")
            return
        for i in range(self.top, -1, -1):
            print("------")
            print(f"  | {self.data[i]} |")
            print("------")

    def clear(self):
        self.top = -1
        print("\nSekarang stack kosong")

def main():
    stackbaru = Stack()
    while True:
        print("\tPROGRAM STACK")
        print("\t===============")
        print("Menu:")
        print("1. Pop stack")
        print("2. Push stack")
        print("3. Cetak")
        print("4. cari stack")
        print("5. Bersihkan stack")
        print("6. Exit")

        menu = input("Menu pilihan Anda: ")

        if menu == '1':
            stackbaru.pop()
        elif menu == '2':
            dta = float(input("\nTambah Data\n-----------\nData yang akan disimpan di stack: "))
            stackbaru.push(dta)
        elif menu == '3':
            stackbaru.print_stack()
        elif menu == '4': 
            dta = float(input("\nCari Data\n-----------\nData yang akan dicari di stack: ")) # membuat inputan untuk menampung value yang akan menjadi argument
            hasil = stackbaru.search(dta) #membuat variabel baru untuk posisi stack di dalam array
            if hasil == -1: #kondisional ketika false
                print(f"Data {dta} tidak ditemukan") #return ketika data tidak ditemukan / false
            else:
                print(f"Data {dta} ditemukan pada posisi {hasil}") #kondisi ketika data ditemukan
        elif menu == '5':
            stackbaru.clear()
        elif menu == '6':
        
            break
        else:
            print("Pilihan tidak valid")

        ulang = input("\n\nUlang? (y/t): ")
        if ulang.lower() != 'y':
            break

if __name__ == "__main__":
    main()