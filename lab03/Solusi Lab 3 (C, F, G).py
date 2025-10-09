print("===== Sistem Verifikasi Akun =====")

nama_lengkap = input("Masukkan nama lengkap: ")
nomor_telepon = input("Nomor telepon: ")

nama_depan, nama_belakang = nama_lengkap.split()

kunci_verifikasi_sistem = nama_depan[:2]
kunci_verifikasi_sistem += str(ord(nama_belakang[0]))
kunci_verifikasi_sistem += nomor_telepon[-3:]

kata_sandi_sistem = nama_depan[-2:]
kata_sandi_sistem += "_" * len(nama_depan)
kata_sandi_sistem += nomor_telepon[2:6]

kunci_verifikasi_user = input("Masukkan Kunci Verifikasi Anda: ")
kata_sandi_user = input("Masukkan Kata Sandi Anda: ")

print("===== Hasil Verifikasi Akun =====")

kunci_cocok = kunci_verifikasi_sistem == kunci_verifikasi_user
sandi_cocok = kata_sandi_sistem == kata_sandi_user

if kunci_cocok and sandi_cocok:
    print("Verifikasi Berhasil!")
    
    nomor_telepon_masked = f"08******{nomor_telepon[-4:]}"
    
    lebar_kolom_1 = min(35, max(len("Username"), len("Nomor telepon")))
    lebar_kolom_2 = min(35, max(len(nomor_telepon_masked), len(nama_depan)))
    
    print(f"| {'Username':<{lebar_kolom_1}} | {nama_depan:<{lebar_kolom_2}} |")
    print("|" + "-" * (lebar_kolom_1 + 2) + "|" + "-" * (lebar_kolom_2 + 2) + "|")
    print(f"| {'Nomor telepon':>{lebar_kolom_2}} | {nomor_telepon_masked:>{lebar_kolom_2}} |")
    
    print(f"\nSelamat Datang {nama_depan}!")
    print(f"Nomor telepon {nomor_telepon_masked} terverifikasi!")

else:
    print("Verifikasi Gagal!")
    if not kunci_cocok:
        print("Kunci Verifikasi Salah!")
    if not sandi_cocok:
        print("Kata Sandi Salah!")