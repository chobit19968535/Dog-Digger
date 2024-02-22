from time import sleep
from login import client
from digger import dog
import digger
from digger import query_modes

user = client()
user.account = "chobit19968535@gmail.com"
user.password = "zapdAj-pepbe4-bykzuf"

dog = dog()

dog.ticker = "6533"
dog.web.login((user.account, user.password))
user.clear()

df_income = dog.query(query_modes.income)
digger.utility.delay()
df_epses = dog.query(query_modes.eps)
digger.utility.delay()

res = digger.math.quarterlize(df_income.iloc[1])

print()