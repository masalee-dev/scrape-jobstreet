import requests
from bs4 import BeautifulSoup
import os
import json
import pandas as pd


url = ("https://id.jobstreet.com/id/Software-Engineer-jobs-in-information-communication-technology/in-Jakarta-Raya")

headers = {'User Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}

s = requests.session()
s.headers.update(headers)

page = s.get(url)

if page.status_code == 200:
    print('Request succeed')
else:
    print(f'Request failed with status code: {page.status_code}')

def get_all_items():
    soup = BeautifulSoup(page.text, 'html.parser')
    joblist = soup.find('div', class_='_17fz4760 _21bfxf1')
    # print(joblist.prettify())

    # scraping data process
    jobdata = []

    for article in joblist.find_all('article', {'class':'_17fz4760 _17fz4761 _16os2sm98 _16os2sm8t _16os2sm84 _16os2sm7p _16os2smbg _16os2smb1 _16os2smac _16os2sm9x _16os2smi _16os2sm6c _16os2sm5g _763n8yb _763n8y9 _763n8ya _817f7q10 _817f7q13 _16os2sm34 _16os2sm37'}):
        position = article.find('div', {'class':'_17fz4760 _16os2sm5i _16os2sm54'})
        company = article.find(attrs={'data-automation':'jobCompany'})
        location = article.find(attrs={'data-automation':'jobLocation'})
        salary = article.find('span', {'class':'_17fz4760 _1uvdxrr2 _16os2sm50 _16os2sm0 _16os2sms _1uvdxrr4'})
        time = article.find(attrs={'data-automation':'jobListingDate'})

        position_text = position.get_text() if position else "Position not found"
        company_text = company.get_text() if company else 'Company not found'
        location_text = location.get_text() if location else 'Location not found'
        salary_text = salary.get_text() if salary else 'Salary not found'
        time_text = time.get_text() if time else 'Time not found'

        print(position_text)
        print(company_text)
        print(location_text)
        print(salary_text)
        print(time_text)
        print("============================================")

        jobdata.append({
            'Postions': position_text,
            'Company': company_text,
            'Location': location_text,
            'Salary': salary_text,
            'Time apply' : time_text
        })

    # writing JSON file
    try:
        os.mkdir('json-result')
    except FileExistsError:
        pass

    with open('json-result/joblist.json', 'w+') as json_data:
        json.dump(jobdata, json_data)
    print('json created')

    # create CSV file and Excel
    df = pd.DataFrame(jobdata)
    df.to_csv('scarping-data-Jobstreet.csv', index=False)
    df.to_excel('scraping-data-Jobstreet.xlsx', index=False)

    print('Data success created')





if __name__ == '__main__':
    get_all_items()
