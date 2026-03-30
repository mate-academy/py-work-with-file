import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    fruits_dict = {}

    with open(data_file_name) as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] in fruits_dict:
                fruits_dict[line[0]] += int(line[1])
            else:
                fruits_dict[line[0]] = int(line[1])

    result = fruits_dict.get("supply", 0) - fruits_dict.get("buy", 0)
    fruits_dict["result"] = result

    ordered_keys = ["supply", "buy", "result"]

    with open(report_file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for key in ordered_keys:
            if key in fruits_dict:
                writer.writerow([key, fruits_dict[key]])
