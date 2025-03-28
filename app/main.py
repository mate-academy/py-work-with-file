def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            values = line.split(",")
            if values[0] == "supply":
                supply += int(values[1])
            if values[0] == "buy":
                buy += int(values[1])
        result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n" # noqa E231
                f"buy,{buy}\n" # noqa E231
                f"result,{result}\n") # noqa E231
