import json
import pickle
import numpy as np


__locations = None
__data_columns = None
__models = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__models.predict([x])[0],2)



def get_location():
    load_saved_artifacts()
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts ...... start")
    global __data_columns
    global __locations
    global __models

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    with open('./artifacts/banglore_home_prices_model.pickle','rb') as f:
        __models  = pickle.load(f)
    
    print("loading saved articles ....... done")
 


if __name__ == "__main__":
    print("the function starts here")
    load_saved_artifacts()
    get_location()