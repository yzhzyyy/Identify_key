A key analysis project submitted in partial fulfilment of the requirements for the MSc in Computer Science, the University of Auckland, 2025.
These codes are for examination purposes only and is confidential to the examination process.

# Key Analysis in Relational Database

## Overview
This project focuses on analyzing keys and uniqueness constraints in relational databases, particularly in the presence of missing and duplicate values. Unlike traditional key discovery methods that assume complete data, this framework aims to identify meaningful keys that remain valid despite data quality issues.

## Experimental Environment
- **Operating System**: macOS / Linux / Windows
- **Programming Language**: Python 3.8.18

## Database Source
The project utilizes the **[Hockey Database](https://relational.fel.cvut.cz/dataset/Hockey)**, a structured dataset containing records from hockey competitions. The database includes multiple tables with attributes related to players, teams, and match results. The dataset is used for key analysis experiments, evaluating both performance and accuracy.

## Features
- **Key Discovery & Validation**: Identifies candidate keys and verifies their validity under different conditions.
- **Uniqueness Ratio Computation**: Measures the uniqueness ratio of attribute combinations to detect potential keys.
- **Subkey Analysis**: Constructs hierarchical subkey structures to explore key relationships.
- **Pruning Strategies**: Optimizes breadth-first and depth-first search (BFS & DFS) for efficient subkey identification.
- **Data Visualization**: Generates pie charts and bar charts to illustrate duplicate distributions and key characteristics.



