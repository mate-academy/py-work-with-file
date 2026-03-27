def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            list_line = line.split(",")
            if list_line:
                operation, amount = list_line[0], list_line[1]
                if operation == "supply":
                    supply += int(amount)
                if operation == "buy":
                    buy += int(amount)
    result = supply - buy
    with open(report_file_name, "w") as file_out:
        file_out.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        )
