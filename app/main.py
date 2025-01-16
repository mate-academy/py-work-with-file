def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as read_file:
        result = {"supply": 0, "buy": 0}
        for line in read_file:
            key, value = line.strip("\n").split(",")
            result[key] += int(value)
        for index, values in enumerate(result.values()):
            if index == 0:
                result_for_dict = values
            else:
                result_for_dict -= values
        result["result"] = abs(result_for_dict)
    with open(report_file_name, "w") as passing:
        for passing_key, passing_value in result.items():
            passing.write("{},{}\n".format(passing_key, passing_value))
