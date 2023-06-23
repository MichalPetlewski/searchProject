from singleton import singleton
import sqlite3

@singleton
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('../products.db', check_same_thread=False)
        self.c = self.conn.cursor()

    def execute(self, query, *params):
        cursor = self.c
        cursor.execute(query, params)
        return cursor.fetchall()

    @staticmethod
    def select_product(fraze):
        query = "SELECT ProductName, description, Image, ID FROM product WHERE ProductName like ? "
        results = Database().execute(query, f'{fraze}%')
        return results


    @staticmethod    
    def select_category_search(category):
        query = f'SELECT ProductName, description, Image, ID FROM product WHERE CategoryID like ?'
        results = Database().execute(query, category)
        return results
    
    
    @staticmethod
    def select_category_name(category_name):
        query = f'SELECT CategoryName from categories where ID like ?'
        cat_name = Database().execute(query, category_name)
        return cat_name


    @staticmethod    
    def select_details(id):
        query = 'select image, productname, description, price  from product where ID like ?'
        results = Database().execute(query, id)
        return results
    
    @staticmethod
    def select_comments(id):
        query = 'select username, rating, commentContent from comments where ProductID like ?'
        results = Database().execute(query, id)
        return results
    
    @staticmethod
    def insert_comment(username, rating, comment, id):
        query = "INSERT INTO comments(username, rating, commentContent, ProductID) VALUES(?, ?, ?, ?)"
        results = Database().execute(query, username, rating, comment, id)
        Database().conn.commit()
        return results
    
    @staticmethod
    def select_avg_rating(id):
        query = f"""
        
        select AVG(rating) from Comments
        where productID = {id}
        group by productID
        """
        results = Database().execute(query)
        for i in results:
            results = i[0]
        if results:
            return results
        else:
            return 'No ratings yet'

    @staticmethod
    def insert_card_data(name, CVV, numbers):
        query =  "INSERT INTO Transactions(OwnerName, CVV, cardNumbers) VALUES(?, ?, ?)"
        results = Database().execute(query, name, CVV, numbers)
        Database().conn.commit()
        return results
