import pandas as pd
import matplotlib.pyplot as plt


def generate_custom_drift_report():

    train_df = pd.read_csv("data/processed/train_processed.csv")
    test_df = pd.read_csv("data/processed/test_processed.csv")

    numerical_columns = [
        "Amount",
        "Amount_log"
    ]

    plt.style.use("dark_background")

    for column in numerical_columns:

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.hist(
            train_df[column],
            bins=60,
            alpha=0.55,
            label="Train Data"
        )

        ax.hist(
            test_df[column],
            bins=60,
            alpha=0.55,
            label="Test Data"
        )

        ax.set_title(
            f"{column} Drift Analysis",
            fontsize=22,
            pad=20
        )

        ax.set_xlabel(
            column,
            fontsize=14
        )

        ax.set_ylabel(
            "Frequency",
            fontsize=14
        )

        ax.legend(fontsize=12)

        ax.grid(
            alpha=0.15
        )

        plt.tight_layout()

        plt.savefig(
            f"reports/{column}_drift.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    print("Premium drift reports generated successfully")


if __name__ == "__main__":
    generate_custom_drift_report()