"""Entry point for evaluating a trained DQN agent."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=Path("dqn/model"))
    parser.add_argument("--episodes", type=int, default=10)
    args = parser.parse_args()
    print(
        f"Evaluation scaffold ready for {args.episodes} episodes using {args.model}. "
        "Load the trained policy here once the environment is implemented."
    )


if __name__ == "__main__":
    main()
