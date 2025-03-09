# SRE Training Program: Refresher Course

This repository contains training materials for a refresher course on core programming concepts relevant to Site Reliability Engineering (SRE). The program is designed to accommodate participants with various skill levels and focuses on three key areas:

1. **Data Structures & Algorithms**
2. **Object-Oriented Programming (OOP) Principles**
3. **Basic Scripting**

## Project Focus

This training program caters to three primary learning personas:

1. **Foundational Learners**: Individuals who need a fundamental understanding of concepts. Materials include clearly commented and explained examples.

2. **Refresher Learners**: Individuals with prior exposure who benefit from succinct yet comprehensive examples to quickly recall concepts.

3. **Critical Thinkers (Challenge-driven)**: Learners who engage actively by identifying and rectifying deliberately flawed code examples.

## Repository Structure

Each main topic has its own directory containing:

- `examples/` - Directory with correctly implemented code examples
- Flawed implementation files for review and correction
- `quizzes/` - Directory with quiz questions related to the topic

``` text
training_program/
├── README.md
├── Data_Structures_Algorithms/
│   ├── examples/
│   │   ├── linked_list_example.py
│   │   ├── linked_list_reversal_correct.py
│   │   ├── bfs_tree_example.py
│   │   └── two_sum_example.py
│   ├── linked_list_flawed.py
│   ├── bfs_tree_flawed.py
│   ├── two_sum_flawed.py
│   ├── requirements.txt
│   └── quizzes/
│       └── dsa_quiz.md
├── OOP_Principles/
│   ├── examples/
│   │   ├── ecommerce_example.py
│   │   ├── singleton_logger_example.py
│   ├── ecommerce_flawed.py
│   ├── singleton_logger_flawed.py
│   ├── requirements.txt
│   └── quizzes/
│       └── oop_quiz.md
└── Basic_Scripting/
    ├── examples/
    │   ├── filter_csv_example.py
    │   ├── logs_analysis_example.py
    │   ├── setup_env_example.py
    ├── filter_csv_flawed.py
    ├── logs_analysis_flawed.py
    ├── setup_env_flawed.py
    ├── requirements.txt
    ├── sample_data/
    │   ├── input.csv
    │   └── app.log
    └── quizzes/
        └── scripting_quiz.md
```

## How to Use This Repository

1. **For Learning**: Begin by studying the correctly implemented examples in each topic's `examples/` directory.

2. **For Practice**: Review the flawed implementations and try to identify and fix the issues.

3. **For Assessment**: Complete the quizzes in each topic's `quizzes/` directory to test your understanding.

## Getting Started

1. Clone this repository or uzip proved file.
2. Install the required dependencies for each section:

   ``` cmd
   cd Data_Structures_Algorithms
   pip install -r requirements.txt
   ```

   Repeat for other directories as needed.

3. Start with the correctly implemented examples to understand the concepts
4. Then challenge yourself with the flawed implementations

## Contributing

If you find any issues or have suggestions for improvements, please submit a pull request or open an issue.
