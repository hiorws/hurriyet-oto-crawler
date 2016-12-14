import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()


def get_page_source(product_url):
    """
    a simple function which returns page source as string
    :param product_url:
    :return page_source:
    """
    page_source = requests.get(url=product_url)
    return page_source.text


def get_advert_details(advert_page_source):
    """
        takes source code of a product page and return it's information as a dictionary

        :param advert_page_source:
        :return product(dict):
        """
    bs = BeautifulSoup(advert_page_source, "html.parser")

    advert_creds = dict()

    # ilan no
    advert_div = bs.find(class_="ilanNo")
    advert_no = advert_div.find("strong").get_text()
    advert_no = str(advert_no).strip()

    advert_creds['ilan_no'] = advert_no

    # marka model
    brand_a = bs.find("a", {"id": "ContentPlaceHolder1_lnkBrand"})
    brand = brand_a.text
    model_a = bs.find("a", {"id": "ContentPlaceHolder1_lnkModel"})
    model = model_a.text
    seri_a = bs.find("a", {"id": "ContentPlaceHolder1_lnkSeries"})
    seri = seri_a.text
    # brand_div = bs.find(class_="detay_markaTip")
    # brand = brand_div.findAll("dd")[0]
    # brand = brand.get_text().encode("utf-8")
    # brand = str(brand).decode('unicode_escape').encode('ascii', 'ignore')
    # brand = brand.split(":")[-1]
    # print(brand)

    # advert_creds['marka_model'] = brand
    advert_creds['marka'] = brand
    advert_creds['model'] = model
    advert_creds['seri'] = seri

    # fiyat
    price_div = bs.find(class_="fiyat_isim")
    price = price_div.find("strong", id="ContentPlaceHolder1_lblPrice").get_text()
    price = str(price).replace(".", "")

    advert_creds['fiyat'] = price

    # ilan detay sol
    advert_detail_div = bs.find(class_="sol")
    detail_value = advert_detail_div.findAll("dd")

    # detail_key = advert_detail_div.findAll("dt")

    # zippo = zip(detail_key, detail_value)
    #
    # for k, v in zippo:
    #     # print(k.get_text(), v.get_text())
    #     pass

    # model yili
    model_year = detail_value[0].get_text()
    model_year = str(model_year)[-4:].strip()

    advert_creds['model_yili'] = model_year

    # kasa tipi
    case_type = detail_value[1].get_text()
    # case_type = str(case_type).decode('unicode_escape').encode('ascii', 'ignore')
    case_type = case_type.split(":")[-1]

    advert_creds['kasa_tipi'] = case_type

    # vites tipi
    gear_type = detail_value[2].get_text()
    # gear_type = str(gear_type).decode('unicode_escape').encode('ascii', 'ignore')
    gear_type = gear_type.split(":")[-1]

    advert_creds['vites_tipi'] = gear_type

    # renk
    color = detail_value[3].get_text()
    # color = str(color).decode('unicode_escape').encode('ascii', 'ignore')
    color = color.split(":")[-1]

    advert_creds['renk'] = color

    # garanti
    guarantee = detail_value[7].get_text()
    # guarantee = str(guarantee).decode('unicode_escape').encode('ascii', 'ignore')
    guarantee = guarantee.split(":")[-1]

    if guarantee.startswith("H"):
        advert_creds['garanti'] = "Hayır"
    else:
        advert_creds['garanti'] = "Evet"

    # ilan tarihi
    advert_date = detail_value[9].get_text()
    # advert_date = str(advert_date).decode('unicode_escape').encode('ascii', 'ignore')
    advert_date = advert_date.split(":")[-1]
    advert_date = advert_date.replace(".", "/")

    advert_creds['ilan_tarihi'] = advert_date

    # ilan detay sag
    advert_detail_div = bs.find(class_="sag")
    detail_value = advert_detail_div.findAll("dd")

    # KM
    kilometer = detail_value[0].get_text()
    # kilometer = str(kilometer).decode('unicode_escape').encode('ascii', 'ignore')
    kilometer = kilometer.split(":")[-1].split(" km")[0]
    kilometer = str(kilometer).replace(".", "")

    advert_creds['km'] = kilometer

    # yakit tipi
    fuel_type = detail_value[1].get_text()
    # fuel_type = str(fuel_type).decode('unicode_escape').encode('ascii', 'ignore')
    fuel_type = fuel_type.split(":")[-1]

    advert_creds['yakit_tipi'] = fuel_type

    # kapi sayisi
    door_count = detail_value[2].get_text()
    # door_count = str(door_count).decode('unicode_escape').encode('ascii', 'ignore')
    door_count = door_count.split(":")[-1]

    advert_creds['kapi_sayisi'] = door_count

    return advert_creds


if __name__ == "__main__":
    # sample url
    sample_url = "http://www.hurriyetoto.com/ticari-arac/ilan-detay/331074/sahibinden-fiat-doblo-combi-16-105-hp-multijet-euro-4-premio-izmir-bornova"
    sample_page_source = get_page_source(sample_url)
    sample_advert_details = get_advert_details(sample_page_source)
    for k, v in sample_advert_details.items():
        print(k, v)

    # print sample_advert_details['garanti']
    # print(sample_advert_details)
    # print(sample_page_source)
