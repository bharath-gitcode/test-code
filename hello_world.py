def greet(name="World"):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main():
    print(greet())
    print(greet("Bharath"))


if __name__ == "__main__":
    main()
