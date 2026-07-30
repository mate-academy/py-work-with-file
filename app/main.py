def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = []
    buy = []

    with open(data_file_name) as file:
        for line in file:
            item = line.strip().split(",")
            if item[0] == "supply":
                supply.append(int(item[1]))
            if item[0] == "buy":
                buy.append(int(item[1]))

    with open(report_file_name, "w") as file:
        file.write(f"supply,{sum(supply)}\n")
        file.write(f"buy,{sum(buy)}\n")
        file.write(f"result,{sum(supply) - sum(buy)}\n")
