def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0
    }
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        data = file_in.readlines()
        for line in data:
            operation = line.split(",")[0]
            amount = line.split(",")[1]
            report[operation] += int(amount)
        supply = report["supply"]
        buy = report["buy"]
        result = supply - buy
        text = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        file_out.write(text)
