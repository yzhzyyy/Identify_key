# Analysis of Candidate Keys in Relational Databases

This repository contains the full implementation, datasets, and experimental results. It provides scripts for reproducing all experiments, including the computation of **Uniqueness Ratio (UR)**, **Completeness Ratio (CR)**, **Specialisation Analysis**, and **Framework Evaluation**.

## -- Initialisation --

All required initialization files are stored in the `/initialisation` folder.  

To reproduce our results on your own machine, please follow the steps below to install the required Python dependencies.


### 1. Prerequisites

Please make sure you have:

- **Python 3.8+** installed  
  (Recommended: Python 3.8, since our experiments were developed with Python 3.8)

- `pip` available (usually included with Python)

You can check your Python version using:

```bash
python --version
````

### 2. Install Dependencies
Install all required packages using:
```bash
pip install -r initialisation/requirements.txt
```
This will install all packages listed in the requirements.txt file located in the `initialisation/`directory.
### 3. Import Hockey Database (MySQL)

We provide a MySQL dump file so that readers can recreate the `hockey` database locally.
Download `hockey_dump.sql` from this repository.
Run the following command:

```bash
mysql -u root -p < hockey_dump.sql
```



## -- Experimental Notebooks --

All experiments are implemented in Jupyter notebooks under the `experiment/` directory.  
The **main notebook** for reproducing our experimental results is:

- **`experiment/hockey_analysis.ipynb`** — contains the complete experimental workflow, including:
  - Loading the local **Hockey** database and preparing the experimental data.
  - Computing the **Uniqueness Ratio (UR)** and **Completeness Ratio (CR)**.
  - Generating UR/CR distribution visualizations.
  - Selecting **Top-k tables** and plotting the **Degree-of-Violation** distribution.
  - Generating **Specialisation analysis** graph and evaluate the running time.

To reproduce the experiments, please run `experiment/hockey_analysis.ipynb` from start to finish.


## -- Framework Evaluation --

The **framework evaluation** experiments analyze the computational performance of the key analysis framework under different data scales — examining how the **number of columns** and **number of rows** affect the runtime of **UR** computation. Two evaluation notebooks are provided under the `evaluation/` directory:

- **`change_col.ipynb`** — studies how execution time scales with the **number of columns** (key length).  
  - The experiment fixes the number of rows (e.g., 7,000) and gradually increases the column combination size to observe runtime growth.  
  - Generated runtime plots and fitted curves (linear, polynomial, and exponential) are automatically saved in:
    ```
    /evaluation/colRunTime/
    ```

- **`change_row.ipynb`** — studies how execution time changes with the **number of rows** in the table.  
  - The experiment fixes the column combination and varies row count (e.g., 20%, 40%, 60%, 80%, and 100% of total rows).  
  - Generated runtime plots and fitting results are stored in:
    ```
    /evaluation/rowRunTime/
    ```

Both notebooks automatically connect to the local **Hockey database** created during data initialization.  
The results confirm that execution time grows approximately **linearly** with both the number of columns and the number of rows, aligning with the expected computational complexity of uniqueness validation.







