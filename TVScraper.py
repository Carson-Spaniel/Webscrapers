import requests, openpyxl
from bs4 import BeautifulSoup

urls = ['https://www.imdb.com/search/title/?genres=action&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=adventure&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=animation&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter',
'https://www.imdb.com/search/title/?genres=biography&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=comedy&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=crime&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter',
'https://www.imdb.com/search/title/?genres=documentary&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=drama&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=family&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter',
'https://www.imdb.com/search/title/?genres=fantasy&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=game_show&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=history&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 
'https://www.imdb.com/search/title/?genres=mystery&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=romance&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=sci_fi&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 
'https://www.imdb.com/search/title/?genres=war&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 'https://www.imdb.com/search/title/?genres=western&title_type=tv_series,mini_series&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7942b3cb-6c49-4bc0-84e8-f789cc3e3e84&pf_rd_r=2QTNAJEQ34H40WHVXZ54&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=tvmeter', 
'https://www.imdb.com/search/keyword/?keywords=robbery&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=superhero&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=husband-wife-relationship&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 
'https://www.imdb.com/search/keyword/?keywords=organized-crime&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=zombie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=based-on-book&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 
'https://www.imdb.com/search/keyword/?keywords=anti-hero&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=mother-daughter-relationship&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries', 'https://www.imdb.com/search/keyword/?keywords=action-hero&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=DVT697VT4M01QBVCXNRY&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvSeries' ]

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
    movies = soup.find('div', class_ = "lister-list").find_all('div', class_ = "lister-item-content")

    for movie in movies:

        rank = movie.find('h3', class_ = "lister-item-header").span.get_text(strip=True).split('.')[0]
        name = movie.find('h3', class_ = "lister-item-header").a.text
        year = movie.find('h3', class_ = "lister-item-header")
        year = year.find('span', class_ = "lister-item-year text-muted unbold").text.strip('()')

        runtime = movie.find('p', class_ = "text-muted")
        runtime = runtime.find('span', class_ = "runtime")
        if runtime is not None:
            runtime = runtime.text
            runtime = runtime[:-4]
        else:
            runtime = 'N/A'

        genre = movie.find('p', class_ = "text-muted")
        genre = genre.find('span', class_ = "genre").text

        rating = movie.find('div', class_ = "ratings-bar")
        if rating is not None:
            rating = rating.strong
            if rating is not None:
                rating = rating.text
            else:
                rating = 'N/A'
        else:
            rating = 'N/A'

        rate = movie.find('p', class_ = "text-muted")
        rate = rate.find('span', class_ = "certificate")
        if rate is not None:
            rate = rate.text
        else:
            rate = 'N/A'

        sheet.append([rank, name, year, rating, runtime, genre, rate])

        print(rank, name, year, rating, runtime, genre, rate)

excel.save('All_TV.xls')
print("\nNumber of urls:", i)