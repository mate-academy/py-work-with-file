def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(f"{data_file_name}", "r") as data_file, \
            open(f"{report_file_name}", "w") as report_file:
        for i in data_file.read().split():
            if "supply" in i:
                supply += int(i[i.find(",") + 1:])
            elif "buy" in i:
                buy += int(i[i.find(",") + 1:])
        result = supply - buy
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
