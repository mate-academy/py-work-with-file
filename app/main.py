def create_report(data_file_name: str, report_file_name: str) -> any:
    data_dict = {}
    with open(data_file_name) as file:
        for line in file:
            name, value = line.split(",")
            if not data_dict.get(name):
                data_dict.update({name: int(value)})
            else:
                data_dict[name] += int(value)

    result = 0
    for key in data_dict:
        if key == "buy":
            result -= data_dict[key]
        else:
            result += data_dict[key]
    with open(report_file_name, "w") as rep_file:
        rep_file.write(f"supply,{data_dict['supply']}\n")
        rep_file.write(f"buy,{data_dict['buy']}\n")
        rep_file.write(f"result,{result}\n")
