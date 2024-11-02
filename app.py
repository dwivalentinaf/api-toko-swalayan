from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data dummy untuk toko swalayan
produk_data = {
    "1": {"name": "Susu", "category": "Minuman", "price": 10000, "stock": 50},
    "2": {"name": "Roti", "category": "Makanan", "price": 5000, "stock": 30},
    "3": {"name": "Sabun", "category": "Kebutuhan Rumah", "price": 8000, "stock": 20},
    "4": {"name": "Shampoo", "category": "Kebutuhan Rumah", "price": 15000, "stock": 40},
    "5": {"name": "Air Mineral", "category": "Minuman", "price": 3000, "stock": 100},
    "6": {"name": "Minyak Goreng", "category": "Makanan", "price": 25000, "stock": 60},
    "7": {"name": "Beras", "category": "Makanan", "price": 12000, "stock": 80},
    "8": {"name": "Gula", "category": "Makanan", "price": 13000, "stock": 70},
    "9": {"name": "Teh", "category": "Minuman", "price": 7000, "stock": 90},
    "10": {"name": "Kopi", "category": "Minuman", "price": 15000, "stock": 50},
    "11": {"name": "Cokelat", "category": "Makanan", "price": 20000, "stock": 45},
    "12": {"name": "Tisu", "category": "Kebutuhan Rumah", "price": 10000, "stock": 35},
    "13": {"name": "Saus Tomat", "category": "Makanan", "price": 5000, "stock": 60},
    "14": {"name": "Mentega", "category": "Makanan", "price": 8000, "stock": 40},
    "15": {"name": "Mie Instan", "category": "Makanan", "price": 2500, "stock": 200},
}

kategori_data = {
    "1": {"name": "Makanan"},
    "2": {"name": "Minuman"},
    "3": {"name": "Kebutuhan Rumah"},
    "4": {"name": "Peralatan Mandi"},
    "5": {"name": "Camilan"},
    "6": {"name": "Sayuran"},
    "7": {"name": "Daging"},
    "8": {"name": "Buah-buahan"},
    "9": {"name": "Produk Susu"},
    "10": {"name": "Rempah-rempah"},
    "11": {"name": "Pembersih"},
    "12": {"name": "Roti & Pastry"},
    "13": {"name": "Makanan Instan"},
    "14": {"name": "Peralatan Dapur"},
    "15": {"name": "Keperluan Bayi"},
}

pelanggan_data = {
    "1": {"name": "Andi", "email": "andi@gmail.com"},
    "2": {"name": "Budi", "email": "budi@gmail.com"},
    "3": {"name": "Citra", "email": "citra@gmail.com"},
    "4": {"name": "Dewi", "email": "dewi@gmail.com"},
    "5": {"name": "Eka", "email": "eka@gmail.com"},
    "6": {"name": "Fajar", "email": "fajar@gmail.com"},
    "7": {"name": "Gilang", "email": "gilang@gmail.com"},
    "8": {"name": "Hana", "email": "hana@gmail.com"},
    "9": {"name": "Iwan", "email": "iwan@gmail.com"},
    "10": {"name": "Joko", "email": "joko@gmail.com"},
    "11": {"name": "Kiki", "email": "kiki@gmail.com"},
    "12": {"name": "Lina", "email": "lina@gmail.com"},
    "13": {"name": "Mira", "email": "mira@gmail.com"},
    "14": {"name": "Nina", "email": "nina@gmail.com"},
    "15": {"name": "Omar", "email": "omar@gmail.com"},
}

# Endpoint untuk Produk
class ProdukList(Resource):
    def get(self):
        return jsonify(produk_data)

    def post(self):
        new_id = str(len(produk_data) + 1)
        data = request.json
        produk_data[new_id] = data
        return jsonify(produk_data[new_id]), 201

class Produk(Resource):
    def get(self, produk_id):
        produk = produk_data.get(produk_id)
        return jsonify(produk) if produk else ('Produk tidak ditemukan', 404)

    def put(self, produk_id):
        if produk_id in produk_data:
            data = request.json
            produk_data[produk_id].update(data)
            return jsonify(produk_data[produk_id])
        return ('Produk tidak ditemukan', 404)

    def delete(self, produk_id):
        if produk_id in produk_data:
            deleted_produk = produk_data.pop(produk_id)
            return jsonify(deleted_produk)
        return ('Produk tidak ditemukan', 404)

# Endpoint untuk Kategori
class KategoriList(Resource):
    def get(self):
        return jsonify(kategori_data)

    def post(self):
        new_id = str(len(kategori_data) + 1)
        data = request.json
        kategori_data[new_id] = data
        return jsonify(kategori_data[new_id]), 201

class Kategori(Resource):
    def get(self, kategori_id):
        kategori = kategori_data.get(kategori_id)
        return jsonify(kategori) if kategori else ('Kategori tidak ditemukan', 404)

    def put(self, kategori_id):
        if kategori_id in kategori_data:
            data = request.json
            kategori_data[kategori_id].update(data)
            return jsonify(kategori_data[kategori_id])
        return ('Kategori tidak ditemukan', 404)

    def delete(self, kategori_id):
        if kategori_id in kategori_data:
            deleted_kategori = kategori_data.pop(kategori_id)
            return jsonify(deleted_kategori)
        return ('Kategori tidak ditemukan', 404)

# Endpoint untuk Pelanggan
class PelangganList(Resource):
    def get(self):
        return jsonify(pelanggan_data)

    def post(self):
        new_id = str(len(pelanggan_data) + 1)
        data = request.json
        pelanggan_data[new_id] = data
        return jsonify(pelanggan_data[new_id]), 201

class Pelanggan(Resource):
    def get(self, pelanggan_id):
        pelanggan = pelanggan_data.get(pelanggan_id)
        return jsonify(pelanggan) if pelanggan else ('Pelanggan tidak ditemukan', 404)

    def put(self, pelanggan_id):
        if pelanggan_id in pelanggan_data:
            data = request.json
            pelanggan_data[pelanggan_id].update(data)
            return jsonify(pelanggan_data[pelanggan_id])
        return ('Pelanggan tidak ditemukan', 404)

    def delete(self, pelanggan_id):
        if pelanggan_id in pelanggan_data:
            deleted_pelanggan = pelanggan_data.pop(pelanggan_id)
            return jsonify(deleted_pelanggan)
        return ('Pelanggan tidak ditemukan', 404)

# Menambahkan resource ke API
api.add_resource(ProdukList, '/produk')
api.add_resource(Produk, '/produk/<produk_id>')
api.add_resource(KategoriList, '/kategori')
api.add_resource(Kategori, '/kategori/<kategori_id>')
api.add_resource(PelangganList, '/pelanggan')
api.add_resource(Pelanggan, '/pelanggan/<pelanggan_id>')

if __name__ == '__main__':
    app.run(debug=True)
