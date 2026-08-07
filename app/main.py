def create_report(date_file_name: str, report_file_name: str) -> None:
    file_csv = open(date_file_name, "r")
    dict_of_result = {}

    for line in file_csv.readlines():
        clean_line = line.rstrip("\n").split(",")
        if not dict_of_result.get(clean_line[0]):
            dict_of_result[clean_line[0]] = int(clean_line[1])
        else:
            dict_of_result[clean_line[0]] += int(clean_line[1])
    if dict_of_result.get("supply") or dict_of_result.get("buy"):
        dict_of_result["result"] \
            = dict_of_result["supply"] - dict_of_result["buy"]

    supply_pop_value = dict_of_result.pop("supply")
    result = {"supply": supply_pop_value, **dict_of_result}
    write_a_file = open(report_file_name, "a")

    for key, value in result.items():
        write_a_file.write(f"{key},{value}\n")
    write_a_file.write("")
