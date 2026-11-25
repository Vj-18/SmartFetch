# SmartFetch – Parcel Delivery Time Prediction System

## Project Overview

SmartFetch is a machine learning-based parcel delivery management and prediction system inspired by logistics services that allow customers to receive packages at convenient delivery times.

The project uses machine learning to predict estimated package delivery time and classify deliveries as On Time or Delayed based on logistics-related factors.

This project is developed as a local portfolio project to demonstrate practical skills in Python, Machine Learning, PostgreSQL, FastAPI, and Frontend Development.

## Problem Statement

Parcel deliveries can be affected by several factors, including:

- Delivery distance
- Package weight
- Traffic conditions
- Weather conditions
- Vehicle type
- Warehouse processing time

SmartFetch aims to use these factors to estimate delivery time and identify potentially delayed packages.

## Project Objectives

1. Generate and analyze a synthetic logistics dataset.
2. Perform data preprocessing and feature engineering.
3. Develop regression models for delivery time prediction.
4. Develop classification models for delivery status prediction.
5. Integrate PostgreSQL for package data management.
6. Build REST APIs using FastAPI.
7. Develop a simple frontend for package predictions.

## Dataset Description

The project uses a synthetic logistics dataset containing 1,000 package records and nine columns.

| Column | Description |
|---|---|
| package_id | Unique package identifier |
| distance_km | Delivery distance |
| package_weight_kg | Package weight |
| traffic_level | Traffic conditions |
| weather_condition | Weather conditions |
| vehicle_type | Delivery vehicle |
| warehouse_processing_hours | Warehouse processing time |
| delivery_time_hours | Actual delivery time |
| delivery_status | On Time or Delayed |

## Machine Learning Tasks

### Regression
Predict the estimated delivery time in hours.

Target: `delivery_time_hours`

### Classification
Predict whether a package will be delivered on time or delayed.

Target: `delivery_status`

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- PostgreSQL
- FastAPI
- SQLAlchemy
- HTML
- CSS
- JavaScript
- Git and GitHub

## Project Development Phases

- [x] Phase 1 – Problem Understanding, Dataset Creation and EDA
- [ ] Phase 2 – Data Preprocessing and Feature Engineering
- [ ] Phase 3 – Machine Learning Model Development
- [ ] Phase 4 – PostgreSQL Database Integration
- [ ] Phase 5 – FastAPI Backend Development
- [ ] Phase 6 – Frontend Integration
- [ ] Phase 7 – Testing and GitHub Documentation

## Project Structure

```text
SmartFetch/
├── notebooks/
├── data/
├── models/
├── backend/
├── frontend/
├── requirements.txt
├── .gitignore
└── README.md
```

## Current Progress

Phase 1: Dataset creation and exploratory data analysis.

More implementation details, model evaluation results, setup instructions, and screenshots will be added as development progresses.

## Project Status

Currently under development.