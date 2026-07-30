from csv import reader, writer


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {"supply": 0, "buy": 0}

    with open(data_file_name) as f:
        for field, value in reader(f):
            data[field] += int(value)

    data["result"] = data["supply"] - data["buy"]

    with open(report_file_name, "w") as f:
        writer(f).writerows((name, value) for name, value in data.items())
