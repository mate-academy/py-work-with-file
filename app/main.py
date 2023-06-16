def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0
    with open(data_file_name, "r") as df:
        for line in df:
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])

    result = supply - buy
    with open(report_file_name, "w") as rf:
        rf.write(f"supply,{supply}\n"
                 f"buy,{buy}\n"
                 f"result,{result}\n")
