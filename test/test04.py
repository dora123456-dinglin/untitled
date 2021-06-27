# import requests
# def get_cookie():
#     url='http://106.12.48.30:8081/login'
#     data_post={'username':'sang','password':'123'}
#     result=requests.post(url,data=data_post)
#     jsession=requests.utils.dict_from_cookiejar(result.cookies)
#     header_common={'Cookie':"JSESSIONID="+jsession['JSESSIONID']}
#     return header_common
# print(get_cookie()
a=[1,3,5,45,34,56]
print(a)

c=sorted(a)
print(c)
