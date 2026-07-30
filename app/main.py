import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = data_file_name
    data_report = report_file_name
    with open(data, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        supply = sum([int(row[1]) for row in rows if row[0] == "supply"])
        buy = sum([int(row[1]) for row in rows if row[0] == "buy"])
    with open(data_report, "w") as result_file:
        result_file.write(f"supply,{supply}\n"   # noqa: E231
                          f"buy,{buy}\n"   # noqa: E231
                          f"result,{supply - buy}\n")   # noqa: E231
    file.close()
    result_file.close()
