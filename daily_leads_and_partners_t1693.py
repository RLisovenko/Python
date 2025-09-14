"""
    Description: https://leetcode.com/problems/daily-leads-and-partners/?lang=pythondata
    Author:      RuslanLisovenko@gmail.com
    Date:        22.11.2023
    groupby.mean - среднее значение  типа еще
    df.groupby(by=["b"]).sum()
    df.groupby("Animal", group_keys=False).apply(lambda x: x)
"""

import pandas as pd
#import rl_tools as rl

#pd.options.display.expand_frame_repr = False

data = [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], ['2020-12-7', 'honda', 2, 1]]
daily_sales = pd.DataFrame(data, columns=['date_id', 'make_name', 'lead_id', 'partner_id']).astype({'date_id':'datetime64[ns]', 'make_name':'object', 'lead_id':'Int64', 'partner_id':'Int64'})

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        daily_sales (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """

    result_List = None      
    result_List = daily_sales.groupby(by=['date_id','make_name'], group_keys=False).nunique()
    result_List = result_List.sort_values(by=['make_name'],ascending=True)    
    result_List =result_List.rename(columns={'lead_id':'unique_leads','partner_id':'unique_partners'})  #Можно было переименовать сразу при создании нового Датафрейма ниже
    result_List =result_List.filter(items=['date_id','make_name','unique_leads','unique_partners'])     #ВЫБИРАЮ НУЖНЫЕ КОЛОНКИ
    #print(result_List)
    data_neu = result_List.reset_index() #konvert Series в DataFrame  after group by  
    #print(data_neu)
    daily_sales_neu = pd.DataFrame(data_neu, columns=['date_id', 'make_name', 'unique_leads', 'unique_partners']) \
                                    .astype({'date_id':'datetime64[ns]', 'make_name':'object', 'unique_leads':'Int64', 'unique_partners':'Int64'})

    return daily_sales_neu

def test_basic():
    #DatenInitialisierung
    print(daily_sales)

    #objCls = clsSolution(daily_sales)
    print("Result: \n", daily_leads_and_partners(daily_sales))

if __name__ == '__main__':
    test_basic()

