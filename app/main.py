def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data_file = open(f"../{data_file_name}", "r")
    data = dict()
    line_number = 1
    for line in data_file:
        parsed_line = line.replace(" ", "")
        parsed_line = parsed_line.replace("/n", "")

        key_value = parsed_line.split(",")

        if key_value[0] in data.keys():
            data.update({
                key_value[0]: int(data[key_value[0]]) + int(key_value[1])
            })
        else:
            data.update({key_value[0]: int(key_value[1])})

        line_number += 1
    data_file.close()

    with open(report_file_name, "w") as f:
        f.write(f'supply,{data["supply"]}\n')
        f.write(f'buy,{data["buy"]}\n')
        f.write(f'result,{data["supply"] - data["buy"]}\n')
