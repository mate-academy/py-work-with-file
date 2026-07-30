def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        stats = {}
        for line in source:
            action, number = line.split(",")
            stats[action] = stats.get(action, 0) + int(number)

        stats["result"] = stats.get("supply", 0) - stats.get("buy", 0)

        with open(report_file_name, "w") as destination:
            destination.write(f"supply,{stats.get('supply', 0)}\n")
            destination.write(f"buy,{stats.get('buy', 0)}\n")
            destination.write(f"result,{stats.get('result')}\n")
