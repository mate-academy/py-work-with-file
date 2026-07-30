from csv import reader, writer


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_report = {"supply": 0, "buy": 0}

    with open(data_file_name) as f:
        for field, value in reader(f):
            data_report[field] += int(value)

    data_report["result"] = data_report["supply"] - data_report["buy"]

    with open(report_file_name, "w") as f:
        writer(f).writerows((key, value) for key, value in data_report.items())
