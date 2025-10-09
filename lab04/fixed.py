
import os


def buka_file(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            next(file, None)  # skip header
            for line in file:
                clean_line = line.strip()
                if not clean_line:
                    continue
                row_values = clean_line.split(",")
                data.append(row_values)
    except FileNotFoundError:
        print("File tidak ditemukan!")
        return []
    return data


def simpan_file(filename, data):
    with open(filename, "w") as f:
        f.write("Nama,Tugas,UTS,UAS\n")  # header tetap
        for row in data:
            f.write(",".join(row) + "\n")


def buat_laporan(datalist):
    for row in datalist:
        nama = row[0]
        tugas = float(row[1])
        uts = float(row[2])
        uas = float(row[3])

        nilai = round(tugas*0.3 + uts*0.35 + uas*0.35, 2)

        if 0 <= nilai < 40:
            huruf = "E"
        elif 40 <= nilai < 55:
            huruf = "D"
        elif 55 <= nilai < 70:
            huruf = "C"
        elif 70 <= nilai < 85:
            huruf = "B"
        else:
            huruf = "A"

        print(f"{nama} mendapatkan nilai akhir sebesar {
              nilai:.2f} dan memperoleh grade {huruf}!")


def edit_data(nama, kolom, nilai_baru, data):
    kolom = kolom.lower()
    if kolom == "tugas":
        nomor_kolom = 1
    elif kolom == "uts":
        nomor_kolom = 2
    elif kolom == "uas":
        nomor_kolom = 3
    else:
        print("Kolom tidak valid!")
        return False

    for i, row in enumerate(data):
        if row[0] == nama:
            data[i][nomor_kolom] = str(nilai_baru)
            print(f"Nilai {kolom} {nama} telah berhasil diperbarui!")
            return True

    print(f"Tidak ada mahasiswa dengan nama {nama} di database!")
    return False


def main():
    halt = False
    while not halt:
        print("\n" + "="*5 + " PacilEdu " + "="*5)
        print("1. Buat laporan")
        print("2. Edit data")
        print("3. Keluar")
        choice = input("Pilih [1 - 3]: ").strip()

        if choice == '1':
            file = input("Masukkan nama file: ")
            data = buka_file(file)
            if data:
                buat_laporan(data)

        elif choice == '2':
            file = input("Masukkan nama file: ")
            if not os.path.exists(file):
                print("File tidak ditemukan!")
                continue

            data = buka_file(file)
            nama = input(
                "Masukkan nama mahasiswa [perhatikan huruf besar dan kecil]: ")
            kolom = input("Masukkan nama kolom [tugas/uts/uas]: ")
            try:
                nilai_baru = float(
                    input("Masukkan nilai baru untuk kolom " + kolom + ": "))
            except ValueError:
                print("Nilai harus berupa angka!")
                continue

            if 0 <= nilai_baru <= 100:
                if edit_data(nama, kolom, nilai_baru, data):
                    simpan_file(file, data)
            else:
                print("Update gagal! Nilai berada di luar batas (0-100).")

        elif choice == '3':
            print("\n    Otsukaresama! 🙇🏼‍\n")
            halt = True
        else:
            print("Mohon masukkan input yang valid.")


if __name__ == "__main__":
    main()
