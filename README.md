Air Quality App:

I developed this App as the freestyle project for the python programming taught by Professor Mike Rossetti at NYU. 
The app allows the patients with respiratory disease to check the air quality of the area where they want to visit in the US. Also, it suggests them what they have to prepare to travel that area. Using this app, the patients can avoid the risk of being exposed to poor air in unfamilar area.



Getting Started:

This app requires the patients to have access to an API key from the AirNow. The user can request an API key at https://docs.airnowapi.org/ and the app will ask for an API key before pulling the information about buses.



Detailed: 
Before using this app, the patients should have gone to air quality web site like AirNow and searched the air quality in specific area and date. Even if they get the information, they did not know what they should do and prepare. In this application, they only need to enter two parameters (zip code and date), and they receive the suggestions (eg wearing a mask) necessary to protect yourself in case of poor air quality area.



Prerequisites:

This app was designed for Python 3 and requires some python packages. The app uses: csv, dotenv, json, os, pdb, requests, datetime


Installation:
Download the source code

git clone https://github.com/jaykoo0708/Free-Style-Project
cd Free-Style-Project\app



Usage
To run the app, from the Free-Style-Project\app working directory, in your shell:
python app\app.py



Author:

Jay Koo



License:

This project is licensed under the MIT License - see the LICENSE.md file for details

