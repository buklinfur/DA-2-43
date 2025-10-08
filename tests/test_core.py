import pandas as pd
import pytest

from visualize_categorical.core import create_synthetic_data, validate_category_column, count_categories


def test_create_synthetic_data_shape():
    df = create_synthetic_data(n=50, column_name="color", seed=42)
    assert df.shape == (50, 1)
    assert "color" in df.columns


def test_validate_and_count(tmp_path):
    df = pd.DataFrame({"color": ["red", "blue", "red"]})
    validate_category_column(df, "color")
    counts = count_categories(df, "color")
    assert counts["red"] == 2
    assert counts["blue"] == 1


def test_validate_missing_column():
    df = pd.DataFrame({"a":[1]})
    with pytest.raises(ValueError):
        validate_category_column(df, "color")
