data_produk = {
    "Produk 1" : {"nama" : "sabun lifegirl", "harga" : 5000, "stok" : 20},
    "Produk 2" : {"nama" : "pasta gigi pepsidont","harga" : 15000, "stok" : 34}, 
    "Produk 3" : {},
    "Produk 4" : {}
    }

while True:
    print("PENGELOLAAN DATA PRODUK")
    print("menampilkan data produk: ketik '1'")
    print("menambahkan data produk: ketik '2'")
    print("mengubah data produk: ketik '3'")
    print("menghapus data produk: ketik '4'")
    print("jika selesai: ketik 'selesai'")
    atur_data = input(": ")

    if atur_data == "selesai":
        print("Data produk anda: ")
        print(data_produk)
        print("Terima Kasih Telah Menggunakan Sistem Pengelolaan Data Produk!")
        break

    elif atur_data == "1":
        print("Data produk anda: ")
        print(data_produk)

    elif atur_data == "2":
        terisi = False
        for i in data_produk:
            if data_produk[i] == {}:
                menambahkan_nama = input("masukan nama produk: ")
                menambahkan_harga = int(input("masukan harga produk: "))
                menambahkan_stok = int(input("masukan stok produk: "))
                data_produk[i] = {"nama": menambahkan_nama, "harga": menambahkan_harga, "stok": menambahkan_stok}
                terisi = True
                print("Data produk sudah dimasukan!:")
                print(data_produk)
                break
        if not terisi:
            print("Semua data produk sudah terisi penuh, anda tidak bisa menambahkan lagi!")

    elif atur_data == "3": 
        pilih_ubah = input("masukan data produk yang ingin anda ubah (contoh: Produk 1): ")
        if pilih_ubah in data_produk and data_produk[pilih_ubah] != {}:
            nama_baru = input("masukkan nama baru: ")
            harga_baru = int(input("masukkan harga baru: "))
            stok_baru = int(input("masukkan stok baru: "))
            data_produk[pilih_ubah] = {"nama": nama_baru, "harga": harga_baru, "stok": stok_baru}
            print("Data produk sudah diubah")
            print(data_produk)
        else:
            print("Data produk masih kosong, silahkan tambahkan data produk dulu")

    elif atur_data == "4":
        pilih_hapus = input("masukan data produk yang ingin anda hapus (contoh: Produk 1): ")
        if pilih_hapus in data_produk and data_produk[pilih_hapus] != {}:
            data_produk[pilih_hapus] = {}
            print("Data produk sudah diubah")
            print(data_produk)
        else:
            print("Data produk masih kosong, silahkan tambahkan data produk dulu")

    else:
        print("Silahkan Ketik '1', '2', '3', '4', atau 'selesai'")
        continue


