def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for data in file:
            action, value = data.split(",")
            if action == "buy":
                buy += int(value)
            else:
                supply += int(value)

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")