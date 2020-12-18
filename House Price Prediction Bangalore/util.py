import json
import pickle
import numpy as np

# Global variables created
__locations = None
__data_columns = None
__model = None

# 2 - Routine to get estimated price
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower()) # since all locations are in lowercase
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # its same like predict in linear model. its takes 2D array as input
    return round(__model.predict([x])[0], 2)

# 1 - Routine for location
def load_saved_artifacts():
    print("Loading saved artifacts....starts")
    global __data_columns
    global __locations

    # open columns.json file to extract locations
    with open("./artifacts/columns1.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:] #to extract locations

    global __model
    with open("./artifacts/banglore_home_prices_model1.pickle",'rb') as f: #rb since its a binary file
        __model = pickle.load(f)
    print("Loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) #Other
    # print(get_estimated_price())