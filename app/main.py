def create_report(
        data_file_name: str,
        report_file_name: str

) -> None:
    with open(data_file_name, "r") as file_out:
        data_content = file_out.read()
        data = data_content.split("\n")
    result_data = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }
    for item in data:
        if item:
            parts = item.split(",")
            str_key = parts[0]
            str_value = int(parts[1])
            result_data[str_key] += str_value

    result = result_data.get("supply") - result_data.get("buy")
    result_data["result"] = result
    custom_str = "".join(
        f"{key},{value}\n" for key, value in result_data.items()  # noqa
    )

    with open(report_file_name, "w") as file_in:
        file_in.write(custom_str)
