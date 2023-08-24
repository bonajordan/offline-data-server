# offline-data-server
A flask application that returns randomly selected json data

The profiles are generated using the python faker module. The profile can be generated for a specified locale(s) or by it's default locale.

The other data are from csv files opened and edited using pandas and stored in a pickledb database.

The datasets (csv files) are gotten from Kaggle.

This simple application can help developers who need to quickly test their api development codes, data pipelines code etc. with any simple data without having to access the internet during development. It can also be helpful to people who just want to study Python code for understanding.

Clone this repository to your PC or copy it to your PC, create a virtual environment for it, activate the virtual environment then navigate to the cloned/copied directory and run 'pip install requirements.txt' to install it's dependencies. Make sure you are connected to the internet when installing the dependencies after that you can disconnect.

Initiate the pickledb database by running 'python pickledb_init.py' to create and populate the pickledb database and start the flask application by running 'python flask_server.py' after which you can start making GET calls to the running server

You can add your own datasets by copying the csv file to the "./DB/csv/" folder, running pickledb_init.py, creating your own url endpoint for the new dataset in the flask_app.py file and creating it's corresponding generator in the generator.py file.


Valid default urls are:

http://localhost:5000/profile

http://localhost:5000/profile/num

http://localhost:5000/profile-country

http://localhost:5000/profile-country/num

http://localhost:5000/weather

http://localhost:5000/weather/num

http://localhost:5000/sport_car_price

http://localhost:5000/sport_car_price/num

http://localhost:5000/employee_info

http://localhost:5000/employee_info/num

http://localhost:5000/supermarket_sales

http://localhost:5000/supermarket_sales/num

http://localhost:5000/book_info

http://localhost:5000/book_info/num

http://localhost:5000/quote

http://localhost:5000/quote/num
		
'num' is a number and 

'country' is any country in the list:
['France', 'Italy', 'Azerbaijan', 'Bangladesh', 'Czech', 'Denmark','Austria', 'Greece', 'India', 'Iran', 'Finland', 'Israel', 'Hungary', 'Armenia','Indonesia', 'Japan', 'Georgia', 'Nepal', 'Belgium', 'China', 'Russia','Ukraine', 'Romania', 'Sweden', 'Brazil', 'Netherlands', 'Slovakia', 'Norway']
	
The 'num' variable returns a json containing that number of corresponding data. 

	Example; "http://localhost:5000/quote/3" returns a json containing 3 quotes and their individual info.
			
The 'country' variable returns a json with a profile specific to a particular country.

	Example; "http://localhost:5000/profile-Japan" returns a json of a fake profile similar to that of a Japanese.
 
	Example; "http://localhost:5000/profile-Japan/3" returns a json containing 3 fake Japanese profiles.
 
	N/B: It is not first letter case sensitive so "Japan" and "japan" are valid. However, take note of the fact that profiles with locales like Japan will return certain special characters for "name", "address" etc. So be aware of encodings and how to handle them. Using the print function of python on the characters shows them exactly how they are to be displayed.


You can reach out to me if you have any issues

HAPPY CODING!!!
