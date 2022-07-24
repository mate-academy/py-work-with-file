import csv


def create_report(data_file_name: str, report_file_name: str):
    data_dict = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as csvfile:
        for row in csv.reader(csvfile):
            operation = row[0]
            value = row[1]
            data_dict[operation] += int(value)
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    with open(report_file_name, "w") as csvfile:
        for operation, value in data_dict.items():
            csvfile.write(f"{operation},{value}\n")
