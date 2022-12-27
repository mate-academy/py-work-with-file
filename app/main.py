def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_in, \
            open(f"{report_file_name}.csv", "w") as file_out:
        for line in file_in:
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            if operation == "buy":
                buy += int(amount)
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}")


create_report("apples.csv", "new")
