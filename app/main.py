def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()
    supply = 0
    buy = 0
    for line in lines:
        line = line.strip()
        if line:
            process, amount = line.split(",")
            if process == "supply":
                supply += int(amount)
            elif process == "buy":
                buy += int(amount)
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
