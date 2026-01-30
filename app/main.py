def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0
        for line in file.readlines():
            if not line:
                continue
            operation, value = line.strip().split(",")
            value = int(value)
            if operation == "supply":
                supply += value
            if operation == "buy":
                buy += value

    res = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
    with open(report_file_name, "w") as f:
        f.write(res)
