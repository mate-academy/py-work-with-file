import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] not in result:
                result[row[0]] = int(row[1])
            else:
                result[row[0]] += int(row[1])
        result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", result["supply"]])
        writer.writerow(["buy", result["buy"]])
        writer.writerow(["result", result["result"]])
