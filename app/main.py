def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in, \
            open(report_file_name, "w") as file_out:
        lines = file_in.readlines()
        data = {}
        for pair in lines:
            key, value = pair.strip().split(",")
            data[key] = data.get(key, 0) + int(value)
        print(f"supply,{data['supply']}", file=file_out)
        print(f"buy,{data['buy']}", file=file_out)
        print(f"result,{data['supply'] - data['buy']}", file=file_out)
