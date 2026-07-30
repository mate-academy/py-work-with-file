def create_report(data_file_name: str, report_file_name: str) -> None:
    results = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            name, amount = line.split(",")
            results[name] += int(amount)
        net_result = results["supply"] - results["buy"]
        report_file.write(
            f"supply,{results['supply']}\n"
            f"buy,{results['buy']}\n"
            f"result,{net_result}\n"
        )
