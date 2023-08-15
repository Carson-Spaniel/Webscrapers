import requests
from bs4 import BeautifulSoup
from collections import Counter
from tqdm import tqdm
import string
import nltk
from nltk.corpus import stopwords
from common import all_skills as common_single_words,filtered_skills as filtered
import time

# Download NLTK stopwords if not already downloaded
# nltk.download('stopwords')

def get_qualifications(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(['script', 'style']):
            script.extract()

        qualifications_section = soup.find("div", class_="description__text")

        if qualifications_section:
            text = qualifications_section.get_text()
            words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

            # Remove stopwords
            stop_words = set(stopwords.words('english'))
            words = [word for word in words if word not in stop_words]

            return words
        else:
            print("Qualifications & Requirements section not found on the page.")
            return []

    else:
        print(f"Failed to fetch the website content for URL: {url}")
        return []

def count_word_frequencies(words):
    word_freq = Counter(words)
    return word_freq

if __name__ == "__main__":
    website_urls = [
        "https://www.linkedin.com/jobs/view/3637861032/?eBP=CwEAAAGJ9eK4r-naSkI1dRk6-LB26cA5GccfpiAHRWY0Pyq8tJM0sj4HswfpFYGDs7b7xtVSx1QspjUhJZch0M7PrvfId8SD_bh5r9G0TYcVXd99u6sU3O8RelEDc9_AffKal7f19AalVI0UZWzMeHa1LTuAvPPxqIoX6bYNVd-L43PAHTnTPS-tMAETeRiJyZbe0GuWOnOto_0uuIHXTO4UaZvaGkpifpBlmlKVyUNBoJ240zKQSVW8H-yk-9e3ku43kQctHMiKqQQlPaE7dkhq1mYy-azgsGeOBEKUigqq4EhKdpktYVRoiMpTGhAujKB3w1gz-HGNgjkcwDkGG-ZZfkBHVuXdPl8EMx_b0BBiVpfx-JDZkZ5alfowYcdRsMBT6JF6&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=rKjJ%2BZe97YJO%2F7fbJWTAGA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=rKjJ%2BZe97YJO%2F7fbJWTAGA%3D%3D",
        "https://www.linkedin.com/jobs/view/3689483932/?eBP=CwEAAAGJ9eK4rwWXsynN6WaEJB2n-3O8jM5PZo6hZfl8XYAy7C2fOxj2axQxr9V3q_TsCC5QGmq4kMXgmSXzmNiws4Kk7UlMVDnoaJRznm_7nPELM7zo2BR4-exiJXkeRuUltYdpU1pcaR_O5j8olsgajI5lUwewAEI7v3fUgMikLD653XrRe2FlzDNof9SqU7vY1GoTqEfpA32BDyLPLz-d1CIAEBRj44UFBLRZbKoF-YpqUKpBjksmXYuyihH6m_NxAM0DiZ6b4s26PqcVzz_x37maXgEhoJLjhw45qipwkWTH_CrlZUdOadICdAO4j-pzfVVkkehGkPuO9qkJrI3Vk_dyVkUbi4LvCXuYuubIeOEOPpGrKYg_M1Pvb37ABq45nL5PMjs&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=iwaU4r7Q6p%2BKV85QgCK0vg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=iwaU4r7Q6p%2BKV85QgCK0vg%3D%3D",
        "https://www.linkedin.com/jobs/view/3674369797/?eBP=CwEAAAGJ9eK4sHsHw3OZzIen3M4PatP8jnysjYXHN6FdJkE2rFDO6nNPQv4rm8Tjhr_Zkiqq6zwU3qzzI1VQLeIbPdthukKC1bafUxOZhiZqmz6V3cqeq8efRENNlr7LWLoE5WTMSfjRpYWZb6PariZU2-eMASVKdCc1HNxynu47zPtJ0htYFWMsldc_d3L8tmTMJLhbqO0Mj9DMC4dE-HzVu-1i_EI24AVEF39xBvisR7RSjTF-sj9xrbMahGMDS2y6CLYLknfw977pC1Uw9R0Y42zkBpSlNmyFGBEmxKwa8DXNv6onvLQUcvRKjtiUfVKSNGD8Ii7DAAeRTs93UAUsSt1ZUdCLwdo0KcSd83ElA9Sf9git_aOcJ6skO7LvxERgHcyQ&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=PXN0jlxcAq%2BkTH30ZbO5bg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=PXN0jlxcAq%2BkTH30ZbO5bg%3D%3D",
        "https://www.linkedin.com/jobs/view/3669642784/?eBP=JOB_SEARCH_ORGANIC&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=ReKs124A6TJeq0nVXWtM5Q%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=ReKs124A6TJeq0nVXWtM5Q%3D%3D",
        "https://www.linkedin.com/jobs/view/3635070471/?eBP=CwEAAAGJ9eK4sDpIRnOeRl0SmUwxaFYVuRbe7z1Nerwok-93MhnxWJk17iiP4Xs-TkhnMc21UNG-20QtFzUw5VpfdPO3cIgWl5jxIWECckxcQ90huViU2RUagO1M07RDfFPboR265HCdtW7IThIZzBk80rldbMvNHg0WPkxrgdn_FRRANHyyHYtrb0mWoB1EyoMpyvan28S2aORVimUGhabSd4y0f3rbSDaQQJm8V-ykSIslytqM0G2o_gSrcP0Qia251t9UgSlYtqWxTcrzE5XDw8G8aF5MogWn6CFoh5nphDkOwolrTStgHzi8IvRCBW4C5wi0ZsIuq5IhWY6rBpz6wg8YGw9lJjOFKodNPRhF1IOoNoDCie2MRYHemzZtAWxXU3vM&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=fXt%2FGmwbGHIaAURMZPWsbg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=fXt%2FGmwbGHIaAURMZPWsbg%3D%3D",
        "https://www.linkedin.com/jobs/view/3662993468/?eBP=CwEAAAGJ9eK4sHKGkWK-Yv8YY4SeOqed5DIzQP3Qqyy7voDgnA45h_BxTTC-NnPFXUKYoxl52J7G-SlqsKCz2EWbpSpRm4rdcCId9iv22swjLrHUimuotwce179uFLw8Z5Ktw39pFXRRk_Kv2XlJbd96xd1KjArVSn6-CU3YuMlG7yA7IzHFQqz5PZhvktUGMEFY69yb_aApngxMTMJ2lhV1clxiO7m75LeCw0o7aFngG1elu6HInCqj1Dlxx9x33elTI6t1Wfo0_GKfMjaGzI6ms_kSQYNr8G_-Ix-CuCeDymoo3hDPv7tDfz6yJklevEneeLsE9jhtn7yofyEzXJWZQkA0ur8dJVXz3bd3IhAiOn0hQBdKqu13CtARr37rIGLShOSjHIg&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=7S%2BjP%2FR%2BHQyWHyPjbNMrLQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=7S%2BjP%2FR%2BHQyWHyPjbNMrLQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3681225673/?eBP=JOB_SEARCH_ORGANIC&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=Xuczrzt2mcXj0jYQDvdA%2Bw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=Xuczrzt2mcXj0jYQDvdA%2Bw%3D%3D",
        "https://www.linkedin.com/jobs/view/3685623922/?eBP=CwEAAAGJ9eK4sFIBv36fYUX0uODNmo1Bv2RVZ4UEsgN6xpbf-k_3OxkSy__iSCN6cPlQxBHLEL0B9r4lMdagu3vx2G07cCT_AS5c-9ClEJhv5tGhGYWBCa-c4AubuA-6uRjhH_sCB_zSjbOfHSi24uWzSZCX7yPbg7pppbSyfvMaDW5bkHw64iQfYiGHK0n-CCAVyo2wvPDjOavaRvNFIhgE0OON-VhtI1waO6eoH5fsfVZHMN4yWA_1ag4SroXBdU_vvDMeRl4B7l2HwFc4amrH1shrJTKucKptwP2cvz9DGZ5tmIUgVZKzCG-iwY6wivI_nejfe99V3ItSS2Tmp8pImGxvLLzARhp91axJtOgrBM1nvUMwqF9eDA6RBOmy-tcdDOBiynA&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=OBvUaBTTaJ%2FRgD7OCytXcw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=OBvUaBTTaJ%2FRgD7OCytXcw%3D%3D",
        "https://www.linkedin.com/jobs/view/3644729803/?eBP=CwEAAAGJ9eK4sD65l6kH_nR9eUIkrO2WkJLyxddruLaRneCQPruEwj_3G73R3YeQmvHbVhuko_-m8wCFflQ1n2CRBfrcj0hpAKJxYlieBP1aAbWYRHRBQB6G6LAqqqBGzOZAO59AHzSgW6l3Nqd0JKJZpuFzJzecCGYicTkwv0h8bnF1nVrWPa8xxbBXJ2n8D3CCGk09x5xlXRvZRjr3XDg96Hqh61UbniA03DMiOH1-Zdae-SHifBZTln7BdGO12SFlTGQ60CDBMNZ4maucUI_-SRpTzuQlhS5_MqxlN_y-L3gWVDyZcVDlIT5YSXOX2zZaayLR7CiQiAJNYvXcvJ_HAmdNFojTAX_NkUNeikFiAMeXBR2ku3SQiLcwEvZNt9vo7Fse&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=tRdlQDClmn9%2BjEUmLX8p%2BQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=tRdlQDClmn9%2BjEUmLX8p%2BQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3681428097/?eBP=CwEAAAGJ9eK4sKf2zh5K2qsfVsLVre_n4xPSffj3qjCH2pcoYtHaWbJAz5pUhEk7xCVMH7fS_ze6ujDaPYtfIv5YfKg5sj4Wxk-IQlnN8_Iu_Woij47_dxDIaQKymbouO5lA7rjJNg_Td6AcHZQC9nhIeZ-IFuv4MC7XWRy5gSf-S_FlTEDyY5BBZT_FTkXs_DZndUSAQqFamLA5gY0uT_lAERaAzqn4TW-nuvUw1_YO9j6wysDSBabOKF4SalriMee_JufArwzu1V5gbKh7lKfe33uhgBG7bQitxg8wj2VXlZrSMG6UBl64DBuEvkRk3xtgS7X8N72A7Qvx-wCC_Qhv3SK2RncWq0eBr_21g5f1sJDHwN8cZ0ILz6IdWl9cJMSLoNRM21k&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=2k5XEFh8xxacTCzNnRh5Rw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=2k5XEFh8xxacTCzNnRh5Rw%3D%3D",
        "https://www.linkedin.com/jobs/view/3681406716/?eBP=CwEAAAGJ9eK4sPOYTlR7ztIf_TQxBk8xeRLubJCLxTbbBz-d6zbM0x42FrYrlepHyin54bESDYzUOyIy-b2u1QhFDBC_Nbr7pvOdTrLJBL093c1HXWp4u6RhnM-3j6Z4UXZo3ZHwbHg_9O_b3QAIxkFFS98qVYEHZ9I0CW-ylGE3Be1oTczbWwxQjfArvdQNWD_ZCXPT8oH4iWsRT9AzJJsPLtJhq-ZiuNbTlIpLwcq7yJAZBVuiwc33zG4jf6iLELVggXt6X-OkYw3P98_YnM8vdIJZyzf5lHQtCNeJhJ67DN75gVDkM_9ttJieA7UGCHXvipwo_DjoBY_4Cj_rnWkmhHHlIHFSzZTLfLJRaJnjSu31EMK10-PduXtQSen7OeFWSkwDIUo&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=%2BlpnQY2AutqhQuoMB5THlA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=%2BlpnQY2AutqhQuoMB5THlA%3D%3D",
        "https://www.linkedin.com/jobs/view/3679561837/?eBP=JOB_SEARCH_ORGANIC&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=l5yRK6MXpmYDMwPbZF0Onw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=l5yRK6MXpmYDMwPbZF0Onw%3D%3D",
        "https://www.linkedin.com/jobs/view/3687072206/?eBP=CwEAAAGJ9eK4sNjhA9fIscQnhXxJwpV02yi3_9WwG0I5Z7GRfAGN3tfv9qnfIRtx13iQ12yHV2kzXuO3uoWrbQ4WNfxJsOe1Q7rIcNsi54ptrwzFRbQxRS46nTJl0Pi-9BBJAkOtNz0TrwU0IznGAH1OV4iItsnumcQd75m62OYNE5pijwC_PydCYr0iP6n6mohx91KZBKQrTydaEVsWHeZSZ55wPkPZhqZkiS79RTnBuoR81vEWUGVm6t_YZRrlGfGf744nBMV_1I90cYPcJN1VMCMePdqby-F9mXY_Uc3SLF8FJLhWsNdb4SIsbUeOvERrOwIpdDDxwG45tL_QI4QfYVFbS0UFo9oPrvbM62knWv6zohKHAuWhcnzcu-w3pInFsmpqU2o&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=zOf0QEYcHsiz5Y1wgfva5w%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=zOf0QEYcHsiz5Y1wgfva5w%3D%3D",
        "https://www.linkedin.com/jobs/view/3675434677/?eBP=CwEAAAGJ9eK4sPmBjZq-F4o-Ul3mF4QJ0n0vHyC1fRvPZqyExNzVSF8DyrLqcjha8icBHcaiVGcIX0C1ZgmGyw45jUX1x7mItyyewurzWSGnnwubR3wx3VnV9CatD4sI-LXj3bT01AasNHae_C8hMLZrzpGr5jxWUnyIrTDsAhh6yYyy89IrzyGkB7mAAAFocZUBLpeZTnLoj8s6La3tv4SVdqlzUGGYr3iOvRolcFqgGf6xRiHIolixGf_aUuPXi8dQTQhAjmd-igo7eJ27fUSJK0ImNU4jrDpeLeRRUFE-hNTa6JS2ijpWOFKceTJeIrrk8xB1ms3yCR0EczhLHNAeLlORYWaQA3ihTeT5AwxxhrPQ3SmA0haZnM2_j_jjRoGfLTXHbx0&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=kUewMssxczlBdhLELvhHPA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=kUewMssxczlBdhLELvhHPA%3D%3D",
        "https://www.linkedin.com/jobs/view/3681127964/?eBP=JOB_SEARCH_ORGANIC&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=AH42dRmbu4bhyV87P5pnFw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=AH42dRmbu4bhyV87P5pnFw%3D%3D",
        "https://www.linkedin.com/jobs/view/3675778747/?eBP=CwEAAAGJ9eK4sPMV8a3TYg9Gp1bnqhIC8B3iJPCIDMEDQkziLIOEQV5CrytCQLkm29jEjCN7sfOtMbxjHuSLMvf39bgTP2ylAeP8ZsuJUyWR_Rij4dneBwpLWQxAjYiQEch1-6yV5WzVyd9UrZzbckSZOf6wy05QShs9dHVjMDHJB2b76wPcW8Xmm0RVwK95obcXvluD-CXJCEGSF1Y9PWTcp5YQDli8e4KClEXLp-LMvzXsC6YYmJYbaQ4oi_EhoAhZTe2n4L35_RDYYck6kX6HSEliYwcEdHTnun8HesaDWS8iu3QlbRmVxIYuxQT3p6PtoaSHrXdQqFCnRKfIR1USKCCAH6Jus8KluIv2wxzO-cSl7VjIuCKwM58EjhvQt0o73pRflOQ&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=kEmOppZ6eOUMOsA0qm8tVw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=kEmOppZ6eOUMOsA0qm8tVw%3D%3D",
        "https://www.linkedin.com/jobs/view/3683146982/?eBP=CwEAAAGJ9eK4sBUndoIyg362my2P2_aYnA8ZpJIr8MqJ7kuSzL7xW8yGWV_OeviFxpcsI7YyJZ6GJVVpkzm0LUBc4jfcu-SNJyGQftJIvT7LpLkGdbHVwPVjb3f9aW6KKcNlpW72TBiOWYGsZA2__2dF3I0PFSdlMsYPhi8Uq9R1l7rurxGk3GGBnVlFpY6VT7f1r6-WyonWMFXJEXVinG9-CArI8OPcfxFGnLlvcBUGpEPirIPHuZ8IjG5wnG3aB9QeSkCM0YY9aHN8B-S8ajuURsU7e6_LEM0qXEDRTWGUVooFQ2Y-p6NbaHUywGPBVjv7HaWrtCBb1B0pvfEopl_Z0FdGCHEJOiWlw1JFPuWFeW8l2HdCjuieli370c0IegfiVeUW2JM&refId=XfoYYSphY4J4RsQmS7P24g%3D%3D&trackingId=cWgAYFAyLHvW1suphWw61g%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=cWgAYFAyLHvW1suphWw61g%3D%3D",
        "https://www.linkedin.com/jobs/view/3638092697/?eBP=CwEAAAGJ9eK-3-Xs-hukoiy9AhK6cp4P8D8FIZD-8gfo8UfhiiZALZPFhVCsNS11feB_TXxBA9UTehW8MFMjJFlMa_N22NWTczlid_eRJWrvl96VuyrFIfIugWircu8Yq60xuohd3bM_DgeqB2-rOFMrutiXG9ciome_u1dTok3J2-OV4SdJbKE_GPYfPu28CXZyfwLVkSrCdeL9CWrDZptdijsO-2GSmWoH2JZOTu35y_uaJmfGVhQinyXT2mu88rx_UEIpre9NJeNuaX78SFHRRkEZaQJTvdSy4onEExMJmEU6YzSj3IChWfS6VMsTTjwSChGeHfYB7pmUzqLJl0t4Y1kgKPHROTtyR1m4YnI1LnY9Jk44mEaURzEN9jfHKVkAZmSBilQ&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=PRl1bhE6lEx6%2FnU49rjX0A%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=PRl1bhE6lEx6%2FnU49rjX0A%3D%3D",
        "https://www.linkedin.com/jobs/view/3669521131/?eBP=CwEAAAGJ9eK-37VLDGLFxzdjP8TPjkyjmmwtU6YbdvZkp856LM8oEpm0uVED-MJ_r00b3hnXgsMKUnOfRVbLQK-wfiPsFJWKvdKay-4prW4gaVWojweg5XzrRs5QP90s1OVZySIh-blHj4vcqHYt7PTa_dpovmQGyr_0YDytVV6yPPVeO23enCMENevMiU3M99RzwOSouqMK3WQjCVQ5xasbEW6j9COIvaT3ugDLXTsl3MoFjpbwVoX0SVUy6TiVai96PSjltfXUVN5k3CABpKdP4mRv8u3Y4DyNG3cQ4NA41eOglj55p4cAcS3-24beqfdjL0XWwyfPRdPyrZkTyZSBDBmndUKj6KaW2-U7nBXyEpEQIpm_SrNOojQ4rO-CLiY8F6h4Jnc&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=q6jdWjKgjCSi0lDkpg%2FwCA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=q6jdWjKgjCSi0lDkpg%2FwCA%3D%3D",
        "https://www.linkedin.com/jobs/view/3680838954/?eBP=CwEAAAGJ9eK-37ocM2wmnwYQCeG0iYjL8WB5dJy6srwNZL8avyG3FEUPzj9G_cJyQaLE7daee4uyAllQWXyqz95udv1ONIuUGrbJutfGjW_cLHhmwgiZN_9ltr3-La2ujPwY7Gi8xNlA1UB-Kik9t0NUPAI7qfsS_LhTM7Upei_QN3ZcoT381PbU3B7rAm3E7vxtNAlPv_NPuJqo0o7gvZyQnyVrxJkrmUI4YiqYNSEiOQlvauJrRW7qlsJkCXeWfSeha3Ki_Ryi28jjuD3lrE8Bbl3mA_vZu0LJW6yuD7Wf8m4Zje2Ie_Q8i7Ba0vYVUUZ2Kv9FTjrYd_vdqo33vpPuCtbAi-vAZB0usw1-Zjd1qqkxLa0je2I3s_tsnm4tePakPhdN3R0&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=a8hpiXjytOQg7UIQy6VkMA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=a8hpiXjytOQg7UIQy6VkMA%3D%3D",
        "https://www.linkedin.com/jobs/view/3688200168/?eBP=CwEAAAGJ9eK-3zUYHxvvXbx84xFKvpZZnmne0ADtiYihvUiN_HvVLpYzaooRynMFugbnu4WMwOWchwH6njtuEpce3eU0qjU0Y3aO7C-2qOXCc3uQhcGqEK9kSm55hSHfV6FahOOlZdUwuXZmFFT0vZuTf2NSAEnwCYprllGu3oud1eMVzXZ88I71QmynHQoRBgq70uuIypt6BnP-WKwmlBZocIt0d1ozTtkh9eRmxBGQkxXjeIYmkmZmfoAzLzg2iLgdyzYYeftUMGoHAQHzWsTgNhAkHYS_3sXsSSPzc7EsfpVHgcL9R1j6SFBueP4f_h83CuLebuKHptk4WlBnK1mQN1qGUMNpbf_wwth9T-fdjwGFwssy2m-jrf0epH1_uDEfeey_CYA&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=t8iy2v0MYTd2Czm%2FBo8IFw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=t8iy2v0MYTd2Czm%2FBo8IFw%3D%3D",
        "https://www.linkedin.com/jobs/view/3688109143/?eBP=JOB_SEARCH_ORGANIC&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=uT4OzMz1RvKKExRlJahKFw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=uT4OzMz1RvKKExRlJahKFw%3D%3D",
        "https://www.linkedin.com/jobs/view/3687962324/?eBP=CwEAAAGJ9eK-4I0U0EH5NDfJaOUIieqGgEET_GOSG3BtCQh6JjmFwUDUagiY32bZdeVGYBI5JNT1g4ulIRVU6gbmUkG_4LiSpLFUXTUZbWqgv2tZOCNbCINB8w14czk5UwBNVn90hV_Rh90u63-NgdkuQCrMq06hoH6mzqEEdfYb6cNCgfOgSB01vCu4wTT1JNWf2tSgA9QnStf5nPFrqM4mHf9DKNiHlV9QsvdfQ3AMPZc3Db_PyIXf0QJLNK4HBngNUlRwiXvMIPXX71vQ3kkyuzghcXYoiFW1gxjaivOxtMnmTkLGuaICvmn9nuLv9hcG5zHwsj7ZnWDB9amRo0-n6gGqtd6MX9U_09DnC7A-Xz4IR2LeL4nQD6t8nsX4yKVd7TNiyT0&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=OjOaf1%2Bee%2BL0ujsWev9%2BoA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=OjOaf1%2Bee%2BL0ujsWev9%2BoA%3D%3D",
        "https://www.linkedin.com/jobs/view/3668245123/?eBP=CwEAAAGJ9eK-4C_QdNNluEaWOEU-OKKE0ym1PyI_SOGNRAXqQ4bJ_AZbhgJAXKd0qtTqfxmlnr8ASRMBRP7RnKgVok56mz5G87zzlJj7xjwmqn8hW7p_EWKaBg7v3q5vPpm3irlx7auWUU3NaY2IdmM6JrOtPNJVgZ7l4SxU7Ed9k0dW_l4Vwl20gvX_YrZ-ckcRgXT-zpSCR8Paqe7BbGWzKzkPtTb7_uDQ8VGYHcgJEhFWpIb774Ij2vPmJ2-Z5aUxDKTVnU-ZrrLF6lNIz2k8OVfM2vGRw0mOxFlb1jhY5JF9bxshHMOyY-zB_kZjtVqlmB7N-u194Y6C7CcaoEcuaHeAPRk7D4qNFRDgNseVa3_vW30cEW6_c8ilQvDDZ3PlpIJvJzHEOw&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=F29XrMp7EY7YrAPCr2E0oA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=F29XrMp7EY7YrAPCr2E0oA%3D%3D",
        "https://www.linkedin.com/jobs/view/3687375715/?eBP=CwEAAAGJ9eK-4FDfB1psVWuatr8Ekn5YhDl32kTDkHHs7xLO1O3BI1Mmc9U9_lwV9XKq2sdjW9fiT5Yjv4VKSpb8GygKywGSVOonysf_tDTe-jXuUAX8cN5yfIpHaLFH02cGSpKqWBJVLmNor2WHzJkVusr_G_oVPraCxIgYmNMVJS6eywROa4FONm-2jVW3DD0_PKT4YoBOJu-8uvOqDaFM712kIFCsyyF1l2TpMBNnSHVM5QGzhqQfA6h0Ik447nuTg6i8KrvpeBzvKRqliOcUnUbPtZGIHml_mqjUTvzqxhozLCBFc6FCE0Ait7sGU9fW8sO5V79Zn3DmYK8YyuCqY7XtNCivnZgBv9U41tkcKbFTZixaekgZOHXMM5TlLh6-VtThkjQ&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=Wm3VvNW2csMAVtD51MOr%2BQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=Wm3VvNW2csMAVtD51MOr%2BQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3684042809/?eBP=CwEAAAGJ9eK-4BnBMfTIpl75Om_cqPj6fc2GUz_GwXRsfD7eLDIBZSLS0Ivbi2v0_F_rLQDebXNOgFK4m-8Fa7t_vStlLAwVFn7C_NtCC7WBPX_oU9b0rGm_lhrF0NoYvgkvSb9x5p6Sk-jQd-BSoQyzhXenLxVDxdNMt_4iTy5th8_sd3csikSu080wNGEhYZofQwyVAiQP3y4GdqxKLuWt4FxT8oCgCbDFPjIimWmMr5X939ul957BBqOA5jkqzVK1rEDvd0Xd3IS9oS-GnrWng3ZZ9DZ2JgfuPSJCvtlkZY76YBdD98NKw4R0l75c2mLA6spS8LnOc_UAOdTSM7Fr6Etu-xFSdnW7LfCegr5F8dnXELqKMWE0KT1EdckOPKQGePcfC2Q&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=KL9s%2FbZsxR33%2Bd9MCoZNsw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=KL9s%2FbZsxR33%2Bd9MCoZNsw%3D%3D",
        "https://www.linkedin.com/jobs/view/3687952647/?eBP=CwEAAAGJ9eK-4GY1ZsF9VltEjK5D_dXW0iHXqFuueKN5nG3Velcitcq6rbmUNqhmLZxokRDDaCmzbrIXmUkIUXoKndyQvsWxG04pr7C2-4j6hXw1gLx80xPtRS91NUU7w_CWIWrTuRHIuaaaQTM52fjMSZRnVinDCFlQrxOyeRy9CitofPJ2fRWQZfXO9jh-3B6LtltoJwbgdMAvTDbcxXBfos8arFKCRbtDFQCOsvuc_f8wRdPoC8Bd2PPd8_y3uHMxLJi5j3BuU5yrnzNPCvaaygqGPxF6fZyJqt7o3-QPANvc-j2kJPPn0nIKUT18hP5iKcG1qESJOUbTz5rpGr2jZxbR9rhqCsFWWwMY1qWdWqur2q1r-SBon1AEmwOJi3-DWWFB3JQ&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=xrap7jfH9juuZBxwVzntEA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=xrap7jfH9juuZBxwVzntEA%3D%3D",
        "https://www.linkedin.com/jobs/view/3688646482/?eBP=JOB_SEARCH_ORGANIC&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=zWZFe%2FhRmsyCAkyHEKvA3w%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=zWZFe%2FhRmsyCAkyHEKvA3w%3D%3D",
        "https://www.linkedin.com/jobs/view/3684700076/?eBP=CwEAAAGJ9eK-4LtWfXZzHgsL-wstH4thajONmmnS7dCPgKfaT2rmjFpHTl1jpWdnG6XM6BvvMZfl3KcfLeYc2RsGc1sM75wDDZ5-WqVq7I6fWJ2eW3AzMN0AxI10BT8B25sgZ3ugrrCm9VATZ2cdTgOc795crLpPON5fZ5443v4YnEzjPPxZ5zzBr5mt-aEdQsDGFEX7UEKZH9KM9YfoY6DMQ9iPUj3JJTwF90f5h1vYVYsVh7i_5jsnm3nh4vIaKr_DQs6YnDzipLRJ0IZLpy3Qgck1jGUcVxoS0aB1FahQZYfeVSoaw99Kji6NOKsb6hyDU8V1FAEs_Mjxp9RgTiTTelgUQR8PtwsLWL388UPAwpm9K37TRUuZC7llBMozxsbmTLaOnmI&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=dS9zjjDT9hi8Mjm9cCH1Kw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=dS9zjjDT9hi8Mjm9cCH1Kw%3D%3D",
        "https://www.linkedin.com/jobs/view/3688876976/?eBP=CwEAAAGJ9eK-4Pp3FHUGgeUIMx1qkf2GX6oatpiPL6Bx3q80rVDqc07AJ22wt2-n_VTeXj704d-1V1n33X2C_Is70hhyQfy6HJKxPfPOOSoY_hKI8MqaUSG_KswphxaGD92Q7pXrQ8PfmapfHK0xNSJtd-HndPbPwyDBn58e2gkWwoYWWIyVRmsP-7Xv_T-Mqff708yl0IBLYN0MDCwSxQPYxRr5IUFNOYYJYEiCHOzQOexCHynYNNazVyS8YaEpYpfwN9XxKECEWzo45T6J_Y2L0Mn_POVtQgpOMKuUYhN_XxK4FFcs1ZBGvDg0a-c62DEu8psbluZj0-8DMJ0NHDOFH13Dk690K1AUk-IKpCtt2DtQXPTAKkpxvMHeKI53u4heEzzhLdL24Q&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=gZGeq7m9vD9LIGDni1qTJw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=gZGeq7m9vD9LIGDni1qTJw%3D%3D",
        "https://www.linkedin.com/jobs/view/3683573551/?eBP=JOB_SEARCH_ORGANIC&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=hV%2F4tulRTnlRnCSAZ%2F45gg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=hV%2F4tulRTnlRnCSAZ%2F45gg%3D%3D",
        "https://www.linkedin.com/jobs/view/3684002752/?eBP=CwEAAAGJ9eK-4F8METO0L2tSZAuDTYdeOKwUoMitGX8AgnXLYRejzw1HMb9fx6QH3G7QCLYD7AgD6FvfbEcGI8gK6dxc7FO3jea0EA35AdfS5DLHYiS9uxPZjxcDPaTyGVlyGo3EgZ7F1u9O4C3j7fQVhE3WRwG3FvlrvJCQBfnlQz1SJA0QHuwAomvGmrBnWNyzhHN_pUtmFx82Obt-PRd_zbED2TpkR9W-4N-oYY06mM9cT_vReV42aflXu4RSyMcbmEMn5DXClPvrz8kA80-uUJ5ecMmhF50bCOG4cDa_s2WLV5QLjRPUkYSFmJdRkE--xh2FP41pl2pZ4qD3mIIVt-OIM-HW5KSaQ_Zi8IiwUcH3_H0B5lyWspcZUYR_3n1Gwi8TSWZXNA&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=tD%2FdyitM0zciSZygjKIkKQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=tD%2FdyitM0zciSZygjKIkKQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3679957073/?eBP=JOB_SEARCH_ORGANIC&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=V%2FLogGw4KwJRhbp05%2Fk1Yw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=V%2FLogGw4KwJRhbp05%2Fk1Yw%3D%3D",
        "https://www.linkedin.com/jobs/view/3688373441/?eBP=CwEAAAGJ9eK-4FGkRCwO2oZdDmu8LE-_w2vHb2kKDaBJp24Y0DfktcC7yZYMuFvVT2h0-ZUs0pQ9kXN4Qq_1xbUdjKJWno6iNnCJHOnIPmK6GD5KSodRtiZexouGzHWkSquimCEh3mhQwEUDQDLX4vvN6DN5f6XA_orj1mKnh6-ClzAD17t_BjEz998jzgOvT0_7pqrJ8DwgF2Axoo7WQd72sr9Ix8ADtqG3w-Ady3MOXOKn7tNoxKsZGKzWql9QbaiI10Pmh3NcEw02i51JB1m6G92ej5UQ6b_aXPhALqGcwvu33a5JAaVEJkVwUmPLiSaQrU4-hXmm_yEdNeVcFrn2Qafl6SS-vphjird-pF__Gh5aYhsvs0ouirKjxa3Ppqtl1vL7t_0&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=YZt3%2BHhzqqNKHc7kU6i4iA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=YZt3%2BHhzqqNKHc7kU6i4iA%3D%3D",
        "https://www.linkedin.com/jobs/view/3689791968/?eBP=CwEAAAGJ9eK-4AwMBRWZCDyxct4ZUU7hCCRfV-25Hx3c6tLgxKTzkfqtGGR4bKl5VwA7D8pEhLQuCK-ARsn6bQTojfw7t0Gc5FI7tA4jpVPMF2253Gv7DtbUy6y3nVh1GHD4UX0eKBsdBgTRhPqfgt_YygjCVEMbawX8Pu0SX6hfSDp9n4gPYmGRRROz1p4Z-4WG1srB53Jq-LYXfeH1k1Usf5-kG03TUfbkO-f2WphHIERQkz0oqBabBQZ4OQr2OauJNzr3-TNNF_jd67dnqQCx2ZaWO94PwdqC98wmnIqbfkm38QgC8xvqnMVRCEgoInuSY2KnGcJfvHeA6RKwxjP-uDK49_JNTN-GR4uphbNE90U7pwTsorShiiMMU2ECkGRGS9p6gwa6Ug&refId=Tk5OdEChVFLXPhDSEArCAg%3D%3D&trackingId=bST3TM%2FHRdCjDUin7hlkYg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=bST3TM%2FHRdCjDUin7hlkYg%3D%3D",
        # Add more URLs here
    ]

    all_words = []

    len_ = len(website_urls)
    if len_ == 1:
        print(f"Searching {len(website_urls)} website:")
    else:
        print(f"Searching {len(website_urls)} websites:")
    for url in tqdm(website_urls):
        words = get_qualifications(url)
        all_words.extend(words)
        time.sleep(1)

    word_freq = count_word_frequencies(all_words)

    # Sort word frequencies in descending order
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

    # Create a modified version of common_single_words
    common_single_words_modified = common_single_words.copy()
    for word in common_single_words:
        if any(char in word for char in string.punctuation):
            common_single_words_modified.append(word.replace("'", "").replace("-", ""))

    # Convert common_single_words_modified to lowercase
    common_single_words_lower = [word.lower() for word in common_single_words_modified]
    filtered_lower = [word.lower() for word in filtered]

    # Print the sorted word frequencies
    print("Most common words in a requirements section for software engineers:")
    print("\t-------------------")
    for word, freq in sorted_word_freq.items():
        if freq <= 2:
            continue
        else:
            lowercase_word = word.lower()  # Convert the word to lowercase
            if lowercase_word not in filtered_lower:
                if lowercase_word in common_single_words_lower:
                    print(f"\t{word:15}: {round((freq/len(website_urls))*100,2)}% ({freq} times)")
                    print("\t-------------------")

    print("\nMost common skills in a requirements section for software engineers:")
    print("\t---------------------------------")    
    for word, freq in sorted_word_freq.items():
        lowercase_word = word.lower()  # Convert the word to lowercase
        if lowercase_word in filtered_lower:
            if word == "c":
                word = "c/c++"
            print(f"\t{word:15}: {round((freq/len(website_urls))*100,2)}% ({freq} times) ")
            print("\t---------------------------------")