from cgitb import text
from enum import Enum
from optparse import Option
from pickle import NONE
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import math as pmath
from analyzer import pca


class dog(object):
    def __init__(self):
        self.sharp_dir = None
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
            soup = BeautifulSoup(html, features="html.parser")
            if(soup == None):
                while (soup == None):
                    soup = BeautifulSoup(html)
                    pass
            
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
                if(cell.text == '無'): 
                    incomes.append(0)
                    continue
                incomes.append(int(cell.text.replace(',','')))

            #rates
            for cell in rows[2].findAll("td"):
                if(cell.text == '無' or cell.text == '前期為零'):
                    rates.append(0)
                    continue
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
                if(cell.text == '無' or cell.text =='前期為零'):
                    epses.append(0)
                    continue
                epses.append(float(cell.text.replace(',','')))

            data = list()
            data_header = list()
            data_header = ['年/季', 'EPS']

            data.append(year_season)
            data.append(epses)
            df = pd.DataFrame(data=data)
            df = df.T
            df.columns = data_header
            df = df.T
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

            #主業利益 = 營收 - 銷貨成本 - 營業費用
            quarter_net_income = list()

            #稅後淨利 = 營收 - 銷貨成本 - 營業費用
            quarter_profit = list()

            #業外損益 = 稅後淨利 - 主業損益
            quarter_non_main_income = list()

            #研發費用與營業費用的比例
            quarter_research_payment_ratio = list()

            dataTable = soup.find("li",attrs={"id":"dataTable"})
            rows = dataTable.findAll("tr")

            for cell in rows[1].findAll("td"):
                if(cell.text == '無'):
                    quarter_incomes.append(0)
                    continue
                quarter_incomes.append(float(cell.text.replace(',','')))

            for cell in rows[2].findAll("td"):
                if(cell.text == '無'):
                    quarter_gross.append(0)
                    continue
                quarter_gross.append(float(cell.text.replace(',','')))

            for cell in rows[3].findAll("td"):
                if(cell.text == '無'):
                    quarter_sales_cost.append(0)
                    continue
                quarter_sales_cost.append(-float(cell.text.replace(',','')))

            for cell in rows[4].findAll("td"):
                if(cell.text == '無'):
                    quarter_management_cost.append(0)
                    continue
                quarter_management_cost.append(-float(cell.text.replace(',','')))

            for cell in rows[5].findAll("td"):
                if(cell.text == '無'):
                    quarter_research_funds.append(0)
                    continue
                quarter_research_funds.append(-float(cell.text.replace(',','')))

            for cell in rows[6].findAll("td"):
                if(cell.text == '無'):
                    quarter_payment.append(0)
                    continue
                quarter_payment.append(-float(cell.text.replace(',','')))

            for cell in rows[7].findAll("td"):
                if(cell.text == '無'):
                    quarter_net_income.append(0)
                    continue
                quarter_net_income.append(float(cell.text.replace(',','')))

            for cell in rows[9].findAll("td"):
                if(cell.text == '無'):
                    quarter_profit.append(0)
                    continue
                quarter_profit.append(float(cell.text.replace(',','')))

            for i in range(len(quarter_profit)):
                quarter_non_main_income.append( quarter_profit[i] - quarter_net_income[i])


            data = list()
            data_header = list()

            data_header =['營收', '毛利', '銷售費用', '管理費用', '研發費用', '營業總支出', '主業損益', '稅後淨利', '業外損益']

            data.append(quarter_incomes)
            data.append(quarter_gross)
            data.append(quarter_sales_cost)
            data.append(quarter_management_cost)
            data.append(quarter_research_funds)
            data.append(quarter_payment)
            data.append(quarter_net_income)
            data.append(quarter_profit)
            data.append(quarter_non_main_income)

            df = pd.DataFrame(data=data)
            df = df.T
            df.columns = data_header
            df = df.T



            return df
        pass

    def analyze(self, statement) -> pd.DataFrame:
        optimizer = pca(statement, self.ticker)
        optimizer.sharp_dir = self.sharp_dir
        optimizer.ppmcc()
        #optimizer.run()


        pass

    def line_chart(self, data) -> pd.Series:
        import matplotlib.pyplot as plt
        if(data.name == '營業總支出'):
            data = -data
        plt.figure(figsize=(10,5))
        plt.plot(data.index, data.values)
        plt.title(data.name,{'fontsize':40}, loc='center', pad=6)  # 設定 title 文字樣式
        plt.rcParams['axes.unicode_minus'] = False
        #plt.xlabel('x-axis',{'fontsize':20})    # 設定 x 軸標籤
        #plt.ylabel('y-axis',{'fontsize':20})  # 設定 y 軸標籤
        plt.yticks(fontsize=25)  # 設定 y 軸刻度
        plt.xticks(fontsize=25)  # 設定 y 軸刻度

        plt.savefig(self.ticker + "_" +  data.name + '.png')
        pass
class web():
    def __init__(self):
        self.login_url = "https://statementdog.com/users/sign_in"
        self.query_url = "https://statementdog.com/analysis/"
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options = self.options)
        
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
    def delay(delay_second = 2):
        sleep(delay_second)
