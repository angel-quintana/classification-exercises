'''
neccesary imports
'''

import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import env

'''
imports data from titanic db
'''
def get_titanic_data():
    filename = 'titanic.csv'
    url = env.get_db_url('titanic_db')
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql('select * from passengers', url)

        #save to csv
        df.to_csv(filename)

'''
imports data from iris db
'''

def get_iris_data():
    filename = 'iris.csv'
    url = env.get_db_url('iris_db')
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql('select * from measurements join species using(species_id)', url)

        #save to csv
        df.to_csv(filename)

'''
imports data from telco_churn db
'''

def get_telco_data():
    filename = 'telco.csv'
    url = env.get_db_url('telco_churn')
    if os.path.exists(filename):
        print('this file exists, reading from csv')
        #read from csv
        df = pd.read_csv(filename)
    else:
        print('this file doesnt exist, reading from sql and saving to csv')
        #read from sql
        df = pd.read_sql('''
        
        select * from customers
	join contract_types using(contract_type_id)
    join internet_service_types using(internet_service_type_id)
    join payment_types using(payment_type_id)''', url)

        #save to csv
        df.to_csv(filename)