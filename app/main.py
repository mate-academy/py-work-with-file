def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.read()
        supply = 0
        buy = 0
        for line in data.split("\n"):
            if "buy" in line:
                buy += int(line.split(",")[1])
            if "supply" in line:
                supply += int(line.split(",")[1])
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply-buy}\n")
