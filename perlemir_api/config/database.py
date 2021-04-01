"""
  Author:     Lane Adair (ladair@unca.edu)
  Date:       February 4, 2020
  Version:    0.0.1
"""



import mysql.connector
import config

conn = mysql.connector.connect(
    host = config.DB_HOST,
    user = config.DB_USER,
    password = config.DB_PWD_HASH
)