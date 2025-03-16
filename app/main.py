import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    try:
        with open(data_file_name, "r", newline="") as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if row[0] == "supply":
                    total_supply += int(row[1])
                elif row[0] == "buy":
                    total_buy += int(row[1])

        result = total_supply - total_buy


        with open(report_file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["supply", total_supply])
            writer.writerow(["buy", total_buy])
            writer.writerow(["result", result])

    except FileNotFoundError:
        print(f"Помилка: файл {data_file_name} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


create_report("C:/Users/OEM/py-work-with-file/apples.csv", "apples_report.csv")
create_report("C:/Users/OEM/py-work-with-file/bananas.csv", "bananas_report.csv")
create_report("C:/Users/OEM/py-work-with-file/grapes.csv", "grapes_report.csv")
create_report("C:/Users/OEM/py-work-with-file/oranges.csv", "oranges_report.csv")
