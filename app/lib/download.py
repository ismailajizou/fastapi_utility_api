import requests

def download(url, filename):
  response = requests.get(url, stream=True)
  response.raise_for_status()  # Raise an exception for bad status codes

  with open(filename, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
      f.write(chunk)