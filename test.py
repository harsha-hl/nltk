from bs4 import BeautifulSoup
with open('data.xml', 'r') as f:
        data = f.read()
bs = BeautifulSoup(data, "xml")

x=bs.find("verb",{'name':'pour'})
print(x.get('deg'))