def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_source:
        for line in file_source.readlines():
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])

    with open(report_file_name, "w") as file_destination:
        result = supply - buy
        file_destination.write(f"supply,{supply}\n")
        file_destination.write(f"buy,{buy}\n")
        file_destination.write(f"result,{result}\n")
