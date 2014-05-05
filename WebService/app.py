import shelve
from subprocess import check_output
import flask
#Merged with flask module above
# from flask import request, jsonify
import StringIO
import pandas as pd
from pandas import Series, DataFrame
import os
from os import environ

app = flask.Flask(__name__, static_url_path = '/oakland')
app.debug = True

def create_filepath(filename):
    return os.path.join('data/%s' % filename)

def open_city_file(filepath):
    '''Pass file path string as parameters, generate dataframe from the file'''    
    df = pd.read_csv(filepath)
    df = df.rename(columns = {'RegionName':'City'})
    return df.fillna(0)
def open_neighbor_file(filepath):
    df = pd.read_csv(filepath)
    df = df.rename(columns = {'RegionName':'Neighborhood'})
    return df.fillna(0)

def get_data_by_state_city(df,state,city):
    '''filter by state and city, drop specified columns, return new dataframe'''
    # Reuse viarable to store changed value. Not change the parameter itself outside the function
    df = df[(df.State==state) & (df.City==city)]  
    return df#.set_index("RegionName", inplace=True)


def select_value_by_year_month(df, year, month):
    '''Generate home value for mapping the whole city at specified year-month'''
    return df[['Neighborhood', year + '-' + month]]
        
def select_value_by_neighborhood(df, neighborhood, drop=[]):
    '''Generate all time home value for a neighborhood'''
    # oakland_df.dropna(how='all') vs. df.dropna() for any row w/ NaN
    df = df[df.Neighborhood==neighborhood].drop(drop,axis=1).transpose() 
    df.index = pd.to_datetime(df.index)
    
    #df can be slice by date: df[20140101]
    return df

@app.route('/oakland/<year>/<month>', methods=['GET'])
def homevalue_get(year,month):
    """get year-month and return homevalue"""
    path = create_filepath('Neighborhood_Zhvi_AllHomes.csv')
    df = open_neighbor_file(path)
    oak_df = get_data_by_state_city(df, 'CA', 'Oakland')
    neighbor_year_month = select_value_by_year_month(oak_df, year,month)

    s = StringIO.StringIO()
    neighbor_year_month.to_csv(s, index=False)

    response = flask.make_response(s.getvalue())
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/oakland/hometopojson', methods=['GET'])
def hometopojson_get():
    with open (create_filepath('oakland_by_neighborhood.json'),'r') as jsonfile:
        data = jsonfile.read()
        response = flask.make_response(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


if __name__ == "__main__":
	# app.debug = True
    app.run(port=int(environ['FLASK_PORT']))