import csv
from dotenv import load_dotenv
import json
import os
import pdb
import requests
import datetime

airStatusDict = {"1":"Go out free","2":"Go out for short time.","3":"Wear a mask","4":"Wear a Special mask","5":"Stay Home ","6":"Stay Home","7":"Unavialbale"}

def validate(date_text): # only validating the date
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        return False



def calculateIndexes(forecastDict,date,zipcode):
    for item in forecastDict:
        #         item["DateForecast"] = trim(item["DateForecast"])

        #         print(date)
        #         print(date == item["DateForecast"])
        if item["DateForecast"].strip() == date and item["ParameterName"] == "O3": #checking the forecast with the today's date

            if str(item["Category"]["Number"]) in airStatusDict:
                value = airStatusDict[str(item["Category"]["Number"])]
                AQI = item["AQI"]
                status = item["Category"]["Name"]
                print()
                print("==========================================")
                print("[Air Quality Overview]")
                print(f"Date: {date}")
                print(f"Zip Code: {zipcode}")
                print(f"AQI(Air Quality Index): {AQI}")
                print(f"Air Quality Status: {status}")
                print("==========================================")
                print("Our suggestion is:", f"{value}")
                print("==========================================")
                print()
                print("Remember when atmospheric contaminants were romantically called stardust?")
                print("                                                     — Lane Olinghouse")


def parse_response(response_text):  # json validation
    # pdb.set_trace()
    # response_text can be either a raw JSON string or an already-converted dictionary
    if isinstance(response_text, str): # if not yet converted, then:
        response_text = json.loads(response_text) # convert string to dictionary
        return response_text



def enterZipCode():
    zip_code = input("please enter a zip code: ")

    while len(zip_code) != 5:
        print("Enter the correct zip code")
        zip_code = input("please enter a zip code: ")
    return zip_code
# url = "http://api.waqi.info/feed/shanghai/?token=demo"
# url = "http://aqicn.org/here/"
# url = "https://api.breezometer.com/baqi/?lat=40.7128&lon=-74.0060&key=5d7391cea8d84309b684d5f16875e5fb"

def getDateFromAPI(url):

    #url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if "Error Message" in response.text:
        print("REQUEST ERROR, PLEASE TRY AGAIN. CHECK YOUR STOCK SYMBOL.")
        quit("Stopping the program")
    return response


def run():
    zip_code = enterZipCode()
    flag = True
    while flag == True:
        try:
            date = input("Enter the date (yyyy-mm-dd)")
            validate(date)
            flag  = False
        except ValueError:
            print("ENTER THE DATE IN THE RIGHT FORMAT")

    url = f"http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date}&distance=25&API_KEY=57C79EF5-9D49-402F-81BC-84049DE053B8"

    # PARSE RESPONSE (AS LONG AS THERE ARE NO ERRORS)
    response = getDateFromAPI(url)
    forecastDict = parse_response(response.text)
    #print(forecastDict)
    calculateIndexes(forecastDict,date,zip_code)

if __name__ == "__main__":
    run()
