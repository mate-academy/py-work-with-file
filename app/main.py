def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as f:
        line_number = 1
        for line in f.readlines():
            operation = line.split(",")
            key = operation[0]
            value = int(operation[1].strip())
            result[key] = result.get(key, 0) + value

            line_number += 1

    with open(report_file_name, "w") as f:
        supply = result.get("supply", 0)
        buy = result.get("buy", 0)
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
