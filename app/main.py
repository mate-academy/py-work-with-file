import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for char in reader:
            if len(char) == 2:
                key, value = char[0], int(char[1])
                if key == "supply":
                    supply_total += value
                elif key == "buy":
                    buy_total += value

    result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
