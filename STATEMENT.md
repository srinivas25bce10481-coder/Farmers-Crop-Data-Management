# 5.2 Project Statement

## Problem Statement

In local agricultural communities, tracking the yearly production data (yield) for individual farmers and specific crops often relies on manual records or disparate spreadsheets. This lack of a centralized, digitized system makes it difficult to retrieve historical data, compare yields, and generate quick, accurate reports. The primary challenge is to create a simple, accessible, and robust digital platform for the non-technical user (e.g., a data collector or farm manager) to **centralize, record, and report on crop production data** efficiently.

## Scope of the Project

The scope of this project is limited to developing a **Minimum Viable Product (MVP)** for data entry and basic reporting.

* **INCLUDED:** Data persistence using SQLite, front-end interface using Streamlit, registration of farmers and crops, creation of production records (Farmer ID, Crop ID, Year, Quantity), and display of farmer-specific production history reports.
* **EXCLUDED (Future Scope):** User authentication/login, data import/export (CSV/Excel), graphical data analysis (charts/graphs), multi-user access, complex yield trend prediction, or geo-location mapping.

## Target Users

1.  **Local Farm Data Collectors/Managers:** Primary users responsible for gathering and inputting production figures from various farms/farmers. They require a simple, form-based interface.
2.  **Agricultural NGOs/Agencies:** Users who need to quickly access and view the production history for a specific farmer to assess performance or eligibility for schemes.

## High-Level Features

| Feature Category | Description |
| :--- | :--- |
| **User Management** | Register new farmers by Name and Village. |
| **Data Integrity** | Enforce unique registration for crop types. |
| **Record Keeping** | Capture production records linking Farmer, Crop, Year, and Quantity. |
| **Reporting** | Generate and display detailed, historical production tables for any selected farmer. |
| **Interface** | Intuitive web interface built with Streamlit, accessible via a browser. |
