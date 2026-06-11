# CLI Alarm Clock

A lightweight, purely terminal-based Python alarm clock built as a 30-minute technical exercise. 

## Engineering Decisions & AI Usage
During this rapid-build exercise, AI was utilized as a sounding board to refine the architecture and accelerate boilerplate generation. 
* **Concurrency:** Chose the `threading` library to separate the blocking CLI input (`Main Thread`) from the alarm polling mechanism (`Daemon Thread`). 
* **State Management:** Opted for an in-memory Python list for storage. A database/JSON file was intentionally excluded to stay strictly within the 30-minute MVP scope.
* **Audio Alerts:** Leveraged macOS's native `afplay` command via `os.system` to play a system sound without introducing heavy third-party dependencies.

## Requirements
* Python 3.x
* macOS (for audio alerts)

## How to Run
1. Clone the repository.
2. Run the script from your terminal:
   ```base
   python3 alarm.py
