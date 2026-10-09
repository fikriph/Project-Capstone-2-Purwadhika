# Database outcrop batuan

outcrops = [
    {
        "id": "25PKP02-01",
        "location": "Bantimala",
        "easting": 791254,
        "northing": 9468849,
        "rock_type": "Batugamping",
        "formation": "Tonasa Fm."
    },
    {
        "id": "25PKP02-02",
        "location": "Bantimala",
        "easting": 791517,
        "northing": 9469003,
        "rock_type": "Batugamping",
        "formation": "Tonasa Fm."
    },
    {
        "id": "25PKP02-03",
        "location": "Bantimala",
        "easting": 797095,
        "northing": 9468604,
        "rock_type": "Batupasir",
        "formation": "Malawa Fm."
    },
    {
        "id": "25PKP02-04",
        "location": "Pangkajene",
        "easting": 802303,
        "northing": 9464288,
        "rock_type": "Batulempung",
        "formation": "Melange Complex"
    },
    {
        "id": "25PKP02-05",
        "location": "Pangkajene",
        "easting": 808962,
        "northing": 9473772,
        "rock_type": "Batulempung",
        "formation": "Melange Complex"
    },
    {
        "id": "25PKP02-06",
        "location": "Bantilama",
        "easting": 808428,
        "northing": 9472963,
        "rock_type": "Batupasir",
        "formation": "Malawa Fm."
    }
]



# Function untuk menampilkan data

def show_data(data):
    print("-----------------------------")
    print("ID         :", data["id"])
    print("Location   :", data["location"])
    print("Easting    :", data["easting"])
    print("Northing   :", data["northing"])
    print("Rock Type  :", data["rock_type"])
    print("Formation  :", data["formation"])


# Read Menu
def read_menu():
    while True:
        print("\n===== READ DATA =====")
        print("1. Melihat semua data")
        print("2. Melihat data tertentu")
        print("3. Melihat data berdasarkan batuan")
        print("4. Kembali ke menu utama")

        sub_menu = input("Pilih menu: ")

        # Melihat semua data
        if sub_menu == "1":
            if len(outcrops) == 0:
                print("\nDatabase masih kosong.")

            else:
                print("\n===== DAFTAR OUTCROP =====")
                print("=====  UTM ZONA 50S  =====")
                print("== DAERAH BANTIMALA DAN SEKITARNYA ==")
                for data in outcrops:
                    show_data(data)

        # Melihat data tertentu
        elif sub_menu == "2":
            if len(outcrops) == 0:
                print("\nDatabase masih kosong.")

            else:
                id = input("Masukkan ID outcrop: ")
                for data in outcrops:
                    if data["id"] == id:
                        show_data(data)
                        break
                else:
                    print("\nData dengan ID tersebut tidak ditemukan.")
        
        #Melihat data berdasarkan jenis batuan
        elif sub_menu == "3":
            jenis_batuan = input("Masukkan jenis batuan apa yang akan dicari: ").lower()
            data_sementara = []
            
            for data in outcrops:
                if data["rock_type"].lower() == jenis_batuan:
                    data_sementara.append(data)
            
            if len (data_sementara) == 0:
                print(f"\nJenis batuan {jenis_batuan} tidak ditemukan")
            
            else:
                print(f"\nBerikut daftar data dari jenis batuan {jenis_batuan}")
                for data in data_sementara:
                    show_data(data)

        # Kembali ke menu utama
        elif sub_menu == "4":
            break

        else:
            print("\nPilihan tidak tersedia.")

# Menu menambahkan data
def add_menu():
    while True:
        print("\n===== MENAMBAH DATA =====")
        print("1. Menambah data")
        print("2. Kembali ke menu utama")

        sub_menu = input("Pilih menu: ")

        # Menambah data
        if sub_menu == "1":
            id = input("Masukkan ID outcrop: ")

            # Mengecek apakah ID sudah digunakan
            for data in outcrops:
                if data["id"] == id:
                    print("ID tersebut sudah digunakan.")
                    break

            # Input data baru yang akan ditambahkan
            else:
                location = input("Masukkan lokasi: ")
                easting = input("Masukkan Easting: ")
                northing = input("Masukkan Northing: ")
                rock_type = input("Masukkan jenis batuan: ")
                formation = input("Masukkan formasi batuan: ")

                # Membuat data baru
                new_data = {
                    "id": id,
                    "location": location,
                    "easting": easting,
                    "northing": northing,
                    "rock_type": rock_type,
                    "formation": formation
                }

                print("\n===== DATA BARU =====")
                show_data(new_data)
                while True:      
                    confirm = input("Apakah data ingin disimpan? (y/n): ")

                    if confirm == "y":
                        outcrops.append(new_data)
                        print("\nData berhasil ditambahkan.")
                        break

                    elif confirm == "n":
                        print("\nPenambahan data dibatalkan.")
                        break
                    
                    else:
                        print("Masukkan 'y' untuk menambahkan dan 'n' untuk membatalkan")

        # Kembali ke menu 
        elif sub_menu == "2":
            break

        else:
            print("\nPilihan tidak tersedia.")

# Menu mengubah data
def update_menu():
    while True:
        print("\n===== MENGUBAH DATA =====")
        print("1. Mengubah data")
        print("2. Kembali ke menu utama")

        sub_menu = input("Pilih menu: ")

        # Mengubah data
        if sub_menu == "1":
            id = input("Masukkan ID outcrop: ")
            for data in outcrops:
                if data["id"] == id:
                    print("\nData ditemukan:")
                    show_data(data)

                    confirm = input("Apakah ingin mengubah data ini? (y/n): ")

                    if confirm == "y":
                        print("\nKolom yang dapat diubah:")
                        print("1. Location")
                        print("2. Easting")
                        print("3. Northing")
                        print("4. Rock Type")
                        print ("5.Formation")

                        column = input("Pilih kolom yang ingin diubah: ")

                        # Membuat data sementara
                        new_data = {
                            "id": data["id"],
                            "location": data["location"],
                            "easting": data["easting"],
                            "northing": data["northing"],
                            "rock_type": data["rock_type"],
                            "formation": data["formation"]
                        }

                        # Mengubah data sementara
                        if column == "1":
                            new_data["location"] = input("Masukkan location baru: ")

                        elif column == "2":
                            new_data["easting"] = input("Masukkan Easting baru: ")

                        elif column == "3":
                            new_data["northing"] = input("Masukkan Northing baru: ")

                        elif column == "4":
                            new_data["rock_type"] = input("Masukkan jenis batuan baru: ")
                        
                        elif column == "5":
                            new_data["formation"] = input("Masukkan formasi batuan baru: ")

                        else:
                            print("\nKolom tidak tersedia.")
                            break

                        print("\n===== DATA SETELAH PERUBAHAN =====")
                        show_data(new_data)

                        while True:
                            confirm_update = input("Apakah perubahan ingin disimpan? (y/n): ")

                            if confirm_update == "y":
                                data["location"] = new_data["location"]
                                data["easting"] = new_data["easting"]
                                data["northing"] = new_data["northing"]
                                data["rock_type"] = new_data["rock_type"]
                                data["formation"] = new_data["formation"]

                                print("\nData berhasil diperbarui.")
                                break

                            elif confirm_update == "n":
                                print("\nPerubahan dibatalkan.")
                                break

                            else:
                                print("Masukkan 'y' untuk konfirmasi update data dan 'n' untuk membatalkan update")

                    else:
                        print("\nPerubahan dibatalkan.")
                    break

            else:
                print("\nData dengan ID tersebut tidak ditemukan.")

        # Kembali ke menu utama
        elif sub_menu == "2":
            break

        else:
            print("\nPilihan tidak tersedia.")

# Menu menghapus data
def delete_menu():
    while True:
        print("\n===== MENGHAPUS DATA =====")
        print("1. Menghapus data")
        print("2. Kembali ke menu utama")

        sub_menu = input("Pilih menu: ")
        # Menghapus data
        if sub_menu == "1":
            id = input("Masukkan ID outcrop: ")
            for data in outcrops:
                if data["id"] == id:
                    print("\nData ditemukan:")
                    show_data(data)

                    while True:
                        confirm = input("Apakah yakin ingin menghapus data ini? (y/n): ")

                        if confirm == "y":
                            outcrops.remove(data)
                            print("\nData berhasil dihapus.")
                            break

                        elif confirm == "n":
                            print("\nPenghapusan dibatalkan.")
                            break
                        
                        else:
                            print("Masukkan 'y' untuk konfirmasi mengapus data dan 'n' untuk membatalkan menghapus")
                    
                    break

            else:
                print("\nData dengan ID tersebut tidak ditemukan.")

        # Kembali ke menu utama
        elif sub_menu == "2":
            break

        else:
            print("\nPilihan tidak tersedia.")

def summary_menu():
    print("\n===== DATABASE SUMMARY =====")

    # Menghitung total outcrop
    print("Total outcrop:", len(outcrops))

    print("\nJumlah berdasarkan jenis batuan:")

    for i in range(len(outcrops)):
        rock = outcrops[i]["rock_type"]

        # Mengecek apakah jenis batuan sudah muncul sebelumnya
        sudah_ada = False

        for j in range(i):
            if outcrops[j]["rock_type"] == rock:
                sudah_ada = True
                break

        # Hanya menghitung dan menampilkan jika belum pernah muncul
        if sudah_ada == False:
            count = 0

            for data in outcrops:
                if data["rock_type"] == rock:
                    count = count + 1

            print(f"{rock} : {count}")

# Menu Utama
while True:
    print("\n================================")
    print("   OUTCROP LOCATION DATABASE")
    print("         UTM ZONA 50S")
    print(" DAERAH BANTIMALA DAN SEKITARNYA")
    print("================================")

    print("1. Read")
    print("2. Menambah data")
    print("3. Mengubah data")
    print("4. Menghapus data")
    print("5. Database summary")
    print("6. Exit")   

    choice = input("Pilih menu: ")

    if choice == "1":
        read_menu()

    elif choice == "2":
        add_menu()

    elif choice == "3":
        update_menu()

    elif choice == "4":
        delete_menu()

    elif choice == "5":
        summary_menu()

    elif choice == "6":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak tersedia.")