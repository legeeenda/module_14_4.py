import sqlite3


def initiate_db(db_name="products.db"):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL,
            image_url TEXT NOT NULL
        )
        """)
        
        connection.commit()
        connection.close()
        print("Таблица Products успешно создана или уже существует.")
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")


def get_all_products(db_name="products.db"):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, description, price, image_url FROM Products")
        products = cursor.fetchall()
        
        connection.close()
        return products
    except Exception as e:
        print(f"Ошибка при получении продуктов: {e}")
        return []


def add_product(title, description, price, image_url, db_name="products.db"):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        

        cursor.execute(
            "INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)", 
            (title, description, price, image_url)
        )
        
        connection.commit()
        connection.close()
        print(f"Продукт '{title}' успешно добавлен.")
    except Exception as e:
        print(f"Ошибка при добавлении продукта: {e}")


from crud_functions import initiate_db, add_product


initiate_db()


add_product("Product1", "Описание 1", 100, "https://via.placeholder.com/150")
add_product("Product2", "Описание 2", 200, "https://via.placeholder.com/150")
add_product("Product3", "Описание 3", 300, "https://via.placeholder.com/150")
add_product("Product4", "Описание 4", 400, "https://via.placeholder.com/150")

print("Данные успешно добавлены в таблицу Products.")
