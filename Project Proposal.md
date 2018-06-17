Problem Statement

Primary User
Patients with respiratory disease

User Needs Statement
Patients with respiratory illness need to check the air quality and prepare a mask when going to an unfamiliar place in New York.

As-is Process Description
1.	Go to Environment & Health Data Portal
2.	Click Neighborhood report 
3.	Enter a zip code
4.	Check outdoor Air Quality
5.	Prepare a mask if air quality is poor

To-be Process Description
1.	Enter a zip code
2.	Receive a recommendation as to if he/she needs to wear a mask

Information Requirements

Information Inputs
Zip code necessary to see the area’s outdoor air quality

Information Outputs
1.	The area’s outdoor air quality result
2.	Comparison with other area
3.	Recommendation for outdoor activity 
    (e.g. Unhealthy: Do not go out, 
          Moderate: Wear a Mask, 
          Good: Go out free

Technology Requirements

APIs and Web Service Requirements
I might need to use NYC opendata API to download all necessary data in my project repository

Python Package Requirements
This application requires pytest for testing purpose. Also, I will use matplotlib package   display regional comparison results in line and bar graphs

Hardware Requirements
The application will be running on my own local machine. I have no plans to open this application to a public server.

