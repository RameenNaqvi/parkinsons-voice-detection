import urllib.request
import os

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/parkinsons/parkinsons.data"
save_path = "data/parkinsons.csv"

print("Downloading dataset...")
urllib.request.urlretrieve(url, save_path)
print("Done! Dataset saved to data folder")
