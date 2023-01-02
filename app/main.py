def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(
                report_file_name, "a"
    ) as report_file:
        list_of_data = data_file.read().split("\n")
        supply = 0
        buy = 0
        for line in list_of_data:
            list_line = line.split(",")
            if list_line[0] == "supply":
                supply += int(list_line[1])
            if list_line[0] == "buy":
                buy += int(list_line[1])
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
