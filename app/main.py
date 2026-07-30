
def create_report(data_file_name: str, report_file_name: str) -> None:
    # On initialise avec 0 pour éviter un KeyError si une opération manque
    totals = {"supply": 0, "buy": 0}

    # 1. Lecture des données
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:  # On ignore les lignes vides
                operation, amount = line.split(",")
                # On additionne à la catégorie correspondante (supply ou buy)
                totals[operation] = totals.get(operation, 0) + int(amount)

    # 2. Calcul du résultat
    result = totals["supply"] - totals["buy"]

    # 3. Écriture du rapport dans le BON fichier
    with open(report_file_name, "w") as report_file:
        # L'ordre des lignes est crucial pour les tests
        report_file.write(f"supply,{totals['supply']}\n")
        report_file.write(f"buy,{totals['buy']}\n")
        report_file.write(f"result,{result}\n")
