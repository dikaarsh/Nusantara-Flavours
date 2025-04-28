from extensions import db
from models import User, Resep, Favorit, Pencarian
from app import app

with app.app_context():
    # Hapus semua isi database sebelumnya
    db.drop_all()
    db.create_all()

    # Insert Users
    users = [
        User(nama="Ardika Arshal", email="ardika@example.com", password="password123"),
        User(nama="Ikhsan Nugraha", email="ikhsan@example.com", password="secure456"),
        User(nama="Okta Rizky", email="okta@example.com", password="mysecret789"),
        User(nama="Suharyadi Putra", email="suharyadi@example.com", password="pass4567"),
    ]
    db.session.add_all(users)

    # Insert Resep
    reseps = [
        Resep(user_id=1, nama_resep="Rawon", kategori="Jawa Timur", nama_daerah="Surabaya", bahan="Daging sapi, kluwek, bawang merah, bawang putih", instruksi="Rebus daging, buat bumbu, campur dan masak", foto="rawon.jpg"),
        Resep(user_id=1, nama_resep="Binte Biluhuta", kategori="Gorontalo", nama_daerah="Gorontalo", bahan="Jagung, udang, kelapa, daun kemangi", instruksi="Masak jagung, campur dengan kelapa dan seafood", foto="binte.jpg"),
        Resep(user_id=2, nama_resep="Tinutuan", kategori="Sulawesi Utara", nama_daerah="Manado", bahan="Singkong, bayam, kangkung, jagung manis", instruksi="Rebus semua bahan hingga matang", foto="tinutuan.jpg"),
        Resep(user_id=2, nama_resep="Ayam Taliwang", kategori="Nusa Tenggara Barat", nama_daerah="Lombok", bahan="Ayam kampung, sambal taliwang", instruksi="Bakar ayam dan olesi sambal", foto="taliwang.jpg"),
        Resep(user_id=3, nama_resep="Nasi Liwet", kategori="Jawa Tengah", nama_daerah="Surakarta", bahan="Beras, santan, daun salam, serai", instruksi="Masak nasi dengan santan dan bumbu", foto="liwet.jpg"),
        Resep(user_id=3, nama_resep="Rendang", kategori="Sumatera Barat", nama_daerah="Padang", bahan="Daging sapi, santan, rempah-rempah", instruksi="Masak perlahan hingga kering dan berminyak", foto="rendang.jpg"),
        Resep(user_id=4, nama_resep="Gudeg", kategori="Jawa Tengah", nama_daerah="Yogyakarta", bahan="Nangka muda, santan, gula merah", instruksi="Masak nangka muda hingga matang", foto="gudeg.jpg"),
        Resep(user_id=4, nama_resep="Lumpia Semarang", kategori="Jawa Tengah", nama_daerah="Semarang", bahan="Kulit lumpia, rebung, ayam, udang", instruksi="Tumis isi, bungkus, goreng hingga matang", foto="lumpia.jpg"),
    ]
    db.session.add_all(reseps)

    # Insert Favorit
    favorit = [
        Favorit(user_id=1, resep_id=1),
        Favorit(user_id=1, resep_id=2),
        Favorit(user_id=2, resep_id=3),
        Favorit(user_id=2, resep_id=4),
        Favorit(user_id=3, resep_id=5),
        Favorit(user_id=3, resep_id=6),
        Favorit(user_id=4, resep_id=7),
        Favorit(user_id=4, resep_id=8),
    ]
    db.session.add_all(favorit)

    # Insert Pencarian
    pencarian = [
        Pencarian(user_id=1, kata_kunci="Rawon", waktu_pencarian="2025-04-01 08:23:00"),
        Pencarian(user_id=2, kata_kunci="Tinutuan", waktu_pencarian="2025-04-02 09:00:00"),
        Pencarian(user_id=3, kata_kunci="Nasi Liwet", waktu_pencarian="2025-04-03 10:45:00"),
        Pencarian(user_id=4, kata_kunci="Rendang", waktu_pencarian="2025-04-04 07:15:00"),
        Pencarian(user_id=1, kata_kunci="Gudeg", waktu_pencarian="2025-04-05 12:30:00"),
        Pencarian(user_id=2, kata_kunci="Lumpia", waktu_pencarian="2025-04-06 13:00:00"),
    ]
    db.session.add_all(pencarian)

    # Commit semua
    db.session.commit()

print("✅ Database berhasil diisi!")
