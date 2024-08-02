def create_report(data_file_name: str, report_file_name: str) -> None:

    read_data = open(data_file_name, "r")
    list_of_elements = []
    result_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    for line in read_data:
        list_of_elements.extend(line.split(","))

    read_data.close()
    curr_word = ""
    for element in list_of_elements:
        if element == "supply" or element == "buy":
            curr_word = element
            continue

        result_dict[curr_word] += int(element)

    if result_dict["supply"] > result_dict["buy"]:
        result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    write_data = open(report_file_name, "w")

    for key, value in result_dict.items():
        write_data.write(f"{key},{value}\n")

    write_data.close()
