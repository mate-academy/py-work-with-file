def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_read,
          open(report_file_name, "w") as file_write):
        res_dict = {}
        for line in file_read:
            type_operation, amount = line.split(",")
            if res_dict.get(type_operation):
                res_dict[type_operation] += int(amount)
            else:
                res_dict[type_operation] = int(amount)
        file_write.write(f"supply,{res_dict.get('supply')}\n"
                         f"buy,{res_dict.get('buy')}\n"
                         f"result,"
                         f"{res_dict.get('supply') - res_dict.get('buy')}\n")
