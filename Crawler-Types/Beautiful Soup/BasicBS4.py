import requests
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=Software-Developer&where=San-Francisco__2C-CA"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
results = soup.find(id = "ResultsContainer")

job_elems = results.find_all('section', class_= "card-content")
# for job_elem in job_elems:
#     title = job_elem.find('h2', class_= "title")
#     company = job_elem.find('div', class_= "company")
#     location = job_elem.find('div', class_= "location")
#     if title is not None and company is not None and location is not None:
#         print(title.text.strip())
#         print(company.text.strip())
#         print(location.text.strip())
software_jobs = results.find_all('h2', string=lambda text: 'software engineer' in text.lower())
for job in software_jobs:
    link_refs = job.find('a')['href']
    print(link_refs)
