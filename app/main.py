def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    print(f"📥 Otwieram plik wejściowy: {data_file_name}")
    with open(data_file_name, "r") as file:
        for line in file:
            print(f"🔹 Odczytana linia: '{line.strip()}'")
            line = line.strip()
            if not line:
                print("⏭️ Pusta linia, pomijam")
                continue

            operation, amount = line.split(",")
            amount = int(amount)
            print(f"➡️ Operacja: {operation}, Ilość: {amount}")

            if operation == "supply":
                supply_total += amount
                print(f"📦 Dodano do supply: {supply_total}")
            elif operation == "buy":
                buy_total += amount
                print(f"🛒 Dodano do buy: {buy_total}")

    result = supply_total - buy_total
    print("📊 Podsumowanie:")
    print(f"   supply = {supply_total}")
    print(f"   buy = {buy_total}")
    print(f"   result = {result}")

    print(f"💾 Zapisuję raport do: {report_file_name}")
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
    print("✅ Raport zapisany!")
