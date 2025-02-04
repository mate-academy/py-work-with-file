# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file, \
            open(report_file_name, "w") as output:
        content = {"supply": 0, "buy": 0}
        for line in file:
            content_line = line.split(",")
            if content_line[0] == "supply":
                content["supply"] += int(content_line[1])
            if content_line[0] == "buy":
                content["buy"] += int(content_line[1])
        content["result"] = content["supply"] - content["buy"]
        for key, value in content.items():
            output.write(f"{key},{value}\n")
