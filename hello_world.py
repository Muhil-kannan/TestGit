import sys

def greet(name: str = "World") -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

def main() -> None:
    """Main entry point of the script."""
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(greet(name))

if __name__ == "__main__":
    main()
