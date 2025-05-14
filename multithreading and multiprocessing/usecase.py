import threading
from bs4 import BeautifulSoup
import requests

urls=[
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/concepts/',
'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print((f'Fetched {len(soup.text)} characters from {url}'))

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print('All threads have finished execution.')