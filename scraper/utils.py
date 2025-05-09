import csv
import os

def save_csv(comments_data, filename="comments.csv"):
    """
    Saves a list of dicts (with keys 'author', 'time', 'text') to scraper/data/filename.
    Creates the data folder if it doesn't exist.
    """
    root_dir = os.path.dirname(os.path.abspath(__file__))     
    data_dir = os.path.join(root_dir, "data")
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, filename)

    with open(file_path, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["author", "time", "text"])
        writer.writeheader()
        writer.writerows(comments_data)

    print(f"Comments saved to {file_path}")
    return file_path
