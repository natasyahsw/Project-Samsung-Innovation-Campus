from utils import konversi_suhu

print("=== KONVERSI SUHU ===")

try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ")
    ke = input("Ke satuan (C/F/K): ")

    hasil = konversi_suhu(nilai, dari, ke)

    if isinstance(hasil, str):  # kalau error
        print(hasil)
    else:
        print(f"Hasil: {nilai}°{dari.upper()} = {hasil:.1f}°{ke.upper()}")

except ValueError:
    print("Error: Input nilai suhu harus berupa angka.")
