import mysql.connector

def create_database():
    try:
        # الاتصال بالسيرفر بدون تحديد قاعدة بيانات
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # 🔥 غيرها للباسورد بتاع MySQL عندك
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # إنشاء قاعدة البيانات لو مش موجودة
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:  # ✅ تعديل هنا
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # إغلاق الاتصال
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
