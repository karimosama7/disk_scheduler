#!/usr/bin/env python3
import random
import sys
import argparse


def fcfs(requests, initial_head):
    """
    First-Come-First-Served (FCFS) disk scheduling algorithm.
    Processes requests in the order they arrive.
    """
    movements = 0
    current_head = initial_head
    sequence = [initial_head]

    for req in requests:
        movements += abs(req - current_head)
        current_head = req
        sequence.append(req)

    return movements, sequence


def scan(requests, initial_head, max_cylinder=4999):
    """
    SCAN disk scheduling algorithm (Elevator Algorithm).
    Moves head in one direction until it reaches the end, then reverses.
    """
    movements = 0
    current_head = initial_head
    sequence = [initial_head]

    # Sort all requests
    remaining = sorted(requests)

    # Find requests greater than initial head position
    greater = [r for r in remaining if r >= current_head]

    # Find requests less than initial head position
    lesser = [r for r in remaining if r < current_head]
    lesser.sort(reverse=True)  # For the backward direction

    # First service all requests greater than head position
    for req in greater:
        movements += abs(req - current_head)
        current_head = req
        sequence.append(req)

    # If we're not already at the end, go to the end
    if greater and greater[-1] < max_cylinder:
        movements += abs(max_cylinder - current_head)
        current_head = max_cylinder
        sequence.append(max_cylinder)

    # Then reverse direction and service all requests less than head position
    for req in lesser:
        movements += abs(req - current_head)
        current_head = req
        sequence.append(req)

    return movements, sequence


def c_scan(requests, initial_head, max_cylinder=4999, min_cylinder=0):
    """
    C-SCAN (Circular SCAN) disk scheduling algorithm.
    Like SCAN but returns to the beginning after reaching the end.
    """
    movements = 0
    current_head = initial_head
    sequence = [initial_head]

    # Sort all requests
    remaining = sorted(requests)

    # Find requests greater than initial head position
    greater = [r for r in remaining if r >= current_head]

    # Find requests less than initial head position
    lesser = [r for r in remaining if r < current_head]

    # First service all requests greater than head position
    for req in greater:
        movements += abs(req - current_head)
        current_head = req
        sequence.append(req)

    # If we have lesser requests, go back to beginning
    if lesser:
        # Go to the end
        if greater and greater[-1] < max_cylinder:
            movements += abs(max_cylinder - current_head)
            current_head = max_cylinder
            sequence.append(max_cylinder)

        # Go back to the beginning (this counts as head movement)
        movements += abs(current_head - min_cylinder)
        current_head = min_cylinder
        sequence.append(min_cylinder)

        # Then service all requests from beginning
        for req in lesser:
            movements += abs(req - current_head)
            current_head = req
            sequence.append(req)

    return movements, sequence


def generate_requests(num_requests=1000, max_cylinder=4999):
    """Generate random cylinder requests."""
    return [random.randint(0, max_cylinder) for _ in range(num_requests)]


def main():
    parser = argparse.ArgumentParser(description="Disk Scheduling Algorithm Simulator")
    parser.add_argument(
        "--initial",
        type=int,
        default=2000,
        help="Initial head position (default: 2000)",
    )
    parser.add_argument(
        "--cylinders",
        type=int,
        default=5000,
        help="Number of cylinders (default: 5000)",
    )
    parser.add_argument(
        "--requests",
        type=int,
        default=1000,
        help="Number of requests to generate (default: 1000)",
    )
    parser.add_argument("--seed", type=int, help="Random seed for reproducibility")
    parser.add_argument(
        "--algorithm",
        choices=["fcfs", "scan", "c-scan", "all"],
        default="all",
        help="Algorithm to run (default: all)",
    )
    parser.add_argument(
        "--show-sequence",
        action="store_true",
        help="Show the sequence of head movements",
    )

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # Check if initial position is valid
    if args.initial < 0 or args.initial >= args.cylinders:
        print(f"Error: Initial head position must be between 0 and {args.cylinders-1}")
        return

    # Generate requests
    requests = generate_requests(args.requests, args.cylinders - 1)

    print(f"Initial head position: {args.initial}")
    print(f"Number of cylinders: {args.cylinders}")
    print(f"Number of requests: {args.requests}")
    print()

    # Run the selected algorithm(s)
    if args.algorithm in ["fcfs", "all"]:
        movements, sequence = fcfs(requests, args.initial)
        print(f"FCFS - Total head movement: {movements}")
        if args.show_sequence:
            print(f"FCFS Sequence: {sequence}")
        print()

    if args.algorithm in ["scan", "all"]:
        movements, sequence = scan(requests, args.initial, args.cylinders - 1)
        print(f"SCAN - Total head movement: {movements}")
        if args.show_sequence:
            print(f"SCAN Sequence: {sequence}")
        print()

    if args.algorithm in ["c-scan", "all"]:
        movements, sequence = c_scan(requests, args.initial, args.cylinders - 1, 0)
        print(f"C-SCAN - Total head movement: {movements}")
        if args.show_sequence:
            print(f"C-SCAN Sequence: {sequence}")
        print()


if __name__ == "__main__":
    main()
