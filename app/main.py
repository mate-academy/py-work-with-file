def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    dictionary = {}

    for line in data_file.readlines():
        if line.strip():
            coma_index = line.index(",")
            if line[:coma_index] not in dictionary:
                dictionary.update(
                    {line[:coma_index]: int(line[coma_index + 1:])}
                )
            else:
                dictionary[line[:coma_index]] += int(line[coma_index + 1:])

    dictionary.update({"result": dictionary["supply"] - dictionary["buy"]})
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(
        f'supply,{dictionary["supply"]}\n'
        f'buy,{dictionary["buy"]}\n'
        f'result,{dictionary["supply"] - dictionary["buy"]}\n'
    )
    report_file.close()
