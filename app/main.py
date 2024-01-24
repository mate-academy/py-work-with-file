import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total = {"supply": 0, "buy": 0}
    source_path = f"C:\MA\py-work-with-file\{data_file_name}"

    with open(source_path, "r") as source_file:
        reader = csv.DictReader(source_file, fieldnames=("key", "value"))
        for line in reader:
            total[line["key"]] += int(line["value"])
        total["result"] = total["supply"] - total["buy"]

    with open(report_file_name, "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerows(total.items())
