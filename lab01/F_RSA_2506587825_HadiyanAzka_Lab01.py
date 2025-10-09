"""
Lab 01 - Blooming Colors
============================

Program ini menggambar sebuah bunga dengan n kelopak
menggunakan Turtle.
Setiap kelopak dibentuk dari dua lengkungan (arc)
sehingga hasilnya melingkar.
Warna kelopak dibuat bergradasi
dari warna awal (R1,G1,B1) ke warna akhir (R2,G2,B2).
Di tengah bunga ditambahkan lingkaran kecil sebagai pusat.
"""

import turtle

# --- Input ---
petalnum = int(turtle.numinput("Lab 01",
"Enter the number of flower petals: ",
minval=2))
radius = int(turtle.numinput("Lab 01",
"Enter the radius of each petal (like 100): ",
minval=1))

# --- Setup turtle ---
turtle.colormode(255)
turtle.title("Lab 01")
t = turtle.Turtle()
t.speed(1.2)
t.width(2)

# TODO: Input warna awal [0-255]
# --- Warna Awal ---
R1 = int(turtle.numinput("Lab 01",
"Set the first post of the red gradient -R1-\
 as a value from 0-255: ",
minval=0, maxval=255))

G1 = int(turtle.numinput("Lab 01",
"Set the first post of the green gradient -G1-\
 as a value from 0-255: ",
minval=0, maxval=255))

B1 = int(turtle.numinput("Lab 01",
"Set the first post of the blue gradient -B1-\
 as a value from 0-255: ",
minval=0, maxval=255))

# TODO: Input warna akhir [0-255]
# --- Warna Akhir ---
R2 = int(turtle.numinput("Lab 01",
"Set the last post of the red gradient -R2-\
 as a value from 0-255: ",
minval=0, maxval=255))

G2 = int(turtle.numinput("Lab 01",
"Set the last post of the green gradient -G2-\
 as a value from 0-255: ",
minval=0, maxval=255))

B2 = int(turtle.numinput("Lab 01",
"Set the last post of the blue gradient -B2-\
 as a value from 0-255: ",
minval=0, maxval=255))

# --- Sudut Kelopak Bunga ---
angle = 150

# TODO: --- Hitung increment gradasi ---
dr = (R2 - R1)/(petalnum - 1)
dg = (G2 - G1)/(petalnum - 1)
db = (B2 - B1)/(petalnum - 1)

# TODO: --- Gambar bunga ---

for petalcount in range(petalnum):
    # TODO: Hitung warna kelopak sekarang
    color = (dr, dg, db)
    
    # TODO: Mengubah outline turtle menjadi hitam
    #       & warna isi menjadi color
    t.color = (color)

    # TODO: Menggambar kelopak bunga dengan fill
    for _ in range(2):
        # TODO: Gambar setengah kelopak
        #       dengan radius dan sudut angle
        t.pendown()
        t.circle(radius, angle)

        # TODO: Putar kekiri sebanyak (180-angle)
        #       untuk menggambar setengah kelopak berikutnya
        t.left(180 - angle)
        t.circle(radius, angle)
        t.left(360/petalnum)

    # TODO: Putar turtle untuk posisi kelopak berikutnya
    t.left(360/petalnum)

# --- Gambar pusat bunga ---
t.penup()
t.goto(0, -radius // 6)  # Turun kebawah agar lingkaran terbuat di tengah
t.pendown()
t.color("black")
t.fillcolor("yellow")
t.begin_fill()
t.circle(radius // 6)
t.end_fill()

t.hideturtle()
turtle.exitonclick()