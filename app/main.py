import csv


def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "a") as report_file
    ):
        csv_reader = csv.reader(file_in)
        full_data = {}
        for data in sorted(csv_reader, reverse=True):
            if data[0] not in full_data:
                full_data.update({data[0]: int(data[1])})
            else:
                full_data[data[0]] += int(data[1])
        full_data.update(
            {"result": full_data["supply"]
             - full_data["buy"]}
        )

        writer = csv.writer(report_file)
        for key, value in full_data.items():
            writer.writerow([key, value])
