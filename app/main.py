import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}

    with (open(data_file_name, newline="") as input_file,
          open(report_file_name, "w", newline="") as output_file):
        reader = csv.reader(input_file)
        for line in reader:
            if line[0] not in ("supply", "buy"):
                continue
            if line[0] in result_dict:
                result_dict[line[0]] += int(line[1])
            else:
                result_dict[line[0]] = int(line[1])
        max_value = max(result_dict.values())
        num_difference = max_value - (sum(result_dict.values()) - max_value)
        output_file.write(f"supply,{result_dict.get('supply')}\n"
                          f"buy,{result_dict.get('buy')}\n"
                          f"result,{num_difference}\n")
