from ast import Index
from email import header
from operator import index
from pickle import FALSE
from time import sleep
from login import client
from digger import dog
import digger
from digger import query_modes
import pandas as pd

user = client()
user.account = "chobit19968535@gmail.com"
user.password = "zapdAj-pepbe4-bykzuf"

dog = dog()

dog.ticker = "3189"
dog.web.login((user.account, user.password))
user.clear()

df_income = dog.query(query_modes.income)
digger.utility.delay()
df_epses = dog.query(query_modes.eps)
digger.utility.delay()

df_income_statement = dog.query(query_modes.income_statement)
digger.utility.delay()

df_report = pd.concat([df_income_statement.transpose(), df_epses.iloc[1]], axis = 1)
df_report.to_excel('Report_' + dog.ticker + '.xlsx', index = None);

#res = digger.math.quarterlize(df_income.iloc[1])



print()