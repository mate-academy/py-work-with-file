def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for line in data.readlines():
            arr = line.split(",")
            if arr[0] == "supply":
                supply += int(arr[1])
            if arr[0] == "buy":
                buy += int(arr[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{str(supply)}\n"
                     f"buy,{str(buy)}\n"
                     f"result,{str(supply - buy)}\n")
