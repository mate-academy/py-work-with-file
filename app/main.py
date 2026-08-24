def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as read_data_file:
        content = read_data_file.read()
        vocab = {}

        for line in content.split():
            key, value = line.strip().split(",")
            vocab[key] = vocab.get(key, 0) + int(value)
        vocab["result"] = 0

        for key, value in vocab.items():
            if key == "supply":
                supply_value = value
            if key == "buy":
                buy_value = value
            if key == "result":
                value = supply_value - buy_value
            print(f"{key},{value}")

    with open(report_file_name, "w") as write_data_file:
        write_data_file.write(f"supply,{supply_value}\n")
        write_data_file.write(f"buy,{buy_value}\n")
        write_data_file.write(f"result,{value}\n")
