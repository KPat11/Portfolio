from exa_py import Exa # type: ignore

#please add your generated api key from exa's website
exa = Exa('API KEY')

#basic input function to obtain query
query = input('Search here: ')

#taking input data and passing it through our search result parameters -- I took off instagram due to inconsistent results
response = exa.search(query, num_results=3, type='keyword', include_domains=['https://www.tiktok.com', 'https://www.x.com', 'https://www.pinterest.com'])

#Formatting terminal outputs for readability
for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()

