# Warehouse Capacity Forecaster

Python forecasting project for estimating warehouse load, utilization pressure, and capacity planning signals.

## Why This Exists

Represents analytics engineering work aimed at turning operational data into planning decisions for logistics teams.

## What This Demonstrates

- capacity and utilization trend estimation
- planning-oriented outputs instead of generic charts
- deterministic forecasting logic with tests

## Architecture

1. historical operational inputs are normalized into planning features
1. forecasting logic estimates future load and pressure thresholds
1. summary outputs highlight likely capacity stress periods

## Run It

```bash
python -m unittest
```

## Verification

Use `python -m unittest` to validate forecast calculations and outputs.
