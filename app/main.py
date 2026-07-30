def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(report_file_name, "w") as report_f,
          open(data_file_name, "r") as data_f):
        report_data = {}

        for line in data_f.readlines():
            name, amount = line.split(",")
            if report_data.get(name):
                report_data[name] += int(amount)
            else:
                report_data[name] = int(amount)

        supply = report_data.get("supply")
        buy = report_data.get("buy")

        report_f.write(f"supply,{supply}\n")
        report_f.write(f"buy,{buy}\n")
        report_f.write(f"result,{supply - buy}\n")
