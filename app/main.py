import os

def create_report(data_file_name: str, report_file_name: str) -> None:

    app_dir = os.path.dirname(__file__)

    project_root = os.path.dirname(app_dir)

    data_path = os.path.join(project_root, data_file_name)
    report_path = os.path.join(project_root, "tests", report_file_name)

    dictionary = {"supply": 0, "buy": 0}

    with open(data_path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            dictionary[operation] += int(amount)

    result = dictionary["supply"] - dictionary["buy"]

    with open(report_path, "w") as report_file:
        for key, value in dictionary.items():
            report_file.write(f"{key},{value}\n")
        report_file.write(f"result,{result}\n")

