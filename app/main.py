from ctypes import HRESULT
import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    result_dict = {}
    with (open(data_file_name, newline='') as data_file,
          open(report_file_name, "w", newline='') as report_file):

        reader = csv.DictReader(data_file)
        fieldnames = reader.fieldnames

        writer = csv.DictWriter(report_file, fieldnames = fieldnames)
        writer.writeheader()

        for row in reader:
            for key, value in row.items():
                if key not in result_dict:
                    result_dict[key] = value
                else:
                    result_dict[key] += value

            writer.writerow(result_dict)
