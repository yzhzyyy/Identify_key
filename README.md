# Analysis of Candidate Keys in Relational Databases

This repository contains the full implementation, datasets, and experimental results. It provides scripts for reproducing all experiments, including the computation of **Uniqueness Ratio (UR)**, **Completeness Ratio (CR)**, **Specialisation Analysis**, and **Framework Evaluation**.

## -- Initialisation --

All required initialization files are stored in the `/initialisation` folder. To reproduce our results on your own machine, please follow the steps below to install the required Python dependencies. Please make sure you have:

- **Python 3.8+** installed  
  (Recommended: Python 3.8, since our experiments were developed with Python 3.8)

- `pip` available (usually included with Python)

You can check your Python version using:

```bash
python --version
````

### Install Dependencies
Install all required packages using:
```bash
pip install -r initialisation/requirements.txt
```
This will install all packages listed in the requirements.txt file located in the `initialisation/`directory.
### Import Hockey Database (MySQL)

We provide a MySQL dump file so that readers can recreate the `hockey` database locally.
Download `hockey_dump.sql` from this repository.
Run the following command:

```bash
mysql -u root -p < hockey_dump.sql
```



## -- Experiment --

This folder contains all **generated experiment outputs** and the main analysis notebook for the Hockey database. It mainly includes: uniqueness ratio results, visualisations (boxplots + lattices), counter-examples, and near-key lists.

---

### `experiment/boxplot_result/`

Stores **boxplot figures** for each table, showing the distribution of **UR(max)** values grouped by the **size of the column set** (|X|).  
This helps visualise how uniqueness changes when more attributes are included.

---

### `experiment/counter_example_result/`

Stores results for **data duplication visualisation** and **counter-example analysis**.
For each near-key that violates uniqueness, this folder contains:
- a **bar chart** showing the degree-of-violation distribution, and  
- a **pie chart** showing the proportion of different violation degrees.

These plots support manual inspection of duplicated records (dirty data).

---

###`experiment/specialisation_result/`

Stores the generated **specialisation lattice graphs** for selected keys (typically those with `UR(max) = 1.0`),  
including the corresponding **UR(max) / CR values** shown on each node.

---

### `experiment/specialisation_time_result/`

Stores the **runtime comparison plots** associated with the specialisation analysis,  
typically comparing the running time of different exploration strategies (e.g., Normal vs BFS vs DFS).

---

### `experiment/ur_result/`

Stores the computed **UR result CSV files** for each table, usually in the format:

- `{table_name}_result.csv`

---

### `experiment/hockey_analysis.ipynb`

The main Jupyter notebook that runs the full Hockey database analysis workflow

---

### `experiment/near_key_all.csv`

A summary CSV file that collects all extracted **near-keys** across all tables.  This file is used as input for later steps such as specialisation analysis and counter-example inspection.



## -- Evaluation --

This folder contains all experiments and analysis scripts used to evaluate our key analysis results, including both **qualitative** and **quantitative** evaluation.

---

### `evaluation/qualitative_analysis/`

This folder contains the **qualitative analysis** part of the evaluation.  
It focuses on interpreting the discovered keys, validating them against domain semantics, and comparing the results with a **gold standard** (e.g., precision/recall analysis).

- **`dataviadotto_data/`**  
  Stores raw and intermediate outputs generated from **DataViadotto profiling** (default setting/version).

- **`dataviadotto_data_N/`**  
  DataViadotto outputs for a specific configuration/version (e.g., Dirtiness level = N).

- **`results/`**  
  Stores final outputs produced during qualitative analysis (e.g., evaluation summaries, precision/recall tables, classification results, etc.).

- **`analysis_gold_standard.py`**  
  Script for comparing our computed key analysis results against the **gold standard**, typically producing precision/recall statistics and detailed comparison outputs.

- **`analysis_primary_gold.py`**  
  Script for comparing the **PRIMARY KEYs defined in the database schema** against the gold standard (or our computed results), used as an additional baseline comparison.

---

### `evaluation/quantitative_analysis/`

This folder contains the **quantitative analysis** part of the evaluation.  
It focuses on measuring runtime performance and scalability, such as how UR computation time changes with different numbers of columns or rows.

- **`colRunTime/`**  
  Stores runtime plots and outputs for experiments studying the impact of the **number of columns (|X|)** on UR computation time.

- **`rowRunTime/`**  
  Stores runtime plots and outputs for experiments studying the impact of the **number of rows (|r|)** on UR computation time.

- **`change_col.ipynb`**  
  Jupyter notebook for running the **column-scale runtime experiment** (UR runtime vs. column set size).  
  Outputs are typically saved under `colRunTime/`.

- **`change_row.ipynb`**  
  Jupyter notebook for running the **row-scale runtime experiment** (UR runtime vs. number of rows).  
  Outputs are typically saved under `rowRunTime/`.



