def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}", "r") as source_file, \
            open(f"{report_file_name}", "w") as report_file:
        dict_with_values = {}
        for row in source_file:
            row.strip()
            product, value = row.split(",")
            value = int(value)
            if product not in dict_with_values:
                dict_with_values[product] = value
            else:
                dict_with_values[product] += value
        print(dict_with_values)

        report_file.write(f"supply,{dict_with_values['supply']}\n")
        report_file.write(f"buy,{dict_with_values['buy']}\n")
        report_file.write(
            f"result,{dict_with_values['supply'] - dict_with_values['buy']}\n"
        )
