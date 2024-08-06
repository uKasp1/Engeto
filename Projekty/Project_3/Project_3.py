"""
Projekt_3.py: druhý projekt do Engeto Online Python Akademie
author: Jan Kašpárek
email: jan.kasparek96@gmail.com
discord: jankasparek0720
"""

import requests
from bs4 import BeautifulSoup
import argparse
import csv


def arguments_parse():
    parse_arg = argparse.ArgumentParser(description="URL input")
    parse_arg.add_argument("web", metavar="web", type=str, help="Enter url")
    parse_arg.add_argument("file_name", metavar="file_name", type=str, help="Enter file name")
    args = parse_arg.parse_args()
    web = args.web
    file_name = args.file_name
    return web , file_name

def row_atr(tr_tag):
    return {
        "Number": tr_tag[0].getText(),
        "Name": tr_tag[1].getText(),
    }

def row_atr_table_region(tr_tag):
    return {
    "Voters in the list": tr_tag[3].getText(),
    "Issued envelopes": tr_tag[4].getText(),
    "Valid votes": tr_tag[7].getText(),
}

def row_atr_table_parties(tr_tag):
    return {
    tr_tag[1].getText():tr_tag[2].getText(),    
}

def url_soup():
    web, _ = arguments_parse()
    url_response = requests.get(web) #gets url 
    soup = BeautifulSoup(url_response.text, 'html.parser') #def of soup
    container = soup.find("div", {"id": "container"}) #taking all web container
    tr_all = container.find_all("tr") # from it find all "tr" attributes
    return tr_all

def tr_area():
    list_links = []
    list_area = []

    for tr in url_soup():
        td_row = tr.find_all("td")
        td_number = tr.find_all("td",{"class": "cislo"}) # find all "td" in every "tr" 
        if td_number:
            data = row_atr(td_row) # from every td take define tags 
            list_area.append(data) # append data to list
            find_a = td_row[0].find("a") # in first "td", find attribute "a"
            if find_a == None:
                continue
            else:
                href = td_row[0].find("a")["href"] # find a "href", link to next page with additional data
            list_links.append("https://volby.cz/pls/ps2017nss/"+href) # merge the link with prefix to list
    return list_area, list_links

def links_url():
    _ , list_links = tr_area()
    list_data = []
    
    for url_r in list_links: 
        dict_data = {} 

        url_r_response = requests.get(url_r) #gets url 
        soup1 = BeautifulSoup(url_r_response.text, 'html.parser') #def of soup
        container = soup1.find("div", {"id": "container"}) #taking all web container
        all_tr = container.find_all("tr") # from it find all "tr" attributes
            
        def tr_region():
            for data in all_tr[2:3]:
                td_row_region = data.find_all("td") # find all "td" in every "tr" 
                data_region = row_atr_table_region(td_row_region) # from every td take define tags 
                for key in data_region:
                    value = data_region.get(key)
                    value = value.replace("\xa0","").strip()
                    dict_data.update({key:value})
        tr_region()
            
        def tr_party():
            for tr_parties in all_tr[3:]:
                td_row_parties = tr_parties.find_all("td") # find all "td" in every "tr"
                td_number = tr_parties.find_all("td",{"class": "cislo"}) 
                if td_number:
                    data_parties = row_atr_table_parties(td_row_parties) # from every td take define tags
                    dict_data.update(data_parties)
            list_data.append(dict_data)
        tr_party()

    return list_data       

def append_data():

    list_area, _  = tr_area()
    list_data = links_url()
    full_list = []
    
    for i, j in zip(list_area, list_data):
        combine_dict = {**i, **j}
        full_list.append(combine_dict)
    return full_list   
        
def create_excell():
    web, file_name = arguments_parse()
    full_list = append_data()
    
    csv_filename = file_name
    field_names = full_list[0].keys()

    with open(csv_filename, "w", newline='', encoding="utf-8-sig") as new_csv_file:
        writer = csv.DictWriter(new_csv_file, fieldnames=field_names, delimiter=";")
        writer.writeheader()
        writer.writerows(full_list)
    print("-"*50)
    print("Data scraped from: ", web, "And saved to:" , csv_filename)
    print("Program closed!")
    print("-"*50)
create_excell()
