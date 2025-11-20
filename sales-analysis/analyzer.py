import pandas as pd
from helpers import calcualte_total, format_currency

# Odczytanie danych
df = pd.read_csv("data/sales.csv")

# Obliczenie sumy dla kazdego z wierszy
totals = []
for index, row in df.iterrows():
    total = calcualte_total(row["quantity"], row["price"])
    totals.append(total)

# Dodaj sume do naszych danych
df["total"] = totals

# Wyświetl z sformatowaną zmienną `totals`
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row["total"])
    print(f"{row['product']}: {formatted_total}")

# Pokaz cała sume
grand_total = df["total"].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\nGrand Total: {formatted_grand_total}")
