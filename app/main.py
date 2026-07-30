def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        new_dict = {}
        for line in file:
            stripped_line = line.strip()
            split_line = stripped_line.split(",")
            if split_line[0] in new_dict:
                new_dict[split_line[0]] += int(split_line[1])
            else:
                new_dict[split_line[0]] = int(split_line[1])

        supply = new_dict.get("supply", 0)
        buy = new_dict.get("buy", 0)
        result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
