import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply": 0, "buy": 0}
    with open(
        data_file_name,
        "r",
    ) as file:
        reader = csv.reader(file)
        for row in reader:
            key, value = row
            result_dict[key] += int(value)

    with open(report_file_name, "w") as file:
        for key, value in result_dict.items():
            file.write(f"{key},{value}\n")

        result = result_dict["supply"] - result_dict["buy"]
        file.write(f"result,{result}\n")
