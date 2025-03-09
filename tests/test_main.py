import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from main import main


def test_main() -> None:
    """Test the main function with sample input data."""
    input_file = "test_input.csv"
    output_file = "test_output.csv"

    # Create test input file
    with open(input_file, "w", encoding="utf-8") as file:
        file.write("supply,30\n")
        file.write("buy,10\n")
        file.write("buy,13\n")
        file.write("supply,17\n")
        file.write("buy,10\n")

    # Run the function
    main(input_file, output_file)

    # Check output file
    with open(output_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    assert lines == ["supply,47\n", "buy,33\n", "result,14\n"]

    # Clean up test files
    os.remove(input_file)
    os.remove(output_file)


if __name__ == "__main__":
    pytest.main()
