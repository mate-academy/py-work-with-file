def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_data_list = []
    supply = 0
    buy = 0
    with open(data_file_name) as source, open(report_file_name, "w") as output:
        for line in source:
            if line.startswith("supply"):
                supply += int(line[7:-1])
            elif line.startswith("buy"):
                buy += int(line[4:-1])
        csv_data_list = [
            f"supply,{supply}\n", f"buy,{buy}\n", f"result,{supply - buy}\n"
        ]
        output.writelines(csv_data_list)
