def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_file = {"supply": [], "buy": []}

    with open(data_file_name, "r") as file:
        for dados in file:
            key, value = dados.split(",")
            dict_file[key].append(int(value))

    sum_supply = sum(dict_file["supply"])
    sum_buy = sum(dict_file["buy"])

    result = f"supply,{sum_supply}\n"
    result += f"buy,{sum_buy}\n"
    result += f"result,{sum_supply - sum_buy}\n"

    with open(report_file_name, "w") as file:
        file.write(result)
