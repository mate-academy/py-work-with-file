def create_report(data_file_name:str, report_file_name: str) -> None:

    with open(data_file_name, "r") as r_file:
        items_list = [line.strip().split(",") for line in r_file]
        items_dict = {}
        for key, value in items_list:
            items_dict[key] = items_dict.get(key, 0) + int(value)

    supply = int(items_dict["supply"]) - int(items_dict["buy"])

    with open(report_file_name, "w") as w_file:
        w_file.write(f"supply,{items_dict['supply']}\n")
        w_file.write(f"buy,{items_dict['buy']}\n")
        w_file.write(f"result,{supply}\n")
