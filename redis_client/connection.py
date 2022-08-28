
"""
@author: Charcape
"""

# Importando librerias
from redis import Redis
from redis.exceptions import ConnectionError


try:
  r_client = Redis(
  host= 'us1-excited-herring-38157.upstash.io',
  port= '38157',
  password= '896941d46bec4fa8b3c8793431dbb6b4')
  
  print("CONNECTED TO REDIS")
  
  
except ConnectionError as e:
    print(e)