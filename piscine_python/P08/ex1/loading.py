import importlib


def check_depedencies() -> None:
    dep_list = ["numpy", "pandas", "matplotlib", "requests"]
    for dep in dep_list:
        try:
            module = importlib.import_module(dep)
            print(f"[OK] {dep} ({module.__version__}) - is installed.")
        except ImportError:
            print(
                f"[KO] {dep} is not installed.\n"
                "To install it, run the following command:\n"
                f"pip install {dep}\n"
                "or\n"
                f"poetry add {dep}\n"
            )


def run_matrix_analysis(output_file: str = "matrix_analysis.png",
                        data_points: int = 1000) -> None:
    """Generate Matrix-like data with numpy, analyze it with pandas, and """
    """plot it."""
    try:
        np = importlib.import_module("numpy")
        pd = importlib.import_module("pandas")
        plt = importlib.import_module("matplotlib.pyplot")
    except ImportError as error:
        missing_dep = str(error).split("'")[1] if "'" in str(error) else str(
            error)
        print("\nCannot run matrix analysis because a required package is "
              "missing.")
        print(f"Missing dependency: {missing_dep}")
        print("Install with:")
        print("- pip install -r requirements.txt")
        print("- poetry install")
        return

    print("\nAnalyzing Matrix data...")
    print(f"Processing {data_points} data points...")

    rng = np.random.default_rng(42)
    ticks = np.arange(data_points)
    signal_a = rng.normal(0.0, 1.0, data_points)
    signal_b = rng.normal(0.15, 1.1, data_points)
    wave = np.sin(ticks / 40.0) * 0.8

    matrix_score = signal_a - signal_b + wave
    state = np.where(matrix_score >= 0, "REAL_WORLD", "SIMULATION")

    frame = pd.DataFrame(
        {
            "tick": ticks,
            "score": matrix_score,
            "state": state,
        }
    )

    print("State summary:")
    print(frame.groupby("state")["score"].agg([
        "count", "mean", "std"]).to_string())

    print("Generating visualization...")
    fig, ax = plt.subplots(figsize=(10, 5))
    colors = np.where(frame["state"] == "REAL_WORLD", "#1f77b4", "#d62728")
    ax.scatter(frame["tick"], frame["score"], s=10, c=colors, alpha=0.6)
    ax.axhline(0, linestyle="--", linewidth=1, color="#222222")
    ax.set_title("Matrix Data Analysis")
    ax.set_xlabel("Tick")
    ax.set_ylabel("Matrix score")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(output_file, dpi=150)
    plt.close(fig)

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    check_depedencies()
    run_matrix_analysis()


if __name__ == "__main__":
    main()
