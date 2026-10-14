def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as file:

        for line in file:
            line = line.strip()
            if not line:
                continue

            list_line = line.split(",")
            key = list_line[0].strip()
            value = int(list_line[1].strip())

            if key not in result:
                result[key] = 0
            result[key] += value

    total_supply = result["supply"]
    total_buy = result["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{total_supply}\n")
        f.write(f"buy,{total_buy}\n")
        f.write(f"result,{total_supply - total_buy}\n")
