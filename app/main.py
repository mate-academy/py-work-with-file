import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(data_file_name, "r", newline="") as file_in:
        reader = csv.reader(file_in)

        for key, value in reader:
            result[key] += int(value)

        result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "w", newline="") as file_out:
        writer = csv.writer(file_out)

        for key, value in result.items():
            writer.writerow([key, value])
