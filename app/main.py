def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data,\
            open(report_file_name, "w") as report:
        supply, buy = 0, 0
        for info in data.readlines():
            demand, amount = info.split(",")
            if demand == "supply":
                supply += int(amount)
            if demand == "buy":
                buy += int(amount)
        result = supply - buy
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{result}\n")
