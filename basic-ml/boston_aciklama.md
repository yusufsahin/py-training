# Boston Housing Regression + EDA Akisi

Bu dosya, `boston.py` scriptinin ne yaptigini ve makine ogrenmesi akisini adim adim aciklar. Script Boston Housing veri setini indirir, EDA yapar, farkli regresyon modellerini egitir, performanslarini karsilastirir ve grafik ciktilari olusturur.

## 1. Amac

Boston Housing veri setindeki ev ve bolge ozelliklerini kullanarak `medv` kolonunu tahmin etmek.

`medv`, bolgedeki medyan ev degerini temsil eder. Bu nedenle problem bir regresyon problemidir.

## 2. Kullanilan Kutuphaneler

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

Bu kutuphaneler veri okuma, veri analizi ve grafik olusturma icin kullanilir.

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

Bu kutuphaneler modeli egitmek, veriyi bolmek, olcekleme yapmak ve performans metriklerini hesaplamak icin kullanilir.

## 3. Veri Yukleme

```python
DATA_URL = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
TARGET_COLUMN = "medv"
```

Veri internetten CSV olarak okunur.

```python
df = pd.read_csv(DATA_URL)
df.columns = df.columns.str.lower()
```

Kolon isimleri kucuk harfe cevrilir. Boylece `MEDV`, `Medv`, `medv` gibi farkli yazimlardan kaynaklanabilecek sorunlar azaltilir.

## 4. EDA - Exploratory Data Analysis

EDA bolumunde veri seti incelenir.

Script sunlari yazdirir:

- Veri setinin satir ve sutun sayisi
- Kolon isimleri
- Ilk 5 satir
- Veri tipleri
- Istatistiksel ozet
- Eksik deger sayilari
- Tekrarlanan satir sayisi
- Hedef degisken olan `medv` ozeti
- `medv` ile diger degiskenler arasindaki korelasyonlar

Ornek:

```python
df.describe().T
df.isna().sum()
df.duplicated().sum()
```

## 4.1. Kolonlar Ne Anlama Geliyor?

Boston Housing veri setinde toplam 14 kolon vardir. Bunlarin 13 tanesi modele verilen ozelliklerdir. `medv` ise tahmin edilmek istenen hedef degiskendir.

| Kolon | Anlami | Tipi | Modeldeki rolu |
|---|---|---|---|
| `crim` | Bolgedeki kisi basina dusen suc orani | `float64` | Bagimsiz degisken |
| `zn` | 25.000 sq.ft. uzeri konut alanlari icin ayrilmis arazi orani | `float64` | Bagimsiz degisken |
| `indus` | Bolgedeki perakende disi is alanlarinin orani | `float64` | Bagimsiz degisken |
| `chas` | Charles Nehri sinirinda olup olmadigi bilgisi. `1` ise nehir kenari, `0` ise degil | `int64` | Bagimsiz degisken |
| `nox` | Nitrik oksit yogunlugu. Hava kirliligi gostergesi olarak dusunulebilir | `float64` | Bagimsiz degisken |
| `rm` | Konut basina ortalama oda sayisi | `float64` | Bagimsiz degisken |
| `age` | 1940 oncesi insa edilmis sahibi tarafindan kullanilan konutlarin orani | `float64` | Bagimsiz degisken |
| `dis` | Boston'daki bes is merkezine agirlikli uzaklik | `float64` | Bagimsiz degisken |
| `rad` | Radyal otoyollara erisim indeksi | `int64` | Bagimsiz degisken |
| `tax` | 10.000 dolar basina emlak vergisi orani | `int64` | Bagimsiz degisken |
| `ptratio` | Bolgedeki ogrenci-ogretmen orani | `float64` | Bagimsiz degisken |
| `b` | Veri setindeki tarihsel ve tartismali demografik bir degisken | `float64` | Bagimsiz degisken |
| `lstat` | Dusuk sosyoekonomik statu grubundaki nufus orani | `float64` | Bagimsiz degisken |
| `medv` | Sahibi tarafindan kullanilan evlerin medyan degeri. Birim genellikle bin dolar olarak kabul edilir | `float64` | Hedef degisken |

Kisaca:

- `medv` tahmin edilmek istenen ev fiyatidir.
- Diger kolonlar ev fiyatini etkileyebilecek bolgesel, ekonomik, demografik ve yapisal ozelliklerdir.
- `chas`, `rad` ve `tax` `int64` tipindedir; diger sayisal kolonlar cogunlukla `float64` tipindedir.
- Tum kolonlarda 506 adet dolu veri vardir, yani bu veri setinde eksik deger yoktur.

Not: `b` kolonu Boston Housing veri setinin etik acidan tartismali kisimlarindan biridir. Modern projelerde bu tur demografik degiskenler kullanilirken adillik, ayrimcilik ve model yanliligi acisindan dikkatli olunmalidir.

## 5. Korelasyon Analizi

```python
corr_with_target = (
    df.corr(numeric_only=True)[TARGET_COLUMN]
    .drop(TARGET_COLUMN)
    .sort_values(key=lambda values: values.abs(), ascending=False)
)
```

Bu kod her degiskenin `medv` ile ne kadar iliskili oldugunu hesaplar.

Mutlak korelasyona gore siralama yapilir. Yani hem pozitif hem negatif iliskiler onemli kabul edilir.

Ornegin:

- `rm`: oda sayisi arttikca ev degeri artabilir.
- `lstat`: dusuk gelirli nufus orani arttikca ev degeri azalabilir.

## 6. EDA Grafikleri

Script `outputs/` klasorune su grafikleri kaydeder:

| Dosya | Aciklama |
|---|---|
| `01_correlation_heatmap.png` | Degiskenler arasi korelasyon haritasi |
| `02_medv_distribution.png` | Hedef degisken dagilimi |
| `03_top_feature_scatterplots.png` | `medv` ile en iliskili degiskenlerin scatter plotlari |
| `04_outlier_boxplots.png` | Standardize edilmis outlier analizi |
| `05_actual_vs_predicted.png` | Gercek degerler ile tahminlerin karsilastirmasi |
| `06_residuals.png` | Tahmin hatalarinin analizi |

Grafikler su fonksiyonla kaydedilir:

```python
def save_plot(path):
    plt.tight_layout()
    plt.savefig(path, dpi=160, bbox_inches="tight")
    plt.close()
```

## 7. Feature ve Target Ayrimi

```python
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]
```

Burada:

- `X`: modele verilecek bagimsiz degiskenler
- `y`: tahmin edilmek istenen hedef degisken

## 8. Train/Test Ayrimi

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE,
)
```

Verinin yuzde 80'i egitim, yuzde 20'si test icin ayrilir.

`random_state=42` kullanildigi icin sonuc tekrar calistirildiginda ayni train/test bolunmesi elde edilir.

## 9. Kullanilan Modeller

Script su regresyon modellerini karsilastirir:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Lineer modellerde olcekleme kullanilir:

```python
Pipeline(
    [
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ]
)
```

Tree-based modellerde `StandardScaler` zorunlu degildir. Bu nedenle Random Forest ve Gradient Boosting dogrudan kullanilir.

## 10. Model Degerlendirme Metrikleri

Her model test verisi uzerinde degerlendirilir.

| Metrik | Anlam |
|---|---|
| `MAE` | Ortalama mutlak hata |
| `MSE` | Ortalama karesel hata |
| `RMSE` | Hatanin karekoku |
| `R2` | Modelin hedef degiskendeki varyansi aciklama orani |

Genel yorum:

- `MAE`, `MSE`, `RMSE` ne kadar dusukse o kadar iyi.
- `R2` ne kadar yuksekse o kadar iyi.

## 11. En Iyi Model Secimi

```python
results_df = pd.DataFrame(results).sort_values("R2", ascending=False)
best_model_name = results_df.loc[0, "Model"]
```

Modeller `R2` skoruna gore siralanir. En yuksek `R2` skoruna sahip model en iyi model olarak secilir.

## 12. Feature Importance veya Katsayi Analizi

En iyi model tree-based bir modelse:

```python
model_to_explain.feature_importances_
```

Bu degerler hangi degiskenlerin tahminlerde daha etkili oldugunu gosterir.

En iyi model lineer modelse:

```python
model_to_explain.coef_
```

Bu degerler model katsayilarini gosterir.

## 13. Residual Analizi

Residual, gercek deger ile tahmin arasindaki farktir.

```python
residuals = y_test - y_pred
```

Residual grafigi modelin sistematik hata yapip yapmadigini anlamaya yardim eder.

Iyi bir modelde residual degerleri sifir cizgisi etrafinda rastgele dagilmalidir.

## 14. Programin Calisma Noktasi

```python
if __name__ == "__main__":
    main()
```

Bu blok sayesinde script terminalden calistirildiginda `main()` fonksiyonu baslar.

Calistirma komutu:

```powershell
python .\boston.py
```

## 15. Genel Akis

```text
Veriyi indir
EDA yap
Grafikleri kaydet
Feature/target ayrimi yap
Train/test bol
Modelleri egit
Metrikleri hesapla
En iyi modeli sec
Feature importance veya katsayilari yazdir
Tahmin grafiklerini kaydet
```

## 16. Kisa Yorum

Bu proje temel bir makine ogrenmesi regresyon akisini gosterir:

- Veri analizi
- Gorsellestirme
- Model egitimi
- Model karsilastirma
- Model yorumlama
- Tahmin hatasi analizi

Bu yapi daha sonra farkli veri setleri ve farkli regresyon problemleri icin de kullanilabilir.
