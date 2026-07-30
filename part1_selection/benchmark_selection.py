"""Benchmark deterministic and randomized selection algorithms."""

import csv
import random
import time
from pathlib import Path
from statistics import mean

from part1_selection.deterministic_select import deterministic_select
from part1_selection.randomized_select import randomized_select


INPUT_SIZES = [100, 500, 1_000, 5_000, 10_000]
TRIALS = 5

ALGORITHMS = {
    "Deterministic Select": deterministic_select,
    "Randomized Quickselect": randomized_select,
}


def generate_input(size: int, distribution: str) -> list[int]:
    """Generate an input array using the requested distribution."""
    if distribution == "random":
        return [random.randint(0, size * 10) for _ in range(size)]

    if distribution == "sorted":
        return list(range(size))

    if distribution == "reverse_sorted":
        return list(range(size, 0, -1))

    if distribution == "duplicate_heavy":
        return [random.randint(0, 10) for _ in range(size)]

    raise ValueError(f"Unknown distribution: {distribution}")


def measure_algorithm(
    algorithm,
    values: list[int],
    k: int,
) -> float:
    """Run one algorithm and return its execution time in milliseconds."""
    start_time = time.perf_counter()
    result = algorithm(values, k)
    end_time = time.perf_counter()

    expected = sorted(values)[k]

    if result != expected:
        raise AssertionError(
            f"{algorithm.__name__} returned {result}, expected {expected}"
        )

    return (end_time - start_time) * 1000


def run_benchmarks() -> list[dict]:
    """Run benchmarks and return summarized timing results."""
    distributions = [
        "random",
        "sorted",
        "reverse_sorted",
        "duplicate_heavy",
    ]

    results = []

    for distribution in distributions:
        for size in INPUT_SIZES:
            values = generate_input(size, distribution)
            k = size // 2

            for algorithm_name, algorithm in ALGORITHMS.items():
                trial_times = []

                for _ in range(TRIALS):
                    elapsed_ms = measure_algorithm(
                        algorithm,
                        values,
                        k,
                    )
                    trial_times.append(elapsed_ms)

                average_ms = mean(trial_times)

                result = {
                    "algorithm": algorithm_name,
                    "distribution": distribution,
                    "input_size": size,
                    "k": k,
                    "trials": TRIALS,
                    "average_time_ms": round(average_ms, 6),
                    "minimum_time_ms": round(min(trial_times), 6),
                    "maximum_time_ms": round(max(trial_times), 6),
                }

                results.append(result)

                print(
                    f"{algorithm_name:<24} "
                    f"{distribution:<17} "
                    f"n={size:<6} "
                    f"avg={average_ms:.6f} ms"
                )

    return results


def save_results(results: list[dict]) -> None:
    """Save benchmark results to a CSV file."""
    output_directory = Path("results")
    output_directory.mkdir(exist_ok=True)

    output_path = output_directory / "selection_results.csv"

    fieldnames = [
        "algorithm",
        "distribution",
        "input_size",
        "k",
        "trials",
        "average_time_ms",
        "minimum_time_ms",
        "maximum_time_ms",
    ]

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {output_path}")


def main() -> None:
    """Run the benchmark program."""
    random.seed(532)

    print("Selection Algorithm Benchmark")
    print("=" * 80)

    results = run_benchmarks()
    save_results(results)


if __name__ == "__main__":
    main()