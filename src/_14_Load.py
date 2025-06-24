import argparse
import os
import sys


def load():
    # Inisialisasi Argument Parser
    parser = argparse.ArgumentParser(description='Buka folder.')
    # Menambahkan argumen posisional
    parser.add_argument('folder', nargs='?', default=None, help='mengakses folder csv ')
    # Penguraian Argumen
    args = parser.parse_args()

    # Pengecekan Argumen
    if args.folder is None:
        print("Tidak ada nama folder yang diberikan!\nUsage : python main.py <nama_folder>")
        sys.exit()

# Memanggil fungsi untuk memeriksa keberadaan folder
    if not os.path.exists(args.folder):
        print(f"Folder \"{args.folder}\" tidak ditemukan!")
        sys.exit()
