# Boston Housing Tree Modelleri + EDA Akisi

Bu dosya, `boston_tree.py` scriptinin ne yaptigini aciklar. Script Boston Housing veri setini indirir, temel EDA yapar, farkli tree-based regresyon modellerini egitir, modelleri karsilastirir ve gorsel ciktilar uretir.

## 1. Amac

Boston Housing veri setindeki ozellikleri kullanarak `medv` kolonunu tahmin etmek.

Bu problem bir regresyon problemidir, cunku `medv` surekli sayisal bir degerdir.

## 2. Veri Seti

Veri seti su URL'den okunur:

```python
DATA_URL = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
```

Hedef kolon:

```python
TARGET_COLUMN = "medv"
```

Toplam veri yapisi:

```text
506 satir
14 kolon
13 bagimsiz degisken
1 hedef degisken
```

## 3. Kolonlar

| Kolon | Anlami | Rol |
|---|---|---|
| `crim` | Bolgedeki kisi basina dusen suc orani | Feature |
| `zn` | Buyuk konut alanlari icin ayrilmis arazi orani | Feature |
| `indus` | Perakende disi is alanlarinin orani | Feature |
| `chas` | Charles Nehri kenarinda olup olmama bilgisi | Feature |
| `nox` | Nitrik oksit yogunlugu, hava kirliligi gostergesi | Feature |
| `rm` | Konut basina ortalama oda sayisi | Feature |
| `age` | Eski konut orani | Feature |
| `dis` | Boston is merkezlerine agirlikli uzaklik | Feature |
| `rad` | Radyal otoyollara erisim indeksi | Feature |
| `tax` | Emlak vergisi orani | Feature |
| `ptratio` | Ogrenci-ogretmen orani | Feature |
| `b` | Tarihsel ve etik acidan tartismali demografik degisken | Feature |
| `lstat` | Dusuk sosyoekonomik statu oranı | Feature |
| `medv` | Medyan ev degeri | Target |

Not: `b` kolonu etik acidan dikkatli kullanilmasi gereken tartismali bir degiskendir.

## 4. Genel Akis

```text
Veriyi indir
EDA yap
Korelasyonlari hesapla
Grafikleri kaydet
Feature ve target ayrimi yap
Train/test olarak bol
Baseline tree modellerini egit
Baseline metrikleri hesapla
Hyperparameter optimization uygula
Tune edilmis modelleri karsilastir
En iyi tune edilmis modeli sec
Feature importance yazdir
Model grafiklerini kaydet
Decision tree yapisini gorsellestir
```

## 5. EDA Adimlari

`run_eda(df)` fonksiyonu veri setini inceler.

Yazdirilan bilgiler:

- Kolon isimleri
- Ilk 5 satir
- Veri tipleri
- Eksik deger sayilari
- Duplicate satir sayisi
- Istatistiksel ozet
- `medv` hedef degisken ozeti
- `medv` ile feature korelasyonlari

Korelasyon hesaplama:

```python
corr_with_target = (
    df.corr(numeric_only=True)[TARGET_COLUMN]
    .drop(TARGET_COLUMN)
    .sort_values(key=lambda values: values.abs(), ascending=False)
)
```

Burada mutlak korelasyona gore siralama yapilir. Boylece hem pozitif hem negatif iliskiler onemli kabul edilir.

## 6. Tree Modelleri

`boston_tree.py` sadece tree-based algoritmalari kullanir.

Kullanilan modeller:

| Model | Aciklama |
|---|---|
| `DecisionTreeRegressor` | Tek karar agaci modelidir |
| `RandomForestRegressor` | Birden fazla karar agacinin ortalamasini alir |
| `ExtraTreesRegressor` | Random Forest'a benzer, daha rastgele bolunmeler kullanir |
| `GradientBoostingRegressor` | Agaclari sirayla kurarak hatalari azaltir |
| `HistGradientBoostingRegressor` | Gradient boosting'in histogram tabanli hizli versiyonudur |
| `AdaBoostRegressor` | Zayif agaclari agirliklandirarak guclu model olusturur |

## 7. Neden StandardScaler Kullanilmiyor?

Tree tabanli modeller genellikle feature scale degerlerinden fazla etkilenmez.

Ornegin:

- `rm` oda sayisi 3-9 araliginda olabilir.
- `tax` 100-700 araliginda olabilir.

Lineer modellerde bu farklar onemli olabilir. Ancak tree modelleri karar kurallarini esiklere gore kurdugu icin olcekleme zorunlu degildir.

Bu nedenle `boston_tree.py` icinde `StandardScaler` kullanilmaz.

## 8. Train/Test Ayrimi

```python
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]
```

Burada:

- `X`: modele verilen ozellikler
- `y`: tahmin edilmek istenen hedef

Train/test ayrimi:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE,
)
```

Verinin yuzde 80'i egitim, yuzde 20'si test icin kullanilir.

## 9. Model Degerlendirme Metrikleri

Her model test verisinde degerlendirilir.

| Metrik | Anlami | Yorum |
|---|---|---|
| `MAE` | Ortalama mutlak hata | Dusuk olmasi iyidir |
| `MSE` | Ortalama karesel hata | Dusuk olmasi iyidir |
| `RMSE` | Karesel hatanin karekoku | Dusuk olmasi iyidir |
| `R2` | Aciklanan varyans orani | Yuksek olmasi iyidir |

Model secimi `R2` skoruna gore yapilir:

```python
results_df = pd.DataFrame(results).sort_values("R2", ascending=False)
```

En yuksek `R2` skoruna sahip model en iyi model olarak secilir.

## 10. Hyperparameter Optimization

`boston_tree.py` once baseline modelleri egitir. Daha sonra her tree modeli icin hyperparameter optimization uygular.

Kullanilan yontem:

```python
RandomizedSearchCV
```

Bu yontem, verilen parametre araliklarindan rastgele kombinasyonlar secer ve cross-validation ile en iyi kombinasyonu bulmaya calisir.

Temel ayarlar:

```python
CV_FOLDS = 5
N_ITER_SEARCH = 20
```

Anlami:

- `CV_FOLDS = 5`: Egitim verisi 5 parcaya bolunur ve model 5-fold cross-validation ile degerlendirilir.
- `N_ITER_SEARCH = 20`: Her model icin 20 farkli parametre kombinasyonu denenir.
- `scoring="r2"`: En iyi parametreler `R2` skoruna gore secilir.

## 11. Optimize Edilen Parametreler

Her model icin farkli hyperparameter araliklari denenir.

### Decision Tree

Denemeler:

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`

Bu parametreler agacin ne kadar derinlesecegini ve ne kadar detayli bolunme yapacagini kontrol eder.

### Random Forest ve Extra Trees

Denemeler:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`

`n_estimators`, kac adet agac kullanilacagini belirler.

### Gradient Boosting

Denemeler:

- `n_estimators`
- `learning_rate`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `subsample`

`learning_rate` kucukse model daha yavas ama daha dikkatli ogrenir. `n_estimators` ise kac boosting adimi yapilacagini belirler.

### Hist Gradient Boosting

Denemeler:

- `max_iter`
- `learning_rate`
- `max_leaf_nodes`
- `min_samples_leaf`
- `l2_regularization`

Bu model gradient boosting'in daha hizli histogram tabanli versiyonudur.

### AdaBoost Tree

Denemeler:

- `n_estimators`
- `learning_rate`
- `estimator__max_depth`
- `estimator__min_samples_leaf`

Burada `estimator__` ile baslayan parametreler AdaBoost icindeki Decision Tree modeline aittir.

## 12. Baseline ve Tune Edilmis Model Farki

Baseline model, elle verilen varsayilan parametrelerle egitilir.

Tune edilmis model ise `RandomizedSearchCV` sonucunda bulunan en iyi parametrelerle egitilir.

Script iki tablo yazdirir:

- Baseline model sonuclari
- Tune edilmis model sonuclari

Tune edilmis model tablosunda sunlar bulunur:

| Kolon | Anlami |
|---|---|
| `Model` | Model adi |
| `Best CV R2` | Cross-validation uzerindeki en iyi R2 skoru |
| `Test MAE` | Test seti MAE degeri |
| `Test MSE` | Test seti MSE degeri |
| `Test RMSE` | Test seti RMSE degeri |
| `Test R2` | Test seti R2 degeri |
| `Best Params` | Bulunan en iyi hyperparameter kombinasyonu |

Sonuclar ayrica su CSV dosyasina kaydedilir:

```text
outputs_tree/hyperparameter_optimization_results.csv
```

## 13. Feature Importance

Tree modellerinde genellikle `feature_importances_` ozelligi bulunur.

```python
model.feature_importances_
```

Bu degerler modelin tahmin yaparken hangi degiskenlere daha cok onem verdigini gosterir.

Ornegin Boston Housing probleminde genellikle su degiskenler on plana cikar:

- `rm`
- `lstat`
- `dis`
- `ptratio`
- `nox`

## 14. Uretilen Grafikler

Script grafiklerini `outputs_tree/` klasorune kaydeder.

| Dosya | Aciklama |
|---|---|
| `01_correlation_heatmap.png` | Degiskenler arasi korelasyon haritasi |
| `02_medv_distribution.png` | Hedef degisken dagilimi |
| `03_top_feature_scatterplots.png` | En yuksek korelasyonlu feature'larin scatter plotlari |
| `04_best_model_feature_importance.png` | En iyi modelin feature importance grafigi |
| `05_actual_vs_predicted.png` | Gercek degerler ve tahminlerin karsilastirilmasi |
| `06_residuals.png` | Tahmin hatalarinin incelenmesi |
| `07_decision_tree_structure.png` | Decision Tree modelinin ilk seviyeleri |
| `hyperparameter_optimization_results.csv` | Tune edilmis model metrikleri ve en iyi parametreler |

## 15. Actual vs Predicted Grafigi

Bu grafik gercek `medv` degerleri ile modelin tahminlerini karsilastirir.

Iyi bir modelde noktalar kirmizi kesikli cizgiye yakin olur.

```python
plt.plot([min_value, max_value], [min_value, max_value], color="red", linestyle="--")
```

Bu kirmizi cizgi ideal tahmin cizgisidir.

## 16. Residual Analizi

Residual, gercek deger ile tahmin arasindaki farktir.

```python
residuals = y_test - y_pred
```

Residual grafiginde hatalar sifir cizgisi etrafinda rastgele dagiliyorsa model daha dengeli calisiyor demektir.

Sistematik bir sekil varsa model bazi bolgelerde surekli fazla veya eksik tahmin yapiyor olabilir.

## 17. Decision Tree Gorseli

Script `DecisionTreeRegressor` modelinin ilk 3 seviyesini gorsellestirir.

```python
plot_tree(
    decision_tree_model,
    feature_names=feature_names,
    filled=True,
    rounded=True,
    max_depth=3,
)
```

Bu grafik karar agacinin hangi feature'lara gore bolundugunu gosterir.

Ornegin model once `lstat` veya `rm` gibi guclu degiskenlerden bolunmeye baslayabilir.

## 18. Calistirma

Terminalden calistirma:

```powershell
python .\boston_tree.py
```

Calisma sonunda:

- Konsolda EDA bilgileri yazilir.
- Model skor tablosu yazilir.
- Hyperparameter optimization sonuclari yazilir.
- En iyi tune edilmis tree modeli yazilir.
- Feature importance yazilir.
- Grafikler `outputs_tree/` klasorune kaydedilir.

## 19. Kisa Ozet

`boston_tree.py`, Boston Housing veri setinde tree tabanli regresyon modellerini karsilastirmak icin hazirlanmistir.

Bu script ile:

- EDA yapilir.
- Korelasyonlar incelenir.
- Tree modelleri egitilir.
- Modeller metriklerle karsilastirilir.
- Hyperparameter optimization uygulanir.
- En iyi model secilir.
- Feature importance yorumlanir.
- Tahmin hatalari gorsellestirilir.

Bu yapi, tree tabanli modelleri ogrenmek ve lineer modellere gore farklarini anlamak icin kullanisli bir egitim ornegidir.
