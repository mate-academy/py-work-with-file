def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if "supply" in line:
                supply += int(line.split(",")[1])

            if "buy" in line:
                buy += int(line.split(",")[1])

    with open(report_file_name, "w") as new_file:
        report = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        new_file.write(report)
