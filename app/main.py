def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        data = file.readlines()
        for line in data:
            value = line.split(",")
            if value[0] == "supply":
                supply += int(value[1])
            if value[0] == "buy":
                buy += int(value[1])
    result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
