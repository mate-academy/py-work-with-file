import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name) as file:
        reader = csv.reader(file)
        for operation, amount in reader:
            data[operation] += int(amount)
    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as file:
        for operation, amount in data.items():
            file.write(f"{operation},{amount}\n")
