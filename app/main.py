def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in:
        text = file_in.read()
        text = text.split()
        my_dict = {}
        for each in text:
            string = (each.split(","))
            key = string[0]
            value = int(string[1])
            if key in my_dict:
                my_dict[key] += value
            else:
                my_dict[key] = value
    if next(iter(my_dict)) == "buy":
        my_dict = {"supply": my_dict["supply"], "buy": my_dict["buy"]}
    list_value = []
    for key, value in my_dict.items():
        list_value.append(value)
    my_dict["result"] = list_value[0] - list_value[1]
    with open(report_file_name, "w") as file_out:
        for key, value in my_dict.items():
            result = f"{key},{value}"
            file_out.write(result + "\n")
