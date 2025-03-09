
# Notes

Below is a general review of the Python script in `filter_csv_example.py`, along with notes on usage examples.

---

## 1. Usage Examples

Assuming your script is in a file named `filter_csv_example.py` and you have a CSV file named `input.csv` (with columns such as `City`, `Country`, `Year`, etc.), here are some ways you can launch the script from the command line.

### 1.1 Basic Filtering

```cmd
python filter_csv_example.py input.csv output.csv City "New York"
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
