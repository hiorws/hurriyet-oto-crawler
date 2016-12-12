# -*- coding: utf-8 -*-
from crawl_multiple_adverts import *
from crawl_single_advert import *
from tqdm import tqdm
import csv

if __name__ == "__main__":
    model_list_source = get_model_list_source()
    model_advert_list = get_model_advert_list_urls(model_list_source)
    all_urls = []

    with open("sample_output.csv", "w") as output_file:
        writer = csv.writer(output_file)
        label_row = ["İlan no", "Marka", "Model", "Seri", "Fiyat", "Model Yılı", "Kasa Tipi", "Vites Tipi", "Renk",
                     "Garanti", "İlan Tarihi", "Kilometre", "Yakıt Tipi", "Kapı Sayısı"]
        writer.writerow(label_row)

    for url in tqdm(model_advert_list[:10]):
        advert_urls = get_advert_urls(url)
        all_urls.extend(advert_urls)
        output_list = list()
        for model_url in all_urls:
            page_source = get_page_source(model_url)
            advert_details = get_advert_details(page_source)
            output_list.append(advert_details)
            with open("sample_output.csv", "w") as output_file:
                writer = csv.writer(output_file)

                for advert in output_list:
                    output = [advert["ilan_no"], advert["marka"], advert["model"], advert["seri"], advert["fiyat"],
                              advert["model_yili"], advert["kasa_tipi"], advert["vites_tipi"], advert["renk"], advert["garanti"],
                              advert["ilan_tarihi"], advert["km"], advert["yakit_tipi"], "kapısayısı"]

                    writer.writerow(output)

