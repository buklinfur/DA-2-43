from __future__ import annotations
from typing import Optional, Sequence
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def create_synthetic_data(n: int = 100,
                          column_name: str = "color",
                          categories: Sequence[str] = ("red", "blue", "yellow"),
                          probs: Optional[Sequence[float]] = None,
                          seed: Optional[int] = None) -> pd.DataFrame:
    """Creates DataFrame with categorial column 'color' and synthetic data in it."""
    if probs is None:
        probs = [1 / len(categories)] * len(categories)
    if len(probs) != len(categories):
        raise ValueError("probs has to be the same size as categories")
    rng = np.random.default_rng(seed)
    vals = rng.choice(categories, size=n, p=probs)
    return pd.DataFrame({column_name: vals})


def load_csv(path: str | Path) -> pd.DataFrame:
    """Returns DataFrame with data from provided csv file by path."""
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File {p} not found.")
    return pd.read_csv(p)


def validate_category_column(df: pd.DataFrame, column: str) -> None:
    """Checks if the DataFrame column is valid."""
    if column not in df.columns:
        raise ValueError(f"Колонка '{column}' отсутствует в DataFrame")
    if df[column].dropna().shape[0] == 0:
        raise ValueError(f"Колонка '{column}' пустая или состоит только из NaN")


def count_categories(df: pd.DataFrame, column: str) -> pd.Series:
    """Returns number of categories in DataFrame."""
    validate_category_column(df, column)
    return df[column].value_counts(dropna=False)


def plot_bar(counts: pd.Series, title: str, xlabel: str,
             ylabel: str, out_path: str | Path, figsize=(6, 4),
             dpi: int = 150, rotate: int = 0) -> None:
    """Creates and saves a bar plot of features."""
    ensure_dir(Path(out_path).parent)
    ax = counts.plot(kind="bar", rot=rotate)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.tight_layout()
    plt.savefig(out_path, dpi=dpi)
    plt.close()


def plot_pie(counts: pd.Series, title: str, out_path: str | Path,
             figsize=(6, 6), dpi: int = 150, autopct: str = "%1.1f%%") -> None:
    """Creates and saves a pie plot of features."""
    ensure_dir(Path(out_path).parent)
    fig, ax = plt.subplots(figsize=figsize)
    counts.plot(kind="pie", autopct=autopct, startangle=90, ax=ax)
    ax.set_ylabel("")
    ax.set_title(title)
    ax.axis("equal")
    plt.tight_layout()
    plt.savefig(out_path, dpi=dpi)
    plt.close()
