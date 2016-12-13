# -*- coding: utf-8 -*-
from crawl_multiple_adverts import *
from crawl_single_advert import *
from tqdm import tqdm
import csv

if __name__ == "__main__":
    model_list_source = get_model_list_source()
    model_advert_list = get_model_advert_list_urls(model_list_source)

    with open("sample_output.csv", "w") as output_file:
        writer = csv.writer(output_file)
        label_row = ["İlan no", "Marka", "Model", "Seri", "Fiyat", "Model Yılı", "Kasa Tipi", "Vites Tipi", "Renk",
                     "Garanti", "İlan Tarihi", "Kilometre", "Yakıt Tipi", "Kapı Sayısı"]
        writer.writerow(label_row)

    output_list = list()
    for url in tqdm(model_advert_list):
        advert_urls = get_advert_urls(url)
        for model_url in advert_urls:
            page_source = get_page_source(model_url)
            advert = get_advert_details(page_source)
            output = [advert["ilan_no"], advert["marka"], advert["model"], advert["seri"], advert["fiyat"],
                      advert["model_yili"], advert["kasa_tipi"], advert["vites_tipi"], advert["renk"],
                      advert["garanti"],
                      advert["ilan_tarihi"], advert["km"], advert["yakit_tipi"], advert["kapi_sayisi"]]
            with open("sample_output.csv", "a") as output_file:
                writer = csv.writer(output_file)
                writer.writerow(output)

    # with open("sample_output.csv", "a") as output_file:
    #     writer = csv.writer(output_file)
    #
    #     for advert in output_list:
    #         output = [advert["ilan_no"], advert["marka"], advert["model"], advert["seri"], advert["fiyat"],
    #                   advert["model_yili"], advert["kasa_tipi"], advert["vites_tipi"], advert["renk"],
    #                   advert["garanti"],
    #                   advert["ilan_tarihi"], advert["km"], advert["yakit_tipi"], advert"kapi_sayisi"]
    #
    #         writer.writerow(output)

