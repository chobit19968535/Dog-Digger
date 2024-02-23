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
        if(mode == query_modes.income_statement):
            url = self.web.query_url + str(self.ticker) + mode.value
            #print(url)
            self.web.driver.get(url)
            utility.delay()
            html = self.web.driver.page_source
            soup = BeautifulSoup(html)
            
            #季營收_每三個月的營收總和
            quarter_incomes = list()

            #季毛利 = 季營收 - 季銷貨成本
            #銷貨成本是銷售商品或提供勞務的直接成本， 但不包含租金、水電、廣告費、研發費...等營運產生的間接費用。
            quarter_gross = list()

            #銷售費用_銷售產品過程中發生的各項費用，例如：包裝費、運輸費、展覽費、廣告費...等
            quarter_sales_cost = list()

            #管理費用_公司為了內部組織上的管理營運產生的各項費用，例如：管理人員工資和福利費
            quarter_management_cost = list()

            #研發費用
            quarter_research_funds = list()

            #營業費用 = 銷售費用 + 管理費用 + 研發費用 + 其他 
            quarter_payment = list()

            #本業利益 = 營收 - 銷貨成本 - 營業費用
            quarter_net_income = list()

            #稅後淨利 = 營收 - 銷貨成本 - 營業費用
            quarter_profit = list()

            dataTable = soup.find("li",attrs={"id":"dataTable"})
            rows = dataTable.findAll("tr")

            for cell in rows[1].findAll("td"):
                quarter_incomes.append(float(cell.text.replace(',','')))

            for cell in rows[2].findAll("td"):
                quarter_gross.append(float(cell.text.replace(',','')))

            for cell in rows[3].findAll("td"):
                quarter_sales_cost.append(-float(cell.text.replace(',','')))

            for cell in rows[4].findAll("td"):
                quarter_management_cost.append(-float(cell.text.replace(',','')))

            for cell in rows[5].findAll("td"):
                quarter_research_funds.append(-float(cell.text.replace(',','')))

            for cell in rows[6].findAll("td"):
                quarter_payment.append(-float(cell.text.replace(',','')))

            for cell in rows[7].findAll("td"):
                quarter_net_income.append(float(cell.text.replace(',','')))

            for cell in rows[9].findAll("td"):
                quarter_profit.append(float(cell.text.replace(',','')))

            data = list()
            data.append(quarter_incomes)
            data.append(quarter_gross)
            data.append(quarter_sales_cost)
            data.append(quarter_management_cost)
            data.append(quarter_research_funds)
            data.append(quarter_payment)
            data.append(quarter_net_income)
            data.append(quarter_profit)

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
    income_statement = '/income-statement'

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
