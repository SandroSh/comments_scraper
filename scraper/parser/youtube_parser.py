def youtube_get_comments(driver, video_url, timeout=10, max_scrolls=2):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    driver.get(video_url)
    time.sleep(5)  
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#comments"))
        )

        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        scrolls = 0
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        while scrolls < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(7) 

            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                print("Reached end of page or no more new comments loaded.")
                break
            last_height = new_height
            scrolls += 1

        comment_threads = driver.find_elements(By.TAG_NAME, "ytd-comment-thread-renderer")
        print(f"Found {len(comment_threads)} comment threads.")

        comments_data = []

        for thread in comment_threads:
            try:
                author = thread.find_element(By.CSS_SELECTOR, "a#author-text").text.strip()
            except:
                author = "N/A"

            try:
                content_element = thread.find_element(By.CSS_SELECTOR, "yt-attributed-string#content-text")
                spans = content_element.find_elements(By.CSS_SELECTOR, "span")
                text = " ".join([span.text.strip() for span in spans if span.text.strip()])
                if not text:
                    text = content_element.text.strip()
            except:
                text = "N/A"

            try:
                time_ago = thread.find_element(By.CSS_SELECTOR, "span#published-time-text").text.strip()
            except:
                time_ago = "N/A"

            comments_data.append({
                "author": author,
                "text": text,
                "time": time_ago
            })

        print(f"Collected {len(comments_data)} comments.")

        for c in comments_data:
            print(f"[{c['author']}] ({c['time']}): {c['text']}")

        return comments_data

    except Exception as e:
        print(f"Error while loading or locating comments: {e}")
        return []
