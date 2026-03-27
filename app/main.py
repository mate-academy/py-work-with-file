def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name) as file:
        for lines in file:
            key, value = lines.strip().split(",")
            if key in result:
                result[key] += int(value)
            else:
                result.update({key: int(value)})

    result.update({"result" : result.get("supply") - result.get("buy")})

    with open(report_file_name, "a") as file:
        for key, value in result.items():
            file.write(f"{key},{value}\n")
