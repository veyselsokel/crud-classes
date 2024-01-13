# Firebase ve MySQL CRUD Uygulaması

Bu Python script'i, Firebase ve MySQL veritabanları üzerinde CRUD (Create, Read, Update, Delete) işlemleri gerçekleştiren basit bir uygulamayı içermektedir. Aşağıda script'in nasıl kullanılacağına dair bir açıklama bulunmaktadır.

## Kullanım

1. **Script'i Çalıştırma:**
    - Script'i çalıştırdığınızda, hangi veritabanıyla çalışmak istediğinizi seçmeniz istenecektir (`1` for Firebase, `2` for MySQL).
    - Seçiminize göre, ilgili veritabanı için CRUD işlemleri yapılacaktır.

2. **Firebase Kullanımı:**
    - FirebaseCRUD sınıfı ile Firebase veritabanı üzerinde işlemler yapabilirsiniz.
    - Belirli bir koleksiyon (collection) üzerinde belge (document) ekleyebilir, okuyabilir, güncelleyebilir ve silebilirsiniz.

    ```python
    # Firebase örnek kullanım
    crud = firebaseCRUD.FirebaseCRUD("users")

    # Belge oluştur
    data = {"name": "John", "age": 30}
    doc_id = crud.create(data)
    print(f"Yeni belge id'si {doc_id} olarak oluşturuldu.")

    # Belge oku
    doc = crud.read(doc_id)
    print(f"Okunan belge: {doc}")

    # Belge güncelle
    crud.update(doc_id, {"age": 31})
    doc = crud.read(doc_id)
    print(f"Güncellenen belge: {doc}")

    # Belge sil
    crud.delete(doc_id)
    ```

3. **MySQL Kullanımı:**
    - MySQLCRUD sınıfı ile MySQL veritabanı üzerinde işlemler yapabilirsiniz.
    - Veri ekleyebilir, okuyabilir, güncelleyebilir ve silebilirsiniz.

    ```python
    # MySQL örnek kullanım
    mysql_crud = MySQLCRUD()

    # Veri ekle
    mysql_crud.veri_ekle({"isim": "Ahmet", "yas": 25})

    # Son eklenen veriyi oku
    last_insert_id = mysql_crud.get_last_insert_id()
    print(mysql_crud.veri_oku(last_insert_id))

    # Veriyi güncelle
    mysql_crud.veri_guncelle(last_insert_id, {"isim": "Mehmet", "yas": 26})
    print(mysql_crud.veri_oku(last_insert_id))

    # Veriyi sil
    mysql_crud.veri_sil(last_insert_id)
    ```

**Notlar:**
- Firebase kullanabilmek için `crud-class-firebase-adminsdk-sednr-24f32980ae.json` adlı Firebase Admin SDK kimlik bilgileri dosyasını sağlamanız gerekmektedir.
- MySQL kullanabilmek için MySQL bağlantı bilgilerini (host, user, password, database) uygun şekilde güncellemeniz gerekmektedir.

Bu örnek script ile Firebase ve MySQL üzerinde temel CRUD işlemlerini gerçekleştirebilirsiniz.
