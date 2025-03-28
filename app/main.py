def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for content in file.readlines():
            content = content.split(",")
            if content[0] == "supply":
                supply += int(content[1])
            elif content[0] == "buy":
                buy += int(content[1])

    with open(report_file_name, "a") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
