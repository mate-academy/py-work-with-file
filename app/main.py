def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])
    with open(report_file_name, "a") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{supply - buy}\n")
