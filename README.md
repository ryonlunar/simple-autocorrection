# Code Autocorrection Damerau-Levenshtein

Repositori ini memuat *command-line app* untuk menyarankan **nama variabel atau fungsi** terdekat berdasarkan algoritma **Damerau-Levenshtein**. Aplikasi mendukung dua skema ambang:

- **Dynamic threshold** → `k = ceil(α·length)` dengan *retry* bertahap
- **Constant threshold** → ambang tetap `max_dist`

Pengguna dapat beralih mode hanya dengan mengganti variabel `MODE` pada skrip utama.

## 👥 Kontributor

| NIM      | Nama Lengkap        |
|----------|---------------------|
| 13523052 | Adhimas Aryo Bimo   |

## ⚙️ Requirement

| Item                  | Versi              |
|-----------------------|--------------------|
| Python                | ≥ 3.8              |
| Dependensi eksternal  | — (hanya *standard library*) |
| OS                    | Linux / Windows / macOS |

## 🔧 Instalasi

```bash
git clone https://github.com/ryonlunar/simple-autocorrection.git
cd simple-autocorrection
```

## 🚀 Menjalankan

### Buka *autocorrect.py*, ubah baris:

```bash
MODE = "dynamic"      # atau "constant"
```
### Simpan lalu jalankan :
```bash
python damerau_levenshtein.py
```

## 📋 Penjelasan Program

1. **`collect_ids(path)`** → memindai semua *.py* di direktori `path`, mengambil ≤ 1000 identifier unik.
2. **`dl(a,b)`** → menghitung jarak Damerau-Levenshtein terbatas.
3. **`budget(L)`** → menghasilkan ambang dinamis.
4. **`suggest(typo, dic, mode, …)`** → mengembalikan ≤ *top k* kandidat terurut *(distance, length)* beserta waktu komputasi.

---

*Proyek ini dikembangkan untuk Tugas IF2211 Strategi Algoritma.*