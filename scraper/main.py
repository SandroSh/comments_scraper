from driver import browser_driver
from parser.youtube_parser import youtube_get_comments




driver = browser_driver()
video_url = "https://www.youtube.com/watch?v=zvpmomFpjUw"
comments = youtube_get_comments(driver, video_url)

print(f"Collected {len(comments)} comments.")
driver.quit()