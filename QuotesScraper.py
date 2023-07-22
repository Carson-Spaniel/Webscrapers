import requests, openpyxl
from bs4 import BeautifulSoup

urls = ['http://quotes.toscrape.com/scroll']

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated TV Shows"
sheet.append(['TV Rank', 'TV Name', 'Year of Release', 'IMDB Rating', 'Runtime','Genre', 'Rated'])
i = 0
for url in urls:
    i +=1
    print(url)
    source = requests.get(url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")
    quotes = soup.find('div', class_ = "quotes")

    for quoted in quotes:

        quote = quoted.find('span', class_ = "text")
        name = quoted.find('small', class_ = "author")

        sheet.append([quote, name])

        print(quotes, name)

##excel.save('All_TV.xls')
print("\nNumber of urls:", i)