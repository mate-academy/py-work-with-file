def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for data in file:
            line, value = data.split(",")
            if line == "buy":
                buy += int(value)
            if line == "supply":
                supply += int(value)

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")