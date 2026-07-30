def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.split(",")
            line[1] = int(line[1].strip())
            if line[0] == "buy":
                buy += line[1]
            else:
                supply += line[1]
        result = supply - buy
    open(report_file_name, "a").write(f"supply,{supply}\n")
    open(report_file_name, "a").write(f"buy,{buy}\n")
    open(report_file_name, "a").write(f"result,{result}\n")
