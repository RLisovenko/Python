"""
        Description: https://leetcode.com/problems/not-boring-movies/?lang=pythondata
        Author:      RuslanLisovenko@gmail.com
        Date:        2111-2023
"""

import pandas as pd

data = [[1, 'War', 'great 3D', 8.9], [2, 'Science', 'fiction', 8.5], [3, 'irish', 'boring', 6.2], [4, 'Ice song', 'Fantacy', 8.6], [5, 'House card', 'Interesting', 9.1]]
cinema = pd.DataFrame(data, columns=['id', 'movie', 'description', 'rating']).astype({'id':'Int64', 'movie':'object', 'description':'object', 'rating':'Float64'})

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:        

    result = None    
    result_List = cinema.loc[(cinema['id']%2>0) & (cinema['description']!= 'boring')].sort_values(by='rating',ascending=False)
    return result_List

def test_basic():
    print(cinema)

    #objCls = clsSolution(cinema)
    print("Result: \n", not_boring_movies(cinema))
#-----------------------------------------------------    
if __name__ == '__main__':
    test_basic()

#---------------------------------------doc hilfer
#pandas.DataFrame.div
#4. Select rows not in list_of_values
#To select rows not in list_of_values, negate isin()/in:
#https://stackoverflow.com/questions/12096252/use-a-list-of-values-to-select-rows-from-a-pandas-dataframe
#
#DataFrame.add  -> +
#DataFrame.sub  -> -
#DataFrame.mul  -> *
#DataFrame.div  -> / float division
#DataFrame.truediv -> float division
#DataFrame.floordiv -> /integer division
#DataFrame.mod
#DataFrame.pow
#            print(5//2) деление на цело ск раз 2
#            print(5/2)  2,5
#            print(5%2)  остаток 1
