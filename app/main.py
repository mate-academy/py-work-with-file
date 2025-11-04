def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f_in:
        totals = {}
        for line in f_in:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue
            if parts[0] not in totals:
                totals[parts[0]] = int(parts[1])
            else:
                totals[parts[0]] += int(parts[1])
    supply = totals.get("supply", 0)
    bought = totals.get("buy", 0)
    result = supply - bought
    with open(report_file_name, "w") as f_out:
        f_out.write(f"supply,{supply}\n")
        f_out.write(f"buy,{bought}\n")
        f_out.write(f"result,{result}\n")
