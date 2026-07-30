def create_report(data_file_name: str, report_file_name: str) -> None:
    enter_file = open(data_file_name, "r")
    new_file = {}
    for line in enter_file.readlines():
        non_empty_string = line.strip()
        if non_empty_string != "":
            operation_type, amount = non_empty_string.split(",")
            new_file[operation_type] = (
                new_file.get(operation_type, 0)
                + int(amount)
            )
    enter_file.close()

    new_file["result"] = new_file["supply"] - new_file["buy"]
    file_out = open(report_file_name, "w")
    file_out.write(f"supply,{new_file['supply']}\n")
    file_out.write(f"buy,{new_file['buy']}\n")
    file_out.write(f"result,{new_file['result']}\n")
    file_out.close()
