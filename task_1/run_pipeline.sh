#!/bin/bash

# Compile the C++ program
g++ -fopenmp matrix_analysis.cpp -o matrix_analysis
if [ $? -ne 0 ]; then
    echo "Compilation failed. Exiting."
    exit 1
fi

# Run the C++ program and pipe its output to the Python script
./matrix_analysis | python3 analyze_performance.py
