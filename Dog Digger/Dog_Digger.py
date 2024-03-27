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


def yfinance():
    import datetime
    from dateutil.relativedelta import relativedelta
    import yfinance as yf
    date = datetime.datetime.now().date()

    end_date = date
    start_date = date + relativedelta(months= -63)

    msft = yf.Ticker("6533.TW")
    # get all stock info
    #msft.info

    # get historical market data
    hist = msft.history(start=start_date, end=end_date, interval="1mo")
    hist.to_excel("6533.TW.xlsx", index=None)

yfinance()
pass

def test():
    user = client()
    dog = dog()

    user.account = "User-email"
    user.password = "User-password"

    #user.account = "chobit19968535@gmail.com"
    #user.password = "zapdAj-pepbe4-bykzuf"

    dog.ticker = "6533"

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

    pass


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

def set_sharp_work_dir(path) -> string:
    dog.sharp_dir = path
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

    df_pbs = dog.query(query_modes.pb)
    digger.utility.delay()

    df_pbs.to_excel('data_' + dog.ticker + '_PBs.xlsx', index = None)
    dog.river_chart()

    df_report = pd.concat([df_report, df_pbs], axis = 1)
    df_report.to_excel('Report_' + dog.ticker + '.xlsx', index = None);

    # 右邊圖表
    dog.line_chart(df_report['營收']);
    dog.line_chart(df_report['毛率']);
    dog.line_chart(df_report['主業損益']);
    dog.line_chart(df_report['業外損益']);

    # 左邊圖表
    dog.line_chart(df_report['EPS']);
    dog.line_chart(df_report['營業總支出']);
    dog.line_chart(df_report['研支比']);
    dog.line_chart(df_report['研營比']);
    pass

def close():
    exit()

#user.account = "chobit19968535@gmail.com"
#dog.ticker = "6533"

#start()
#dig()