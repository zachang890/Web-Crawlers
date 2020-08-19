import requests
from bs4 import BeautifulSoup

def acquireRecentNews(url):
    def timesAcquire(search_results, param):
        val = search_results.find_all('time', string=lambda text: param in text.lower())
        l = [time.text for time in val]
        return l, val

    source = requests.get(url)
    soup = BeautifulSoup(source.content, 'html.parser') #create the actual object

    search_results = soup.find('div', class_="lBwEZb BL5WZb xP6mwf")
    time_dict = {}
    time_list = ['minutes', 'hour', 'yesterday', 'days']
    iterate = 0
    while len(time_dict) < 3 and iterate < 4:
        times_addition, soup_obj_addition = timesAcquire(search_results, time_list[iterate])
        for entry, soup_obj in zip(times_addition, soup_obj_addition):
            time_dict[entry] = soup_obj
            if len(time_dict) == 3:
                break
        iterate += 1
    article_link = {}
    time_source = {}
    for key in time_dict:
        header = time_dict[key].find_parent('div').find_parent('div').find_previous_sibling('h3')
        a_ref = header.find('a')
        article_link[a_ref.text] = "news.google.com" + a_ref['href'][1:]
        news_source = time_dict[key].find_parent('div').find('a').text
        time_source[key] = news_source
    return article_link, time_source


d, t = acquireRecentNews("https://news.google.com/search?q=water%20crisis&hl=en-US&gl=US&ceid=US%3Aen")
for key, entry in zip(d.keys(), t.keys()):
    print(key)
    print(d[key])
    print(t[entry])
    print(entry)
    print('\n')