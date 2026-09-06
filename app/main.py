def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(f"{data_file_name}", "r") as file:

        for line in file.readlines():
            line_str = line.split(",")
            if line_str[0] == "supply":
                supply += int(line_str[1])
            if line_str[0] == "buy":
                buy += int(line_str[1])

        result = supply - buy

        with open(f"{report_file_name}", "w") as report:
            report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
