def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "w") as report_file:
        supply = 0
        buy = 0
        for line in data_file:
            string = line[:-1]
            if "supply" in string:
                supply += int(string[7:])
            if "buy" in string:
                buy += int(string[4:])
        result = supply - buy
        total = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        report_file.write(total)
