import mysql.connector
from dotenv import dotenv_values


ENV_KEYS=dotenv_values(".env")

try:
    con=mysql.connector.connect(
        host=ENV_KEYS.get("DB_HOST"),
        database=ENV_KEYS.get("DB_NAME"),
        user=ENV_KEYS.get("DB_USERNAME"),
        password=ENV_KEYS.get("DB_PASSWORD")
      )
    
    con.close()
except mysql.connector.Error as e:
    print(e)