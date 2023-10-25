import csv


def create_report(data_flie_name: str, report_file_name: str) -> None:
    with open(data_flie_name, "r") as csv_r:
        reader = csv.reader(csv_r)
        result = {
            "supply": 0,
            "buy": 0
        }
        for row in reader:
            if row[0] == "supply":
                result["supply"] += int(row[1])
            if row[0] == "buy":
                result["buy"] += int(row[1])
        result["result"] = result["supply"] - result["buy"]

    with open(report_file_name, "w", newline="") as csv_w:
        writer = csv.writer(csv_w)
        writer.writerows([["supply", result["supply"]],
                          ["buy", result["buy"]],
                          ["result", result["result"]]])
