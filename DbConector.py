import psycopg2
from configparser import ConfigParser


class DbConector:

    def __init__(self):
        self.db_config = self.config()

    def write_film_offer(self, user_id, film):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT film FROM film_offer WHERE user_id='{0}'".format(user_id))
        result = cur.fetchone()
        if result is None:
            cur.execute("INSERT INTO FROM film_offer VALUES {0}, {1}".format(user_id, film))
        conn.close()

    def get_film_offers(self, user_id):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT film FROM film_offer WHERE user_id='{0}'".format(user_id))
        result = cur.fetchone()
        conn.close()
        return result

    def get_connection(self):
        conn = psycopg2.connect(**self.db_config)
        return conn


    def config(self, filename = 'database.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db
