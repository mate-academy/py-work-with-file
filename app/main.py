import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file_reader:
        catalog = {}
        rows = csv.reader(file_reader)
        for naimen, kolvo in rows:
            catalog[naimen] = kolvo

    result = int(catalog.get("supply")) - int(catalog.get("buy"))
    print(f"supply,{catalog.get('supply')},buy,{catalog.get('buy')},{result}")

    with open(report_file_name, "w") as file_writer:
        file_writer.write(f"supply,{catalog.get('supply')}\n")
        file_writer.write(f"buy,{catalog.get('buy')}\n")
        file_writer.write(f"result,{result}\n")


# create_report("../apples.csv", "../apples_report")
