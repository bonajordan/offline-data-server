from flask import Flask, jsonify,url_for
from generator import Generator


app = Flask(__name__)


@app.route("/",methods=["GET"])
def home():
    return jsonify({"message":"Hello, Data Seeker!"})



#--------------------------PROFILE------------------------------------
@app.route("/profile",methods=["GET"])
def get_mock_profile():
    profile = {"profile":Generator().profile_generator()}
    return jsonify(profile)

@app.route("/profile/<int:i>",methods=["GET"])
def get_mock_profiles(i):
    profiles = {"profiles":Generator().profile_generator(num=i)}
    return jsonify(profiles)

@app.route("/profile-<country>",methods=["GET"])
def get_mock_profile_with_locale(country):
    profile = {"profile":Generator().profile_generator(locale=country)}
    return jsonify(profile)

@app.route("/profile-<country>/<int:i>",methods=["GET"])
def get_mock_profiles_with_locale(country,i):
    profiles = {"profiles":Generator().profile_generator(locale=country,num=i)}
    return jsonify(profiles)



#--------------------------WEATHER------------------------------------
@app.route("/weather",methods=["GET"])
def get_weather_report():
    weather_report = Generator().weather_generator()
    return jsonify({"Weather-Report":weather_report})

@app.route("/weather/<int:i>",methods=["GET"])
def get_weather_reports(i):
    weather_reports = Generator().weather_generator(num=i)
    return jsonify({"Weather-Reports":weather_reports})



#--------------------------SPORT CAR PRICE------------------------------------
@app.route("/sport_car_price",methods=["GET"])
def get_sport_car_price():
    sport_car_price = Generator().sport_car_price_generator()
    return jsonify({"Sport Car Price":sport_car_price})

@app.route("/sport_car_price/<int:i>",methods=["GET"])
def get_sport_car_prices(i):
    sport_car_prices = Generator().sport_car_price_generator(num=i)
    return jsonify({"Sport Car Prices":sport_car_prices})


#----------------------EMPLOYEE SALARY--------------------------------
@app.route("/employee_info",methods=["GET"])
def get_employee_info():
    employee_info = Generator().employee_info_generator()
    return jsonify({"Employee Info":employee_info})

@app.route("/employee_info/<int:i>",methods=["GET"])
def get_employees_info(i):
    employees_info = Generator().employee_info_generator(num=i)
    return jsonify({"Employees Info":employees_info})




#--------------------SUPERMARKET SALES DATA----------------------------------
@app.route("/supermarket_sales",methods=["GET"])
def get_supermarket_sale_info():
    sale_info = Generator().supermarket_sale_info()
    return jsonify({"Supermarket Sale":sale_info})

@app.route("/supermarket_sales/<int:i>",methods=["GET"])
def get_supermarket_sales_info(i):
    sales_info = Generator().supermarket_sale_info(num=i)
    return jsonify({"Supermarket Sales":sales_info})



#--------------------BOOKS DATA----------------------------------
@app.route("/book_info",methods=["GET"])
def get_book_info():
    book_info = Generator().book_info_generator()
    return jsonify({"Book Info":book_info})

@app.route("/book_info/<int:i>",methods=["GET"])
def get_books_info(i):
    books_info = Generator().book_info_generator(num=i)
    return jsonify({"Books Info":books_info})


#--------------------QUOTES----------------------------------
@app.route("/quote",methods=["GET"])
def get_quote():
    quote = Generator().quote_generator()
    return jsonify({"Quote":quote})

@app.route("/quote/<int:i>",methods=["GET"])
def get_quotes(i):
    quotes = Generator().quote_generator(num=i)
    return jsonify({"Quotes":quotes})

if __name__ == "__main__":
    app.run(debug=True)





