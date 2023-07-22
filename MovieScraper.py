import requests, openpyxl
from bs4 import BeautifulSoup

urls = ['https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1','https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2', 'https://www.imdb.com/search/title/?genres=animation&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_3',
'https://www.imdb.com/search/title/?genres=biography&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_4', 'https://www.imdb.com/search/title/?genres=comedy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_5', 
'https://www.imdb.com/search/title/?genres=crime&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_6', 'https://www.imdb.com/search/title/?genres=drama&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_7', 'https://www.imdb.com/search/title/?genres=family&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_8', 
'https://www.imdb.com/search/title/?genres=fantasy&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_9', 'https://www.imdb.com/search/title/?genres=film_noir&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_10', 'https://www.imdb.com/search/title/?genres=history&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_11', 
'https://www.imdb.com/search/title/?genres=music&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_13', 'https://www.imdb.com/search/title/?genres=musical&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_14', 'https://www.imdb.com/search/title/?genres=mystery&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_15', 
'https://www.imdb.com/search/title/?genres=romance&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_16', 'https://www.imdb.com/search/title/?genres=sci_fi&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_17', 'https://www.imdb.com/search/title/?genres=sport&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_18', 'https://www.imdb.com/search/title/?genres=war&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_20', 'https://www.imdb.com/search/title/?genres=western&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=f11158cc-b50b-4c4d-b0a2-40b32863395b&pf_rd_r=9A25KAASPJMH1SYD3KD9&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_21', 
'https://www.imdb.com/search/title/?genres=action&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1', 'https://www.imdb.com/search/title/?genres=adventure&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_2',
'https://www.imdb.com/search/title/?genres=family&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_9', 'https://www.imdb.com/search/title/?genres=fantasy&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_10', 'https://www.imdb.com/search/title/?genres=sci-fi&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_18', 'https://www.imdb.com/search/title/?genres=romance&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_17',
'https://www.imdb.com/search/keyword/?keywords=superhero&title_type=movie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_21', 'https://www.imdb.com/search/title/?genres=war&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_23', 'https://www.imdb.com/search/title/?genres=animation&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_3', 'https://www.imdb.com/search/title/?genres=mystery&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_16',
'https://www.imdb.com/search/title/?title_type=feature&genres=mystery&genres=Comedy&explore=genres&ref_=adv_explore_rhs', 'https://www.imdb.com/search/title/?genres=war&title_type=feature&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_23', 'https://www.imdb.com/search/keyword/?keywords=heist&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 
'https://www.imdb.com/search/keyword/?keywords=robbery&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=battle&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=neo-noir&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 
'https://www.imdb.com/search/keyword/?keywords=car-chase&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=good-versus-evil&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=cyberpunk&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie',
'https://www.imdb.com/search/keyword/?keywords=breaking-the-fourth-wall&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=plot-twist&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=tvMovie', 'https://www.imdb.com/search/keyword/?keywords=bank-heist&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie',
'https://www.imdb.com/search/keyword/?keywords=chick-flick&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=plot-twist&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=heist&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie',
'https://www.imdb.com/search/keyword/?keywords=robbery&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=based-on-book&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=action-hero&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 
'https://www.imdb.com/search/keyword/?keywords=shootout&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=zombie&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=organized-crime&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 
'https://www.imdb.com/search/keyword/?keywords=epic&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=race-against-time&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 
'https://www.imdb.com/search/keyword/?keywords=futuristic&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=opening-action-scene&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 
'https://www.imdb.com/search/keyword/?keywords=police-detective&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/keyword/?keywords=blockbuster&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=7846868c-8414-4178-8f43-9ad6b2ef0baf&pf_rd_r=32BPSYPH68WGX36WK9XE&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=moka&ref_=kw_ref_typ&sort=moviemeter,asc&mode=detail&page=1&title_type=movie', 'https://www.imdb.com/search/title/?genres=western&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_24',
'https://www.imdb.com/search/title/?genres=comedy&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_5', 'https://www.imdb.com/search/title/?genres=family&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_9', 'https://www.imdb.com/search/title/?genres=action&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_1', 
'https://www.imdb.com/search/title/?genres=adventure&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_2', 'https://www.imdb.com/search/title/?keywords=superhero&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_21',
'https://www.imdb.com/search/title/?genres=war&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_23', 'https://www.imdb.com/search/title/?genres=mystery&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_16', 
'https://www.imdb.com/search/title/?genres=fantasy&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_10', 'https://www.imdb.com/search/title/?genres=sport&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_20',
'https://www.imdb.com/search/title/?genres=sci-fi&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_18', 'https://www.imdb.com/search/title/?genres=romance&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_17', 'https://www.imdb.com/search/title/?genres=animation&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_3',
'https://www.imdb.com/search/title/?genres=crime&languages=en&sort=user_rating,desc&title_type=feature&num_votes=10000,&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=d0addcab-e8f0-45ef-9965-515319b79038&pf_rd_r=0FFYD4G39SQN21R6SYM8&pf_rd_s=right-4&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvtre_6']

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Movies"
sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Rating', 'Runtime','Genre', 'Rated'])
i = 0
for url in urls:
    i +=1
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

##excel.save('All_Movie_Genres.xls')
print("\nNumber of urls:", i)