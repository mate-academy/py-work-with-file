def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            if "supply" in line:
                supply += int(line.split(",")[1])
            elif "buy" in line:
                buy += int(line.split(",")[1])

        with open(report_file_name, "w") as report_file:
            report_file.write(
                f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
