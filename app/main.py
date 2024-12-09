# write your code here
def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    dictionary = {}
    content = open(data_file_name)
    for line in content:
        line_item = line.split(",")
        line_item[1] = int(line_item[1][:-1])
        if line_item[0] in dictionary.keys():
            dictionary[line_item[0]] += line_item[1]
        else:
            dictionary[line_item[0]] = line_item[1]
    dictionary["result"] = dictionary["supply"] - dictionary["buy"]
    result = open(report_file_name, "w")
    result.write(f"supply,{dictionary["supply"]}\nbuy,"
                 f"{dictionary["buy"]}\n"
                 f"result,{dictionary["result"]}\n")
