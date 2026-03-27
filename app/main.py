def create_report(data_file_name: str, report_file_name: str) -> None:
    var_dict = {}
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")

    for line in data_file:
        if not line.strip():
            continue
        line_lst = line.strip()
        line_lst = line_lst.split(",")
        op = line_lst[0]  # .strip()
        amount = line_lst[1]  # .strip()
        amount = int(amount)

        if op not in var_dict:
            var_dict[op] = amount
        else:
            var_dict[op] += amount
    result = var_dict["supply"] - var_dict["buy"]

    report_file.write(f"supply,{var_dict.get('supply')}\n")
    report_file.write(f"buy,{var_dict.get('buy')}\n")
    report_file.write(f"result,{result}\n")

    data_file.close()
    report_file.close()
