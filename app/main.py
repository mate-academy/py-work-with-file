import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    text_dict = {"supply": 0, "buy": 0, "result": 0}
    with open(f"{data_file_name}", "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)
    for row in data:
        if row[0] in text_dict:
            number = text_dict.get(row[0])
            text_dict[row[0]] = number + int(row[1])
    text_dict["result"] = text_dict["supply"] - text_dict["buy"]
    text_list = [[f"{key},{vel}\n"] for key, vel in text_dict.items()]
    line_text = ["".join(i) for i in text_list]
    with open(f"{report_file_name}", "w") as file:
        file.write("".join(line_text))
