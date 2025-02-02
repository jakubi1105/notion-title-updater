import requests
import datetime


NOTION_TOKEN = "ntn_pp7219770194Mau5Da7odbuho5DO93C2xP6rQ2EY9iK0yp"
PAGE_ID = "81884ae2fd854a9bb4f048c25c0954f8"

heute = datetime.datetime.now().strftime("%Y-%m-%d")

# API-Header
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# API-Request-Daten zum Updaten der Überschrift
data = {
    "properties": {
        "title": {
            "title": [
                {"text": {"content": heute}}
            ]
        }
    }
}

# API-Request senden (PATCH statt POST, da wir eine bestehende Seite ändern)
url = f"https://api.notion.com/v1/pages/{PAGE_ID}"
response = requests.patch(url, headers=headers, json=data)

# Antwort ausgeben
if response.status_code == 200:
    print("Überschrift erfolgreich aktualisiert!")
else:
    print("Fehler:", response.text)