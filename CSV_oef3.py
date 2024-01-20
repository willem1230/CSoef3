import csv

datum = []
product = []
hoeveelheid = []
verkoopwaarde = []

with open('winkelverkocht.csv', 'r', newline="") as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        #datum.append(str(row["Datum"]))
        product.append(str(row["Product"]))
        hoeveelheid.append(float(row["Hoeveelheid"]))
        verkoopwaarde.append(float(row["Verkoopwaarde"]))

print("de totale verkoopwaarde is:", sum(verkoopwaarde))

aantal_a = [i for i, n in enumerate(product) if n == "Product A"]
aantal_b = [i for i, n in enumerate(product) if n == "Product B"]
aantal_c = [i for i, n in enumerate(product) if n == "Product C"]


totale_verkoopwaarde_a = sum([verkoopwaarde[i] for i in aantal_a])
totale_verkoopwaarde_b = sum([verkoopwaarde[i] for i in aantal_b])
totale_verkoopwaarde_c = sum([verkoopwaarde[i] for i in aantal_c])

totale_verkoopwarde_product = ["Product A", "Product B", "Product C"]
totale_verkoopwaarde = [totale_verkoopwaarde_a, totale_verkoopwaarde_b, totale_verkoopwaarde_c]

totale_verkoopwaarde_index = totale_verkoopwaarde.index(max(totale_verkoopwaarde))

print("het totaal verkochte product a:", totale_verkoopwaarde_a, "b:", totale_verkoopwaarde_b, "c:", totale_verkoopwaarde_c)
print("Het best verkochte product is:", totale_verkoopwarde_product[totale_verkoopwaarde_index])


print("de hoogste verkoopdag is index:", verkoopwaarde.index(max(verkoopwaarde)))

gemiddelde_verkoopwaarde_per_dag = sum(verkoopwaarde) / len(verkoopwaarde)
print("het gemiddelde verkoopwaarde is:", gemiddelde_verkoopwaarde_per_dag )

