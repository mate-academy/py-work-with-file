import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_ = {"supply": 0, "buy": 0}

    import os.path

    with open(os.path.dirname(__file__) + "/../" + data_file_name,
              newline="") as start_file:
        reader = csv.reader(start_file, delimiter=",")
        for row in reader:
            dict_[row[0]] += int(row[1])

    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        data = [
            ["supply", dict_["supply"]],
            ["buy", dict_["buy"]],
            ["result", dict_["supply"] - dict_["buy"]]
        ]
        writer.writerows(data)
