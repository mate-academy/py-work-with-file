import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_slovnik = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(f"{data_file_name}", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            operation = row[0]
            value = int(row[1])
            data_slovnik[operation] += value

    data_slovnik["result"] = data_slovnik["supply"] - data_slovnik["buy"]

    with open(f"{report_file_name}", mode="w", newline="") as new_csvfile:
        writer = csv.writer(new_csvfile)

        for key,value in data_slovnik.items():
            writer.writerow([key,value])
