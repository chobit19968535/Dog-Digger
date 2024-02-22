from enum import Enum
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import math as pmath

class dog(object):
    def __init__(self):
        self.ticker = "2330"
        self.web = web()
        self.web.session_start()

    def query(self, mode) -> Enum:
        if(mode == query_modes.income):
            url = self.web.query_url + str(self.ticker) + mode.value
            #print(url)
            self.web.driver.get(url)
            utility.delay();
            html = self.web.driver.page_source
            soup = BeautifulSoup(html)

            years = list()
            incomes = list()
            rates = list()

            dataTable = soup.find("li",attrs={"id":"dataTable"})
            rows = dataTable.findAll("tr")

            #year-season
            for cell in rows[0].findAll("th"):
                years.append(cell.text)

            #incomes
            for cell in rows[1].findAll("td"):
                incomes.append(int(cell.text.replace(',','')))

            #rates
            for cell in rows[2].findAll("td"):
                rates.append(float(cell.text.replace(',','')))

            data = list()
            data.append(years)
            data.append(incomes)
            data.append(rates)
            df = pd.DataFrame(data=data)

            return df
        if(mode == query_modes.eps):
            url = self.web.query_url + str(self.ticker) + mode.value
            #print(url)
            self.web.driver.get(url)
            utility.delay()
            html = self.web.driver.page_source
            soup = BeautifulSoup(html)

            year_season = list()
            epses = list()

            dataTable = soup.find("li",attrs={"id":"dataTable"})

            rows = dataTable.findAll("tr")

            #year-season
            for cell in rows[0].findAll("th"):
                year_season.append(cell.text)

            #eps
            for cell in rows[1].findAll("td"):
                epses.append(float(cell.text.replace(',','')))

            data = list()
            data.append(year_season)
            data.append(epses)
            df = pd.DataFrame(data=data)
            return df
        pass
    pass

class web():
    def __init__(self):
        self.login_url = "https://statementdog.com/users/sign_in"
        self.query_url = "https://statementdog.com/analysis/"
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome()

    def session_start(self):
        self.driver.get(self.login_url)
        pass

    def login(self, args):
        Input_email = self.driver.find_element(By.ID, "user_email")
        Input_password = self.driver.find_element(By.ID, "user_password")
        Login_button = self.driver.find_element(By.CLASS_NAME, "submit-btn")

        Input_email.send_keys(args[0])
        Input_password.send_keys(args[1])
        Login_button.click()
        pass

class query_modes(Enum):
    income = '/monthly-revenue'
    eps = '/eps'

class math():
    def quarterlize(dataframe) -> pd.Series:
        quarterlized_list = list()
        quarter_cnts = pmath.floor(len(dataframe)/3)
        quarter_now = list()
        quarter_size = 3

        for Q in range(quarter_cnts):

            sum =0
            sum+= (dataframe[Q*quarter_size + 0])
            sum+= (dataframe[Q*quarter_size + 1])
            sum+= (dataframe[Q*quarter_size + 2])
            quarterlized_list.append(sum)

        for q in range(quarter_cnts*quarter_size, len(dataframe)):
            quarter_now.append(dataframe[q])


        quarterlized_df = pd.DataFrame(quarterlized_list)
        quarter_now_df = pd.DataFrame(quarter_now)
        dst  = (quarterlized_df, quarter_now_df)
        return(dst)

class utility():
    def delay(delay_second = 1):
        sleep(delay_second)
