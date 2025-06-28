def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    result = {}
    with open(data_file_name, "r") as data_file:
        with open(report_file_name, "w") as write_file:
            for data in data_file:
                key, value = data.split(",")
                result[key] = (
                    int(value)
                    if not result.get(key)
                    else result.get(key) + int(value)
                )
            result["result"] = result["supply"] - result["buy"]
            write_file.write(f"supply,{result.get('supply')}\n")
            write_file.write(f"buy,{result.get('buy')}\n")
            write_file.write(f"result,{result.get('result')}\n")
