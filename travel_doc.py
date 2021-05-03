from argparse import ArgumentParser
import pandas as pd
import sys
class Travel:
    '''This displays a list of 
    travel destinations.
    '''
    
    def __init__(self, filepath):
        '''Initializes Travel object'''
        self.filepath = filepath
    
    def travel_dataframe(df_list):    #Casslyn's Function
        '''This will display a dataframe of
        travel destinations ranked from 1-5.

        
        Args: 
        df_list: a string containing a filepath to travel dataframe
        travel_list: a variable that reads travel dataframe
        
        Returns: a sorted coloumn of ranked countries 1-5
        '''
        travel_list = pd.read_csv(df_list)
        return travel_list.sort_values(ascending=False)
                 
    def travel(self):    #Casslyn's Function
        '''Returns a sorted coloumn of ranked countries 1-5 with
        a description.
    
        Att:?????????
        best_rank: a variable that merges three dataframe columns together 
    
        SideEffects: alters list of dataframe
   
        Returns: a list of ranked countries with their description '''
    
   
    best_rank = self.travel_list.[["Rank","Country","Dont miss"]] 
    return best_rank
    

        
    def filter_distance( dataframe, miles):    #Malik's Function
        '''
        Takes the travel dataframe and specified miles and 
        returns a dataframe where specified values are true 
        and the distance to the country is less than the miles specified.
 
        Args:
            dataframe(dataframe): resulting dataframe of travel
            miles(float): distance specified by the user
 
        Returns:
            results(dataframe): dataframe where all the desired values are true
        '''
        for countries in dataframe:
            results = dataframe[dataframe["Distance"] <= miles].groupby("Country")["Rank"].min()
            return results

    def most_popular(dataframe):                 #Malik's Function
        '''
        Find the max number of travelled for any location 
        and return a list of the countries with number of people travelled.

        Args:
            dataframe (dataframe): resulting dataframe of travel

        Returns:
            popular(list): a list of countries with 
            the max number of people travelled in the dataframe

   
    def user_input(user_input,list_x): #Casslyn's Fuction
        '''This asks for user input to get a list of
        hotels or a rank of family friendly countries
        
        Args:
            user_input: a string asking for user input
            list_x: a list containing keywords for user input
                
        SideEffects: Alters rank of list
            
        
        Retruns: a list of family friendly coutnries from least to greatest 
        '''
        user_input = input('Type 1 for “where to stay” or 2 “family friendly” to see a list of countries:')
        stay_dict = {"Nay Pald Hideaway":1,"Greenland Fairy Meadow Resort":2,
        "Velaa Private Island Resort":3,"wild camping in Mull":4,
        "Hotel Melia":5}
        
        key_stay = "Key box for countries: 1 = Philippines,2 = Pakistan,3 = Maldives,4 = Scotland,5 = Dubai"
        country_family_rank = {"Dubai":1,
        "Scotland":4,"Maldives":2,
        "Pakistan":3,"Philippines":5}
        n_2 = sorted(country_family_rank)
        
        while True:
        
            user_input = input('Type 1 for “where to stay” or 2 for “family friendly” to see a list of countries:' )
        
            if user_input != '1' or user_input != '2':
                print(input("You did not type in the correct words. Please try again:"))
                continue
        
            if user_input == '1':
                print(key_stay,stay_dict)
                break
        
            if user_input == '2':
                print(n_2)
                break
    def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables pd_list.
    """
        parser = ArgumentParser()
        parser.add_argument("pd_list", help="CSV containing travel destinations")
        #parser.add_argument("rating_csv", help="CSV containing ratings")
        return parser.parse_args(arglist)

                
   def main():
    '''Main will test and run code. Will display dataframe
        and user input
    '''
  if __name__ == "__main__":
       main()
                     




