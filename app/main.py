def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    temp_data = [0, 0, 0]
    with open(data_file_name, "r") as source:
        for line in source.readlines():
            temp = line.split(",")
            if temp[0] == "supply":
                temp_data[0] += int(temp[1])
            if temp[0] == "buy":
                temp_data[1] += int(temp[1])

    with open(report_file_name, "a") as report:
        report.write(f"supply,{temp_data[0]}\n")
        report.write(f"buy,{temp_data[1]}\n")
        result = temp_data[0] - temp_data[1]
        report.write(f"result,{result}\n")
