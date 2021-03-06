import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect("dbname='a3'")
        """
        If you're using your own computer, and not grieg, you should use the line below instead
        with the correct credentials
        conn = psycopg2.connect("dbname='DBNAME' user='USERNAME' host='localhost' password='PASSWORD'")
        """
        conn.set_client_encoding('UTF8')
    except Exception as e:
        print("Unable to connect to the database")
    return conn
