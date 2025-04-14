
# simple_web_scraper.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_jobs():
    url = 'https://vacancymail.co.zw/jobs/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    jobs = []
    job_cards = soup.find_all('div', class_='job-title-box')[:10]

    for job in job_cards:
        try:
            title = job.find('a', class_='job-title').text.strip()
            company = job.find('div', class_='job-desc').find('b').text.strip()
            location = job.find('div', class_='location').text.strip()
            expiry = job.find('span', class_='expiry-date').text.strip() if job.find('span', class_='expiry-date') else 'N/A'

            job_data = {
                'Job Title': title,
                'Company': company,
                'Location': location,
                'Expiry Date': expiry
            }

            jobs.append(job_data)
        except Exception as e:
            print(f"Error parsing job: {e}")

    df = pd.DataFrame(jobs)
    df.to_csv('scraped_data.csv', index=False)
    print("Jobs saved to scraped_data.csv")

if __name__ == '__main__':
    fetch_jobs()




