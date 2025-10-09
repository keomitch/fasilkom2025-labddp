"""
Lab 01 - Blooming Colors
============================

Program ini menggambar sebuah bunga dengan n kelopak menggunakan Turtle.
Setiap kelopak dibentuk dari dua lengkungan (arc) sehingga hasilnya melingkar.
Warna kelopak dibuat bergradasi dari warna awal (R1,G1,B1) ke warna akhir (R2,G2,B2).
Di tengah bunga ditambahkan lingkaran kecil sebagai pusat.
"""

import turtle

# --- Input ---
n = int(turtle.numinput("Lab 01", "Masukkan jumlah kelopak bunga: ", minval=2))
r = int(turtle.numinput("Lab 01", "Masukkan radius kelopak (misal 100): ", minval=1))

turtle.colormode(255)
turtle.title("Lab 01")

# --- Warna Awal ---
R1 = int(turtle.numinput("Lab 01", "R1 (0-255): ", minval=0, maxval=255))
G1 = int(turtle.numinput("Lab 01", "G1 (0-255): ", minval=0, maxval=255))
B1 = int(turtle.numinput("Lab 01", "B1 (0-255): ", minval=0, maxval=255))

# --- Warna Akhir ---
R2 = int(turtle.numinput("Lab 01", "R2 (0-255): ", minval=0, maxval=255))
G2 = int(turtle.numinput("Lab 01", "G2 (0-255): ", minval=0, maxval=255))
B2 = int(turtle.numinput("Lab 01", "B2 (0-255): ", minval=0, maxval=255))


# --- Sudut Kelopak Bunga ---
angle = 150

# --- Setup turtle ---
t = turtle.Turtle()
t.speed(0)
t.width(2)

# --- Hitung increment gradasi ---
dr = (R2 - R1) / (n - 1)
dg = (G2 - G1) / (n - 1)
db = (B2 - B1) / (n - 1)

# --- Gambar bunga ---
for i in range(n):
    color = (
        int(R1 + i * dr),
        int(G1 + i * dg),
        int(B1 + i * db),
    )
    t.color("black")
    t.fillcolor(color)

    t.begin_fill()
    for _ in range(2):
        t.circle(r, angle)
        t.left(180 - angle)
    t.end_fill()

    t.left(360 / n)

# --- Gambar pusat bunga ---
t.penup()
t.goto(0, -r // 6)  # Turun kebawah agar lingkaran terbuat di tengah
t.pendown()
t.color("black")
t.fillcolor("yellow")
t.begin_fill()
t.circle(r // 6)
t.end_fill()

t.hideturtle()
turtle.exitonclick()
