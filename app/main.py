import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    if not data_file_name.endswith(".csv"):
        return None
    with open(data_file_name, "r") as f, open(report_file_name, "w") as g:
        reader = csv.reader(f)
        storage = {}
        for row in reader:
            item, value = row[0], int(row[1])
            if item not in storage:
                storage[item] = 0
            storage[item] += value
        value = storage["supply"]
        g.write(f"supply,{value}\n")
        value = storage["buy"]
        g.write(f"buy,{value}\n")
        result = storage["supply"] - storage["buy"]
        g.write(f"result,{result}\n")
