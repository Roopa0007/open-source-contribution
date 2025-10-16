import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.covid19api.com/summary"
data = requests.get(url).json()

countries = [c["Country"] for c in data["Countries"]]
cases = [c["TotalConfirmed"] for c in data["Countries"]]

df = pd.DataFrame({"Country": countries, "Cases": cases})
top10 = df.sort_values(by="Cases", ascending=False).head(10)

plt.figure(figsize=(8,5))
plt.bar(top10["Country"], top10["Cases"], color='purple')
plt.title("Top 10 Countries - COVID Cases")
plt.xlabel("Country")
plt.ylabel("Total Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
