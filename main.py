# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pymysql.cursors

import firebaseCRUD
from MySqlCrud import MySQLCRUD

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database = input("Hangi database ile çalışmak istiyorsun 1:Firebase 2:MySQL")
    if database == "1":
        crud = firebaseCRUD.FirebaseCRUD("users")
        data = {"name": "John", "age": 30}
        doc_id = crud.create(data)
        print(f"Yeni belge id'si {doc_id} olarak oluşturuldu.")
        doc = crud.read(doc_id)
        print(f"Okunan belge: {doc}")
        crud.update(doc_id, {"age": 31})
        doc = crud.read(doc_id)
        print(f"Güncellenen belge: {doc}")
        doc = crud.read(doc_id)
        print(f"Silinecek belge: {doc}")
        crud.delete(doc_id)
    elif database =="2":
        mysql_crud = MySQLCRUD()
        mysql_crud.veri_ekle( {"isim": "Ahmet", "yas": 25})
        #print(mysql_crud.get_last_insert_id())
        last_insert_id=mysql_crud.get_last_insert_id()
        print(mysql_crud.veri_oku(last_insert_id))

        mysql_crud.veri_guncelle(last_insert_id, {"isim": "Mehmet", "yas": 26})
        print(mysql_crud.veri_oku(last_insert_id))
        mysql_crud.veri_sil(last_insert_id)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
