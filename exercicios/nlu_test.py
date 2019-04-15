import requests

data = {
  'language': 'en',
  'text': 'me sinto solitário',
}

headers = { 'Authorization': 'Bearer 1e3f6cdf-427f-4f03-932d-aea60297f524' }
r = requests.post('https://nlp.bothub.it/parse/', headers=headers, data=data)
print(r.json())