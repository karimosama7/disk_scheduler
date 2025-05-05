# Disk Scheduling Algorithms Simulator

## Team Members
1. Ahmed Hussein Al-Ahmady
2. Ahmed Abdel-Halim Abdel-Halim Al-Ashmawi
3. Al-Zahraa El-Sayed Mohamed Mohamed Salem
4. Ola Tarek Nasr Gohar
5. Karim Osama Bayoumi Saleh

This program simulates and compares three common disk scheduling algorithms:
- **FCFS** (First-Come-First-Served)
- **SCAN** (Elevator Algorithm)
- **C-SCAN** (Circular SCAN)

## Description

The simulator generates a random series of disk cylinder requests and services them according to each scheduling algorithm. It then reports the total head movement required by each algorithm, allowing you to compare their efficiency.

The program simulates a disk with 5,000 cylinders (numbered 0 to 4,999) and by default generates 1,000 random cylinder requests to process.

## Features

- Implements FCFS, SCAN, and C-SCAN disk scheduling algorithms
- Allows customization of initial head position
- Supports varying the number of requests and cylinders
- Provides detailed movement sequences (optional)
- Includes random seed option for reproducible results
- Command-line interface for easy usage

## Requirements

- Python 3.x

## Installation

No installation required. Simply download the `disk_scheduler.py` file to your local machine.

## Usage

### Basic Usage

```bash
python disk_scheduler.py --initial 2000
```

This will run all three algorithms with the initial head position at cylinder 2000.

### Command-Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--initial` | Initial head position | 2000 |
| `--cylinders` | Number of cylinders on the disk | 5000 |
| `--requests` | Number of requests to generate | 1000 |
| `--seed` | Random seed for reproducible results | None |
| `--algorithm` | Algorithm to run (`fcfs`, `scan`, `c-scan`, or `all`) | `all` |
| `--show-sequence` | Show the sequence of head movements | False |

### Examples

1. Run with a specific initial head position:
   ```bash
   python disk_scheduler.py --initial 1500
   ```

2. Run only the SCAN algorithm:
   ```bash
   python disk_scheduler.py --algorithm scan --initial 2500
   ```

3. Use a specific random seed for reproducible results:
   ```bash
   python disk_scheduler.py --seed 42 --initial 1000
   ```

4. Show the detailed sequence of head movements:
   ```bash
   python disk_scheduler.py --initial 500 --show-sequence
   ```

5. Custom number of requests:
   ```bash
   python disk_scheduler.py --requests 500 --initial 1200
   ```

## Algorithm Descriptions

### FCFS (First-Come-First-Served)
- Processes requests in the order they arrive
- Simple but often inefficient for disk scheduling
- Can lead to excessive head movement (high seek times)

### SCAN (Elevator Algorithm)
- Moves the head in one direction until it reaches the end, then reverses
- Resembles how an elevator works (hence the name)
- Generally more efficient than FCFS for disk scheduling
- Reduces the "starvation" problem where some requests might wait too long

### C-SCAN (Circular SCAN)
- Similar to SCAN but instead of reversing direction, it returns to the beginning
- Provides more uniform wait times for sectors
- Treats the cylinders as a circular list
- Typically performs well for systems with heavy disk usage

## Output

The program will output the total head movement required by each algorithm. Lower head movement indicates better performance.

Example output:
```
Initial head position: 2000
Number of cylinders: 5000
Number of requests: 1000

FCFS - Total head movement: 2516677

SCAN - Total head movement: 4558
  
C-SCAN - Total head movement: 9996
```

## License

This project is provided for educational purposes.
