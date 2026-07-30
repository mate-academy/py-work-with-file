import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_data = {"supply": 0, "buy": 0, "result": 0}
    data_file = open(data_file_name, "r")
    reader = csv.reader(data_file)
    for row in reader:
        result_data[row[0]] += int(row[1])
    result_data["result"] = result_data["supply"] - result_data["buy"]
    data_file.close()

    with open(report_file_name, "w") as f:
        writer = csv.writer(f)
        for key, value in result_data.items():
            writer.writerow([key, value])
