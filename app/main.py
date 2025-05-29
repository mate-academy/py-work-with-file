# from ctypes import HRESULT


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}

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

        for key, value in result_dict.items():
            report_file.write(f"{key},{value}\n")
