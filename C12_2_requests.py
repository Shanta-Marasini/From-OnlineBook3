import requests
print("hello my World")

#To download files from web
#this downloads whats in the url
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# res = requests.get("https://s.pinimg.com/webapp-new/webapp/js/runtime-18167f10a0a5ba5ba00f.js")
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)                    #checking for error
print(res.status_code==requests.codes.ok)
print(len(res.text))
print(type(res))
print(res.text)
#next way for checking for errors

try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem:' + str(exc))

#how to write it in your computer
# fileObj = open('romeoJuliet.txt','wb')
# for chunk in res.iter_content(100000):      #chunk size of 100000
#     fileObj.write(chunk)
