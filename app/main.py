def create_report(data_file_name: str, report_file_name: str):
    result = {"buy": 0, "supply": 0}

    with open(data_file_name, "r") as f:
        file = f.read().replace("\n", " ")
        file = file.replace(",", " ").split()
        for buy in range(len(file) - 1):
            if file[buy] == "buy":
                result["buy"] += int(file[buy + 1])
            if file[buy] == "supply":
                result["supply"] += int(file[buy + 1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{result['supply']}\n"
                     f"buy,{result['buy']}\n"
                     f"result,{result['supply'] - result['buy']}\n")
