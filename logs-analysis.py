#!/usr/bin/env python3

import psycopg2


def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=news")

    # Open a cursor to perform database operations
    cur = conn.cursor()
