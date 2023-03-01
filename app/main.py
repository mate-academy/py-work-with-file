def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0
    result_amount = 0
    with open(data_file_name, "r") as data:
        for elem in data.read().split():
            if elem.split(",")[0] == "supply":
                supply_amount += int(elem.split(",")[1])
            if elem.split(",")[0] == "buy":
                buy_amount += int(elem.split(",")[1])
    result_amount = supply_amount - buy_amount
    report = f"supply,{supply_amount}\nbuy," \
             f"{buy_amount}\nresult,{result_amount}\n"
    with open(report_file_name, "w") as report_file:
        report_file.write(report)
