import requests
from bs4 import BeautifulSoup
from collections import Counter
from tqdm import tqdm
import string
import nltk
from nltk.corpus import stopwords
from common import all_skills as common_single_words,filtered_skills as filtered

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

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
        "https://www.linkedin.com/jobs/view/3687331388/?eBP=CwEAAAGJ9ZDsK7UU-QgTqpLDroDkPIwMBz0zRTrOGO1i8wHzYySPestFX6Tc818f61S7I5Navwz3wzDF8kFQHtqJrZtfiRXViuHur2Rto2SpuA9hfLFjVreQVsZc12OhLjKolfMmtH3PGRXTOuqEKV8tRm3bCkzjHy9rl4OcuvsdHlIJdp8xumZFDc1t1mwWoUo0fnCEXceD5X4gRkydRyk9tzKkQEJNJJGkbHQV1m8g9Qc7CxpjrSIweiLaaJyTUGjKTJdaBC4nfTig2eMPVflbD-dTdu7lflqFL8u0hsrUitSUtz0Aa1BKjRs1h9BfAznvU2OmJRsiKBzO_Fa7RpxTgVFCC8IQvIzOec1TbN-4FpOXKX9HmjVZ0a5KdKzyuu8495IU&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=UuFq7mTEuyE5LSPDDHdISA%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/3683675367/?eBP=CwEAAAGJ9ZDsK77N9qga5iREpNjRQrx7-gBtFYQxI22MtnyhpIN1YY3UGkVr_ckvYUKJ8GsnRlhAS9BmMRQjn1XSbVrYmnkCFspEyBlu7hrVldZPLcujkv3OcPuRY2ERnrmCHB7RGsE1Cf-dz0PKHgOMSzz8f-ttZNJONfjw3Mj3b5mLH1yMEQNHdzMMXQUE_aZdCZvY4T3KXZr5AphaaZY7X7ZTg8Yw43VhPIOrAUaeuu8zVhucBCkjhBFUUdoWR2D1psUdW56wq_QljlUlAy-V29SoUW6xUnRh_PS10HjS01nY4WCEcDHrMWWBlYkZGiXMTFEpeHae3Og28mtC6AG2yRvKjJBfyT-_z8aB81Xrtwac3st6ZgXEBQhyElEF7wCuBo2mFQM&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=dGoleucOz4uUXfgoXyewoQ%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/3644221250/?eBP=CwEAAAGJ9ZDsKz5poKVpJ-Nra6lgy5Uf8tVaSchFt7WWRmrXU86qK2S7HPbKelTDMoPOiV8ao6ZQzlnvqkIyfR2c1tuQ7JE3vNqtm9z1f24453iNAlczQRInn89vWvVrRNvY_pSVGn4Di4Pa2zjWJsZdDfv6TTre543pM58nw37lFms1ZJqeGX7S5_xTYV25_GWb1t3H8n1D24jKPWCCgdUoxRKILRvA4UAf4KeTWOzWW4gtcebLc1fu9HGQQVqSqm0ZVsYEfQ-KMvTX5tM6-LC7UFooA1zWfw6-aucwA5upDVUB6Zwv3rV9SXoeKE0zm7hWesCE1zRZrjHCE1fp25Br4xR89VpP6HYwdktICWxJy1VJHMttdKXyenWFyHqzjpKsA25cCxC1QA&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=%2B%2FUK%2BMGddre7Dy1l7DkzlA%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/3669642784/?eBP=JOB_SEARCH_ORGANIC&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=l9GiRmLGYIIyyFSFysYQig%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/3670074707/?eBP=CwEAAAGJ9ZDsKgE-uDnrz3eZTRXSRnBK8W_4GAiTcooVCIkSUWPe05Zxg1XsRLpt5xhGB6z0f7GKz_AZ0KzIjrH2HTDdFvgw2Kd9d9efcloIQIBdaUvAvVkL7pSfSigXdIY1FpGaptGujpDb_0Dj-j31757tf3AqeEqH6h-s1GkI7Fiq95x4VIvR41PYXUrPArVw4nKuimuPgW5yaNLsYqpJXdVfqHiudCT-tXvzjRhmyvVIcO52rspbyJRrcYKXe-9AReAmN9sxtswDMZXtVYHDMb4Ojx5c_6WeizuyyXRL3udsUmQLrFqx8rwpQmEqLLDkAM4U8Z9BN0TKczWW5MO_QWF3-FU6ihat5uMU-ewHEhCPNW7waRGu1TzIL1WxHlXP6vBii-OaNA&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=whRB7e2%2B24MPO92SbOxnMA%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/3688646482/?eBP=JOB_SEARCH_ORGANIC&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=IgxEJtK96pdZlLtSOArXUA%3D%3D&trk=flagship3_search_srp_jobs",
        "https://www.linkedin.com/jobs/view/2991003984/?eBP=CwEAAAGJ9ZDsKp8Y71Kr1Ziz2BHOpZrVCS5296BeXTV1Zab5WOp1Za_LcMOJj-XDUQWe0IuZpgGLL8VMdi6zX-v18mYi7tw5RqkhqycusWK6znWyTYnzLVgVkBM4qQvkPb_Nf7W0fIQLTzeofoS-zOlFyyMqIgWhZHJ6Fjfpn42cDVUSe_d4cDJh5iAKawccOPK65VpQKm8SHef02b5YhIOX8maPdxw5UuWwe_AtebcmedUUVxAxFTFJRrw35z-VK34d3RQAsPwFdR4E3LJJapykZtE66LX2QF9rD9sdOB-ltfGXCxdS2iwvsD5LA7c2_12v8SOp6XdDRzCcIpZybxpPOAy-xzYfHIXmCcJAUPKODCSlsWBfV8zuFjlw_LXbs4TIKh-mbuE&refId=p32Zn4ne%2BkmxxljaJi7pFg%3D%3D&trackingId=Rhe38YNC31kPhlROHMYWwg%3D%3D&trk=flagship3_search_srp_jobs",

        #all software engineer jobs
        "https://www.linkedin.com/jobs/view/3683869869/?eBP=CwEAAAGJ9cyTPKM9hbgpi5z4AT9AdGJCs8JKipGIC1RtNuFtmV1Or5yJMMT3rmVDQL2kNLQ8eEX9PXWcJvNQP9wqVmkEeUI88TUNsiVKMcLTfqfg2NvFQk5bI8vEATaTZ69gDweYvayw6sTnIuLZuYAjCX117TWosaC5QtF4EALvnF6ygduuEcvfG2HGsHw2aNu3IHc7uoOrTAZjCgVK32dy9r21WdyuyV1ixBx3bpag7rhXCn9ZzfBXHJbDSOKuf975I6aNrGwQSfnXwS_j4wcT9A6xbSVUtieQDOeWHiBLGFA72l4PWo0noHsBtKpJmnncmsNbhmQNODvCtnpZhSEwfmhfoUpJcAfMLw&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=cVcZEixY%2FHG%2FRHmq1GNMsw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=cVcZEixY%2FHG%2FRHmq1GNMsw%3D%3D",
        "https://www.linkedin.com/jobs/view/3637861032/?eBP=CwEAAAGJ9cyTPPkiH28XGjFQ5nOAU_k_qcRh-fbp4VWf7wvLXIYNbpeN-OWtikOkfAy3BlzEnakPAVlG33LrdDdBrKKdqUipqTg0gu1DRorm2o7PF1QbHw8ZkfTDsJmryWBj8LEyGYxqoRtX8aA2U60WmXT9DXCpsyTUJg7MOvmcQYENc3N2VULNlahQ0sDWMUgFj8IBzI7DJ5w4VJVFhtnPh5x_cIJzm95ZuFSlTXdu2nPdAlI9jBgtPE5xc1Q5OJ2GEHkiGaOKSDoWLt-ufMU3s2_OQuPR5QX_zMvWI8hLXtHQ5DF-ZGmXkx8dW9XZkt8VW1vVOVPl9eOJjrbenJSSw5U9aP_MjTcjh0q2ON-zOceDxmFbDLWP79BYL0bN4t-SsEJ0&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=m3mthIQ1Gm580r%2By15CWHg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=m3mthIQ1Gm580r%2By15CWHg%3D%3D",
        "https://www.linkedin.com/jobs/view/3689483932/?eBP=CwEAAAGJ9cyTPJXEYC-cioylfnEVAq_w7XvnH2XCiaT5CRCuXJPQOEnVai7KfKD3Gj6UK_aE1sDt_Xo1avs-KCW9AyJDr2CHAIbkJJuwDBRHD2H0mJqJnjLiDPIMF-xkdluGV53Ah7Gxp_IQG3JgTqB7bSJEWc3NBIQQUfkGk6w_aRn19jxjgGMUUgppF-28ap2TNR4DL5KIjQoTsoHzYpXed9gT8LJJVDiHLIEeemQVDrYsS2KDLMmXCAgsBDuyIOl8PxWM5mAjCjg3pyp5Z66CdxYY1DEj9bvOc_lDt-HfEc8XT3STzbsVSMdVvfmdZkZoCme-T5BJQYry30tr8-UtUWzYmH7u_okZ2K9QmxkC7hV6kJaDjSdChI28ZcrVGxVS1F4u&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=ZwFfP5YGX%2BuleFUd7vc6DQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=ZwFfP5YGX%2BuleFUd7vc6DQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3674369797/?eBP=CwEAAAGJ9cyTPP0d1QeqqYqnUj-W0wfOs-GH72UxTbpqM4ntHLdyHhStg2zpLLm9hLlpmsgh6RKpjVYTsI6l6_wZE6ecLPpwJpc9dFPnYNzIqmbMyZJtN-LGAHTwriBDxBsyIYQIvyMiZWGSyOZtlJBpsD3Dqgj1A9idy9ih86ZhR1PJ67ySojXlO3uyrXCA96wVxEuzYHiq2_5btmDd_Rf3h8DrKdz5-whLmv6IZh4CYvcXAoWn544u444qyq3ygGDtihYcGj2eBn3FzJLvWA8xdm83QyryDcRBTjRLTKF3xqM1o_fj9-N4qWZ9CXhczxbkfz08b4nNf-BihFMeT5s7Tmo8Li7gZRh8Vg2qXqnVBRhB-7Y28Cg3kteezJWnsws02645_Gc&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=%2Bn9WK10%2FSqM0zivFhSHuqA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=%2Bn9WK10%2FSqM0zivFhSHuqA%3D%3D",
        "https://www.linkedin.com/jobs/view/3669642784/?eBP=JOB_SEARCH_ORGANIC&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=AWiM30C2Ds%2BvNLFm0SpHJA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=AWiM30C2Ds%2BvNLFm0SpHJA%3D%3D",
        "https://www.linkedin.com/jobs/view/3669642784/?eBP=JOB_SEARCH_ORGANIC&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=AWiM30C2Ds%2BvNLFm0SpHJA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=AWiM30C2Ds%2BvNLFm0SpHJA%3D%3D",
        "https://www.linkedin.com/jobs/view/3660605962/?eBP=CwEAAAGJ9cyTPJrj_B5JcZ5OeuFAFpxXHn3CbaTAlo76zkjgx7mgpdDkG4W5yaLzVTF9-NNQ_hWBYCbpgMj4CtWxZ7YbRsCOBuLgdIV7t_vnfCJAlCvQkUSKdb21P40xCWaHkuOjFffPHt1GafwytYenksS5pTnpcU5YJMk1jFiHqxYdUaVtsfzevvNseZOVPzFzdrWpQ2Y56k9GS4UBCjOPeGiNmWlix21glodGeOopaTEFGoMlsBXuZEBiE72noayeo1pvVs8WFWetPx1LUqPG6rfi4IT_i6e3gnRbK1-nAMlDtf8EAVdp44S1tV-QQcFqtgx1ncQjA4rCbW582Hn1ygb4ZC3aJZ83dlY2SxZA6Gl3GNJtp2bPpJmJA7CB8zv97Hvh&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=wBWZox3g2ufPSG%2B7UAu%2Bqg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=wBWZox3g2ufPSG%2B7UAu%2Bqg%3D%3D",
        "https://www.linkedin.com/jobs/view/3672793777/?eBP=CwEAAAGJ9cyTPDg25kEvVAI1U5XwHsr4rRj5Gu4UAz5uL-9EVSnhEa6RuMREEyprUVAAX8B8IPve1f9Ft26ouDpXRBaHWPZbJYD9Na9vSz-kNolLbtbdml1zUjX6W00WzRoZF2igpEnVWFdA5XMDmsCqZ6gBEdb_0P4dsI4ppKeCBDKMmD3j73mDdoFd3Nu_ZzxRJCPysU7frDCMbrzjm3RVJ0vK4NwM-es8b0Mc1zHG9BRp7Yslyuv1MPRP5YPofIJ2a78UnYW9sTRlAql7mGX5H9R4sjll5yNeqk0UzwY22-bab6tuwP1_MXG-AkmBZfvYQ_3JIMbVfvcc5Nb-zp_CC7i6k4gCKoyDcJMKpCqVuGsqGALu-6y7fAORPk1IJSY4IM5w&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=pAa1Gozc4g%2BuPnH87ANJ%2FQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=pAa1Gozc4g%2BuPnH87ANJ%2FQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3635070471/?eBP=CwEAAAGJ9cyTPPb076Fcrg41A7EoFej30bFSn1LLgbE_c-Tn1Kqh4P29k5P1vPK3USYhqgiXPDVG_FO_7zrBiGVbqjJq_1ve_kGv5CmuhfsEhBnfs6n4mpLef6yiKtFai70ntCmUoynNAQCNxWHqaivQYZde30QSQnkMCszxWGzAs0eptXhKkwDvDmGwDtdoHywGE59qwVRmj_iVC2YQrTcn3Qzv-QkUawTgZ02O2kQvKcbDMlotAzQBuNTbfMAWtvc3CKRPfZ9l-OdRTXkCHKw9soufyXLaxJZq2rZLceQ1zwUaSbgbEf3zPZrlM89YPcVzCm5GWC14LFAJ8gp4VovXI9deigav9f29J17FN6ZnMeH9wRyHwSeuIRGvctVVJDGlD2O4&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=B9VGP9i8mkRgVfcStsne3A%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=B9VGP9i8mkRgVfcStsne3A%3D%3D",
        "https://www.linkedin.com/jobs/view/3685623922/?eBP=CwEAAAGJ9cyTPAm5Yn2njo9F0H7N1vFlCjOLqS2VE4bYyWCK0mO2NGfEphPeeKvxXmHphBF35jlq8vMEAhrgX5bzTxjgmCZUulEpL_rKgZp-GpS5YU0bn9yKzKhFGiJjP2rONmnvC55paXp1g5dJue4mWv4xBXsEsjWxvdIqt1QovZid9x-ifNseYp85UzK0bDSMrVCuEoFYO1pFCL6Qi14fIT9WO0ryL4w_Lt0xvi0kx4R-x6a2cKGA4hKGPBsjDwSzKtwc5W2wi4s1UKqKUFNLxTpUdLtZ3DGal_PKXrvXiEW0wE9Cpf_DZ9O7aDAyo_vWDXmRKBUPl9b4kpYUfQgLY2PWJBXmaGKGYzjtp4Pz2JAt-BxB66z31qwxH6M158_cIik7&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=LyY2aeLgPFHiN1D%2BRZroBw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=LyY2aeLgPFHiN1D%2BRZroBw%3D%3D",
        "https://www.linkedin.com/jobs/view/3662993468/?eBP=CwEAAAGJ9cyTPZnJBAAvdcAAc1BOFvO_Q4J2tuddlgh7p_BU-T9pRa-NzNzUZnhHHB3KK0v7_hy1Zujc5lmAOHJa0I33ucItOePehXUjAm8Iy5w_1VLC6lJCcDIl_1252UZZpsSRaWoiVIbDO6f02NwR2jwvOZgBgpWoExAbKOf3Xc2IGF4ySAkzlMLvnRJ3dw38nMMu0zRfjDQaHzeWGRS-RFdf5BTveo9glnXu3RfxJFXrg6Yi50BJ0xZqj0CkJk85Q48g92MH_u5GXBKVZClMDupeVhFlS8_i8JJi9cNqlfRCGID_6KrOco9T5Ffcqmz0PSNWko8uI93nNTvPjUQ5luNqSlmc3bTWsNNQ-rgzeV7HdqpyzxUIv6BzydX0cFoVGDXqfqs&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=7%2Ffuu8Kp5hGaD1BYCAhSAA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=7%2Ffuu8Kp5hGaD1BYCAhSAA%3D%3D",
        "https://www.linkedin.com/jobs/view/3681225673/?eBP=JOB_SEARCH_ORGANIC&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=Lxb3XFEZgp7x9Ed5D3MY%2Fw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=Lxb3XFEZgp7x9Ed5D3MY%2Fw%3D%3D",
        "https://www.linkedin.com/jobs/view/3681428097/?eBP=CwEAAAGJ9cyTPYeN6BHvhFOObHn7CIkDAgMU8BETIV6FrtOC2bJhmk3j44NMKNyHifnWfnKnXFBE6qeaCdAVCCcbD6S8rQTmd0boRMKXQDdh2K0ZbNYVrOABa31b5dQZwsde4hdjue7vOS29DrcdhjgBEX2BeWYXwkuZY-dDJapK8roxy4dFDbMKo6e-iynXl-xgzRk-o2f_uFuixqiVTS49X-Nm-jUdb5uVgAqXMRrwTBj-dIMXr_A8f4idNXZd74KArFe9saVpGXQXRUNPUEkfsu3vsFFl-vGj3a7PXbjDT0T5RHTJNuoI67Oul3GmnzcWo4kYpTR2XRn2HOddvKmmeWHEyFFjDxP1xdCtpR65jhY15YzD1LOdsWBcaRHGoZIWpRvw9BY&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=nqa7HlF11sEvaU3hnJ0Qeg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=nqa7HlF11sEvaU3hnJ0Qeg%3D%3D",
        "https://www.linkedin.com/jobs/view/3644729803/?eBP=CwEAAAGJ9cyTPcxQuLuP9DbhYx06Q3s8V2r9cup7lkSnpIimn6MPhsRZFIL3UAFqA1Aip-zZw2GU_PH9lVHl3anu5jI7SOsR4yM4fUXEZLVdeBNr5kzDghmHInZE1xaCN59Th0dgR9uhDBvqakJ7C_pGnP6dh-6pnNRNTkp-uXibW2fidtJiSqmlS4GrmLgfFp0-gBneTZS6HtEZDP7_31X_GdJMZL-OkzDN0-AP5V2JTQ4jE3XYLlAxg0CEqN5_v3zMkWu7oAVdRE8EfvRjHTO1wpQJfvNt1wdU_JlKhk994wj79GxmyFfvZAOJHQsBdF8KWqsVqUP61s0MwfpOe_VgpTcPkomFLKBxzA4ispVbjqDCPiuVs4Ybgw0Lra3OcO9xDSBgC0o&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=fOwp7qeBGaLrEE8n8zlLAw%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=fOwp7qeBGaLrEE8n8zlLAw%3D%3D",
        "https://www.linkedin.com/jobs/view/3679561837/?eBP=JOB_SEARCH_ORGANIC&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=BmO6H7Pdgy0he1Tv7xi5SA%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=BmO6H7Pdgy0he1Tv7xi5SA%3D%3D",
        "https://www.linkedin.com/jobs/view/3681406716/?eBP=CwEAAAGJ9cyTPd1zhSZvYKSlCAf1XZkePjZnDwpUxpy_54pzoEsBa01Hnd7PUc_6UQBmBaoadInaEUpe1kbavF-I6dH0RD7Wd6BQzgX5JK-A0dsxbtF3T5Uu5_PPt5-qbhscx3HRJkhl79Id81lwZn1ADepx1237HRO2ogo4BBcUbG1V84FuwiiCiRx3WzuFc4fDMiVnDzLFyj2uoVxtVjjeSDdVIMGuocZQM6wt9_m5A2YCENXkBWP3yr3mlcHA9rtAp8Nc0VGuC_BdgRjgl9NDcH9OKMg77IAVMc0luN3fSGBlzonfOBjiWHnSx9ANXCFZT6Zc1VLaQukZ7X7AOq6nwAfxVfoKSQWrT5JJcttLQluWlCmelQnVL9uRLJ6CUkrCLHi8uf0&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=yr5UPFHxmeC9WCWT3IunBQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=yr5UPFHxmeC9WCWT3IunBQ%3D%3D",
        "https://www.linkedin.com/jobs/view/3689137531/?eBP=CwEAAAGJ9cyTPYwWibBr4bQvcFdgZbzZpOJH7z8yfjXowIc4DluetYF1mXix-HJhj7c2Rho0LZ4ld_uJWR1B3JK9osrdoHgrBVEkKGlxJW_xVGUSxNI5YQVaNuAxvSkaNzue_kiuB3OEtTiLgBbdjExQGMWhOx-Qui0M5NlG_-QywwR-raAvCiQkMyLLwG-2Z5504w0CbqUUK3JLncz87QcN2r358uhXgsZRs9ilfl5MDF2jJ-XJf-fsXHsSUEcpd6bgjukluG8XQI0h4ocBJ8LkEXggIbtBUoSknry2-e3m014s3WpNeOMkrIJVRWEidZlZ_6j9fGkNOhWQbdMV0Qef_AxeYc19RUq9MR4z4XJr-iz4sKdxKlqNBS-kyormG_o0KF-Fc-4&refId=h6qhSM1fyRKUQoL3KHiyew%3D%3D&trackingId=sQh%2FhXpVnYquP09xtPyHaQ%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3Bj%2F0DujyHRfyQKFjy2CV6Zw%3D%3D&lici=sQh%2FhXpVnYquP09xtPyHaQ%3D%3D",

        # Add more URLs here
    ]

    all_words = []

    print("Searching websites:")
    for url in tqdm(website_urls):
        words = get_qualifications(url)
        all_words.extend(words)

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
    for word, freq in sorted_word_freq.items():
        # if freq <= 2:
        #     continue
        # else:
            lowercase_word = word.lower()  # Convert the word to lowercase
            if lowercase_word in common_single_words_lower:
                print(f"{word}: {freq}")

    print("\nMost common skills in a requirements section for software engineers:")    
    for word, freq in sorted_word_freq.items():
        # if freq <= 2:
        #     continue
        # else:
            lowercase_word = word.lower()  # Convert the word to lowercase
            if lowercase_word in filtered_lower:
                print(f"{word}: {freq}")
    