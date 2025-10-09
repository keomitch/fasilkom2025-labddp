judul = "Sistem Verifikasi Akun Burhanpedia"
print("+" + "-"*40 + "+")
print("|" + " "*40 + "|")
print("|   " + judul + "   |")
print("|" + " "*40 + "|")
print("+" + "-"*40 + "+")
print()

# INPUT PENGGUNA

print(" DATA PENGGUNA\n" + "-"*14)

# cek kesahan nama depan
nama_depan_sah = False
while nama_depan_sah == False:
  nama_depan = input("Nama Depan (1 kata)   : ")
  if ' ' in nama_depan:
    print("Mohon masukkan satu kata nama saja.\n")
    continue
  else:
    nama_depan_sah = True

# cek kesahan nama belakang
nama_belakang_sah = False
while nama_belakang_sah == False:
  nama_belakang = input("Nama Belakang (1 kata): ")
  if ' ' in nama_depan:
    print("Mohon masukkan satu kata nama saja.\n")
    continue
  else:
    nama_belakang_sah = True

# cek kesahan nomor telepon
nomor_telepon_sah = False
while nomor_telepon_sah == False:
  nomor_telepon = input("Nomor Telepon (harus dimulai 08-): ")
  # https://id.wikipedia.org/wiki/Nomor_telepon_di_Indonesia
  if nomor_telepon[:2] == "08" and 10 <= len(nomor_telepon) <= 15:
     nomor_telepon_sah = True
  else:
     print("Mohon masukkan nomor telepon yang sah.\n")
     continue

# BUAT KUNCI VERIFIKASI (kv)

kv1 = nama_depan[:2]
kv2 = str(ord(nama_belakang[0]))
kv3 = nomor_telepon[-3:]
kv_sistem = kv1 + kv2 + kv3

# BUAT KATA SANDI (ks)

ks1 = nama_depan[-2:]
ks2 = "_"*len(nama_depan)
ks3 = nomor_telepon[2:6]
ks_sistem = ks1 + ks2 + ks3

# inbox (hanya untuk mengetes)
print()
print("<This is a dummy>")
print("Periksa inbox Anda:")
print(kv_sistem + "\n" + ks_sistem)

# LAKUKAN VERIFIKASI

print("\nVERIFIKASI & SANDI")
print("Silahkan masukkan kunci verifikasi dan kata sandi Anda.")
print("-"*18)

# cek kesahan kunci verifikasi dan kata sandi
kvks_sah = False
while kvks_sah == False:
  kunci_verifikasi = input("Kunci verifikasi: ")
  kata_sandi = input("Kata Sandi      : ")
  if kunci_verifikasi == kv_sistem and kata_sandi == ks_sistem:
    kvks_sah = True
  else:
    print("kunci verifikasi atau kata sandi Anda tidak sah.\n")
    continue

# laporan verifikasi selesai
lennd = len(nama_depan)
lennt = len(nomor_telepon)
print("\n--- 200: Verifikasi berhasil! ---")
print("| Username        |  " + f"{nama_depan:>15}" + " |")
if lennd > lennt:
  print("|" + "-"*17 + "|--" + "-"*lennd + "--|")
elif lennt >= lennd:
  print("|" + "-"*17 + "|--" + "-"*lennt + "--|")
print("| Nomor telepon   |  " + f"{nomor_telepon:>15}" + " |")
print("Selamat datang " + nama_depan + "!")
print("Nomor telepon " + nomor_telepon +" terverifikasi!")