from functools import reduce


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {"supply" : 0, "buy" : 0}

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "a") as report_file):

        for line in data_file:
            if line:
                operation_type = line.split(",")[0]
                amount = int(line.split(",")[1])

            if operation_type in result_dict:
                result_dict[operation_type] += amount
            else:
                result_dict.update({operation_type : amount})

        for index, (key, value) in enumerate(result_dict.items()):
            if index != len(result_dict) - 1:
                report_file.write(f"{key},{value}\n")
            else:
                report_file.write(f"{key},{value}\n")
                report_file.write(f"result,"
                                  f"{reduce(
                                      lambda x, y: x - y,
                                      result_dict.values())}\n")
