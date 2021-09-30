import bs4,requests
print('Hello my World')

#using beautifulSoup module for parsing html

# response = requests.get('https://nostarch.com')
# response.raise_for_status()
# parseObj = bs4.BeautifulSoup(response.text,'html.parser')     #string can keep file obj too
# print(type(parseObj))

fileObj = open('exampleHtml.html')
parseFileObj = bs4.BeautifulSoup(fileObj.read(),'html.parser')
# print(parseFileObj)

#Select method to select particular html tag
#select method returns a list of tags objects
# listTags = parseFileObj.select('#author')
# print(type(listTags))
# print(len(listTags))
# print(type(listTags[0]))
# print(str(listTags[0]))
# print(listTags[0].getText())
# print(listTags[0].attrs)

pLists = parseFileObj.select('p')
print(f'There are {len(pLists)} paragraphs.')
for x in pLists:
 print(x)
 print(str(x))
 print(x.getText())
 print(x.attrs)
 print()