def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        supply = 0
        buy = 0
        for line in file_in.readlines():
            operation, number = line.split(",")
            if operation == "supply":
                supply += int(number)
            if operation == "buy":
                buy += int(number)
        result = supply - buy

        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
