def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        file_list = file.readlines()
        results = {
            "supply": 0,
            "buy":0
        }
        for line in file_list:
            if line.strip():
                split_data = line.split(",")
                key, value = split_data[0], split_data[1]
                results[key] = results.get(key, 0) + int(value)
        results["result"] = results["supply"] - results["buy"]
    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply,{results["supply"]}\n")
        write_file.write(f"buy,{results["buy"]}\n")
        write_file.write(f"result,{results["result"]}\n")
