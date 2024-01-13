import pymysql

class MySQLCRUD:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='129050Veysel',
            database='deneme',
            cursorclass=pymysql.cursors.DictCursor  # DictCursor ile sonuçları sözlük olarak alırız
        )
        self.cursor = self.conn.cursor()

        # Tablo oluşturulması veya mevcut tablonun kontrolü (gerektiğinde)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS veriler (
                id INT PRIMARY KEY AUTO_INCREMENT,
                isim VARCHAR(255),
                yas INT
            )
        """)
        self.conn.commit()

    def veri_ekle(self, veri):
        query = "INSERT INTO veriler (isim, yas) VALUES (%s, %s)"
        values = ( veri["isim"], veri["yas"])

        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"{self.get_last_insert_id()} anahtarıyla veri başarıyla eklendi.")

    def veri_oku(self, belge_id):
        query = "SELECT * FROM veriler WHERE id = %s"
        values = (belge_id,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            return result
        else:
            print(f"{belge_id} anahtarıyla eşleşen veri bulunamadı.")
            return None

    def veri_guncelle(self, belge_id, yeni_veri):
        query = "UPDATE veriler SET isim = %s, yas = %s WHERE id = %s"
        values = (yeni_veri["isim"], yeni_veri["yas"], belge_id)

        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"{belge_id} anahtarıyla veri başarıyla güncellendi.")

    def veri_sil(self, belge_id):
        query = "DELETE FROM veriler WHERE id = %s"
        values = (belge_id,)

        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"{belge_id} anahtarıyla veri başarıyla silindi.")

    def get_last_insert_id(self):
        query = "SELECT LAST_INSERT_ID()"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if result:
            return result["LAST_INSERT_ID()"]
        else:
            print(f"veri bulunamadı.")
            return None

