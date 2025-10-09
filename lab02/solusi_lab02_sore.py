import math

# --- Title ---
print('''<><><><><><><><><><><><><><><><><><>
|                                  |
|         Library Perpucil         |
|                                  |
<><><><><><><><><><><><><><><><><><>
''')

# --- Pengambilan input ---
nama_peminjam = input("Masukkan Nama Peminjam: ")
npm_peminjam = int(input("Masukkan NPM Peminjam: "))
nama_buku = input("Masukkan Nama Buku yang Dipinjam: ")
tarif_per_hari = float(input("Masukkan Tarif Pinjaman per Hari: "))

# --- Pengambilan input yang perlu divalidasi ---
while True: 
    # TODO: --- Pengambilann input ---
    print()
    bulan_peminjaman = int(input("Masukkan Bulan Peminjaman: "))
    tanggal_peminjaman = int(input("Masukkan Tanggal Peminjaman: "))

    print()
    bulan_pengembalian = int(input("Masukkan Bulan Pengembalian: "))
    tanggal_pengembalian = int(input("Masukkan Tanggal Pengembalian: "))

    # --- Validasi input ---
    # Pengecekan bulan (1-12)
    if bulan_peminjaman < 1 or bulan_peminjaman > 12 or\
        bulan_pengembalian < 1 or bulan_pengembalian > 12:
        print("Input bulan tidak valid. Harus dalam rentang 1-12.")
        continue

    # Pengecekan tanggal (1-30)
    if tanggal_peminjaman < 1 or tanggal_peminjaman > 30 or\
        tanggal_pengembalian < 1 or tanggal_pengembalian > 30:
        print("Input tanggal tidak valid. Harus dalam rentang 1-30.")
        continue

    # Pengecekan peminjaman sebelum pengembalian
    if bulan_peminjaman > bulan_pengembalian: # Dilakukan di bulan berbeda
        print("Peminjaman harus dilakukan sebelum pengembalian!")
        continue

    elif bulan_peminjaman == bulan_pengembalian and tanggal_peminjaman > tanggal_pengembalian: # Dilakukan di bulan yang sama
        print("Peminjaman harus dilakukan sebelum pengembalian!")
        continue

    break

# --- Total hari ---
total_hari = (30 - tanggal_peminjaman) + (bulan_pengembalian - bulan_peminjaman - 1) * 30 + tanggal_pengembalian

# --- Total tarif ---
persentase_pajak = 0.5
tarif_bersih = total_hari * tarif_per_hari
tarif_dengan_pajak = round(tarif_bersih + persentase_pajak * math.sqrt(tarif_bersih))

# --- Unique ID ---
unique_id = hex(npm_peminjam // len(nama_peminjam))

# --- Success message ---
print()
print("--- Checkout Peminjaman ---")
print(f"{nama_peminjam} melakukan transaksi dengan ID {unique_id}. Buku dipinjam selama {total_hari} hari dengan total biaya peminjaman sebesar Rp{tarif_dengan_pajak}")