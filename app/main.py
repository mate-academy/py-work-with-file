import csv
import os.path


def create_report(data_file_name: str, report_file_name: str) -> None:
    if os.path.isfile(data_file_name):
        report_dict = {}
        with open(data_file_name, mode="r") as csv_file:
            operations_reader = csv.reader(csv_file)
            for operation in operations_reader:
                if operation[1].isnumeric():
                    if operation[0] not in report_dict:
                        report_dict[operation[0]] = int(operation[1])
                    else:
                        report_dict[operation[0]] += int(operation[1])

        report_dict["result"] = report_dict["supply"] - report_dict["buy"]
        sorted_values = sorted(report_dict.values(), reverse=True)
        sorted_dict = {}

        for i in sorted_values:
            for k in report_dict.keys():
                if report_dict[k] == i:
                    sorted_dict[k] = report_dict[k]

        with open(report_file_name, 'w') as f:
            for key in sorted_dict:
                f.write("%s,%s\n" % (key, report_dict[key]))
