import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_report = {"supply": 0, "buy": 0}
    with open(data_file_name) as csv_file:
        input_data = tuple(csv.reader(csv_file))
        for operation, value in input_data:
            dict_report[operation] += int(value)

        dict_report["result"] = dict_report["supply"] - dict_report["buy"]

    with open(report_file_name, "w") as csv_file:
        writer = csv.writer(csv_file, lineterminator="\n")
        writer.writerows(tuple(dict_report.items()))
