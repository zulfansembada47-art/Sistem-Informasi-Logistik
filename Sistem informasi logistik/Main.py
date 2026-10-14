class graph:
    def __init__(self):
        self.adj_list = {}

    def tambah_kota(self, kota):
        if kota not in self.adj_list.keys():
            self.adj_list[kota] = []
            print(f"Hub kota {kota} Berhasil Ditambahkan")
            return True
        else:
            print(f"Hub Kota {kota} Sudah Ada")
            return False

    def rute_antar_kota(self, kota1, kota2, jarak):
        if kota1 == kota2:
            print("Kota Asal dan Tujuan Tidak Boleh Sama!")
            return False
        if kota1 in self.adj_list.keys() and kota2 in self.adj_list.keys():
            self.adj_list[kota1].append((kota2, jarak))
            self.adj_list[kota2].append((kota1, jarak))
            return True
        return False


class Node:
    def __init__(self, no_resi, nama_pengirim, kota_asal, kota_tujuan, berat_paket, total_biaya_kirim):
        self.no_resi           = no_resi
        self.nama_pengirim     = nama_pengirim
        self.kota_asal         = kota_asal
        self.kota_tujuan       = kota_tujuan
        self.berat_paket       = berat_paket
        self.total_biaya_kirim = total_biaya_kirim
        self.left              = None
        self.right             = None


class binarysearchtree:
    def __init__(self):
        self.root = None

    def contains(self, no_resi):
        temp = self.root
        while temp is not None:
            if no_resi < temp.no_resi:
                temp = temp.left
            elif no_resi > temp.no_resi:
                temp = temp.right
            else:
                return True
        return False

    def insert(self, no_resi, nama_pengirim, kota_asal, kota_tujuan, berat_paket, total_biaya_kirim):
        new_node = Node(no_resi, nama_pengirim, kota_asal, kota_tujuan, berat_paket, total_biaya_kirim)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.no_resi < temp.no_resi:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.no_resi > temp.no_resi:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                return False

    def input_resi(self, graph):
        while True:
            input_kota_asal   = input("Masukkan Kota Asal    : ").strip().title()
            input_kota_tujuan = input("Masukkan Kota Tujuan  : ").strip().title()

            if input_kota_asal == input_kota_tujuan:
                print("Kota Asal dan Tujuan Tidak Boleh Sama!")
                continue

            if input_kota_asal not in graph.adj_list.keys():
                print("Rute pengiriman belum tersedia dalam jaringan!")
                pilih = input("Masih Ingin Input Resi Pengiriman? (Y/N) ").strip().upper()
                if pilih == "N":
                    print("Kembali Ke Sub Menu")
                    return
                continue

            if input_kota_tujuan not in graph.adj_list.keys():
                print("Rute pengiriman belum tersedia dalam jaringan!")
                pilih = input("Masih Ingin Input Resi Pengiriman? (Y/N) ").strip().upper()
                if pilih == "N":
                    print("Kembali Ke Sub Menu")
                    return
                continue

            jarak_km = None
            for tetangga, jarak in graph.adj_list[input_kota_asal]:
                if tetangga == input_kota_tujuan:
                    jarak_km = jarak
                    break

            if jarak_km is None:
                print("Rute pengiriman belum tersedia dalam jaringan!")
                pilih = input("Masih Ingin Input Resi Pengiriman? (Y/N) ").strip().upper()
                if pilih == "N":
                    print("Kembali Ke Sub Menu")
                    return
                continue

            no_resi = input("Masukkan No. Resi (4 digit) : ").strip()
            if len(no_resi) != 4 or not no_resi.isdigit():
                print("No. Resi harus tepat 4 digit angka!")
                continue
            if no_resi[0] != "2":
                print("No. Resi harus diawali angka '2'!")
                continue
            if self.contains(no_resi):
                print("No. Resi sudah terdaftar!")
                continue

            nama_pengirim = input("Masukkan Nama Pengirim : ").strip().title()
            if nama_pengirim == "":
                print("Nama pengirim tidak boleh kosong!")
                continue
            elif not any(huruf.isalpha() for huruf in nama_pengirim):
                print("Nama pengirim harus mengandung huruf!")
                continue

            try:
                berat_paket = float(input("Masukkan Berat Paket (kg) : "))
                if berat_paket <= 0:
                    print("Berat paket harus lebih dari 0!")
                    continue
            except ValueError:
                print("Berat paket harus berupa angka!")
                continue

            total_biaya_kirim = (jarak_km * 2000) + (berat_paket * 5000)
            print(f"Total Biaya Kirim Adalah : Rp {total_biaya_kirim:,.0f}")

            self.insert(no_resi, nama_pengirim, input_kota_asal, input_kota_tujuan, berat_paket, total_biaya_kirim)

            print("\n================================")
            print("        Input Resi Berhasil     ")
            print("================================")
            print(f"No. Resi      : {no_resi}")
            print(f"Nama Pengirim : {nama_pengirim}")
            print(f"Kota Asal     : {input_kota_asal}")
            print(f"Kota Tujuan   : {input_kota_tujuan}")
            print(f"Berat Paket   : {berat_paket} Kg")
            print(f"Total Biaya   : Rp {total_biaya_kirim:,.0f}")
            print("================================")

            while True:
                pilih = input("Apakah ingin melakukan input resi lagi (Y/N)? ").strip().upper()
                if pilih == "Y":
                    break
                elif pilih == "N":
                    print("Kembali ke Sub Menu...")
                    return
                else:
                    print("Input Tidak Valid, Silahkan Masukkan Y/N")

    def inorder(self):
        hasil = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            hasil.append(current_node)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return hasil

    def lihat_semua_resi(self):
        if self.root is None:
            print("Belum Ada Data Resi Terdaftar.")
            return
        hasil = self.inorder()
        print("\n================================")
        print("   Seluruh Data Resi Terdaftar  ")
        print("================================")
        for i, node in enumerate(hasil, start=1):
            print(f"\nData ke-{i}")
            print(f"No. Resi      : {node.no_resi}")
            print(f"Nama Pengirim : {node.nama_pengirim}")
            print(f"Kota Asal     : {node.kota_asal}")
            print(f"Kota Tujuan   : {node.kota_tujuan}")
            print(f"Berat Paket   : {node.berat_paket} Kg")
            print(f"Total Biaya   : Rp {node.total_biaya_kirim:,.0f}")
            print("--------------------------------")
        print(f"Total Resi: {len(hasil)}")
        print("\nKembali ke Sub Menu...")

    def urutkan_biaya_terbesar(self):
        if self.root is None:
            print("Belum Ada Data Resi Terdaftar.")
            return
        list_sementara = self.inorder()
        for i in range(len(list_sementara) - 1):
            min_index = i
            for j in range(i + 1, len(list_sementara)):
                if list_sementara[j].total_biaya_kirim > list_sementara[min_index].total_biaya_kirim:
                    min_index = j
            if i != min_index:
                temp = list_sementara[i]
                list_sementara[i] = list_sementara[min_index]
                list_sementara[min_index] = temp
        print("\n================================")
        print(" Resi Berdasarkan Biaya Terbesar")
        print("================================")
        for i, node in enumerate(list_sementara, 1):
            print(f"\nPeringkat ke-{i}")
            print(f"No. Resi      : {node.no_resi}")
            print(f"Nama Pengirim : {node.nama_pengirim}")
            print(f"Kota Asal     : {node.kota_asal}")
            print(f"Kota Tujuan   : {node.kota_tujuan}")
            print(f"Berat Paket   : {node.berat_paket} Kg")
            print(f"Total Biaya   : Rp {node.total_biaya_kirim:,.0f}")
            print("--------------------------------")
        print("\nKembali ke Sub Menu...")

g   = graph()
bst = binarysearchtree()

g.tambah_kota("Zulwonogiri")
g.tambah_kota("Jakarta")
g.tambah_kota("Yogyakarta")
g.tambah_kota("Semarang")
g.tambah_kota("Bandung")

g.rute_antar_kota("Zulwonogiri", "Jakarta",    150)
g.rute_antar_kota("Jakarta",     "Yogyakarta", 560)
g.rute_antar_kota("Yogyakarta",  "Semarang",   120)
g.rute_antar_kota("Semarang",    "Bandung",    300)
g.rute_antar_kota("Bandung",     "Zulwonogiri", 200)

list_kurir    = []
manifest      = {}
resi_terpakai = []



def input_data_kurir():
    while True:
        print("\n== Input Data Kurir ==")
        id_kurir = input("Masukkan ID Kurir: ").strip()

        if id_kurir == "":
            print("ID Kurir tidak boleh kosong!")
            continue
        elif not id_kurir.isdigit():
            print("ID Kurir harus berupa angka!")
            continue

        for kurir in list_kurir:
            if kurir["id_kurir"] == id_kurir:
                print(f"ID Kurir '{id_kurir}' sudah terdaftar!")
                break
        else:
            nama_kurir = input("Masukkan Nama Kurir : ").strip().title()
            if nama_kurir == "":
                print("Nama Kurir tidak boleh kosong!")
                continue
            elif not any(huruf.isalpha() for huruf in nama_kurir):
                print("Nama Kurir harus mengandung huruf!")
                continue

            print("Jenis Kendaraan:")
            print("1. Motor")
            print("2. Mobil")
            print("3. Truck")
            jenis = input("Pilih Jenis Kendaraan (1/2/3) : ").strip()

            if jenis == "1":
                jenis_kendaraan = "Motor"
            elif jenis == "2":
                jenis_kendaraan = "Mobil"
            elif jenis == "3":
                jenis_kendaraan = "Truck"
            else:
                print("Pilihan tidak valid! Pilih 1, 2, atau 3.")
                continue

            list_kurir.append({
                "id_kurir"        : id_kurir,
                "nama_kurir"      : nama_kurir,
                "jenis_kendaraan" : jenis_kendaraan
            })

            print("\n================================")
            print("  Data Kurir Berhasil Diinputkan ")
            print("================================")
            print(f"ID Kurir        : {id_kurir}")
            print(f"Nama Kurir      : {nama_kurir}")
            print(f"Jenis Kendaraan : {jenis_kendaraan}")
            print("================================")

        while True:
            pilih = input("\nApakah ingin menambahkan data Kurir lagi (Y/N)? ").strip().upper()
            if pilih == "Y":
                break
            elif pilih == "N":
                print("Kembali ke Sub Menu...")
                return
            else:
                print("Input Tidak Valid, Masukkan Y atau N!")


def plotting_manifest(bst):
    while True:
        print("\n== Plotting Penugasan Manifest ==")

        if not list_kurir:
            print("Belum ada data kurir terdaftar!")
            return
        
        if bst.root is None:
            print("Belum ada data resi terdaftar!")
            return

        print("\n--- Daftar Kurir ---")
        for kurir in list_kurir:
            print(f"ID: {kurir['id_kurir']} | Nama: {kurir['nama_kurir']} | Kendaraan: {kurir['jenis_kendaraan']}")

        id_kurir = input("\nMasukkan ID Kurir yang ditugaskan : ").strip()

        kurir_valid = None
        for kurir in list_kurir:
            if kurir["id_kurir"] == id_kurir:
                kurir_valid = kurir
                break

        if kurir_valid is None:
            print(f"ID Kurir '{id_kurir}' tidak ditemukan!")
            continue

        print(f"Kurir terpilih: {kurir_valid['nama_kurir']} ({kurir_valid['jenis_kendaraan']})")

        if id_kurir not in manifest:
            manifest[id_kurir] = []

        while True:
            hasil_resi = bst.inorder()

            if not hasil_resi:
                print("Belum ada data resi terdaftar!")
                break

            print("\n--- Daftar Resi Tersedia ---")
            ada_resi = False
            for node in hasil_resi:
                if node.no_resi not in resi_terpakai:
                    print(f"No. Resi: {node.no_resi} | {node.nama_pengirim} | {node.kota_asal} → {node.kota_tujuan} | Rp {node.total_biaya_kirim:,.0f}")
                    ada_resi = True

            if not ada_resi:
                print("Semua resi sudah ditugaskan ke kurir!")
                break

            no_resi = input("\nMasukkan No. Resi (atau '0' untuk selesai) : ").strip()

            if no_resi == "0":
                if not manifest[id_kurir]:
                    print("Kurir belum mendapat resi apapun!")
                else:
                    print(f"Manifest kurir {kurir_valid['nama_kurir']} berhasil disimpan!")
                break

            resi_ada = False
            for node in hasil_resi:
                if node.no_resi == no_resi:
                    resi_ada = True
                    break

            if not resi_ada:
                print(f"No. Resi '{no_resi}' tidak ditemukan!")
                continue

            if no_resi in resi_terpakai:
                print(f"No. Resi '{no_resi}' sudah ditugaskan ke kurir lain!")
                continue

            manifest[id_kurir].append(no_resi)
            resi_terpakai.append(no_resi)
            print(f"No. Resi '{no_resi}' berhasil ditugaskan ke {kurir_valid['nama_kurir']}!")

        if manifest.get(id_kurir):
          
            print(f"  Manifest {kurir_valid['nama_kurir']}")
          
            for resi in manifest[id_kurir]:
                print(f"  - No. Resi: {resi}")
            

        while True:
            pilih = input("\nApakah ingin plotting kurir lain (Y/N)? ").strip().upper()
            if pilih == "Y":
                break
            elif pilih == "N":
                print("Kembali ke Sub Menu...")
                return
            else:
                print("Input Tidak Valid, Masukkan Y atau N!")

def tampil_manifest(bst):
    print("\n== Tampil Manifest & Bonus Insentif ==")

    if not list_kurir:
        print("Belum ada data kurir terdaftar!")
        return

    if not manifest:
        print("Belum ada manifest yang dibuat!")
        return

    for kurir in list_kurir:
        id_kurir   = kurir["id_kurir"]
        nama_kurir = kurir["nama_kurir"]
        jenis      = kurir["jenis_kendaraan"]

        list_resi    = manifest.get(id_kurir, [])
        jumlah_paket = len(list_resi)

        if jumlah_paket == 0:
            lencana = "Kurir Santai"
            bonus   = 0
        elif 1 <= jumlah_paket <= 3:
            lencana = "Kurir Reguler"
            bonus   = 25000
        elif 4 <= jumlah_paket <= 6:
            lencana = "Kurir Produktif"
            bonus   = 60000
        else:
            lencana = "Kurir Elite"
            bonus   = 120000

        print(f"\n{'='*40}")
        print(f"{'='*40}")
        print(f"  ID Kurir        : {id_kurir}")
        print(f"  Nama Kurir      : {nama_kurir}")
        print(f"  Jenis Kendaraan : {jenis}")
        print(f"  Lencana         : {lencana}")
        print(f"  Bonus Insentif  : Rp {bonus:,.0f}")
        print(f"  Jumlah Paket    : {jumlah_paket} paket")

        if jumlah_paket == 0:
            print("\n  Kurir ini belum membawa paket apapun.")
        else:
            print("\n  Rincian Paket ")
            total_semua = 0
            hasil_resi  = bst.inorder()
            for no_resi in list_resi:
                for node in hasil_resi:
                    if node.no_resi == no_resi:
                        print(f"\n  No. Resi      : {node.no_resi}")
                        print(f"  Nama Pengirim : {node.nama_pengirim}")
                        print(f"  Kota Asal     : {node.kota_asal}")
                        print(f"  Kota Tujuan   : {node.kota_tujuan}")
                        print(f"  Berat Paket   : {node.berat_paket} Kg")
                        print(f"  Total Biaya   : Rp {node.total_biaya_kirim:,.0f}")
                        print(f"  {'─'*35}")
                        total_semua += node.total_biaya_kirim
                        break
            print(f"\n  Total Biaya Semua Paket : Rp {total_semua:,.0f}")

        print(f"{'='*40}")

    print("\nKembali ke Sub Menu...")

while True:
    print("\n========== MENU UTAMA ==========")
    print("1. Kelola Jaringan Hub ")
    print("2. Kelola Administrasi Resi Pengiriman")
    print("3. Kelola Kurir Dan Manifest Pengantaran")
    print("0. Exit Program")
    menu = input("Pilih Menu: ").strip()

    if menu == "1":
        while True:
            print("\n--- Kelola Jaringan Hub ---")
            print("1.1) Input Hub Kota Baru")
            print("1.2) Input Rute Antar-Kota")
            print("0.)  Kembali ke Menu Utama")
            menu1 = input("Pilih Menu: ").strip()

            if menu1 == "1.1":
                kota = input("Masukkan Nama Kota: ").strip().title()
                if kota == "":
                    print("Nama kota tidak boleh kosong!")
                elif kota.isdigit():
                    print("Nama kota tidak boleh hanya berupa angka!")
                elif not any(karakter.isalnum() for karakter in kota):
                    print("Nama kota tidak boleh hanya berisi simbol!")
                else:
                    g.tambah_kota(kota)

            elif menu1 == "1.2":
                if len(g.adj_list) < 2:
                    print("Minimal 2 kota harus terdaftar!")
                else:
                    print("Kota terdaftar:", ", ".join(g.adj_list.keys()))
                    kota1 = input("Kota Asal   : ").strip().title()
                    kota2 = input("Kota Tujuan : ").strip().title()

                    rute_ada = False
                    if kota1 in g.adj_list:
                        for tetangga, jarak in g.adj_list[kota1]:
                            if tetangga == kota2:
                                rute_ada = True
                                break

                    if rute_ada:
                        print(f"Rute {kota1} <-> {kota2} Sudah Ada!")
                    else:
                        try:
                            jarak = float(input("Jarak (KM)  : "))
                            if jarak <= 0:
                                print("Jarak harus lebih dari 0 KM!")
                            elif g.rute_antar_kota(kota1, kota2, jarak):
                                print(f"Rute {kota1} <-> {kota2} ({jarak} KM) Berhasil Ditambahkan")
                            else:
                                print("Gagal! Pastikan kedua kota sudah terdaftar.")
                        except ValueError:
                            print("Jarak harus berupa angka!")

            elif menu1 == "0":
                break
            else:
                print("Menu Tidak Tersedia!")

    elif menu == "2":
        while True:
            print("\n--- Kelola Administrasi Resi Pengiriman ---")
            print("2.1) Input Resi Pengiriman Baru")
            print("2.2) Lihat Seluruh Data Resi Terdaftar")
            print("2.3) Urutkan Transaksi Resi Berdasarkan Biaya Terbesar")
            print("0.)  Kembali ke Menu Utama")
            menu2 = input("Pilih Menu: ").strip()

            if menu2 == "2.1":
                bst.input_resi(g)
            elif menu2 == "2.2":
                bst.lihat_semua_resi()
            elif menu2 == "2.3":
                bst.urutkan_biaya_terbesar()
            elif menu2 == "0":
                break
            else:
                print("Menu Tidak Tersedia!")

    elif menu == "3":
        while True:
            print("\nKelola Kurir Dan Manifest Pengantaran")
            print("3.1) Input Data Kurir")
            print("3.2) Plotting Penugasan Manifest")
            print("3.3) Tampil Manifest & Aturan Bonus Insentif")
            print("0.)  Kembali ke Menu Utama")
            menu3 = input("Pilih Menu: ").strip()

            if menu3 == "3.1":
                input_data_kurir()          
            elif menu3 == "3.2":
                plotting_manifest(bst)      
            elif menu3 == "3.3":
                tampil_manifest(bst)        
            elif menu3 == "0":
                break
            else:
                print("Menu Tidak Tersedia!")

    elif menu == "0":
        print("\nTerima Kasih Telah Menggunakan Program Ini!")
        break
    else:
        print("Menu Tidak Tersedia!")