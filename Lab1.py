import urllib2
import pandas as pd
import os
from time import strftime
import numpy as np


total_df = pd.DataFrame()

# загружает один файл по id
def get_csv_by_district(n):
    if n < 1 or n > 27 :
        print('Invalid argument!')
    else:
        url = '''http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R{0}.txt'''.format(str(n).zfill(2))
        vhi_url = urllib.request.urlopen(url)
        out = open('vhi_id_{0}_{1}.csv'.format(n,strftime('%Y-%m-%d_%Hh%Mm%Ss')), 'wb')
        out.write(vhi_url.read())
        out.close()
        print('VHI is downloaded...')
        
# загружает в директорию
def collect_all(path=r"data"):
    try:
        os.mkdir(path)
    except OSError:
        path = path + strftime('%Y%m%d_%H%M%S')
        os.mkdir(path)
    finally:
        d_id = [x for x in range(27) if ((x != 0)&(x != 12)&(x != 19))]
        for i in d_id:
            collect_data(i, path)
        print("downloaded to " + "path")
    return path        
    
# генериюет файлы с директории и меняет индексы
def merge(path=r"data"):
    filelist = os.listdir(path=path)
    distr = ['''Cherkasy''', '''Chernihiv''', '''Chernivtsi''', '''Crimea''', '''Dnipropetrovs'k''', '''Donetsk''',
             '''Ivano-Frankivs'k''', '''Kharkiv''', '''Kherson''', '''Khmel'nyts'kyy''', '''Kiev''', '''Kiev City''',
             '''Luhans'k''', '''Lviv''', '''Mykolayiv''', '''Odessa''', '''Poltava''', '''Rivne''', '''Sevastopol''',
             '''Sumy''', '''Ternopil''', '''Transcarpathia''', '''Vinnytsya''', '''Volyn''', '''Zaporizhzhya''',
             '''Zhytomyr''']
    d_id = [x for x in range(27) if ((x != 0)&(x != 12)&(x != 19))]
    new_id = [22, 24, 23, 25, 3, 4, 8, 19, 20, 21, 9, 11, 12, 13, 14, 15, 16, 17, 18, 6, 1, 2, 7, 5]
    

def get_retrieval(region, year=None):
    curr_df = total_df.ix[region]
    if year == None:
        return curr_df
    else:
        return curr_df[curr_df['year'] == year]


def get_VHI_analisys_region(region, area_percent):
    retrieval = get_retrieval(region)[['year', 'VHI', '%Area_VHI_LESS_15', '%Area_VHI_LESS_35']]

    retrieval = retrieval.drop(list(retrieval[retrieval['VHI'] == -1].index))
    newret_15 = retrieval[(retrieval['VHI'] < 15.0) & (retrieval['%Area_VHI_LESS_15'] > area_percent)]
    newret_35 = retrieval[(retrieval['VHI'] < 35.0) & (retrieval['VHI'] > 15.0) & (retrieval['%Area_VHI_LESS_35'] > area_percent)]
    return newret_15, newret_35



def get_VHI_min_max(region, year):
    retreival = get_retrieval(region, year)
    return retreival['VHI'].max(), retreival['VHI'].min()






