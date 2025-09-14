"""
        Description: https://leetcode.com/problems/duplicate-emails/description/?lang=pythondata
        Author:     RuslanLisovenko@gmail.com
        Date:       2011-2023 -> 29.11.2023
"""

import pandas as pd
import numpy as np

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com'],[4, 'R@gmail.com'],[5, 'r@gmail.com'],[7, 'R@gmail.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:        
    
    #result_List =  None       

    person = person.groupby(by=['email'], group_keys=False).nunique()    
    person = person.query('id > 1') 
    #print(person)
    person = list(person.reset_index().filter(items=['email']).values)
    #print(person)
    person =  pd.DataFrame(person, columns=['Email']).astype({'Email':'object'})
    #print(person)
    return person

def test_basic():
    #objCls = clsSolution(person)
    print("Result: \n", duplicate_emails(person))

#-----------------------------------------------------    
if __name__ == '__main__':
    test_basic()