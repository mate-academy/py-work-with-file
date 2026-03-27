def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = [0, 0]
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            line = line.split(",")
            if line[0] == "supply":
                report_data[0] += int(line[1])
            else:
                report_data[1] += int(line[1])
    with open(report_file_name, "a") as file:
        file.write(f"supply,{report_data[0]}\n")
        file.write(f"buy,{report_data[1]}\n")
        file.write(f"result,{report_data[0] - report_data[1]}\n")
