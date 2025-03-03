def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_ = {}

    with open(data_file_name) as input_file:
        for line in input_file:
            key, value = line.rstrip("\n").split(",")
            dict_[key] = dict_.get(key, 0) + int(value)

        dict_["result"] = dict_["supply"] - dict_["buy"]

    order = ["supply", "buy", "result"]

    with open(report_file_name, "w") as result:
        for key in order:
            result.write(f"{key},{dict_[key]}\n")  # noqa: E231
