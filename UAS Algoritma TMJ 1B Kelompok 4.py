from pyfiglet import Figlet

def Print_Tiket(arr_tiket, arr_harga):
    for i in range(len(arr_tiket)):
        print(f"{i+1}. {arr_tiket[i]} - Rp{arr_harga[i]}")

haris = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

tikets_weekend_adult = ["ADULT REGULAR WEEKEND", "ADULT PREMIUM WEEKEND", "Regular Adult All-Day Flexi"]
tikets_weekend_adult_harga = [171500, 220500, 185000]

tikets_weekend_child = ["CHILD REGULAR WEEKEND", "CHILD PREMIUM WEEKEND", "Regular Child All-Day Flexi"]
tikets_weekend_child_harga = [147000, 171500, 160000]

tikets_weekdays_adult = ["ADULT REGULAR WEEKDAYS", "ADULT PREMIUM WEEKDAYS", "Regular Adult All-Day Flexi"]
tikets_weekdays_adult_harga = [147500, 196500, 185000]

tikets_weekdays_child = ["CHILD REGULAR WEEKDAYS", "CHILD PREMIUM WEEKDAYS", "Regular Child All-Day Flexi"]
tikets_weekdays_child_harga = [112700, 147500, 160000]

rincian_belanja = []

# TAMPILAN TERMINAL MULAI DARI SINI

print(Figlet().renderText("AQUARIUM SAFARI"))
print("Selamat datang di Jakarta Aquarium Safari!\nSilahkan masukkan kredensial anda:")

repeat = ""
while repeat.lower() != 'n':
    
    #Input data diri pengguna
    nama = input("Nama: ")
    nmr_telepon = input("Nomor telepon: ")
    email = input("Email: ")
    usia = int(input("Usia: "))

    print("""
Hari:
1. Senin
2. Selasa
3. Rabu
4. Kamis
5. Jumat
6. Sabtu
7. Minggu""")
    num_hari = 0
    while num_hari < 1 or num_hari > 7:
        num_hari = int(input("Ketik nomor: "))

    is_weekend = True
    if num_hari < 6: is_weekend = False

    # Menampilkan daftar tiket sesuai hari dan usia
    temp_tikets = ""
    temp_tikets_harga = 0

    print("\nPILIHAN TIKET:")
    
    # adult weekend
    if usia >= 12 and is_weekend:
        Print_Tiket(tikets_weekend_adult, tikets_weekend_adult_harga)
        temp_tikets = tikets_weekend_adult
        temp_tikets_harga = tikets_weekend_adult_harga

    # child weekend
    elif usia < 12 and is_weekend:
        Print_Tiket(tikets_weekend_child, tikets_weekend_child_harga)
        temp_tikets = tikets_weekend_child
        temp_tikets_harga = tikets_weekend_child_harga

    # adult weekdays
    elif usia >= 12 and not is_weekend:
        Print_Tiket(tikets_weekdays_adult, tikets_weekdays_adult_harga)
        temp_tikets = tikets_weekdays_adult
        temp_tikets_harga = tikets_weekdays_adult_harga

    # child weekdays
    else:
        Print_Tiket(tikets_weekdays_child, tikets_weekdays_child_harga)
        temp_tikets = tikets_weekdays_child
        temp_tikets_harga = tikets_weekdays_child_harga

    
    num_tiket = 0
    while num_tiket < 1 or num_tiket > 3:
        num_tiket = int(input("Ketik nomor: "))

    tiket_nama = temp_tikets[num_tiket - 1]
    tiket_harga = temp_tikets_harga[num_tiket - 1]

    # Masukkan data ke rincian belanja
    arr = [nama, usia, haris[num_hari - 1], tiket_nama, tiket_harga]
    rincian_belanja.append(arr)

    # Tanyakan pengguna apakah ingin memesan tiket lagi
    repeat = ""
    while repeat.lower() != 'n' and repeat.lower() != 'y':
        repeat = input("Pesan untuk orang selanjutnya? (Y/N): ")
    print()

# Menampilkan rincian belanja
bar_len = 32
space_len = 10
print("\n" + "=" * bar_len)
print(" " * space_len + "RINCIAN BELANJA")
print("=" * bar_len)

# Menampilkan item yang dibelanjakan
for i in range(len(rincian_belanja)):
    print(f"""
{i+1}. Pengunjung: {rincian_belanja[i][0]}, {rincian_belanja[i][1]} tahun
   Hari Kunjungan: {rincian_belanja[i][2]}
   Kategori Tiket: {rincian_belanja[i][3]}
   Harga Tiket: Rp{str(rincian_belanja[i][4])},-
""")

print("-" * bar_len)

# Menjumlahkan harga total
total = 0
for arr in rincian_belanja:
    total += arr[4]

print(" " * space_len + "TOTAL : Rp" + str(total) + ",-")
print("=" * bar_len)