def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if line.rstrip().split(",")[0] == "supply":
                supply += int(line.rstrip().split(",")[1])
            if line.rstrip().split(",")[0] == "buy":
                buy += int(line.rstrip().split(",")[1])
    result = supply - buy
    file.close()
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    file.close()
