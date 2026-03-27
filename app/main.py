def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data_result = {}

    with open(data_file_name, "r") as file:
        for text in file:
            key, value = text.split(",")
            if key in data_result:
                data_result[key] += int(value)
            else:
                data_result[key] = int(value)

    with open(report_file_name, "w") as file:
        result = f"supply,{data_result['supply']}\n" \
                 f"buy,{data_result['buy']}\n" \
                 f"result,{data_result['supply'] - data_result['buy']}\n"

        file.write(result)
