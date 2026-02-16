from .validation_rules import run_rules

import pandas as pd

def run_validation (df, config_data):
    results = run_rules(df, config_data)

    summary = generate_summary(results)

    return {
        "results": results,
        "summary": summary
    }

def generate_summary(results):
    total_failure = len([r for r in results if r["status"] == "fail"])
    critical_failures = len([r for r in results if r["status"] == "fail" and r["severity"] == "critical"])
    warning_failures = len([r for r in results if r["status"] == "fail" and r["severity"] == "warning"])

    return {
        "total_checks_executed": len(results),
        "total_failures": total_failure,
        "critical_failures": critical_failures,
        "warning_failures": warning_failures
    }


def enforced_pipeline(summary, config_data):
    if (
        config_data.get("env") == "prod" and summary["critical_failures"] > 0

    ):
        raise Exception(
            f"Pipeline stopped. {summary['critical_failures']} critical validation failures detected."
        )
    elif (
        config_data.get("env") == "prod" and summary["warning_failures"] > 0
    ):
        raise Warning(f"Warning Message. {summary['warning_failures']} detected.")
