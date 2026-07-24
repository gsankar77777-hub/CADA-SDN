from entropy import EntropyEngine


def main():

    source_ips = [
        "10.0.0.1",
        "10.0.0.1",
        "10.0.0.2",
        "10.0.0.3",
        "10.0.0.4",
        "10.0.0.5",
        "10.0.0.5",
        "10.0.0.5",
    ]

    entropy = EntropyEngine.shannon(source_ips)

    print("=" * 40)
    print("Shannon Entropy")
    print("=" * 40)
    print(entropy)


if __name__ == "__main__":
    main()