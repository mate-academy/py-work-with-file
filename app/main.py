def create_report(data_file_name: str, report_file_name: str) -> None:
    content = {}
    with open(data_file_name, "r") as input_file:
        lines = input_file.readlines()
        for line in lines:
            line = line.strip().split(",")
            if line[0] in content:
                content[line[0]] += int(line[1])
            else:
                content[line[0]] = int(line[1])
    with open(report_file_name, "a") as output_file:
        content["result"] = content["supply"] - content["buy"]
        output_file.write(f"supply,{content['supply']}\n")
        output_file.write(f"buy,{content['buy']}\n")
        output_file.write(f"result,{content['result']}\n")
