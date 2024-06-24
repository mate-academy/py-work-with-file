def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            spl = line.split(",")
            if spl[0] == "supply":
                operations["supply"] += int((spl[1]))
            else:
                operations["buy"] += int(spl[1])
        operations["result"] = operations["supply"] - operations["buy"]
    with open(report_file_name, "w") as file:
        for key, value in operations.items():
            file.write(f"{key},{value}\n")
