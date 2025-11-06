from himpunan.himpunan import Himpunan

def main():
    A_input = input("Masukkan elemen himpunan A (pisahkan dengan spasi): ").split()
    B_input = input("Masukkan elemen himpunan B (pisahkan dengan spasi): ").split()

    A = Himpunan(*A_input)
    B = Himpunan(*B_input)

    print("\nHimpunan A:", A)
    print("Himpunan B:", B)

    while True:
        print("\n=== MENU OPERASI ===")
        print("1. Gabungan (A ∪ B)")
        print("2. Irisan (A ∩ B)")
        print("3. Selisih (A - B)")
        print("4. Selisih Simetris (A ⊕ B)")
        print("5. Perkalian Kartesius (A × B)")
        print("6. Himpunan Bagian (P(A))")
        print("7. Keluar")

        pilihan = input("Pilih operasi (1-7): ")

        if pilihan == "1":
            print("Hasil Gabungan:", A + B)
        elif pilihan == "2":
            print("Hasil Irisan:", A / B)
        elif pilihan == "3":
            print("Hasil Selisih (A - B):", A - B)
        elif pilihan == "4":
            print("Hasil Selisih Simetris:", A * B)
        elif pilihan == "5":
            print("Hasil Perkalian Kartesius:")
            for pasangan in (A ** B):
                print(pasangan)
        elif pilihan == "6":
            print("Himpunan Bagian dari A:")
            P_A = A.ListKuasa()
            for subset in P_A:
                print(subset)
            print(f"Total Himpunan Bagian: {len(P_A)}")
        elif pilihan == "7":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()