from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


DATA_URL = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
TARGET_COLUMN = "medv"
OUTPUT_DIR = Path("outputs")
RANDOM_STATE = 42


def print_section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def calculate_rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def load_data():
    print_section("1. Veri Yukleme")
    print(f"Kaynak URL: {DATA_URL}")
    df = pd.read_csv(DATA_URL)
    df.columns = df.columns.str.lower()

    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"Beklenen hedef kolon bulunamadi: {TARGET_COLUMN}")

    print(f"Veri seti basariyla yuklendi. Satir/Sutun: {df.shape}")
    return df


def run_eda(df):
    print_section("2. Genel Veri Analizi")
    print("Kolonlar:")
    print(list(df.columns))

    print("\nIlk 5 satir:")
    print(df.head())

    print("\nVeri tipleri ve null bilgisi:")
    df.info()

    print("\nIstatistiksel ozet:")
    print(df.describe().T)

    print("\nEksik deger sayilari:")
    print(df.isna().sum())

    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate satir sayisi: {duplicate_count}")

    print_section("3. Hedef Degisken Analizi")
    print(df[TARGET_COLUMN].describe())

    corr_with_target = (
        df.corr(numeric_only=True)[TARGET_COLUMN]
        .drop(TARGET_COLUMN)
        .sort_values(key=lambda values: values.abs(), ascending=False)
    )

    print("\nMEDV ile en yuksek korelasyona sahip degiskenler:")
    print(corr_with_target)

    return corr_with_target


def save_plot(path):
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Grafik kaydedildi: {path}")


def create_eda_plots(df, corr_with_target):
    print_section("4. EDA Grafiklerinin Olusturulmasi")
    OUTPUT_DIR.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid", palette="deep")

    plt.figure(figsize=(12, 9))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Boston Housing Korelasyon Heatmap")
    save_plot(OUTPUT_DIR / "01_correlation_heatmap.png")

    plt.figure(figsize=(9, 5))
    sns.histplot(df[TARGET_COLUMN], kde=True, bins=30)
    plt.title("MEDV Dagilimi")
    plt.xlabel("MEDV - Medyan Ev Degeri")
    plt.ylabel("Frekans")
    save_plot(OUTPUT_DIR / "02_medv_distribution.png")

    top_features = corr_with_target.head(4).index.tolist()
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    axes = axes.ravel()
    for index, feature in enumerate(top_features):
        sns.scatterplot(data=df, x=feature, y=TARGET_COLUMN, ax=axes[index], alpha=0.75)
        axes[index].set_title(f"{feature.upper()} vs MEDV")
    save_plot(OUTPUT_DIR / "03_top_feature_scatterplots.png")

    plt.figure(figsize=(13, 7))
    numeric_df = df.select_dtypes(include=[np.number])
    scaled_df = (numeric_df - numeric_df.mean()) / numeric_df.std()
    sns.boxplot(data=scaled_df, orient="h")
    plt.title("Standardize Edilmis Degiskenlerde Outlier Gorunumu")
    plt.xlabel("Z-score")
    save_plot(OUTPUT_DIR / "04_outlier_boxplots.png")


def build_models():
    return {
        "Linear Regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        ),
        "Ridge Regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", Ridge(alpha=1.0, random_state=RANDOM_STATE)),
            ]
        ),
        "Lasso Regression": Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", Lasso(alpha=0.01, random_state=RANDOM_STATE, max_iter=10000)),
            ]
        ),
        "Random Forest Regressor": RandomForestRegressor(
            n_estimators=300,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "Gradient Boosting Regressor": GradientBoostingRegressor(random_state=RANDOM_STATE),
    }


def evaluate_models(X_train, X_test, y_train, y_test):
    print_section("5. Model Egitimi ve Karsilastirma")
    results = []
    fitted_models = {}

    for name, model in build_models().items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results.append(
            {
                "Model": name,
                "MAE": mean_absolute_error(y_test, y_pred),
                "MSE": mean_squared_error(y_test, y_pred),
                "RMSE": calculate_rmse(y_test, y_pred),
                "R2": r2_score(y_test, y_pred),
            }
        )
        fitted_models[name] = model

    results_df = pd.DataFrame(results).sort_values("R2", ascending=False).reset_index(drop=True)
    print(results_df.to_string(index=False))

    best_model_name = results_df.loc[0, "Model"]
    best_model = fitted_models[best_model_name]
    print(f"\nEn iyi model: {best_model_name} (R2={results_df.loc[0, 'R2']:.4f})")

    return results_df, best_model_name, best_model


def explain_best_model(best_model_name, best_model, feature_names):
    print_section("6. En Iyi Model Feature Analizi")

    model_to_explain = best_model
    if isinstance(best_model, Pipeline):
        model_to_explain = best_model.named_steps["model"]

    if hasattr(model_to_explain, "feature_importances_"):
        importance_df = pd.DataFrame(
            {
                "Feature": feature_names,
                "Importance": model_to_explain.feature_importances_,
            }
        ).sort_values("Importance", ascending=False)
        print(f"{best_model_name} feature importance:")
        print(importance_df.to_string(index=False))
        return importance_df

    if hasattr(model_to_explain, "coef_"):
        coef_df = pd.DataFrame(
            {
                "Feature": feature_names,
                "Coefficient": model_to_explain.coef_,
                "AbsCoefficient": np.abs(model_to_explain.coef_),
            }
        ).sort_values("AbsCoefficient", ascending=False)
        print(f"{best_model_name} katsayilari:")
        print(coef_df[["Feature", "Coefficient"]].to_string(index=False))
        return coef_df

    print("Bu model icin feature importance veya katsayi bilgisi bulunamadi.")
    return None


def create_model_plots(best_model, X_test, y_test):
    print_section("7. Model Degerlendirme Grafiklerinin Olusturulmasi")
    y_pred = best_model.predict(X_test)
    residuals = y_test - y_pred

    plt.figure(figsize=(7, 7))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.8)
    min_value = min(y_test.min(), y_pred.min())
    max_value = max(y_test.max(), y_pred.max())
    plt.plot([min_value, max_value], [min_value, max_value], color="red", linestyle="--")
    plt.title("Actual vs Predicted MEDV")
    plt.xlabel("Gercek MEDV")
    plt.ylabel("Tahmin MEDV")
    save_plot(OUTPUT_DIR / "05_actual_vs_predicted.png")

    plt.figure(figsize=(9, 5))
    sns.scatterplot(x=y_pred, y=residuals, alpha=0.8)
    plt.axhline(0, color="red", linestyle="--")
    plt.title("Residual Analizi")
    plt.xlabel("Tahmin MEDV")
    plt.ylabel("Residual")
    save_plot(OUTPUT_DIR / "06_residuals.png")


def main():
    df = load_data()
    corr_with_target = run_eda(df)
    create_eda_plots(df, corr_with_target)

    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
    )

    print(f"\nTrain boyutu: {X_train.shape}, Test boyutu: {X_test.shape}")

    _, best_model_name, best_model = evaluate_models(X_train, X_test, y_train, y_test)
    explain_best_model(best_model_name, best_model, X.columns)
    create_model_plots(best_model, X_test, y_test)

    print_section("8. Tamamlandi")
    print(f"Tum grafikler '{OUTPUT_DIR.resolve()}' klasorune kaydedildi.")


if __name__ == "__main__":
    main()
