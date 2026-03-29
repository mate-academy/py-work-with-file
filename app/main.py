def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            else:
                buy += int(line.split(",")[1])
        result = supply - buy
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\n"
                              f"buy,{buy}\n"
                              f"result,{result}\n")
