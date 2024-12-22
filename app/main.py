import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    try:
        data_file = open(data_file_name, "r")
        reader = csv.reader(data_file)

        for row in reader:
            if row:
                operation, amount = row
                try:
                    amount = int(amount)
                except ValueError:
                    print(f"Skipping invalid data: {row}")
                if operation == "supply":
                    total_supply += amount
                elif operation == "buy":
                    total_buy += amount

        data_file.close()

        result = total_supply - total_buy

        report_file = open(report_file_name, "w", newline="")
        writer = csv.writer(report_file)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])

        report_file.close()

        print(f"Report successfully created in {report_file_name}")

    except FileNotFoundError:
        print(f"Error: The file {data_file_name} was not found.")
    except IOError:
        print("Error: There was an issue with reading or writing the files.")
