def create_report(data_file_name: str, report_file_name: str) -> None:
    print("data_file_name:", data_file_name)
    print("report_file_name:", report_file_name)

    report_dict = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as file:
        print("count", len(file.readlines()))
        for line in file.readlines():
            if not line:
                continue

            key, value = line.strip().split(",")

            report_dict[key] = report_dict.get(key, 0) + int(value)

        supply_total = report_dict.get("supply")
        buy_total = report_dict.get("buy")
        report_dict["result"] = supply_total - buy_total

    with open(report_file_name, "w") as file:
        report = [f"{key},{value}" for key, value in report_dict.items()]
        file.write("\n".join(report) + "\n")
