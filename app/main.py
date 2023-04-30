import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data, open(report_file_name, "w") as report:
        reader = csv.reader(data)
        item_dict = {"supply": 0, "buy": 0}

        for row in reader:
            key, value = row
            item_dict[key] += int(value)

        for key, value in item_dict.items():
            report.write(f"{key},{value}\n")

        report.write(f'result,{item_dict["supply"] - item_dict["buy"]}\n')
