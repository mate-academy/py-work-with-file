def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0
    print(data_file_name)
    with open(data_file_name, "r") as file:
        for line in file:
            if line.startswith("supply"):
                supply += int(line[7:])
            if line.startswith("buy"):
                buy += int(line[4:])
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n"
                   f"buy,{buy}\n"
                   f"result,{supply - buy}\n"
                   )
