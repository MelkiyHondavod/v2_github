import requests

headers = {
    'authority': 'api.av.by',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://av.by',
    'referer': 'https://av.by/',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-api-key': '5f76cde7ebefc9.04631320',
    'x-device-type': 'web.desktop',
}

response = requests.get('https://api.av.by/home/filters/home/init', headers=headers)