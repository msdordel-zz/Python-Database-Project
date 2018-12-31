#!/usr/bin/env python3

import psycopg2


def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    
    #queries go here
    
    def popular_articles():
    # Returns the top 3 most popular articles
    connection, cursor = connect()

    query = """

            """
    cursor.execute(query)
    article_count = cursor.fetchall()
    connection.close()
        
    return article_count
    
    def popular_authors():
    # Returns a list of the most popular authors
    connection, cursor = connect()

    query = """

            """
    cursor.execute(query)
    authors = cursor.fetchall()
    connection.close()

    return authors

def error_days():
    # Reports Days that have more then 1% errors
    connection, cursor = connect()

    query = """

            """
    
    cursor.execute(query)
    errors = cursor.fetchall()
    connection.close()

    return errors
    
        # Close communication with the database
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
