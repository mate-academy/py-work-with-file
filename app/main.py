def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        content = {}

        for line in data_file:
            line = line.split(",")
            if line[0] == "supply":
                content["supply"] = content.get("supply", 0) + int(line[1])
            else:
                content["buy"] = content.get("buy", 0) + int(line[1])

    content["result"] = content["supply"] - content["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{content['supply']}\n"
            f"buy,{content['buy']}\n"
            f"result,{content['result']}\n"
        )
