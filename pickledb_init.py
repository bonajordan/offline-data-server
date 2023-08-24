import pandas as pd
import pickledb, os


class PCKDatabase:
    """Initiates the pickledatabase and
        populates it with data from .csv files saved in ./DB/csv
    """
    def __init__(self):
        cwd = os.getcwd()
        self.dictionary = {}
        self.path_to_csv_files = os.path.join(cwd,"DB/csv/")
        self.csv_files = [z for (x,y,z) in os.walk(self.path_to_csv_files)][0]
        self.database_conn = pickledb.load("DB/database.db",auto_dump=True)


    def create_dict(self):
        """Creates a dictionary with csv filename without the '.csv' extension  as KEY and pandas.DataFrame of the
            corresponding csv file as VALUE"""
        for file_name in self.csv_files:
            key = file_name[:-4]
            abspath = f"{self.path_to_csv_files}{file_name}"
            dataframe = pd.read_csv(abspath)
            self.dictionary[key] = pd.read_csv(abspath)
        self.populate_database(self.dictionary)            


    def populate_database(self,dict_):
        if dict_:
            for key in dict_:
                self.database_conn.set(key,self.pd_to_dict_for_pickledb(dict_[key]))
                

    def pd_to_dict_for_pickledb(self,dataframe):
        """Takes a pandas dataframe and converts it to a dictionary with indexes as key
            and value of {column_name:column_value}"""
        indexes = list(dataframe.index)
        d = {}
        for ind in indexes:
            d[str(ind)]= dataframe.iloc[ind].to_dict()
        return d


    def get_all_database_keys(self):
        """Returns all keys in the pickledb database"""
        return self.database_conn.getall()


    def get_value_from_database(self,key):
        """Takes a key and returns it's value in the pickledb database"""
        return self.database_conn.get(key)

if __name__ == "__main__":
    print("Creating and populating pickledb database............")
    PCKDatabase().create_dict()
    print("Pickledb database created and populated!")


