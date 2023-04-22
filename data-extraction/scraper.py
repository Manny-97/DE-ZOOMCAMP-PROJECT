import pandas as pd
from bs4 import BeautifulSoup
import time

from selenium import webdriver



def get_html(page: int):
    """ """
    print('Opening Chrome.......')
    driver = webdriver.Chrome(executable_path='D:/KTM project/Motogp/chromedriver_win32/chromedriver.exe')
    driver.get(f'https://www.motogp.com/en/statistics/gp-race-winners/All-seasons/All-circuits/All-classes/All-countries/?page={page}')
    time.sleep(10)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
   
    table = soup.find_all('tr', class_="table_row")
    return table


def extract_rider_info(table):
    """ """
    reviews = []
    for t in table:
        p=1
        try:
            name=t.find("span",{"class":"surname qa_table_rider_surname"}).text.replace('\n',"")
            
        except:
            name = None
        try:
            season=t.find("span",{"class":"font-weight-bold"}).text.replace('\n',"")
        except:
            season = None
        try:
            country=t.find("span",{"class":"country"}).text.replace('\n',"")
        except:
            country = None
        try:
            circuit=t.find("span",{"class":"pl-1 d-block d-sm-none"}).text.replace('\n',"")
        except:
            circuit = None
        try:
            constructor=t.find("td",{"class":"table_item constructor qa_table_constructor d-none d-sm-table-cell"}).text.replace('\n',"")
        except:
            constructor = None
        try:
            ride_class=t.find("td",{"class":"table_item category qa_table_category d-table-cell text-right pr-8"}).text.replace('\n',"")
        except:
            ride_class = None
        rider_name = {"name": name, "season": season, "country": country, "circuit": circuit, "constructor": constructor, "ride_class": ride_class}
        
        reviews.append(rider_name)
    return reviews


def convert_to_parquet(last_page: int):
    """ """
    list_of_table = []
    for i in range(1, last_page):
        table = get_html(i)
        list_of_table.append(table)
    list_of_rider_info = []
    for t in list_of_table:
        ref = extract_rider_info(t)
        list_of_rider_info.append(ref)

    full_data = [item for rider_info in list_of_rider_info for item in rider_info]

    df = pd.DataFrame(full_data)


    df.to_csv("data/raw/motogp.csv", index=False)
    print(df.tail())

if __name__ == "__main__":
    convert_to_parquet(last_page=169)