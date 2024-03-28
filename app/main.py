def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = []
    buy = []
    with open(data_file_name, "r") as file:
        for line in file:
            if "supply" in line:
                supply.append(int(line.split(",")[1]))
            if "buy" in line:
                buy.append(int(line.split(",")[1]))

    with open(report_file_name, "a") as new_file:
        new_file.write(f"supply,{sum(supply)}\n")
        new_file.write(f"buy,{sum(buy)}\n")
        new_file.write(f"result,{sum(supply) - sum(buy)}\n")
