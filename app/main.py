def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        supply = 0
        buy = 0
        for line in file_in:
            element, value = line.split(",")
            if element == "supply":
                supply += int(value)
            if element == "buy":
                buy += int(value)
        result = supply - buy
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
