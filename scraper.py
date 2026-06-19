import requests
from bs4 import BeautifulSoup
import csv
import json

URL = "https://realpython.github.io/fake-jobs/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for card in soup.find_all("div", class_="card-content"):
    title = card.find("h2").get_text(strip=True)
    company = card.find("h3").get_text(strip=True)
    location = card.find("p", class_="location").get_text(strip=True)

    jobs.append({
        "job_title": title,
        "company": company,
        "location": location
    })

with open("jobs.json", "w", encoding="utf-8") as f:
    json.dump(jobs, f, indent=4)

with open("jobs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["job_title", "company", "location"])
    writer.writeheader()
    writer.writerows(jobs)

print(f"Saved {len(jobs)} jobs to CSV and JSON.")
