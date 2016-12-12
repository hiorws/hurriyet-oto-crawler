# -*- coding: utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup
import re


def get_model_list_source():
    """
    a simple function which returns "tüm markalar" page source as string
    :return page_source:
    """

    url = "http://www.hurriyetoto.com/tum-markalar/"
    main_page_rq = rq.get(url=url)
    return main_page_rq.content


def get_model_advert_list_urls(model_list_source):
    """
    a function that fetches model specific advert list pages from list
    :param model_list_source:
    :return:
    """
    origin_url = "http://www.hurriyetoto.com"
    main_page_soup = BeautifulSoup(model_list_source, "html.parser")
    model_urls = []
    search_pattern = re.compile("ContentPlaceHolder1_rptBrand_lstModel_\\d*_lnkModel_")
    model_links = main_page_soup.find_all(id=search_pattern)
    for link in model_links:
        model_url = origin_url + link.get("href")
        model_urls.append(model_url)

    return model_urls


def get_advert_urls(model_url):
    """
    a function that fetches advert pages from model specific advert list pages
    :param model_url:
    :return:
    """
    model_url_ = model_url
    origin_url = "http://www.hurriyetoto.com"
    advert_urls = []
    search_pattern = re.compile("^ContentPlaceHolder1_SearchLister_rptResults_hlTitleToDetail_")
    while True:
        model_page = rq.get(model_url_)
        model_page_source = model_page.content
        model_page_soup = BeautifulSoup(model_page_source, "html.parser")
        next_page = model_page_soup.find("a", {"id": "ContentPlaceHolder1_SearchLister_hlNextPage"})
        advert_a_tags = model_page_soup.find_all(id=search_pattern)
        for advert_tag in advert_a_tags:
            advert_url = origin_url + advert_tag.get("href")
            advert_urls.append(advert_url)
        if next_page is not None:
            model_url_ = origin_url + next_page.get("href")
        else:
            break
    return advert_urls

if __name__ == "__main__":
    model_list_source = get_model_list_source()
    model_advert_list = get_model_advert_list_urls(model_list_source)
    all_urls = []
    for url in model_advert_list:
        advert_urls = get_advert_urls(url)
        all_urls.extend(advert_urls)
        print(len(all_urls))