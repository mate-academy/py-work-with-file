def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0

    with open(f"{data_file_name}", "r") as data_in_file:
        for data_in_line in data_in_file:
            data = data_in_line.split(",")
            if data[0] == "supply":
                supply += int(data[1])
            else:
                buy += int(data[1])

    with open(f"{report_file_name}", "w") as result:
        result.write(f"supply,{str(supply)}\n"
                     f"buy,{str(buy)}\n"
                     f"result,{str(supply-buy)}\n")
