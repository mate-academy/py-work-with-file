def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Create a report from market data after a working day.

    Args:
        data_file_name (str): Input CSV file with operation data
        report_file_name (str): Output file for the report
    """
    # Initialize counters
    total_supply = 0
    total_buy = 0

    # Read data from input file
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            # Skip empty lines (including the last line if it's empty)
            line = line.strip()
            if not line:
                continue

            # Split the line into operation type and amount
            operation, amount_str = line.split(",")
            amount = int(amount_str)

            # Update totals based on operation type
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    # Calculate result
    result = total_supply - total_buy

    # Write report to output file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")


# Example usage and test function
def test_create_report() -> None:
    """Test the create_report function with sample data"""

    # Create test input file
    test_data = """supply,30
buy,10
buy,13
supply,17
buy,10
"""

    # Write test data to a file
    with open("test_data.csv", "w") as f:
        f.write(test_data)

    # Generate report
    create_report("test_data.csv", "test_report.csv")

    # Read and display the report
    with open("test_report.csv", "r") as f:
        report_content = f.read()
        print("Generated Report:")
        print(report_content)

    # Expected output:
    # supply,47
    # buy,33
    # result,14


# Run the test
if __name__ == "__main__":
    test_create_report()
