# rer8
def create_report(data_file_name: str, report_file_name: str) -> None:
    new_data = {}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue  # пропускаємо порожні рядки
            try:
                key, value = line.split(",", 1)
                value = int(value)
                new_data[key] = new_data.get(key, 0) + value
            except ValueError:
                continue  # пропускаємо некоректні рядки

    supply = new_data.get("supply", 0)
    buy = new_data.get("buy", 0)
    new_data["result"] = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f'result,{new_data["result"]}\n')
