def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as df:
        supply = 0
        buy = 0
        for line in df.readlines():
            if "buy" in line:
                buy += int(line.split(",")[1])
            if "supply" in line:
                supply += int(line.split(",")[1])

    with open(report_file_name, "w") as rf:
        rf.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
