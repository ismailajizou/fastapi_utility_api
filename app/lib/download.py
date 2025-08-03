import requests

def download(url: str, filename: str) -> bool:
  try:
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an exception for bad status codes

    with open(filename, 'wb') as f:
      for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
      return True
  except requests.exceptions.RequestException as e:
    return False