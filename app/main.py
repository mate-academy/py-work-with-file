def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(data_file_name, "r") as file:
        data = file.read().split()
        for element in data:
            name, count = element.split(",")
            data_dict.update({name: data_dict.get(name, 0) + int(count)})

    with open(report_file_name, "w") as file:
        supply = data_dict.get("supply")
        file.write(f"supply,{supply}\n") # noqa
        buy = data_dict.get("buy")
        file.write(f"buy,{buy}\n") # noqa
        result = data_dict.get("supply") - data_dict.get("buy")
        file.write(f"result,{result}\n") # noqa
