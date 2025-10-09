# Key Analysis in Relational Database

This repository contains the full implementation, datasets, and experimental results for the paper:

> **Meaningful Key Discovery under Incomplete Information: A Framework Based on Uniqueness Ratios and Subkey Analysis**

It provides scripts for reproducing all experiments, including the computation of **Uniqueness Ratio (UR)**, **Completeness Ratio (CR)**, **Specialisation Analysis**, and **Framework Evaluation**.


## Overview

This project implements a framework for **key analysis in incomplete relational datasets**.  
It integrates four core stages:

1. **Basic Analysis** — Performs the initial computation of the maximum uniqueness ratio (max-UR) and completeness ratio (CR) to evaluate the distinctiveness and data integrity of column combinations.

2. **Filtering Keys with Thresholds** — Identifies and retains near-keys by applying predefined thresholds on UR, thereby narrowing the search space to the most promising candidate combinations.

3. **Specialisation** — Explores subset relationships among candidate keys to uncover sub-key hierarchies, employing BFS and DFS strategies with pruning to improve computational efficiency.

4. **Counter-example Analysis** — Examines duplicate or inconsistent tuples that violate near-keys, distinguishing between meaningful business rules and dirty data to refine the final set of meaningful keys and uniqueness constraints.

## Experimental Environment

### Database Setup
The project utilizes the **[Hockey Database](https://relational.fel.cvut.cz/dataset/Hockey)**, a structured dataset containing records from hockey competitions.
We use a MySQL database created from the provided `data_initialization/Hockey.sql` file, which contains all experimental tables used in the paper.

#### Step 1: Install MySQL
Please ensure MySQL (version 8.0 or later) is installed and running locally.
You can verify the installation by running:
```angular2html
mysql --version
```

#### Step 2: Run the setup script
Use the following Python script to automatically create the database and import all tables:
```angular2html
python data_initialization/setup_database.py --password YOUR_PASSWORD
```
Once executed successfully, the database `Hockey` will be created and ready for use by all subsequent scripts.

#### Step 3: Verify the database
After setup, you can confirm that the tables were correctly loaded by logging into MySQL:
```angular2html
mysql -u root -p
USE Hockey;
SHOW TABLES;
```



## Experiments

The experimental framework is implemented across two Jupyter notebooks located in the `experiment/` directory. Together, they cover the complete workflow of the study — from data loading and basic key analysis to subkey pruning, counter-example detection.

- **`hockey_analysis.ipynb`** — implements the core workflow of the framework. It covers:
  - Loading the local **Hockey** database and preparing experimental data.  
  - Computing the **Uniqueness Ratio (UR)** and **Completeness Ratio (CR)**.  
  - Producing UR and CR distribution visualizations.  
  - Selecting **Top-k tables** and plotting the **Degree-of-Violation distribution**.  
  - The calculation outputs and runtime metrics are automatically stored in:
    ```
    /result/runTime_data/
    ```

- **`subkey_pruning.ipynb`** — focuses on **efficiency optimization** and **performance evaluation**. It implements:
  - Construction of the **specialisation graph**.  
  - Application of **pruning strategies** to enhance computational efficiency.  
  - Runtime comparisons between **Brute Force**, **BFS**, and **DFS** algorithms.  
  - Visualization of how pruning parameters and thresholds influence runtime.  

### How to Run

After activating the Python environment (e.g., `conda activate hockey-keys`), start Jupyter Notebook or JupyterLab using:
```bash
jupyter lab
```

## Framework Evaluation

The **framework evaluation** experiments analyze the computational performance of the key analysis framework under different data scales — examining how the **number of columns** and **number of rows** affect the runtime of **UR** computation. Two evaluation notebooks are provided under the `evaluation/` directory:

- **`change_col.ipynb`** — studies how execution time scales with the **number of columns** (key length).  
  - The experiment fixes the number of rows (e.g., 7,000) and gradually increases the column combination size to observe runtime growth.  
  - Generated runtime plots and fitted curves (linear, polynomial, and exponential) are automatically saved in:
    ```
    /result/colRunTime/
    ```

- **`change_row.ipynb`** — studies how execution time changes with the **number of rows** in the table.  
  - The experiment fixes the column combination and varies row count (e.g., 20%, 40%, 60%, 80%, and 100% of total rows).  
  - Generated runtime plots and fitting results are stored in:
    ```
    /result/rowRunTime/
    ```

Both notebooks automatically connect to the local **Hockey database** created during data initialization.  
The results confirm that execution time grows approximately **linearly** with both the number of columns and the number of rows, aligning with the expected computational complexity of uniqueness validation.







