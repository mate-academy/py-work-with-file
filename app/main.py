def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"../{data_file_name}", "r") as data_file:
        lines_list = data_file.readlines()

        data_dict = {}
        for line in lines_list:
            if line.strip() == "":
                continue
            data_list = line.split(",")
            key_val = data_list[0]
            value_val = int(data_list[1])
            data_dict[key_val] = (
                value_val if key_val not in data_dict
                else data_dict[key_val] + value_val
            )

        supply = data_dict.get("supply", 0)
        buy = data_dict.get("buy", 0)
        text_file = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"

        with open(report_file_name, "w") as report_file:
            report_file.write(text_file)
