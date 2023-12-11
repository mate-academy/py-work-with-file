def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        text = file.read()
        text = text.replace("\n", " ")
        text = text.split()
        for sell in text:
            if "supply" in sell:
                supply += int(sell.strip("supply,"))
            else:
                buy += int(sell.strip("buy,"))
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")  # noqa
