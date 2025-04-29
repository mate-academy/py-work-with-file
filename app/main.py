def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, open(report_file_name, "w") as report_file:
        supply = 0
        buy = 0

        for line in data_file:
            one_line = line.strip().split(",")
            if len(one_line) != 2:
                continue
            if one_line[0] == "supply":
                supply += int(one_line[1])
            elif one_line[0] == "buy":
                buy += int(one_line[1])

        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
