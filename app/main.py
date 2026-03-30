def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data:
        data = data.read()
        data = data.split()
        supply = 0
        buy = 0
        for items in data:
            key, value = items.split(",")
            if key == "supply":
                supply += int(value)
            elif key == "buy":
                buy += int(value)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
