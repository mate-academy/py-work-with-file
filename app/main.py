import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        data_file = list(reader)
    total_supply = 0
    total_buy = 0
    for action, value in data_file:
        if action == "supply":
            total_supply += int(value)
        elif action == "buy":
            total_buy += int(value)
    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(f"supply, {total_supply}\n")
        file.write(f"buy, {total_buy}\n")
        file.write(f"result, {result}\n")
