import pandas as pd
from bs4 import BeautifulSoup
import time

from selenium import webdriver



def get_html(page: int):
    """This method uses selenium to call the web page, and then uses 
    beautifulsoup to extract the statistics table from the html of the page.
    Args:
    page (int): The page number for which we want to extract data.
    """
    print('Opening Chrome.......')
    path_to_exec = 'D:/KTM project/Motogp/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path_to_exec)
    baseurl = 'https://www.motogp.com/en/statistics/gp-race-winners/All-seasons/'
    driver.get(f'{baseurl}All-circuits/All-classes/All-countries/?page={page}')
    time.sleep(10)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
   
    table = soup.find_all('tr', class_="table_row")
    return table


def extract_rider_info(table):
    """This function extract each rider's information from the table.
    Args:
    table: The html reult of a table_row extracted from the source page.
    """
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
            const_class = "table_item constructor qa_table_constructor d-none d-sm-table-cell"
            constructor=t.find("td",{"class":const_class}).text.replace('\n',"")
        except:
            constructor = None
        try:
            ride_class = "table_item category qa_table_category d-table-cell text-right pr-8"
            ride_class=t.find("td",{"class":ride_class}).text.replace('\n',"")
        except:
            ride_class = None
        rider_name = {
            "name": name, "season": season, "country": country, 
            "circuit": circuit, "constructor": constructor, 
            "ride_class": ride_class
            }
        
        reviews.append(rider_name)
    return reviews


def convert_to_csv(last_page: int):
    """This function calls the other previous functions from page 1 
    to the last page, and dump the reult into a csv file
    Args:
    last_page: the last page you want to extract data up to.
    """
    list_of_table = []
    for i in range(1, last_page):
        print("Collecting data for page ", i)
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
    convert_to_csv(last_page=169)