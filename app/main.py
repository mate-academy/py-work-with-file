def create_report(data_file_name: str, report_file_name: str) -> None:
    data_table = {}

    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        for line in file_in.readlines():
            line = line.split(",")
            if line[0] not in data_table:
                data_table[line[0]] = int(line[1])
            else:
                data_table[line[0]] += int(line[1])
        result = (f'supply,{data_table["supply"]}\n'
                  f'buy,{data_table["buy"]}\n'
                  f'result,{data_table["supply"] - data_table["buy"]}\n')

        file_out.write(result)
