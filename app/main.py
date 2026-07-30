def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        data = file.read()
        work_day_list = data.split("\n")
        result_day = {}

        for item in work_day_list:
            split_item = item.split(",")
            if split_item[0] == "":  # added this line to skip empty lines
                continue
            if split_item[0] not in result_day:
                result_day[split_item[0]] = int(split_item[1])
            else:
                result_day[split_item[0]] += int(split_item[1])

        result_day["result"] = result_day["supply"] - result_day["buy"]

    with open(report_file_name, "w") as file:
        lines = []

        if result_day["supply"] >= result_day["buy"]:
            lines.append(f"{'supply'},{result_day['supply']}")
            lines.append(f"{'buy'},{result_day['buy']}")
            lines.append(f"{'result'},{result_day['result']}")
        else:
            lines.append(f"{'buy'},{result_day['buy']}")
            lines.append(f"{'supply'},{result_day['supply']}")
            lines.append(f"{'result'},{result_day['result']}")

        lines.append("")

        file.write("\n".join(lines))
