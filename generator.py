import faker, random, datetime
import pickledb


#'employees_info','sport_car_prices','weather','supermarket_sales','books','quotes'--------------> default keys in pickledb database

dict_of_locales = {"France":"fr_FR","Italy":"it_IT","Azerbaijan":"az_AZ","Bangladesh":"bn_BD","Czech":"cs_CZ",
                     "Denmark":"da_DK","de_AT":"Austria",
                     "Greece":"el_GR","India":["ta_IN","hi_IN","en_IN"],"Iran":"fa_IR",
                     "Finland":"fi_FI","Israel":"he_IL","Hungary":"hu_HU","Armenia":"hy_AM",
                     "Indonesia":["id_ID"],"Japan":"ja_JP","Georgia":"ka_GE","South-Korea":"ko_KR",
                     "Nepal":"ne_NP","Belgium":"nl_BE","China":"zh_CN",
                     "Russia":"ru_RU","Ukraine":"uk_UK","Romania":"ro_RO","Sweden":"sv_SE",
                     "Brazil":"pt_BR","Netherlands":"nl_NL","Slovakia":"sk_SK",
                     "Norway":"no_NO"
                    }

db_conn = pickledb.load("DB/database.db",False)


class Generator:
    def __init__(self):
        self.database_conn = db_conn
        self.current_year = datetime.datetime.utcnow().year #current year
        self.max_year = self.current_year - 18          #max year for profile age
        self.min_year = self.current_year - 70          #min year for profile age
        self.valid_profile_years = [year for year in range(self.min_year,self.max_year+1)] #list containing numbers representing years

    def employee_info_generator(self,num=1):
        """Generates random employee info"""
        employee_info = self.data_generator_from_db("employees_info",num)
        return employee_info
   
    def sport_car_price_generator(self,num=1):
        """Generates random sport car pricing info"""
        sport_car_price = self.data_generator_from_db("sport_car_prices",num)
        return sport_car_price
    
    def weather_generator(self,num=1):
        """Generates random simple weather info"""
        weather_report = self.data_generator_from_db("weather",num)
        return weather_report

    def supermarket_sale_info(self,num=1):
        """Generates random supermarket sales info"""
        sale_info = self.data_generator_from_db("supermarket_sales",num)
        return sale_info

    def book_info_generator(self,num=1):
        """Generates random book info"""
        book_info = self.data_generator_from_db("books",num)
        return book_info

    def quote_generator(self,num=1):
        """Generates a random quote"""
        quote = self.data_generator_from_db("quotes",num)
        return quote

    def profile_generator(self,locale=None,num=1):
        """Generates a random profile using the faker package, if locale is specified then the faker instance
        is instantiated with the appropriate locale(s)"""
        if num <= 1:
            if locale:
                f = faker.Faker(dict_of_locales[locale.capitalize()])
                profile = self.profile_value_converter_editor(f.profile())
                return profile
            else:
                f = faker.Faker()
                profile = self.profile_value_converter_editor(f.profile())
                return profile
        elif num > 1:
            if locale:
                f = faker.Faker(dict_of_locales[locale.capitalize()])
                profiles = [self.profile_value_converter_editor(f.profile()) for i in range(num)]
                return profiles
            else:
                f = faker.Faker()
                profiles = [self.profile_value_converter_editor(f.profile()) for i in range(num)]
                return profiles


    def data_generator_from_db(self,data_key,num=1):
        """Handles data generation from data pre-saved in pickledb database
        Saved data in database is in example format {"weather":{"0":{key:value},"1":{key:value}...},
        "salaries":{"0":{key:value},"1":{key:value}...}}
        """
        data = self.database_conn.get(data_key)
        keys = list(data.keys())        #Get keys of the specific data needed
        if num <= 1:
            random_key = random.choice(keys)
            result = data.get(random_key)
            return result
        elif num > 1:
            random_keys = random.choices(keys,k=num)
            results = [data.get(key) for key in random_keys]
            return results


    def profile_value_converter_editor(self,profile):
        """Fake profiles generated with the faker package have a key 'birthdate' with a value of type datetime.date and a
            key 'current_location' with a value of type 'Decimal' which are not json serializable so they need
            to be converted to string and float respectively.

            Birthdate is also edited to ensure ages are between 18 to 65
        """
        profile["current_location"] = (float(profile["current_location"][0]),
                                       float(profile["current_location"][1]))
        
        bd_year = profile["birthdate"].year
        birthdate_string = str(profile["birthdate"])
        if (self.max_year < bd_year) or (self.min_year > bd_year):
            year = random.choice(self.valid_profile_years)
            birthdate = birthdate_string.split("-")
            birthdate[0] = str(year)
            birthdate_string = "-".join(birthdate)
            profile["birthdate"] = birthdate_string
        else:
            profile["birthdate"] = birthdate_string
            
        return profile
