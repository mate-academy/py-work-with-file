def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, encoding="utf-8") as file:
        data = file.read()
        l_data = [line.split(",") for line in data.splitlines()]
        sup_data = sum(int(i[1]) for i in l_data if i[0] == "supply")
        buy_data = sum(int(i[1]) for i in l_data if i[0] == "buy")
        res_data = sup_data - buy_data

    with open(report_file_name, "w", encoding="utf-8") as output:
        output.write(f"supply,{sup_data}\n")
        output.write(f"buy,{buy_data}\n")
        output.write(f"result,{res_data}\n")
