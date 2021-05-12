from argparse import ArgumentParser
import pandas as pd
import sys

class Travel:
    '''This displays a list of 

    travel destinations.
    
    '''
    

    def __init__(self, filepath):

        '''Initializes Travel object'''

        self.filepath = pd.read_csv('travel_dest.csv')
    

    def travel_dataframe(self):    #Casslyn's Function
        

        '''This will display a dataframe of

        travel destinations ranked from 1-5.
        
        SideEffects: alters list of dataframe
        
        Returns: a sorted coloumn of ranked countries 1-5
        
        '''
        
        self_run = self.filepath.sort_values(by='Country', ascending=False)

       
        print(self_run)
                 

    def travel(self):    #Casslyn's Function
        
        '''Returns a sorted coloumn of ranked countries 1-5 with

        a description.
    

        Args:

        best_rank: a variable that merges three dataframe columns together 
    

        SideEffects: alters list of dataframe
   

        Returns: a list of ranked countries with their description
        
        '''
    
   

        best_rank = self.filepath[["Rank","Country","Don't miss"]] 

        return best_rank
    

        

    def filter_distance(self,miles):    #Malik's Function


        '''Takes the travel dataframe and specified miles and 

        returns a dataframe where specified values are true 

        and the distance to the country is less than the miles specified.
 

        Args:

        dataframe(dataframe): resulting dataframe of travel

        miles(float): distance specified by the user
 

        Returns:

        results(dataframe): dataframe where all the desired values are true
        
        '''
        #for countries in dataframe:

        results = self.filepath[self.filepath["Distance"]<= miles].groupby("Country")["Rank"].min()
        #return results
        print(results)


    def most_popular(self):   #Malik's Function
        '''Find the max number of travelled for any location 

        and return a list of the countries with number of people travelled.


        Args:

        dataframe (dataframe): resulting dataframe of travel


        Returns:

        popular(list): a list of countries with 

        the max number of people travelled in the dataframe
            
        '''
              

        most_pop = self.filepath.max()

        most_travelled = self.filepath[self.filepath == most_pop].index.tolist()
        

        print(f'This is the most popular destinations traveled {most_travelled}')


    def user_input(self): #Casslyn's Fuction

        '''This asks for user input to get a list of

        hotels or a rank of family friendly countries
        

        Args:

        user_input: a string asking for user input

        list_x: a list containing keywords for user input
                

        SideEffects: Alters rank of list
            
        

        Retruns: a list of family friendly countries from least to greatest'''
        

        

        stay_dict = {"Nay Pald Hideaway":1,"Greenland Fairy Meadow Resort":2,

        "Velaa Private Island Resort":3,"wild camping in Mull":4,

        "Hotel Melia":5}
        

        key_stay = "Key box for countries: 1 = Philippines,2 = Pakistan,3 = Maldives,4 = Scotland,5 = Dubai"

        country_family_rank = {"Dubai":1,

        "Scotland":4,"Maldives":2,

        "Pakistan":3,"Philippines":5}

        n_2 = sorted(country_family_rank)
        

        while True:
        

            user_type = input('Type 1 for “where to stay” or 2 for “family friendly” to see a list of countries:' )
        
           
        

            if user_type == '1':

                print(key_stay,stay_dict)

                break
        

            if user_type == '2':

                print(n_2)

                break

def parse_args(arglist):

    '''Parse command-line arguments.
    

    Args:

    arglist (list of str): a list of command-line arguments.
    

    Returns:

    args: the parsed command-line arguments as a namespace
    
    '''

    parser = ArgumentParser()

    parser.add_argument("filepath", help="CSV containing travel destinations")
    parser.add_argument("miles", type=int, help= "Distance from countries")

    args = parser.parse_args(arglist)
    

    return args




def main(argmain,miles):

    '''Main will test and run all methods within Travel class.'''

    var = Travel(argmain)

    var.travel_dataframe()
    
    var.travel()

    var.filter_distance(miles)

    var.most_popular()

    var.user_input()
    
    

if __name__ == "__main__":

    '''This will invoke

    main() function.
    

    Returns: altered dataframes related to its method
    
    '''
    args = parse_args(sys.argv[1:])
    
    main(args.filepath,args.miles)
                     





