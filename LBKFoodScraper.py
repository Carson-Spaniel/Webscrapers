import requests, openpyxl
from bs4 import BeautifulSoup

urls = ['https://www.tripadvisor.com/Restaurants-g56208-Lubbock_Texas.html']

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
    foods = soup.find('div', class_ = "YtrWs").find_all('a', class_ = "Lwqic Cj b")
    print(foods)


##excel.save('All_TV.xls')
print("\nNumber of urls:", i)