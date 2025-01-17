import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

# UAS PEMROGRAMAN LANJUT
# Nama Kelompok : 
# Farhan Ramadan - 41524110029
# Muhammad Rifgi Al Hakim - 41523120013
# Sendy Ferdiansyah - 41523120026

class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.front = -1
        self.rear = -1
        self.data = [None] * self.max_size

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Maaf, queue penuh")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.data[self.rear] = value
            print(f"Data {value['np']} masuk ke queue")
            self.visualize()

    def dequeue(self):
        if self.is_empty():
            print("Data telah kosong!")
        else:
            print(f"Data yang terambil: {self.data[self.front]['np']}")
            self.data[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.max_size
            self.visualize()

    def print_queue(self, highlight_name=None):
        if self.is_empty():
            print("Queue kosong")
        else:
            table = Table(title="Data yang terdapat dalam queue")
            table.add_column("No", justify="center")
            table.add_column("Nama Penumpang", justify="left")
            table.add_column("Alamat Penumpang", justify="left")
            table.add_column("Jenis Kelamin", justify="center")
            table.add_column("No Tempat Duduk", justify="center")
            table.add_column("Biaya", justify="right")

            i = self.front
            while True:
                p = self.data[i]
                name_display = f"[red]{p['np']}[/red]" if p['np'] == highlight_name else p['np']
                table.add_row(str(i + 1), name_display, p['ap'], p['jk'], p['td'], str(350000))
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size

            console = Console()
            console.print(table)

    def clear(self):
        self.front = self.rear = -1
        self.data = [None] * self.max_size
        print("\nSekarang queue kosong")
        self.visualize()

    def visualize(self):
        fig, ax = plt.subplots(figsize=(20, 4))
        ax.set_xlim(-1, self.max_size)
        ax.set_ylim(-1, 2)
        for i in range(self.max_size):
            rect = plt.Rectangle((i, 0), 1, 1, edgecolor="black", facecolor="white")
            ax.add_patch(rect)
            if self.data[i] is not None:
                ax.text(i + 0.5, 0.5, str(self.data[i]['np']), ha='center', va='center', fontsize=12)

        if not self.is_empty():
            ax.text(self.front, -0.5, 'Front', ha='center', va='center', color='red')
            ax.text(self.rear, 1.5, 'Rear', ha='center', va='center', color='blue')

        plt.axis('off')
        plt.show()

    def search(self, name):
        if self.is_empty():
            print("Queue kosong")
        else:
            i = self.front
            found = False
            while True:
                if self.data[i] is not None and self.data[i]['np'] == name:
                    found = True
                    break
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size

            if found:
                print(f"\nData {name} ditemukan:")
                self.print_queue(highlight_name=name)
            else:
                print(f"Data {name} tidak ditemukan dalam queue.")

    def bubble_sort(self):
        if self.is_empty():
            print("Queue kosong, tidak bisa melakukan sorting.")
            return

        n = (self.rear - self.front + self.max_size) % self.max_size + 1

        for i in range(n):
            for j in range(0, n - i - 1):
                idx1 = (self.front + j) % self.max_size
                idx2 = (self.front + j + 1) % self.max_size
                if self.data[idx1]['np'] > self.data[idx2]['np']:
                    self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

        print("Queue telah di-sort berdasarkan nama penumpang menggunakan Bubble Sort.")

class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def is_full(self):
        return len(self.data) >= self.max_size

    def is_empty(self):
        return len(self.data) == 0

    def push(self, value):
        if self.is_full():
            print("Maaf, stack penuh")
        else:
            self.data.append(value)
            print(f"Data {value['np']} masuk ke stack")

    def pop(self):
        if self.is_empty():
            print("Stack kosong!")
        else:
            value = self.data.pop()
            print(f"Data yang terambil: {value['np']}")
            return value

    def print_stack(self):
        if self.is_empty():
            print("Stack kosong")
        else:
            table = Table(title="Data yang terdapat dalam stack")
            table.add_column("No", justify="center")
            table.add_column("Nama Penumpang", justify="left")
            table.add_column("Alamat Penumpang", justify="left")
            table.add_column("Jenis Kelamin", justify="center")
            table.add_column("No Tempat Duduk", justify="center")
            table.add_column("Biaya", justify="right")

            for i, item in enumerate(reversed(self.data)):
                table.add_row(str(i + 1), item['np'], item['ap'], item['jk'], item['td'], str(350000))

            console = Console()
            console.print(table)

def validate_gender(jk):
    return jk.upper() == 'L' or jk.upper() == 'P'

def validate_seat_number(jk, td, occupied_seats):
    seat_number = int(td)
    if jk.upper() == 'L':
        return 8 <= seat_number <= 20 and seat_number not in occupied_seats
    elif jk.upper() == 'P':
        return 1 <= seat_number <= 6 and seat_number not in occupied_seats
    return False

def menu():
    print("\nMenu Pilihan:")
    print("1. Tampilkan Queue")
    print("2. Tampilkan Stack")
    print("3. Tampilkan Searching")
    print("4. Tampilkan Sorting")
    print("5. Keluar")

def main():
    queue = None
    stack = None
    total_spent = 0
    bonuses = [
      (5250000, 7000000, "Liburan ke Bali"),
      (4550000, 4900000, "Liburan ke Surabaya"),
      (3850000, 4200000, "Liburan ke Yogyakarta"),
      (3150000, 3500000, "Liburan ke Bandung"),
      (2100000, 2800000, "Liburan ke Jakarta")
    ]

    while True:
        tiket = input("\tSilahkan Pilih Tiket (SE/EP/EK): ").upper()

        if tiket in ["SE", "EP", "EK"]:
            harga = {"SE": 350000, "EP": 325000, "EK": 300000}[tiket]
            pajak = {"SE": 0.025, "EP": 0.02, "EK": 0.015}[tiket]
            print(f"\tKelas Bus yang Dipilih Adalah: {['Super Executive', 'Eksekutif Plus', 'Eksklusif'][['SE', 'EP', 'EK'].index(tiket)]}")
            print(f"\tDengan Harga  : Rp. {harga} / orang")
            print("\t--------------------------------")
            jb = int(input("Masukan Jumlah Beli: "))
            print("\t--------------------------------")
            queue = Queue(jb)
            stack = Stack(jb)
            occupied_seats = set()

            for _ in range(jb):
                while True:
                    np = input("Masukan Nama Penumpang: ")
                    ap = input("Masukan Alamat Penumpang: ")
                    jk = input("Masukan Jenis Kelamin (L/P): ")
                    if not validate_gender(jk):
                        print("Jenis kelamin tidak valid. Masukkan L untuk Laki-laki atau P untuk Perempuan.")
                        continue
                    print("tempat duduk untuk Laki-laki adalah 8-22 dan untuk Perempuan adalah 1-6")
                    td = input("Silakan PIlih Tempat Duduk: ")
                    if not validate_seat_number(jk, td, occupied_seats):
                        print("Nomor tempat duduk tidak sesuai atau sudah terisi. Harap masukkan nomor tempat duduk yang valid.")
                        continue

                    penumpang = {"np": np, "ap": ap, "jk": jk, "td": td}

                    queue.enqueue(penumpang)
                    stack.push(penumpang)
                    occupied_seats.add(int(td))
                    total_spent += harga
                    break

            statusb = "Tidak Dapat Bonus"
            for min_spent, max_spent, bonus in bonuses:
                if min_spent <= total_spent <= max_spent:
                    statusb = f"Anda Mendapatkan Bonus {bonus}"
                    break

            print("----------------------------------------------------------------------------------------------------")
            print(f"Bonus Anda : {statusb}")
            print("----------------------------------------------------------------------------------------------------")
            print(" No | Nama Penumpang  | Alamat Penumpang | Jenis Kelamin | No Tempat Duduk | Biaya ")
            print("----------------------------------------------------------------------------------------------------")

            i = 1
            idx = queue.front
            while True:
                p = queue.data[idx]
                print(f" {i} | {p['np']} | \t {p['ap']} | {p['jk']} | {p['td']} | {harga}")

                if idx == queue.rear:
                    break
                idx = (idx + 1) % queue.max_size
                i += 1

            total_payment = total_spent + (total_spent * pajak)

            print("----------------------------------------------------------------------------------------------------")
            print(f"Pajak Pembayaran Anda Adalah (Rp.)\t : {total_spent * pajak}")
            print("----------------------------------------------------------------------------------------------------")
            print(f"Total Pembayaran Anda Adalah (Rp.)\t : {total_payment}")
            print("----------------------------------------------------------------------------------------------------")

            while True:
                ub = int(input("Masukkan Uang Pembayaran (Rp.)\t :"))
                if ub < total_payment:
                    print("Uang yang Anda masukkan kurang dari total pembayaran. Harap masukkan uang yang mencukupi.")
                else:
                    break

            print("----------------------------------------------------------------------------------------------------")
            print(f"Uang Kembali Adalah (Rp.)\t : {ub - total_payment}")
            print("----------------------------------------------------------------------------------------------------")

            batal = input("Apakah Anda ingin membatalkan pembelian? (y/t): ")

            if batal.lower() == 'y':
                queue.dequeue()
                occupied_seats.remove(int(td))

            break

    while True:
        menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            if queue is None:
                print("Queue belum dibuat. Silakan masukkan tiket terlebih dahulu.")
            else:
                queue.print_queue()
        elif pilihan == '2':
            if stack is None:
                print("Stack belum dibuat. Silakan masukkan tiket terlebih dahulu.")
            else:
                stack.print_stack()
        elif pilihan == '3':
            if queue is None:
                print("Queue belum dibuat. Silakan masukkan tiket terlebih dahulu.")
            else:
                name_to_search = input("Masukkan nama penumpang yang ingin dicari: ")
                queue.search(name_to_search)
        elif pilihan == '4':
            if queue is None:
                print("Queue belum dibuat. Silakan masukkan tiket terlebih dahulu.")
            else:
                queue.bubble_sort()
                queue.print_queue()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

