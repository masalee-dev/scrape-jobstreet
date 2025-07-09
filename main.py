import requests
from bs4 import BeautifulSoup

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
    joblist = soup.find('div', class_='ube6hn0 _21bfxf1')
    # print(joblist.prettify())

    jobdata = []

    for articel in joblist.find_all('article', {'class':'ube6hn0 ube6hn1 wc8kxl93 wc8kxl8o wc8kxl7z wc8kxl7k wc8kxlbb wc8kxlaw wc8kxla7 wc8kxl9s wc8kxlh wc8kxl67 wc8kxl5f czgzl0b czgzl09 czgzl0a m81yar10 m81yar13 wc8kxl33 wc8kxl36'}):
        position = articel.find('div', {'class':'ube6hn0 wc8kxl5h wc8kxl53'})
        company = articel.find(attrs={'data-automation':'jobCompany'})
        location = articel.find(attrs={'data-automation':'jobLocation'})
        salary = articel.find('span', {'class':'ube6hn0 wc8kxl4z wc8kxlr m81yar0 m81yar1 m81yar1t m81yar6 _1lwlriv4 _1aaa7yq0'})
        time = articel.find('span', {'class':'ube6hn0 wc8kxl4z m81yar0 m81yar1 m81yar1u m81yar6 _1lwlriv4'})

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




if __name__ == '__main__':
    get_all_items()
