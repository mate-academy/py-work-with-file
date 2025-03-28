def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as input_f, \
            open(report_file_name, "w") as report_f:
        operation_list = input_f.readlines()
        operation_list = [operation.replace("\n", "")
                          for operation in operation_list]
        operation_dict = {
            "supply": 0,
            "buy": 0
        }
        for operation in operation_list:
            op_type, amount = operation.split(",")
            operation_dict[op_type] += int(amount)
        operation_dict["result"] = \
            operation_dict["supply"] - operation_dict["buy"]
        operation_list_new = [f"{line},{operation_dict[line]}"
                              for line in operation_dict]
        report_f.write("\n".join(operation_list_new) + "\n")
