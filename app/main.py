def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_in:
        for line in file_in.readlines():
            operation, value = line.split(",")
            if operation == "supply":
                supply += int(value)
            elif operation == "buy":
                buy += int(value)

    result = supply - buy

    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
