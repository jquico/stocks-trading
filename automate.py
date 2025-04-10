import subprocess
import sys
import os

# Function to execute scripts sequentially
def run_script(script_path):
    """Executes a script from the given path."""
    try:
        print(f"Running {script_path}...")
        result = subprocess.run(['python', script_path], check=True)
        print(f"{script_path} executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")
        sys.exit(1)

def main():
    # Set the directory where all scripts are located
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # List of scripts to run in order
    scripts = [
        "data/downloader.py",  # Download stock data
        "indicators/base_indicators.py",  # Calculate base indicators
        "indicators/advanced_indicators.py",  # Calculate advanced indicators
        "models/rule_based.py",  # Run rule-based model
        "models/ppo_trainer.py",  # Train PPO model
        "models/hybrid_model.py",  # Run hybrid model (if needed)
        "evaluation/metrics.py",  # Evaluate metrics (optional)
        "evaluation/backtest.py",  # Run backtests
        "train.py",  # Training script (if separate)
        "run_live.py"  # Run live trading (optional)
    ]

    # Iterate over the scripts and execute them
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        run_script(script_path)

if __name__ == "__main__":
    main()
