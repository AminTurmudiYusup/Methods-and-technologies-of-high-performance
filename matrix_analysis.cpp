#include <iostream>
#include <vector>
#include <chrono>
#include <omp.h>
#include <cstdlib> // For rand()

// Function to initialize a matrix with random values
void initializeMatrix(std::vector<std::vector<double>>& matrix, int n) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = rand() % 100; // Random values between 0 and 99
        }
    }
}

// Function to calculate the trace of a matrix (sum of diagonal elements)
double trace(const std::vector<std::vector<double>>& matrix, int n) {
    double tr = 0.0;
    for (int i = 0; i < n; ++i) {
        tr += matrix[i][i];
    }
    return tr;
}

// Function to perform matrix multiplication (C = A * B)
void multiplyMatrices(const std::vector<std::vector<double>>& A, 
                      const std::vector<std::vector<double>>& B,
                      std::vector<std::vector<double>>& C, int n) {
    #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            C[i][j] = 0.0;
            for (int k = 0; k < n; ++k) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    // Define matrix sizes to test
    std::vector<int> matrix_sizes = {500, 700, 1000};
    // Define the number of threads to test
    std::vector<int> num_threads_list = {1, 2, 4, 8};

    // Seed random number generator
    srand(time(0));

    // Iterate over thread counts
    for (int threads : num_threads_list) {
        // Set the number of threads for OpenMP
        omp_set_num_threads(threads);

        // Iterate over matrix sizes
        for (int n : matrix_sizes) {
            // Create matrices
            std::vector<std::vector<double>> B(n, std::vector<double>(n));
            std::vector<std::vector<double>> C(n, std::vector<double>(n));
            std::vector<std::vector<double>> BC(n, std::vector<double>(n));

            // Initialize matrices with random values
            initializeMatrix(B, n);
            initializeMatrix(C, n);

            // Measure the execution time
            auto start = std::chrono::high_resolution_clock::now();

            // Perform matrix multiplication and trace calculations
            multiplyMatrices(B, C, BC, n);
            double trC = trace(C, n);
            double trBC = trace(BC, n);

            auto end = std::chrono::high_resolution_clock::now();
            std::chrono::duration<double> elapsed = end - start;

            // Output results in the format: matrix_size thread_count execution_time
            std::cout << n << " " << threads << " " << elapsed.count() << std::endl;
        }
    }

    return 0;
}
