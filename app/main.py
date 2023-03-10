def create_report(data_file_name: str, report_file_name: str):
    open_file = open(data_file_name, "r")
    new_dict = dict()
    for data in open_file:
        data_trans = data.replace("\n", "")
        arr = data_trans.split(",")
        transaction = arr[0]
        sum_trans = arr[1]
        if sum_trans.isdigit():
            sum_trans = int(sum_trans)
            if transaction in new_dict.keys():
                new_dict[transaction] += sum_trans
            else:
                new_dict[transaction] = sum_trans
    supply = new_dict["supply"]
    buy = new_dict["buy"]
    result = supply - buy
    new_dict["result"] = result
    new_dict.clear()
    new_dict["supply"] = supply
    new_dict["buy"] = buy
    new_dict["result"] = result
    with open(report_file_name, "w") as file_rec:
        for new_data, value in new_dict.items():
            file_rec.write(f"{new_data},{value}\n")
