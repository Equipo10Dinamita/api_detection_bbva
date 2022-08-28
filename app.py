
"""
@author: EquipoDinamita
"""

# Importando librerias
from flask import Flask, jsonify, request, redirect
import os
from redis_client.connection import r_client


app = Flask(__name__)
app.url_map.strict_slashes = False



""" Endpoint de prueba """

@app.route('/api/bbva-detection/v1', methods=["GET"])
def test():
    response = {
        "status": 'success',
        "message": 'Bienvenido al api de Detección de Movimiento de BBVA'
    }
    return response,200

@app.route('/api/bbva-detection/v1/aforo', methods=["GET"])
def aforo():
    response =  { 
        "status" : "success", 
        "message": str(r_client.get("person"))
                 
    }
    return response,200



if __name__ == "__main__":
    app.run()
    


