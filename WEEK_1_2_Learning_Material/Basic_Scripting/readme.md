# Basic Scripting

This directory contains examples and exercises focused on basic scripting concepts relevant to Site Reliability Engineering (SRE).

## Learning Objectives

By working through these examples and exercises, you will:

1. Learn to write practical utility scripts for common SRE tasks
2. Understand file handling, error handling, and command-line argument parsing
3. Practice processing and analyzing logs and CSV data
4. Learn techniques for setting up and configuring environments

## Contents

### Examples (Correctly Implemented)

- `examples/filter_csv_example.py`: Script to filter CSV files based on column values
- `examples/logs_analysis_example.py`: Script to analyze log files and extract error patterns
- `examples/setup_env_example.py`: Script to set up an environment with dependencies and configurations

### Flawed Implementations (For Review)

- `filter_csv_flawed.py`: Contains errors in CSV filtering implementation
- `logs_analysis_flawed.py`: Contains flaws in log analysis implementation
- `setup_env_flawed.py`: Contains problems in environment setup implementation

### Sample Data

- `sample_data/input.csv`: Sample CSV file for testing the filtering script
- `sample_data/app.log`: Sample log file for testing the log analysis script

### Quizzes

- `quizzes/scripting_quiz.md`: Quiz questions on basic scripting concepts

## Instructions

1. Start by reviewing the correctly implemented examples to understand the scripting concepts
2. Then, examine the flawed implementations to identify and fix the issues
   - Look for bugs, inefficiencies, and logical errors
   - The flawed implementations contain comments highlighting areas to focus on
3. After fixing the flawed implementations, compare your solutions with the correct implementations
4. Test your understanding by completing the quiz

## Prerequisites

- Basic Python knowledge
- Understanding of fundamental programming concepts

## Setup

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Notes Filter CSV Example

Below is a general review of the Python script in `filter_csv_example.py`, along with notes on usage examples.

---

## 1. Usage Examples

Assuming your script is in a file named `filter_csv_example.py` and you have a CSV file named `input.csv` (with columns such as `City`, `Country`, `Year`, etc.), here are some ways you can launch the script from the command line.

### 1.1 Basic Filtering

```cmd
python filter_csv_example.py input.csv output.csv City "New York"
python filter_csv_example.py ../sample_data/input.csv ../sample_data/output.csv City "New York"
python filter_csv_example.py ../sample_data/input.csv ../sample_data/output.csv City "New York" --preview 5
```

This command will:

1. Print information about the input CSV (e.g., columns, total rows).
2. Filter `input.csv` by the column named `City`, matching rows where the column value is `New York`.
3. Write only the matching rows to `output.csv`.
4. Print how many rows matched.

### 1.2 Preview the Filtered Results

If you want to preview a certain number of rows from the filtered output, use the `--preview` argument:

``` cmd
python filter_csv_example.py input.csv output.csv City "New York" --preview 5
```

## Additional Resources

- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Python argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [Python subprocess Documentation](https://docs.python.org/3/library/subprocess.html)
