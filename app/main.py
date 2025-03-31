def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as file:
        for line in file:
            key, value = line.split(",")
            key = str(key)
            value = int(value)
            result.update({key: result.get(key, 0) + value})
        result.update({"result": result.get("supply") - result.get("buy")})

    with open(report_file_name, "w") as file:
        for key, value in result.items():
            file.write(f"{key},{value}\n")
