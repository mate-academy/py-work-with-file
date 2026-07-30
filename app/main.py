def create_report(data_file_name: str, report_file_name: str):
    dictionary = {}

    with open(data_file_name, "r") as f:
        for line in f.readlines():
            value = line.split(",")
            if value[0] not in dictionary:
                dictionary[value[0]] = int(value[1])
            else:
                dictionary[value[0]] += int(value[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{dictionary['supply']}\n"
                f"buy,{dictionary['buy']}\n"
                f"result,{dictionary['supply'] - dictionary['buy']}\n")
