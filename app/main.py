def create_report(data_file_name: str, report_file_name: str) -> None:
    dicti = {}
    result = 0

    with open(data_file_name, "r") as file:
        dicti = {"supply": 0, "buy": 0}
        for line in file:
            line = line.strip().split(",")
            dicti[line[0]] += int(line[1])
        result = dicti["supply"] - dicti["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply,{dicti['supply']}\n")
        file.write(f"buy,{dicti['buy']}\n")
        file.write(f"result,{result}\n")
