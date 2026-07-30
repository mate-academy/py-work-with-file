def create_report(data_file_name: str, report_file_name: str) -> None:
    file_dict = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue

            operation, amount = line.strip().split(",")
            file_dict[operation] = file_dict[operation] + int(amount)

    file_dict["result"] = file_dict["supply"] - file_dict["buy"]

    with open(report_file_name, "w") as new_file:
        for key, value in file_dict.items():
            new_file.write(f"{key},{value}\n")
