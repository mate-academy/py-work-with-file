import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_atrs = {}

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        csv_list = [row for row in csv_reader]
        for atr in ("supply", "buy"):
            for el in csv_list:
                if el[0] == atr:
                    total_atrs[atr] = total_atrs.get(atr, 0) + int(el[1])

    with open(report_file_name, "a",) as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerows(total_atrs.items())
        result = total_atrs.get("supply", 0) - total_atrs.get("buy", 0)
        report_file.write(f"result,{result}\n")
