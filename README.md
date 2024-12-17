# Kode Wilayah Permendagri-72-2019

Tersedia dalam bentuk json dan csv file yang tersedia di [`dist`](dist)

base.csv yang di ubah ke dalam json menggunakan [`baseCsvToJson.py`](baseCsvToJson.py).

di dalam base.json terdapat "Nama Wilayah" dan "value", value berisi kode wilayah.

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

jika ingin menjalankan program nya gunakan python 3.11+ dan install requirements:

```bash
   pip install -r requirements
```

Jalankan program nya:

```bash
   python baseCsvToJson.py
```
