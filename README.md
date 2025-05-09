# Social Media Scraper

A modular web scraping tool built with Selenium to extract public comments from YouTube videos and save them as structured CSV files.

---

## Features

- Extracts YouTube comment data:
  - Author name
  - Comment text (including emojis and nested spans)
  - Timestamp
- Scrolls to load more comments
- Saves to CSV in a clean `data/` folder
- Modular design for easy reuse and extension

---
## Installation

1. Clone the repository:
```bash
git https://github.com/SandroSh/social_media_scraper.git
cd social_media_scraper
```

2. Install required packages:
```bash
pip install -r requirements.txt
```
