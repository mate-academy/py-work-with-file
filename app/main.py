def create_report(data_file_name: str, report_file_name: str) -> None:
    oper_dict = {}
    with open("/Users/yuliamala/PycharmProjects/py-work-with-file_solution/"
              + data_file_name, "r") as file:
        for pair in file.readlines():
            oper, num = pair.split(",")
            num = int(num.strip("\n"))
            oper_dict[oper] = oper_dict.setdefault(oper, 0) + num

    with open(report_file_name, "w") as file:
        for oper, num in sorted(oper_dict.items(), reverse=True):
            file.write(f"{oper},{num}\n")
        file.write(f"result,{oper_dict['supply'] - oper_dict['buy']}\n")
