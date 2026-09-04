def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_of_value = {}

    with open(data_file_name, "rt") as f:
        lines = f.readlines()

        for line in lines:
            split_value = line.split(",")
            key = split_value[0]
            value = int(split_value[1].strip())
            if split_value[0] not in dict_of_value:
                dict_of_value[key] = value
            else:
                dict_of_value[key] += value

    with open(report_file_name, "a") as f:
        result = None

        for key, value in dict_of_value.items():
            f.write(f"{key}, {value}\n")

        for value in dict_of_value.values():
            if result is None:
                result = value
            else:
                result -= value

        f.write(f"result, {result}\n")
