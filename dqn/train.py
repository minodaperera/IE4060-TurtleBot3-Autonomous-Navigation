"""Entry point for training a DQN agent on the maze environment."""

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=Path("dqn/model"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    print(
        f"Training scaffold ready for {args.episodes} episodes. "
        f"Implement the environment and replay loop; models will be saved to {args.output}."
    )


if __name__ == "__main__":
    main()
