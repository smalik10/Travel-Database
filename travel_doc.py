import pandas as pd
class travel:
    '''This displays a list of 
    travel destinations.'''
    def __init__(self, dest):
         '''This will retrieve data from 
         a csv file
    Args:
    dest: a file path to the trave list'''
     self.dest = open("travel_destinations.csv", r, encoding = "utf-8")
    
    def travel(df_list):    #Casslyn's Function
        '''This will display a dataframe of
        travel destinations.

        
        Args: 
        df_list: a varible that merges columns together
        
        Returns: a dataframe '''
        
    def filter_distance( dataframe, miles):    #Malik's Function
'''
        Takes the travel dataframe and specified miles and returns a dataframe where specified values are true and the distance to the country is less than the miles specified.
 
        Args:
            dataframe(dataframe): resulting dataframe of travel
            miles(float): distance specified by the user
 
        Returns:
            results(dataframe): dataframe where all the desired values are true
        '''

    def most_popular(dataframe):                 #Malik's Function
        '''
        Find the max number of travelled for any location and return a list of the countries with number of people travelled.

        Args:
            dataframe (dataframe): resulting dataframe of travel

        Returns:
            popular(list): a list of countries with the max number of people travelled in the dataframe

    def seasons_t(t1,t1):
        ''''This shows the user when is the
        best time to travel to a country in 
        comparison to another
        
        Args:
        t1: a tuple/set of countries
        t2: another tuple/set of countries/filter
        
        
        Returns: countries that share things together
        '''
        #Syntax for intersection
        #t1.intersection(t2)
        #ti.intersection_update(t2)
        #return
        #Casslyn Merritt
    def user_input():                          #Casslyn's Fuction
        user_input = input(“Type “where to stay” or “family friendly” to see a list of countries : )
        list_x = ("where to stay", "family friendly")
        for x in list:
            stay_dict = [Nay Pald Hideaway:1,]#finish dict 
            country_family_rank = {1:”Dubai United Arb Emirates”,
                                   3: “Scotland”,2: “Maldives”,
                                   4: “Pakistan”,5: “Philippines”} 
        if user_input == "where to stay":
            return stay_dict
        else:
            print(“you did not type in the correct words”)
            if user  if user_input == “family friendly”:
                return sort(country_family_rank)
            else:
                print(“Incorrect”)
           




