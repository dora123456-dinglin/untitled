# import requests
# get_url='https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=5&count=10&group_id=6963999344546611745&item_id=6963999344546611745&_signature=_02B4Z6wo00901cbww7gAAIDBxFcqEnfQCo3G1McAABESzOedUXESfXJ9plbZpNZsuasLBKlQJmQZ9wNJ5l35wCTS3WzkLrLF5wxiFWtshBdvUVgGm4mXxn4wojLI5QvCnOlLW.6NRz0OWCZ7dd'
#
# result_get=requests.get(get_url)
#
# res_result=result_get.json()
# a=res_result['data'][1]['comment']['text']
# print(a)
# if a=="一起创业的要离婚不是一人一半吗":
#     print('该用例通过')
# else:
#     print("该用例失败")
#
import requests
header={'cookie':''}
a=requests.get("https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=5&count=10&group_id=6963999344546611745&item_id=6963999344546611745&_signature=_02B4Z6wo00901cbww7gAAIDBxFcqEnfQCo3G1McAABESzOedUXESfXJ9plbZpNZsuasLBKlQJmQZ9wNJ5l35wCTS3WzkLrLF5wxiFWtshBdvUVgGm4mXxn4wojLI5QvCnOlLW.6NRz0OWCZ7dd",header=,timeout=)
result=a.json()
b=result['data'][1]['comment']['text']
print(b)

