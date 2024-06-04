def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        info = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }

        lines = []
        for line in file.readline():
            lines.append(line.split(","))

        for key, value in lines:
            if key == "supply":
                info["supply"] += value
            if key == "buy":
                info["buy"] += value

        info["result"] = info["supply"] - info["buy"]

    with open(report_file_name, "w") as file:
        file.write(f"supply, {info["supply"]}\n")
        file.write(f"buy, {info["buy"]}\n")
        file.write(f"result, {info["result"]}\n")
