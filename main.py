import keyboard  # Modul untuk deteksi input real-time
import os        # Untuk membersihkan layar tiap update
import time      # Untuk menambahkan jeda waktu

A = 15  # Ukuran Peta 15x15

# Inisialisasi peta dengan semua sel kosong (⬜)
peta = [["⬜" for _ in range(A)] for _ in range(A)]

# Fungsi untuk menampilkan peta
def buat_peta(posisi_robot):
    os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar
    for i in range(A):
        baris = ""
        for j in range(A):
            if (i, j) == posisi_robot:
                baris += "🤖 "  # Robot berada di posisi ini
            else:
                baris += peta[i][j] + " "  # Isi dari peta (⬜ atau ⬛)
        print(baris)
    print()  # Baris kosong sebagai pemisah tampilan

# Fungsi untuk memperbarui posisi robot
def gerakan_robot(posisi_robot, arah):
    x, y = posisi_robot

    if arah == "up" and x > 0:
        return (x - 1, y)
    elif arah == "down" and x < A - 1:
        return (x + 1, y)
    elif arah == "left" and y > 0:
        return (x, y - 1)
    elif arah == "right" and y < A - 1:
        return (x, y + 1)
    else:
        return posisi_robot  # Tidak bergerak jika di luar batas

# Fungsi untuk memindahkan robot dengan jejak hitam (⬛)
def gerak_per_tahap(posisi_robot, tujuan):
    while posisi_robot != tujuan:
        x, y = posisi_robot
        tx, ty = tujuan

        # Tandai jejak sebelumnya dengan hitam (⬛)
        peta[x][y] = "⬛"

        # Tentukan langkah selanjutnya
        if x < tx:
            posisi_robot = (x + 1, y)
        elif x > tx:
            posisi_robot = (x - 1, y)
        elif y < ty:
            posisi_robot = (x, y + 1)
        elif y > ty:
            posisi_robot = (x, y - 1)

        # Tampilkan peta yang diperbarui
        buat_peta(posisi_robot)
        time.sleep(0.1)  # Tambahkan jeda untuk membuat gerakan terlihat

    return posisi_robot

# Inisiasi posisi awal robot
posisi_robot = (5, 5)  # Robot mulai di posisi (5, 5)

# Fungsi untuk input tombol keyboard
def main():
    global posisi_robot
    buat_peta(posisi_robot)  # Menampilkan peta

    # Loop untuk mendeteksi input tombol panah
    while True:
        if keyboard.is_pressed("up"):
            tujuan = gerakan_robot(posisi_robot, "up")
            posisi_robot = gerak_per_tahap(posisi_robot, tujuan)
        elif keyboard.is_pressed("down"):
            tujuan = gerakan_robot(posisi_robot, "down")
            posisi_robot = gerak_per_tahap(posisi_robot, tujuan)
        elif keyboard.is_pressed("left"):
            tujuan = gerakan_robot(posisi_robot, "left")
            posisi_robot = gerak_per_tahap(posisi_robot, tujuan)
        elif keyboard.is_pressed("right"):
            tujuan = gerakan_robot(posisi_robot, "right")
            posisi_robot = gerak_per_tahap(posisi_robot, tujuan)
        elif keyboard.is_pressed("esc"):
            print("Program selesai.")
            break

# Menjalankan program
main()
