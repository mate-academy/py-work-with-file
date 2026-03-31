def create_report(data_file_name: str, report_file_name: str) -> None:
    counts = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            op, value = line.split(",")
            counts[op] += int(value)
            result = counts["supply"] - counts["buy"]
            with open(report_file_name, "w", encoding="utf-8") as out:
                out.write(f'supply,{counts["supply"]}\n')
                out.write(f'buy,{counts["buy"]}\n')
                out.write(f"result,{result}\n")
