
# Nusantara Flavours - Full Version

## Cara Menjalankan
1. Buka terminal di folder ini.
2. Buat virtual environment (opsional tapi disarankan):
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install semua package:
```bash
pip3 install flask flask_sqlalchemy
```
4. Jalankan aplikasi:
```bash
python3 app.py
```
5. Akses di browser:
- http://127.0.0.1:5000/ -> Beranda
- http://127.0.0.1:5000/kategori -> Kategori
- http://127.0.0.1:5000/favorit -> Favorit
- http://127.0.0.1:5000/resep/1 -> Detail Resep

