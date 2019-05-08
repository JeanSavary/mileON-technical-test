# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np 

# -- Retrieve data -- #
DATA = pd.read_csv('GrammarandProductReviews.csv')


# -- Define classes -- #
class User():

    def __init__(self, username, interests):

        self.username = username
        self.interests = interests.split(',')

    def describe(self):

        print(
            """
            → Username : {}\n
            → Interests : {}
            """.format(
                self.username, 
                ', '.join(map(str, self.interests))
                )
        )

class Product():

    def __init__(self, name, categories,  reviews_number, avg_rating):

        self.name = name
        self.categories = categories
        self.reviews_number = reviews_number
        self.avg_rating = avg_rating

        pass

    def describe(self):

        print(
            """
                → Product name : {}\n
                → Product tags : {}\n
                → Product reviews number : {}\n
                → Product average rating : {}
            """.format(
                self.name, 
                self.categories,
                self. reviews_number, 
                self.avg_rating
                )
        )

# -- Main section -- #
if __name__ == "__main__":
    
    john = User(
        username="John", 
        interests='Food, Movies, Personal Care, Music, Book, Sport'
    )
    
    product_table = {} #Dict that will contain product_id as keys and Product objects as values

    for product_id in DATA.id.unique() :

        product_df = DATA[DATA.id == product_id]
        product_table[product_id] = Product(
            name = product_df.name.unique()[0],
            categories = product_df.categories.unique()[0],
            reviews_number = len(product_df),
            avg_rating = product_df['reviews.rating'].mean()
        )

    print(len(DATA))

    # -- Find the 3 most recommended products that John could buy -- #
