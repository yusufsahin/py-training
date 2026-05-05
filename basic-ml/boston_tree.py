from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import (
    AdaBoostRegressor,
    ExtraTreesRegressor,
    GradientBoostingRegressor,
    HistGradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree


DATA_URL = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
TARGET_COLUMN = "medv"
OUTPUT_DIR = Path("outputs_tree")
RANDOM_STATE = 42
CV_FOLDS = 5
N_ITER_SEARCH = 20


def print_section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def calculate_rmse(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return np.sqrt(mse)


def save_plot(path):
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()
    print(f"Grafik kaydedildi: {path}")


def load_data():
    print_section("1. Veri Yukleme")
    print(f"Kaynak URL: {DATA_URL}")

    df = pd.read_csv(DATA_URL)
    df.columns = df.columns.str.lower()

    if TARGET_COLUMN not in df.columns:
        raise ValueError(f"Beklenen hedef kolon bulunamadi: {TARGET_COLUMN}")

    print(f"Veri seti yuklendi. Satir/Sutun: {df.shape}")
    return df


def run_eda(df):
    print_section("2. EDA - Genel Veri Analizi")
    print("Kolonlar:")
    print(list(df.columns))

    print("\nIlk 5 satir:")
    print(df.head())

    print("\nVeri tipleri:")
    print(df.dtypes)

    print("\nEksik degerler:")
    print(df.isna().sum())

    print(f"\nDuplicate satir sayisi: {df.duplicated().sum()}")

    print("\nIstatistiksel ozet:")
    print(df.describe().T)

    print_section("3. Hedef Degisken ve Korelasyon")
    print("MEDV hedef degisken ozeti:")
    print(df[TARGET_COLUMN].describe())

    corr_with_target = (
        df.corr(numeric_only=True)[TARGET_COLUMN]
        .drop(TARGET_COLUMN)
        .sort_values(key=lambda values: values.abs(), ascending=False)
    )

    print("\nMEDV ile korelasyonlar:")
    print(corr_with_target)

    return corr_with_target


def create_eda_plots(df, corr_with_target):
    print_section("4. EDA Grafiklerinin Olusturulmasi")
    OUTPUT_DIR.mkdir(exist_ok=True)
    sns.set_theme(style="whitegrid", palette="deep")

    plt.figure(figsize=(12, 9))
    sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Boston Housing Korelasyon Heatmap")
    save_plot(OUTPUT_DIR / "01_correlation_heatmap.png")

    plt.figure(figsize=(9, 5))
    sns.histplot(df[TARGET_COLUMN], bins=30, kde=True)
    plt.title("MEDV Dagilimi")
    plt.xlabel("MEDV")
    plt.ylabel("Frekans")
    save_plot(OUTPUT_DIR / "02_medv_distribution.png")

    top_features = corr_with_target.head(4).index.tolist()
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    axes = axes.ravel()

    for index, feature in enumerate(top_features):
        sns.scatterplot(data=df, x=feature, y=TARGET_COLUMN, ax=axes[index], alpha=0.75)
        axes[index].set_title(f"{feature.upper()} vs MEDV")

    save_plot(OUTPUT_DIR / "03_top_feature_scatterplots.png")


def build_tree_models():
    return {
        "Decision Tree": DecisionTreeRegressor(
            max_depth=4,
            min_samples_leaf=5,
            random_state=RANDOM_STATE,
        ),
        "Random Forest": RandomForestRegressor(
            n_estimators=300,
            max_depth=None,
            min_samples_leaf=1,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "Extra Trees": ExtraTreesRegressor(
            n_estimators=300,
            max_depth=None,
            min_samples_leaf=1,
            random_state=RANDOM_STATE,
            n_jobs=-1,
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=RANDOM_STATE,
        ),
        "Hist Gradient Boosting": HistGradientBoostingRegressor(
            max_iter=200,
            learning_rate=0.05,
            max_leaf_nodes=31,
            random_state=RANDOM_STATE,
        ),
        "AdaBoost Tree": AdaBoostRegressor(
            estimator=DecisionTreeRegressor(max_depth=4, random_state=RANDOM_STATE),
            n_estimators=200,
            learning_rate=0.05,
            random_state=RANDOM_STATE,
        ),
    }


def build_hyperparameter_search_spaces():
    return {
        "Decision Tree": {
            "max_depth": [2, 3, 4, 5, 6, 8, 10, None],
            "min_samples_split": [2, 5, 10, 20],
            "min_samples_leaf": [1, 2, 4, 6, 8],
            "max_features": [None, "sqrt", "log2"],
        },
        "Random Forest": {
            "n_estimators": [100, 200, 300, 500],
            "max_depth": [3, 5, 8, 10, None],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "max_features": [1.0, "sqrt", "log2"],
        },
        "Extra Trees": {
            "n_estimators": [100, 200, 300, 500],
            "max_depth": [3, 5, 8, 10, None],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "max_features": [1.0, "sqrt", "log2"],
        },
        "Gradient Boosting": {
            "n_estimators": [100, 200, 300, 500],
            "learning_rate": [0.01, 0.03, 0.05, 0.08, 0.1],
            "max_depth": [2, 3, 4],
            "min_samples_split": [2, 5, 10],
            "min_samples_leaf": [1, 2, 4],
            "subsample": [0.7, 0.85, 1.0],
        },
        "Hist Gradient Boosting": {
            "max_iter": [100, 200, 300, 500],
            "learning_rate": [0.01, 0.03, 0.05, 0.08, 0.1],
            "max_leaf_nodes": [15, 31, 63],
            "min_samples_leaf": [10, 20, 30],
            "l2_regularization": [0.0, 0.01, 0.1, 1.0],
        },
        "AdaBoost Tree": {
            "n_estimators": [50, 100, 200, 300],
            "learning_rate": [0.01, 0.03, 0.05, 0.08, 0.1],
            "estimator__max_depth": [2, 3, 4, 5],
            "estimator__min_samples_leaf": [1, 2, 4],
        },
    }


def evaluate_models(X_train, X_test, y_train, y_test):
    print_section("5. Tree Model Egitimi ve Karsilastirma")
    results = []
    fitted_models = {}

    for model_name, model in build_tree_models().items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results.append(
            {
                "Model": model_name,
                "MAE": mean_absolute_error(y_test, y_pred),
                "MSE": mean_squared_error(y_test, y_pred),
                "RMSE": calculate_rmse(y_test, y_pred),
                "R2": r2_score(y_test, y_pred),
            }
        )
        fitted_models[model_name] = model

    results_df = pd.DataFrame(results).sort_values("R2", ascending=False).reset_index(drop=True)
    print(results_df.to_string(index=False))

    best_model_name = results_df.loc[0, "Model"]
    best_model = fitted_models[best_model_name]

    print(f"\nEn iyi tree modeli: {best_model_name} (R2={results_df.loc[0, 'R2']:.4f})")
    return results_df, best_model_name, best_model, fitted_models


def tune_tree_models(X_train, X_test, y_train, y_test):
    print_section("6. Hyperparameter Optimization")
    models = build_tree_models()
    search_spaces = build_hyperparameter_search_spaces()
    tuned_results = []
    tuned_models = {}

    for model_name, model in models.items():
        print(f"\n{model_name} icin RandomizedSearchCV basladi...")
        search = RandomizedSearchCV(
            estimator=model,
            param_distributions=search_spaces[model_name],
            n_iter=N_ITER_SEARCH,
            scoring="r2",
            cv=CV_FOLDS,
            random_state=RANDOM_STATE,
            n_jobs=-1,
            verbose=0,
        )
        search.fit(X_train, y_train)

        best_model = search.best_estimator_
        y_pred = best_model.predict(X_test)
        tuned_models[model_name] = best_model

        tuned_results.append(
            {
                "Model": model_name,
                "Best CV R2": search.best_score_,
                "Test MAE": mean_absolute_error(y_test, y_pred),
                "Test MSE": mean_squared_error(y_test, y_pred),
                "Test RMSE": calculate_rmse(y_test, y_pred),
                "Test R2": r2_score(y_test, y_pred),
                "Best Params": search.best_params_,
            }
        )

        print(f"En iyi CV R2: {search.best_score_:.4f}")
        print(f"Test R2: {r2_score(y_test, y_pred):.4f}")
        print(f"En iyi parametreler: {search.best_params_}")

    tuned_results_df = (
        pd.DataFrame(tuned_results)
        .sort_values("Test R2", ascending=False)
        .reset_index(drop=True)
    )

    print("\nTune edilmis model sonuclari:")
    print(
        tuned_results_df[
            ["Model", "Best CV R2", "Test MAE", "Test MSE", "Test RMSE", "Test R2"]
        ].to_string(index=False)
    )

    best_tuned_model_name = tuned_results_df.loc[0, "Model"]
    best_tuned_model = tuned_models[best_tuned_model_name]
    print(
        f"\nEn iyi tune edilmis model: {best_tuned_model_name} "
        f"(Test R2={tuned_results_df.loc[0, 'Test R2']:.4f})"
    )

    return tuned_results_df, best_tuned_model_name, best_tuned_model, tuned_models


def get_feature_importance(model, feature_names):
    if not hasattr(model, "feature_importances_"):
        return None

    return pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": model.feature_importances_,
        }
    ).sort_values("Importance", ascending=False)


def explain_best_model(best_model_name, best_model, feature_names):
    print_section("7. En Iyi Tune Edilmis Tree Model Feature Importance")
    importance_df = get_feature_importance(best_model, feature_names)

    if importance_df is None:
        print(f"{best_model_name} modeli feature_importances_ saglamiyor.")
        return None

    print(importance_df.to_string(index=False))

    plt.figure(figsize=(9, 6))
    sns.barplot(data=importance_df.head(10), x="Importance", y="Feature")
    plt.title(f"{best_model_name} - Top 10 Feature Importance")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    save_plot(OUTPUT_DIR / "04_best_model_feature_importance.png")

    return importance_df


def create_model_plots(best_model, X_test, y_test):
    print_section("8. Tahmin ve Residual Grafikleri")
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


def create_decision_tree_plot(decision_tree_model, feature_names):
    print_section("9. Decision Tree Gorseli")
    plt.figure(figsize=(22, 10))
    plot_tree(
        decision_tree_model,
        feature_names=feature_names,
        filled=True,
        rounded=True,
        max_depth=3,
        fontsize=8,
    )
    plt.title("Decision Tree Regressor - Ilk 3 Seviye")
    save_plot(OUTPUT_DIR / "07_decision_tree_structure.png")


def save_hyperparameter_results(tuned_results_df):
    print_section("10. Hyperparameter Optimization Sonuc Kayitlari")
    output_path = OUTPUT_DIR / "hyperparameter_optimization_results.csv"
    results_to_save = tuned_results_df.copy()
    results_to_save["Best Params"] = results_to_save["Best Params"].astype(str)
    results_to_save.to_csv(output_path, index=False)
    print(f"Hyperparameter sonuclari kaydedildi: {output_path}")


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

    _, _, _, baseline_models = evaluate_models(X_train, X_test, y_train, y_test)
    tuned_results_df, best_model_name, best_model, tuned_models = tune_tree_models(
        X_train,
        X_test,
        y_train,
        y_test,
    )
    explain_best_model(best_model_name, best_model, X.columns)
    create_model_plots(best_model, X_test, y_test)
    create_decision_tree_plot(tuned_models.get("Decision Tree", baseline_models["Decision Tree"]), X.columns)
    save_hyperparameter_results(tuned_results_df)

    print_section("11. Tamamlandi")
    print(f"Tum tree model grafikleri '{OUTPUT_DIR.resolve()}' klasorune kaydedildi.")


if __name__ == "__main__":
    main()
