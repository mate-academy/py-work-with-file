def create_report(data_file_name: str, report_file_name: str) -> None:
    my_dict = {"supply": 0,
               "buy": 0}

    with open(data_file_name, "r") as file:
        content = file.readlines()

    with open(report_file_name, "w") as report_file:
        for line in content:
            operation, quantity = line.split(",")
            if operation in my_dict:
                my_dict[operation] += int(quantity)

        my_dict["result"] = my_dict["supply"] - my_dict["buy"]

        for key, value in my_dict.items():
            report_file.write(",".join([key, str(value)]) + "\n")
