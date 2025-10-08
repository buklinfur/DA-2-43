# Visualization of categorical data (DA-1-45 assignment).

A small Python package for visualizing categorical data, designed as a solution of the DA-1-45 assignment. It provides reusable functions for counting categories, generating bar plots and pie charts, and a CLI for easy usage with CSV files or synthetic data.

---

## Project Structure

```
DA-1-45/
├─ visualize_categorical/
│  ├─ __init__.py
│  ├─ core.py
│  ├─ cli.py
│  └─ exit_codes.py
├─ tests/
│  ├─ test_core.py
├─ setup.py
├─ README.md
├─ requirements.txt
```

---

## Modules

### `core.py`

* `create_synthetic_data(n, column_name, categories, probs, seed)` – generate synthetic categorical data.
* `load_csv(path)` – load CSV into DataFrame.
* `validate_category_column(df, col)` – check column exists and is categorical.
* `count_categories(df, col)` – return counts of categories.
* `plot_bar(counts, title, xlabel, ylabel, out_path)` – bar plot.
* `plot_pie(counts, title, out_path)` – pie chart.

### `cli.py`

* CLI for running the package.
* Arguments:

| Argument    | Type | Required | Description                                        |
| ----------- | ---- | -------- | -------------------------------------------------- |
| `--input`   | str  | No       | CSV file path. If missing, synthetic data is used. |
| `--column`  | str  | Yes      | Column name to analyze.                            |
| `--n`       | int  | No       | Number of rows for synthetic data.                 |
| `--out-dir` | str  | No       | Output directory for plots.                        |
| `--seed`    | int  | No       | Random seed for reproducibility.                   |
| `--help`    | -    | No       | Show CLI help message.                             |

Returns exit codes defined in `exit_codes.py`.

### `exit_codes.py`

| Code | Meaning            |
| ---- | ------------------ |
| 0    | Success            |
| 1    | File not found     |
| 2    | Invalid input      |
| 3    | Missing config key |
| 4    | Runtime failure    |
| 99   | Unknown error      |

---

## Installation

```bash
git clone <repo_url>
cd DA-1-45
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -e .
pip install -r requirements.txt  # optional
```

---

## Usage

### CLI

CSV input:

```bash
python -m visualize_categorical.cli --input data/my_data.csv --column color --out-dir figures
```

Synthetic data:

```bash
python -m visualize_categorical.cli --n 100 --column mood --out-dir figures --seed 42
```

Help:

```bash
python -m visualize_categorical.cli --help
```

### Python

```python
from visualize_categorical.core import create_synthetic_data, count_categories, plot_bar

df = create_synthetic_data(n=50, column_name="color")
counts = count_categories(df, "color")
plot_bar(counts, title="Color Distribution", xlabel="Color", ylabel="Count", out_path="bar.png")
```

---

## Testing

```bash
pytest -v
```

* Tests cover data creation, category counting, and validation.
