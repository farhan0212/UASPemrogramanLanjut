import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table

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
            print("Maaf, antrian penuh")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.max_size
            self.data[self.rear] = value
            print(f"Data {value['np']} telah ditambahkan")
            self.visualize()

    def dequeue(self):
        if self.is_empty():
            print("Data kosong!")
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
            print("Antrian kosong")
        else:
            table = Table(title="Data Antrian")
            table.add_column("No", justify="center", style="cyan")
            table.add_column("Nama Penumpang", justify="left", style="magenta")
            table.add_column("Alamat", justify="left", style="green")
            table.add_column("Jenis Kelamin", justify="center", style="yellow")
            table.add_column("No Tempat Duduk", justify="center", style="blue")
            table.add_column("Biaya", justify="right", style="red")

            i = self.front
            while True:
                p = self.data[i]
                name_display = f"[red]{p['np']}[/red]" if p['np'] == highlight_name else p['np']
                table.add_row(str(i + 1), name_display, p['ap'], p['jk'], p['td'], "350000")
                if i == self.rear:
                    break
                i = (i + 1) % self.max_size

            console = Console()
            console.print(table)

    def clear(self):
        self.front = self.rear = -1
        self.data = [None] * self.max_size
        print("Antrian telah dikosongkan")
        self.visualize()

    def visualize(self):
        fig, ax = plt.subplots(figsize=(20, 4))
        ax.set_xlim(-1, self.max_size)
        ax.set_ylim(-1, 2)
        for i in range(self.max_size):
            rect_color = 'blue' if self.data[i] else 'gray'
            rect = plt.Rectangle((i, 0), 1, 1, color=rect_color)
            ax.add_patch(rect)
            if self.data[i]:
                ax.text(i + 0.5, 0.5, self.data[i]['np'], color='white', fontsize=12, ha='center', va='center')
        ax.axis('off')
        plt.show()

    def search(self, name):
        if self.is_empty():
            print("Data kosong!")
            return

        i = self.front
        found = False
        while True:
            if self.data[i] and self.data[i]['np'] == name:
                found = True
                break
            if i == self.rear:
                break
            i = (i + 1) % self.max_size

        if found:
            print(f"Data ditemukan pada posisi {i + 1}")
            self.print_queue(highlight_name=name)
        else:
            print("Data tidak ditemukan")

    def bubble_sort(self):
        if self.is_empty():
            print("Data kosong!")
            return

        n = (self.rear - self.front + self.max_size) % self.max_size + 1
        for i in range(n):
            for j in range(0, n - i - 1):
                idx1 = (self.front + j) % self.max_size
                idx2 = (self.front + j + 1) % self.max_size
                if self.data[idx1]['np'] > self.data[idx2]['np']:
                    self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        print("Data telah diurutkan")

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
            print(f"Data {value['np']} telah ditambahkan")

    def pop(self):
        if self.is_empty():
            print("Data kosong!")
        else:
            value = self.data.pop()
            print(f"Data yang terambil: {value['np']}")
            return value

    def print_stack(self):
        if self.is_empty():
            print("Data kosong!")
        else:
            table = Table(title="Data Stack")
            table.add_column("No", justify="center", style="cyan")
            table.add_column("Nama Penumpang", justify="left", style="magenta")
            table.add_column("Alamat", justify="left", style="green")
            table.add_column("Jenis Kelamin", justify="center", style="yellow")
            table.add_column("No Tempat Duduk", justify="center", style="blue")
            table.add_column("Biaya", justify="right", style="red")

            for i, item in enumerate(reversed(self.data)):
                table.add_row(str(i + 1), item['np'], item['ap'], item['jk'], item['td'], "350000")

            console = Console()
            console.print(table)

    @staticmethod
    def validate_gender(jk):
        return jk.upper() in ["L", "P"]

    @staticmethod
    def validate_seat_number(jk, td, occupied_seats):
        try:
            seat_number = int(td)
            if jk.upper() == "L":
                return 8 <= seat_number <= 22 and seat_number not in occupied_seats
            elif jk.upper() == "P":
                return 1 <= seat_number <= 6 and seat_number not in occupied_seats
        except ValueError:
            return False
        return False

def main():
    queue = None
    stack = None
    while True:
        print("Menu:")
        print("1. Tambah data penumpang")
        print("2. Tampilkan antrean")
        print("3. Cari data penumpang")
        print("4. Urutkan antrean")
        print("5. Keluar")

        choice = input("Pilih menu: ")
        if choice == "1":
            max_size = int(input("Masukkan kapasitas antrean: "))
            queue = Queue(max_size)
            stack = Stack(max_size)

            for _ in range(max_size):
                np = input("Nama penumpang: ")
                ap = input("Alamat penumpang: ")
                jk = input("Jenis kelamin (L/P): ")
                if not Stack.validate_gender(jk):
                    print("Jenis kelamin tidak valid!")
                    continue
                td = input("Nomor tempat duduk: ")
                if not Stack.validate_seat_number(jk, td, set()):
                    print("Nomor tempat duduk tidak valid!")
                    continue
                penumpang = {"np": np, "ap": ap, "jk": jk, "td": td}
                queue.enqueue(penumpang)
                stack.push(penumpang)

        elif choice == "2":
            if queue:
                queue.print_queue()
            else:
                print("Antrean belum dibuat.")

        elif choice == "3":
            if queue:
                name = input("Masukkan nama penumpang: ")
                queue.search(name)
            else:
                print("Antrean belum dibuat.")

        elif choice == "4":
            if queue:
                queue.bubble_sort()
                queue.print_queue()
            else:
                print("Antrean belum dibuat.")

        elif choice == "5":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
