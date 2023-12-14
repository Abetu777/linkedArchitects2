import pandas as pd
import requests
import re
from getArchtects import archDf, archList

# Load your data, assuming archDf and archList are already defined

# Function to get related architects
def getRerativArchitects(word: str):
    url = "https://ja.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": word,
        "format": "json",
        "prop": "wikitext"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for HTTP errors

        data = response.json()
        if 'parse' not in data:
            print(f"キー 'parse' が見つかりませんでした。", word)
            return []

        content = data['parse'].get('wikitext', {}).get('*', '')

        matches = re.findall(r'\[\[(.*?)\]\]', content)
        rerativList = [match for match in matches if match in archList]
        print(word)
        return rerativList

    except requests.exceptions.Timeout as e:
        print(f"Timeout occurred for '{word}': {e}")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Request failed for '{word}': {e}")
        return []

# Loop through archList
for word in archList:
    rerativList = getRerativArchitects(word)
    for match in rerativList:
        if match not in archDf.columns:
            print(f"Column '{match}' not found in DataFrame.")
            continue
        else:
            # Directly modify the DataFrame to avoid SettingWithCopyWarning
            archDf.loc[word, match] += 1

archDf.to_csv('mapArchitects2.csv')
