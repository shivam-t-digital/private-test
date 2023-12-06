# # import os
# # from flask import Flask

# # import psycopg2
# # from psycopg2 import sql
# # from urllib.parse import urlparse
# # import socks
# # import socket
# # import requests

# # app = Flask(__name__)

# # proxyDict = {
# #     "http": os.environ.get('FIXIE_URL', ''),
# #     "https": os.environ.get('FIXIE_URL', '')
# # }

# # @app.route('/')
# # def hello():
# #     try:
# #         r = requests.get('https://www.google.com', proxies=proxyDict)
# #         return r.text
# #     except Exception as e:
# #         return f"Error in HTTP request: {e}"

# # @app.route('/dbconnect')
# # def connect():
# #     try:
# #         # Parse the database URL
# #         db_url = "postgres://ucrol25emqd2ch:p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e@ec2-52-2-248-148.compute-1.amazonaws.com:5432/d2r45oj3jf7gs7"
# #         url = urlparse(db_url)

# #         # Set up the proxy settings
# #         print(proxyDict)

# #         # Set up the connection parameters
# #         conn_params = {
# #             'database': url.path[1:],
# #             'user': url.username,
# #             'password': url.password,
# #             'host': url.hostname,
# #             'port': url.port,
# #             'sslmode': 'require',  # Use 'require' to enable SSL
# #             'sslcert': '/certificates/postgresql.crt',  # Path to client certificate file
# #             'sslkey': '/certificates/postgresql.key'  # Path to client key file
# #         }

# #         # Set up the proxy
# #         socks.set_default_proxy(socks.SOCKS5, addr=proxyDict['https'], port=1080)
# #         socket.socket = socks.socksocket

# #         # Connect to the database via proxy
# #         connection = None
# #         try:
# #             connection = psycopg2.connect(**conn_params)
# #             cursor = connection.cursor()

# #             # Example query
# #             query = sql.SQL('SELECT * FROM pgadmin."Prospect" limit 1;')
# #             cursor.execute(query)

# #             # Fetch results
# #             results = cursor.fetchall()
# #             print('results:', results)
# #             return "private_working"

# #         except Exception as db_error:
# #             return f"Database connection error: {db_error}"

# #         finally:
# #             if connection:
# #                 cursor.close()
# #                 connection.close()

# #     except Exception as e:
# #         return f"Error: {e}"

# # if __name__ == '__main__':
# #     app.run(debug=True)


# import os, requests
# from flask import Flask

# import psycopg2
# from psycopg2 import sql
# from urllib.parse import urlparse
# import socks
# import socket

# app = Flask(__name__)

# proxyDict = {
#               "http"  : os.environ.get('FIXIE_URL', ''),
#               "https" : os.environ.get('FIXIE_URL', '')
#  }

# @app.route('/')
# def hello():
#     # return 'Hello from Python!'
#     r = requests.get('https://www.google.com', proxies=proxyDict)
#     # r = requests.get('https://www.google.com')
#     return r.text

# @app.route('/dbconnect')
# def connect():
#     # Parse the database URL
#     db_url = "postgres://ucrol25emqd2ch:p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e@ec2-52-2-248-148.compute-1.amazonaws.com:5432/d2r45oj3jf7gs7"
#     url = urlparse(db_url)
#     # Set up the proxy settings
#     print(proxyDict)
#     # proxy_host = proxyDict['http']
#     proxy_ips = ['54.173.229.200', '54.175.230.252']
#     proxy_port = 1080
#     proxy_type = socks.SOCKS5  # Change this based on your proxy type

#     selected_proxy_ip = proxy_ips[0]
#     # Set up the connection parameters
#     conn_params = {
#         'database': url.path[1:],
#         'user': url.username,
#         'password': url.password,
#         'host': url.hostname,
#         'port': url.port,
#         'sslmode': 'require',  # Use 'require' to enable SSL
#         'sslcert': '/certificates/postgresql.crt',  # Path to client certificate file
#         'sslkey': '/certificates/postgresql.key',  # Pat
#         'sslrootcert': '/certificates/root.crt'
#     }

#     # Set up the proxy
#     socks.set_default_proxy(proxy_type, addr=selected_proxy_ip, port=proxy_port)
#     socket.socket = socks.socksocket

#     # Connect to the database via proxy
#     try:
#         connection = psycopg2.connect(**conn_params)
#         cursor = connection.cursor()

#         # Example query
#         query = sql.SQL('SELECT * FROM pgadmin."Prospect" limit 1;')
#         cursor.execute(query)

#         # Fetch results
#         results = cursor.fetchall()
#         print('results:', results)
#         return "private_working"

#     except Exception as e:
#         print(f"Error: {e}")

#     # finally:
#     #     if connection:
#     #         cursor.close()
#     #         connection.close()

# if __name__ == '__main__':
#    app.run(debug=True)


import sqlalchemy
import os
import urllib.parse as urlparse

# Parse Fixie URL from environment variable
# fixie_url = "http://fixie:YpcpuxmrFDMenhX@velodrome.usefixie.com:80"
fixie_url = "https://r09cndoizux678:44m6nmtadw9bg10eowfxi45cyrbyku@us-east-shield-04.quotaguard.com:9294"
parsed_fixie = urlparse.urlparse(fixie_url)
fixie_host, fixie_port = parsed_fixie.hostname, parsed_fixie.port
fixie_user, fixie_pass = parsed_fixie.username, parsed_fixie.password

# Your PostgreSQL connection string
# Example: "postgresql://username:password@hostname:port/dbname"
postgres_connection_string = "postgres://ucrol25emqd2ch:p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e@ec2-52-2-248-148.compute-1.amazonaws.com:5432/d2r45oj3jf7gs7"
print("fixie_user: ",fixie_user)
print("fixie_pass: ",fixie_pass)
# Create an engine that routes through the proxy
engine = sqlalchemy.create_engine(
    # Equivalent URL:
    # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
    sqlalchemy.engine.url.URL.create(
        drivername="postgresql",
        username="ucrol25emqd2ch",
        password="p31d791a3fe8bcb5b5102d7b8b43f08ca70ee2cc9d7943c23b4db6b110324346e",
        host="ec2-52-2-248-148.compute-1.amazonaws.com",
        port=5432,
        database="d2r45oj3jf7gs7",

    ),
    connect_args={
        "sslmode": 'require',  # Use 'require' to enable SSL
        'sslcert': '/postgresql.crt',  # Path to client certificate file
        'sslkey': '/postgresql.key',  # Pat
        'sslrootcert': '/root.crt',
        'user': fixie_user,
        'password': fixie_pass,
        'host': fixie_host,
        'port': fixie_port
    },
    # ...
)

# Test the connection
try:
    print("engine: ",engine)
    with engine.connect() as connection:
        print("connection: ",connection)
        result = connection.execute("SELECT 101")
        for row in result:
            print("Connection test: ", row)
    print("Connection to the database was successful!")
except Exception as e:
    print("Error connecting to the database: ", e)
