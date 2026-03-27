def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", encoding="utf-8") as file:
        data = {
            "supply": 0,
            "buy": 0,
        }
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            parts = clean_line.split(",")
            if len(parts) < 2:
                continue
            key = parts[0]
            value = int(parts[1])
            if key not in data:
                data[key] = value
            else:
                data[key] += value

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        for key, value in data.items():
            report_file.write(f"{key},{value}\n")
        result = data["supply"] - data["buy"]
        report_file.write(f"result,{result}\n")
