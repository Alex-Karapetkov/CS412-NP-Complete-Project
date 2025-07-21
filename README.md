# 🧭 Traveling Salesman Problem (TSP): Approximation vs Exact Algorithms

This project explores and compares **approximation** and **exact** algorithms for solving the **Traveling Salesman Problem (TSP)**, developed as part of the final project for **CS 412: Applied Algorithms** at James Madison University.

---

## 📌 Project Description

The **Traveling Salesman Problem (TSP)** asks:

> “Given a list of cities and the distances between each pair, what is the shortest possible route that visits each city exactly once and returns to the origin city?”

As a classic **NP-hard** problem, TSP is widely applicable in:
- Logistics and delivery optimization
- Telecommunications network design
- Chip manufacturing paths
- Ride-sharing and vehicle routing systems

This project implements:
- A **2-approximation algorithm** using a **Minimum Spanning Tree (Prim's Algorithm)**
- An **exact solution** using the **2-Opt heuristic**

---

## 📁 Repository Structure

The repository is organized with a top-level code_solution/ directory that contains all source code and supporting files. Inside it, you'll find two main Python scripts: 
- cs412_tsp_approx.py, which implements the approximation algorithm using Prim’s Minimum Spanning Tree and a preorder DFS walk
- cs412_tsp_optimal.py, which implements the exact solution using the 2-Opt heuristic.

The gen.py script provides a utility to generate test case input files from user-supplied city coordinates using Euclidean distance. A nested test_cases/ folder includes all test inputs (testcaseX_input.txt) and their corresponding expected outputs (testcaseX_output.txt), along with a run_test_cases.sh script to execute all cases at once and a test_case_results.txt file summarizing output.

## Project Presentation Slides
📄 Project presentation slides are available in the Presentation_Slides/ folder.

---

## 🧪 Test Case Format

Each test case input file (`testcaseX_input.txt`) follows this format:

<number_of_vertices> <number_of_edges>
<vertex1> <vertex2> <distance>
...


Each corresponding output file (`testcaseX_output.txt`) includes:
- Total tour cost
- The tour, space-separated (starting and ending at the same city)

---

## 🚀 How to Run

### ✅ Prerequisites
Make sure **Python 3** is installed on your system.

### ▶️ Run Approximation or Exact Algorithm

```bash
# Run approximation solution
python code_solution/cs412_tsp_approx.py < code_solution/test_cases/testcase1_input.txt
```
# Run exact solution
```bash
python code_solution/cs412_tsp_optimal.py < code_solution/test_cases/testcase1_input.txt
```
🔁 Run All Test Cases
```bash
cd code_solution/test_cases/
bash run_test_cases.sh
```

## 🧠 Algorithms Used
### Approximation (cs412_tsp_approx.py)
- Constructs Minimum Spanning Tree using Prim's Algorithm

- Performs preorder DFS to get a tour

- Time Complexity: O(m log m)

- Guarantee: At most 2× the optimal tour cost

### Exact (cs412_tsp_optimal.py)
- Uses 2-Opt Heuristic to iteratively improve tour

- Time Complexity: O(n³)

- Suitable for smaller graphs due to runtime cost

## 🛠 Input Generator Utility
gen.py allows for generating test cases from city (x, y) coordinates using Euclidean distances.

Example:
``` bash
python code_solution/gen.py
```
Prompts for:

- Number of cities

- Each city’s coordinates

Outputs a output.txt file formatted as TSP input.

📊 Performance Highlights
```
Test Case	Approx. Cost	Exact Cost	Approx. Tour	Exact Tour
2	13	19	a → d → b → e → c → a	b → c → a → d → e → b
3	50	80	a → b → c → d → a	b → a → c → d → b
...	...	...	...	...
```

See test_case_results.txt for full comparison of all test cases.

## 📎 References
- OpenDSA: Hamiltonian Cycle to TSP Reduction

- CS 412 Lecture Notes on Approximation and Heuristic Algorithms

✅ Author
Alex Karapetkov
B.S. in Computer Science – James Madison University (2024)
