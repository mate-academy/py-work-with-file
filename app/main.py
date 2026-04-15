import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0, "result": 0}
    with open(f"../{data_file_name}", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            key = row[0]
            value = row[1]
            result[key] += int(value)
        result["result"] = result["supply"] - result["buy"]
    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        for key, value in result.items():
            writer.writerow([key, value])
