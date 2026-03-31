def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}", "r") as file:
        content = file.read().split()
    dictionary = {}
    for i in content:
        i = i.split(",")
        if i[0] in dictionary:
            dictionary[f"{i[0]}"] += int(i[1])
        else:
            dictionary[f"{i[0]}"] = int(i[1])
    dictionary["result"] = dictionary["supply"] - dictionary["buy"]
    result = ""
    for key, value in dictionary.items():
        result += f"{key},{value}\n"
    result = result.split()
    if len(result[0]) < len(result[1]):
        result[0], result[1] = result[1], result[0]
    result = "\n".join(result) + "\n"
    with open(f"{report_file_name}", "w") as report:
        report.write(result)
