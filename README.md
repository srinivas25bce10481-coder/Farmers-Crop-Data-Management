# Farmers Crop Data Management System

## Project Title
**Farmers Crop Data Management System**

## Overview of the Project
This project is a simple, browser-based data management application designed to help track and report the crop production data of individual farmers. It provides a structured interface for registering new farmers and crops, recording yearly production quantities, and viewing production history reports using a persistent SQLite database backend. The application is built using **Streamlit** for the front-end interface and **SQLite** for data storage.

## Features
* **Farmer Registration:** Easily add new farmers with their name and village.
* **Crop Registration:** Register new crop types, ensuring uniqueness to maintain data integrity.
* **Production Record Entry:** Record specific crop quantities (in tons) harvested by a farmer in a given year.
* **Production Reporting:** Generate a tabular report showing the historical production data for any selected farmer.
* **Data Visualization:** Uses Pandas DataFrames within Streamlit for clean table display of reports.

## Technologies/Tools Used
* **Python 3.x**
* **Streamlit:** For creating the interactive web application interface.
* **SQLite3:** Standard Python library for the embedded SQL database backend.
* **Pandas:** Used for displaying organized, tabular data (DataFrames) in the reports.

## Steps to Install & Run the Project

1.  **Clone the Repository (if applicable):**
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```

2.  **Install Required Libraries:**
    Ensure you have Python installed. Then, install the necessary dependencies using pip.
    ```bash
    pip install streamlit pandas
    ```
    *(Note: `sqlite3` is included with the standard Python library.)*

3.  **Save the Code:**
    Save the provided Python code as a file named Farmers Crop Data Management.py .

4.  **Run the Application:**
    Execute the following command in your terminal from the project directory:
    ```bash
    streamlit run Farmers Crop Data Management.py
    ```

5.  **Access the App:**
    The application will automatically open in your default web browser (usually at `http://localhost:8501`).

## Instructions for Testing
1.  Navigate to the **'Add Farmer'** page in the sidebar and add a few farmer records (e.g., *Name: Ramesh, Village: Kothri*).
2.  Navigate to the **'Add Crop'** page and add a few crop types (e.g., *Wheat, Rice, Maize*).
3.  Navigate to **'Record Production'**. Select a farmer and a crop, enter a year (e.g., 2024), and a quantity (e.g., 5.5). Record several different entries for the same farmer.
4.  Navigate to **'View Report'**. Select the farmer you added data for. Click **'Show Report'** to verify that all recorded production data is displayed correctly in the table.

## Screenshots 
![](Screenshot%201.png)
