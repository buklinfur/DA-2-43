import argparse
import sys
from pathlib import Path

from .core import create_synthetic_data, load_csv, count_categories, plot_bar, plot_pie
from visualize_categorical import exit_codes


def parse_args():
    p = argparse.ArgumentParser(description="Visualize categorical column")
    p.add_argument("--input", type=str, default=None, help="CSV file (optional).\
                   If not specified, generating synthetic data")
    p.add_argument("--column", type=str, default="color", help="Name of categorial column")
    p.add_argument("--out-dir", type=str, default="figures", help="Where to save the results")
    p.add_argument("--n", type=int, default=100, help="Size of synthetic dataset. (if in use)")
    p.add_argument("--seed", type=int, default=42, help="seed for generation")
    return p.parse_args()


def run_cli():
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.input:
        df = load_csv(args.input)
    else:
        df = create_synthetic_data(n=args.n, column_name=args.column, 
                                   seed=args.seed)

    counts = count_categories(df, args.column)

    bar_path = out_dir / f"bar_{args.column}.png"
    pie_path = out_dir / f"pie_{args.column}.png"

    plot_bar(counts, title=f"Distribution by {args.column}",
             xlabel=args.column, ylabel="Amount", out_path=bar_path)
    plot_pie(counts, title=f"Fractions by {args.column}", out_path=pie_path)


def main() -> int:
    """Main entrypoint for CLI script."""
    try:
        run_cli()
        return exit_codes.SUCCESS

    except FileNotFoundError as e:
        print(f"[ERROR] File not found: {e}", file=sys.stderr)
        return exit_codes.ERR_FILE_NOT_FOUND

    except ValueError as e:
        print(f"[ERROR] Invalid input: {e}", file=sys.stderr)
        return exit_codes.ERR_INVALID_INPUT

    except KeyError as e:
        print(f"[ERROR] Missing config key: {e}", file=sys.stderr)
        return exit_codes.ERR_CONFIG

    except RuntimeError as e:
        print(f"[ERROR] Runtime failure: {e}", file=sys.stderr)
        return exit_codes.ERR_RUNTIME

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}", file=sys.stderr)
        return exit_codes.ERR_UNKNOWN


if __name__ == "__main__":
    sys.exit(main())
