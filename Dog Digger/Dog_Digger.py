from login import client
from digger import dog
from digger import query_modes

user = client()
user.account = "chobit19968535@gmail.com"
user.password = "zapdAj-pepbe4-bykzuf"

dog = dog()
dog.web.login((user.account, user.password))
user.clear()

df_income = dog.query(query_modes.income)

print()