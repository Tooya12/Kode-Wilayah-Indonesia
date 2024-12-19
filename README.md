# Kode Wilayah Permendagri-72-2019 dan Kepmendagri No 100.1.1-6117 Tahun 2022

Tersedia dalam bentuk json dan csv file yang tersedia di [`dist`](dist)

permendagri-2019.csv dan kepmendagri-2022.csv yang di ubah ke dalam json menggunakan [`wilayahCsvToJson.py`](wilayahCsvToJson.py).

di dalam permendagri-2019.json dan kepmendagri-2022.json terdapat "Nama Wilayah" dan "value".

value berisi kode wilayah.

## Stucture file json
```bash
   Provinsi
    ├── Kabupaten/Kota
    │   ├── Kecamatan
    │   │   ├── Kelurahan/Desa
    │   │   │   └── value
    │   │   └── value
    │   └── value
    └── value
```

Jika ingin menjalankan program nya gunakan python 3.11+ dan install requirements:

```bash
   pip install -r requirements.txt
```

Jalankan program nya:

```bash
   python wilayahCsvToJson.py
```

## Credits
- [cahyadsn](https://github.com/cahyadsn/wilayah) Untuk data Kepmendagri No 100.1.1-6117 Tahun 2022
