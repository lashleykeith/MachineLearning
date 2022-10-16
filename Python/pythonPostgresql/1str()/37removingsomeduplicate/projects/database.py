import psycopg2

def connect():
    return psycopg2.connect(user='postgres', password='14Lunchtime', database='learning', host='localhost')
