# app/main.py

def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Reads transaction data from a CSV file and generates a summary report.

    Args:
        data_file_name: The path to the input CSV file.
        report_file_name: The path to the output report file.
    """
    total_supply = 0
    total_buy = 0

    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                # Ignore potential empty lines
                if not line.strip():
                    continue

                parts = line.strip().split(",")
                operation_type = parts[0]

                # Ensure amount is a valid integer
                try:
                    amount = int(parts[1])
                except (ValueError, IndexError):
                    print(f"Warning: Skipping invalid line: {line.strip()}")
                    continue

                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    except FileNotFoundError:
        print(f"Error: The file {data_file_name} was not found.")
        return

    result = total_supply - total_buy

    # Write the report to the specified file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")


# Exemplo de como chamar a função (opcional, para testes)
if __name__ == "__main__":
    # Você pode usar um dos arquivos existentes no projeto para testar
    # Por exemplo: "apples.csv", "bananas.csv", etc.
    create_report("apples.csv", "report_apples.csv")
    print("Report for apples.csv has been generated as report_apples.csv")

    create_report("bananas.csv", "report_bananas.csv")
    print("Report for bananas.csv has been generated as report_bananas.csv")
