import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    new_dict = {}
    with open(data_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[0] not in new_dict:
                new_dict[row[0]] = int(row[1])
            else:
                new_dict[row[0]] += int(row[1])
    new_dict["result"] = new_dict["supply"] - new_dict["buy"]
    with open(report_file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for key in ["supply", "buy", "result"]:
            writer.writerow([key, new_dict[key]])
