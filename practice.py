import sys,requests,bs4,webbrowser
print('Hello my world')

# #open new tabs for eah google search results on top
#
# #1. get the search text from command line arguments
# res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()
#
# #an html page is downloaded we have to search for top links
# soup = bs4.BeautifulSoup(res.text,'html.parser')
# links = soup.select('.package-snippet')
#
# #open a browser for each result
# numOpen = min(5,links)
# for i in range(numOpen):
#     openTab = 'https://pypi.org' + links[i].get('href')
#     webbrowser.open(openTab)

response = requests.get('https://www.google.com/search?' + 'hello there')
response.raise_for_status()

bsoup = bs4.BeautifulSoup(response.text,'html.parser')
mlinks = bsoup.select('a')
for x in mlinks:
    print(x)