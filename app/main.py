from collections import OrderedDict


def f(key_list: list[str]) -> int:
    return ["supply", "buy", "result"].index(key_list[0])


def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dictionary = {}
    with open(data_file_name, "r") as data_file:
        data_list = data_file.readlines()
        for line in data_list:
            operation_type = line.split(",")[0]
            amount = int(line.split(",")[1].split("\n")[0])
            if operation_type not in report_dictionary:
                report_dictionary[operation_type] = amount
            else:
                report_dictionary[operation_type] += amount
    result = report_dictionary["supply"] - report_dictionary["buy"]
    report_dictionary["result"] = result
    sort_key = f
    items = report_dictionary.items()
    report_dictionary = dict(OrderedDict(sorted(items, key=sort_key)))
    with open(report_file_name, "w") as report:
        for key, value in report_dictionary.items():
            report.write(f"{key},{value}\n")
