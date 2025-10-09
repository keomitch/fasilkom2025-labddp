import math

# <Title>

judul = "Perpucil Self-Billing Service"
print('+' + '-'*49 + '+')
print('|' + ' '*49 + '|')
print('|' + ' '*10 + judul + ' '*10 + '|')
print('|' + ' '*49 + '|')
print('+' + '-'*49 + '+')

# <Variable Declarations>

print()
print("*** Isian Data Peminjam ***")
print("keterangan: TH adalah tarif harian (tarif per hari terpinjam)")
print()
npm = int(input("NPM          : "))
nama_peminjam = input("Nama peminjam: ")
buku = input("Judul buku   : ")
tarif_harian = int(input("TH (dalam rupiah): "))
print()

print(" -> Tanggal Meminjam")
print("keterangan: isi dengan angka")
a = tanggalbulan_pinjam = int(input("Bulan (1-12): "))
b = tanggalhari_pinjam = int(input("Hari (1-30): "))
print()
print(" -> Tanggal Mengembalikan")
print("keterangan: isi dengan angka")
c = tanggalbulan_kembali = int(input("Bulan (1-12): "))
d = tanggalhari_kembali = int(input("Hari (1-30): "))

# validity checker
if c < a or (c == a and d < b):
  print()
  print("Tanggal invalid. Mulai ulang program.")
  quit()
if a < 1 or b < 1 or c < 1 or d < 1:
  print()
  print("Tanggal invalid. Mulai ulang program.")
  quit()
if a > 12 or b > 30 or c > 12 or d > 30:
  print()
  print("Tanggal invalid. Mulai ulang program.")
  quit()

# <Code Payload>

uid = hex(npm // len(nama_peminjam))[2:]
jumlah_hari_peminjaman = (c - a)*30 + (d - b) + 1
persen_pajak = 0.5 / 100
tarif_kotor = jumlah_hari_peminjaman * tarif_harian
tarif_bersih = round(tarif_kotor + persen_pajak * math.sqrt(tarif_kotor))

# <Printout>

print()
print("--- STRUK PENGEMBALIAN ---")
print()
print("Pelanggan Perpucil dengan UID", uid, "atas nama:")
print()
print("\t" + str(npm))
print("\t" + nama_peminjam)
print()
print("telah meminjam buku", buku)
print("selama", str(jumlah_hari_peminjaman), "hari")
print("dengan total biaya peminjaman sebesar Rp " + str(tarif_bersih) + ".")
print()
print("Tunjukkan struk ini ketika melakukan pengembalian buku.")
print()
print("-"*26)