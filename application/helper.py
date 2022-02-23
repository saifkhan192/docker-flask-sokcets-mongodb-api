import os

from pymongo import MongoClient


def evaluate_formula(formula, time, distance):
    formula = formula.replace("time", str(time))
    formula = formula.replace("distance", str(distance))
    fare_amount = eval(formula)
    return fare_amount


# def start_debugger():
#     # if os.environ.get('VSCODE_DEBUG'):
#     debugAddress = os.environ.get('DEBUG_CONFIG', "0.0.0.0:5678").split(":")
#     try:
#         import ptvsd
#         ptvsd.enable_attach(address=debugAddress)
#     except Exception as ex:
#         pass
