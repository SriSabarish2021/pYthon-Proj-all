import requests
from bs4 import BeautifulSoup

get_data=requests.get('https://dev.to/rodcast/asyncawait-understanding-javascript-api-requests-and-responses-in-the-data-fetching-lifecycle-7o8')


soup = BeautifulSoup(get_data.text, "html.parser")
print(soup.title.text)