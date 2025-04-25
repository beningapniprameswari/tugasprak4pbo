def tampilkan_menu():

    print("\nPilih aksi:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Tampilkan daftar tugas")
    print("4. Keluar")

def tambah_tugas(daftar_tugas):

    tugas = input("Masukkan tugas yang ingin ditambahkan: ").strip()
    if not tugas:
        raise ValueError("Tugas tidak boleh kosong.")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

def hapus_tugas(daftar_tugas):

    if not daftar_tugas:
        raise Exception("Daftar tugas kosong, tidak ada yang bisa dihapus.")
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if nomor < 1 or nomor > len(daftar_tugas):
            raise IndexError(f"Tugas dengan nomor {nomor} tidak ditemukan.")
        tugas_dihapus = daftar_tugas.pop(nomor - 1)  
        print(f"Tugas '{tugas_dihapus}' berhasil dihapus!")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

def tampilkan_tugas(daftar_tugas):
    
    if not daftar_tugas:
        print("Daftar tugas kosong.")
    else:
        print("Daftar Tugas:")
        for idx, tugas in enumerate(daftar_tugas, 1):
            print(f"- {idx}. {tugas}")

def main():

    daftar_tugas = []  
    while True:
        tampilkan_menu()  
        pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
        try:
            if pilihan == '1':
                tambah_tugas(daftar_tugas)
            elif pilihan == '2':
                hapus_tugas(daftar_tugas)
            elif pilihan == '3':
                tampilkan_tugas(daftar_tugas)
            elif pilihan == '4':
                print("Keluar dari program.")
                break
            else:
                raise ValueError("Pilihan tidak valid. Harap pilih 1, 2, 3, atau 4.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()  