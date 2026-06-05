from pathlib import Path
import pandas as pd

repo_root = Path(__file__).resolve().parent.parent
csv_path = repo_root / "lookup" / "urls2.txt"

df = pd.read_csv(csv_path, header=None, names=["url"])

df = df.astype({"url": str})

url_counts = df["url"].value_counts()

max_url = url_counts.idxmax()
max_count = url_counts.max()
print(f"Most frequent URL: {max_url}")
print(f"Occurrence count: {max_count}")