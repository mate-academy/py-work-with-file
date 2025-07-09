def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {}
    with open(data_file_name, "r") as file:
        for line in file:
            name, value = line.split(",")
            result[name] = result.get(name, 0) + int(value)

    with open(report_file_name, "a") as file:
        file.write(f"supply,{str(result["supply"])}\n")
        file.write(f"buy,{str(result["buy"])}\n")
        file.write(f"result,{str((result["supply"] - result["buy"]))}\n")
