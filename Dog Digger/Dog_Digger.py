from ast import Index
from email import header
from operator import index
from pickle import FALSE
import string
from time import sleep
from login import client
from digger import dog
import digger
from digger import query_modes
import pandas as pd

user = client()
dog = dog()


def test():
    user = client()
    dog = dog()

    user.account = "User-email"
    user.password = "User-password"

    #user.account = "chobit19968535@gmail.com"
    #user.password = "zapdAj-pepbe4-bykzuf"

    dog.ticker = "3189"

    df_income = dog.query(query_modes.income)
    digger.utility.delay()
    df_epses = dog.query(query_modes.eps)
    digger.utility.delay()

    df_income_statement = dog.query(query_modes.income_statement)
    digger.utility.delay()

    df_report = pd.concat([df_income_statement.transpose(), df_epses.iloc[1]], axis = 1)
    dog.analyze(df_report)

    column_name = ['研營比']
    research_income_ratio =  pd.DataFrame(-df_report['研發費用']/df_report['營收']*100, columns=column_name)
    df_report = pd.concat([df_report, research_income_ratio], axis = 1)

    column_name = ['研支比']
    research_payment_ratio =  pd.DataFrame(df_report['研發費用']/df_report['營業總支出']*100, columns=column_name)
    df_report = pd.concat([df_report, research_payment_ratio], axis = 1)

    column_name = ['毛率']
    gross_margin =  pd.DataFrame(df_report['毛利']/df_report['營收']*100, columns=column_name)
    df_report = pd.concat([df_report, gross_margin], axis = 1)

    df_report.to_excel('Report_' + dog.ticker + '.xlsx', index = None);

def start():
    dog.web.login((user.account, user.password))
    user.clear()
    return

def set_accountName(userName)-> string:
    user.account = userName
    return

def set_password(password)-> string:
    user.password = password
    return

def set_ticker(ticker_number)-> string:
    dog.ticker = ticker_number
    print(dog.ticker)
    return

def dig():
    df_income = dog.query(query_modes.income)
    digger.utility.delay()
    df_epses = dog.query(query_modes.eps)
    digger.utility.delay()

    df_income_statement = dog.query(query_modes.income_statement)
    digger.utility.delay()

    df_report = pd.concat([df_income_statement.transpose(), df_epses.iloc[1]], axis = 1)
    dog.analyze(df_report)

    column_name = ['研營比']
    research_income_ratio =  pd.DataFrame(-df_report['研發費用']/df_report['營收']*100, columns=column_name)
    df_report = pd.concat([df_report, research_income_ratio], axis = 1)

    column_name = ['研支比']
    research_payment_ratio =  pd.DataFrame(df_report['研發費用']/df_report['營業總支出']*100, columns=column_name)
    df_report = pd.concat([df_report, research_payment_ratio], axis = 1)

    column_name = ['毛率']
    gross_margin =  pd.DataFrame(df_report['毛利']/df_report['營收']*100, columns=column_name)
    df_report = pd.concat([df_report, gross_margin], axis = 1)

    df_report.to_excel('Report_' + dog.ticker + '.xlsx', index = None);