import pandas as pd
import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from validator.validation_rules import (
    check_required_columns,
    check_age_range,
    check_salary_range,
    check_country_allowed
)
from validator.engine import run_validation, enforced_pipeline


@pytest.fixture
def sample_config():
    return {
        "env": "dev",
        "required_columns": ["customer_id", "age", "salary", "country"],
        "allowed_countries": ["US", "IND", "CA"],
        "rules": {
            "req_cols": {"severity": "critical"},
            "age": {"min": 18, "max": 60, "severity": "warning"},
            "salary": {"min": 0, "severity": "critical"},
            "country": {"severity": "warning"}
        }
    }


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "customer_id": [1, 2],
        "age": [25, 70],
        "salary": [50000, -100],
        "country": ["US", "MX"]
    })


def test_required_columns_pass(sample_df, sample_config):
    results = check_required_columns(sample_df, sample_config)
    assert results == []


def test_age_range_failure(sample_df, sample_config):
    results = check_age_range(sample_df, sample_config)
    assert len(results) == 1
    assert results[0]["rule"] == "age_range"


def test_salary_range_failure(sample_df, sample_config):
    results = check_salary_range(sample_df, sample_config)
    assert len(results) == 1
    assert results[0]["severity"] == "critical"


def test_country_allowed_failure(sample_df, sample_config):
    results = check_country_allowed(sample_df, sample_config)
    assert len(results) == 1
    assert "invalid country" in results[0]["message"].lower()


def test_engine_summary(sample_df, sample_config):
    output = run_validation(sample_df, sample_config)
    summary = output["summary"]

    assert summary["total_failures"] == 3
    assert summary["critical_failures"] == 1


def test_enforce_pipeline_raises():
    summary = {
        "critical_failures": 1
    }

    config = {"env": "prod"}

    with pytest.raises(Exception):
        enforced_pipeline(summary, config)
