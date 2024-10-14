def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(f"{data_file_name}") as file:
        for line in file:
            value = line.split(",")
            if value[0] == "supply":
                supply += int(value[1])
            elif value[0] == "buy":
                buy += int(value[1])
    with open(f"{report_file_name}", "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
