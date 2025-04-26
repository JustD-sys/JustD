class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Menambahkan tugas baru ke daftar."""
        self.tasks.append(task)
        print(f"Tugas '{task}' telah ditambahkan.")

    def remove_task(self, task):
        """Menghapus tugas dari daftar."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tugas '{task}' telah dihapus.")
        else:
            print(f"Tugas '{task}' tidak ditemukan dalam daftar.")

    def display_tasks(self):
        """Menampilkan semua tugas dalam daftar."""
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("Daftar Tugas:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Tampilkan Tugas")
        print("4. Keluar")
        
        choice = input("Pilih opsi (1-4): ")
        
        if choice == '1':
            task = input("Masukkan tugas yang ingin ditambahkan: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Masukkan tugas yang ingin dihapus: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
