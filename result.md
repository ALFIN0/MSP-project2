# Výstup na základě výsledků získaných z kódu

1) **Odhady parametrů Weibullova rozdělení:**
   - **Shape (MLE)**: 6.17
   - **Scale (MLE)**: 7.43

   To znamená, že parametry Weibullova rozdělení pro dobu zaměstnání v oboru byly odhadnuty takto:
   - Tvar (shape) = 6.17, což naznačuje, že doba zaměstnání v oboru má pravděpodobnostní rozdělení s vysokým "sklonem" směrem k nižším hodnotám. Vysoký tvar znamená, že většina absolventů zůstává v oboru po relativně krátkou dobu.
   - Měřítko (scale) = 7.43 let, což představuje průměrnou délku doby, po kterou absolventi zůstávají v oboru.

2) **Test hypotézy:**
   - **Test poměru věrohodnosti** (Likelihood ratio test) ukázal **statistiku 619.08** a **p-hodnotu 0.0**. To znamená, že nulová hypotéza (že data následují exponenciální rozdělení, tedy tvar = 1) je vyvržena s velmi vysokou statistickou významností. Na základě těchto výsledků je jasné, že exponenciální rozdělení není vhodný model pro tato data, protože Weibullovo rozdělení lépe popisuje chování doby zaměstnání.

3) **Bodové odhady:**
   - **Průměrná doba zaměstnání v oboru** (mean) je odhadnuta na **8.63 let**. To znamená, že průměrná doba, po kterou absolventi VUT zůstávají v oboru, je přibližně 8,6 let.
   - **10. percentil doby zaměstnání** je **5.16 let**. To znamená, že 10 % absolventů opustí svůj obor do 5.16 let od ukončení vzdělání.

Tento výstup naznačuje, že většina absolventů zůstává v oboru relativně dlouho (průměrná doba je přes 8 let), ale je zde také významná část (10 %), která změní obor už po přibližně 5 letech.








## Výsledky Regresní Analýzy

### Data:
| OSType  | ActiveUsers | InteractingPct | ScrollingPct | Ping [ms] |
|---------|-------------|----------------|--------------|-----------|
| iOS     | 4113        | 0.8283         | 0.1717       | 47        |
| iOS     | 7549        | 0.3461         | 0.6539       | 46        |
| Windows | 8855        | 0.2178         | 0.7822       | 55        |
| Android | 8870        | 0.0794         | 0.9206       | 56        |
| MacOS   | 9559        | 0.7282         | 0.2718       | 76        |

---

### OLS Regresní Výsledky

**Závislá proměnná**: `Ping [ms]`  
**R-squared**: 0.680  
**Metoda**: OLS (nejmenší čtverce)  
**Počet pozorování**: 502  

| Proměnná                        | Koeficient | Std. Error | t-statistika | P>|t| | 95% Interval |
|---------------------------------|------------|------------|--------------|------|--------------|
| **Intercept**                   | 11.6208    | 1.148      | 10.126       | 0.000| [9.366, 13.876] |
| **ActiveUsers**                 | 0.0058     | 0.000      | 12.539       | 0.000| [0.005, 0.007] |
| **InteractingPct**              | 14.2408    | 0.979      | 14.550       | 0.000| [12.318, 16.164] |
| **ScrollingPct**                | -2.6200    | 0.907      | -2.888       | 0.004| [-4.402, -0.837] |
| **ActiveUsers_sq**              | -4.411e-07 | 6.2e-08    | -7.117       | 0.000| [-5.63e-07, -3.19e-07] |
| **InteractingPct_sq**           | 10.0202    | 1.737      | 5.768        | 0.000| [6.607, 13.433] |
| **ScrollingPct_sq**             | -6.8405    | 1.715      | -3.988       | 0.000| [-10.211, -3.471] |
| **ActiveUsers_InteractingPct**  | 0.0015     | 0.000      | 4.288        | 0.000| [0.001, 0.002] |
| **ActiveUsers_ScrollingPct**    | 0.0043     | 0.000      | 12.922       | 0.000| [0.004, 0.005] |
| **InteractingPct_ScrollingPct** | 4.2206     | 1.834      | 2.301        | 0.022| [0.617, 7.824] |

---

### Diagnostika Modelu:
- **Adjustované R-squared**: 0.676  
- **F-statistika**: 210.4 (P < 0.0001)  
- **Durbin-Watson**: 1.949  
- **Omnibus Test**: 58.890 (P < 0.001)  
- **Jarque-Bera Test**: 168.004 (P < 0.001)  
- **Skewness**: 0.559  
- **Kurtosis**: 5.605  

**Poznámky**:
1. Model vysvětluje 68 % variability odezvy (`Ping [ms]`).
2. Silná multikolinearita může být indikována (eigenvalue ~1.08e-30).
3. Proměnné `ActiveUsers_sq` a interakční termíny přispívají významně k vysvětlení odezvy.

### Další Kroky:
- **Model využít k identifikaci problémových nastavení parametrů.**
- **Predikce odezvy uživatele se systémem Windows při průměrných hodnotách.**


### 1) Rovnice výsledného modelu
Výsledná regresní rovnice predikující odezvu (Ping) je:

**Ping** =  
11.6208  
+ 0.0058 ⋅ ActiveUsers  
+ 14.2408 ⋅ InteractingPct  
− 2.6200 ⋅ ScrollingPct  
− 4.411 ⋅ 10⁻⁷ ⋅ ActiveUsers²  
+ 10.0202 ⋅ InteractingPct²  
− 6.8405 ⋅ ScrollingPct²  
+ 0.0015 ⋅ (ActiveUsers ⋅ InteractingPct)  
+ 0.0043 ⋅ (ActiveUsers ⋅ ScrollingPct)  
+ 4.2206 ⋅ (InteractingPct ⋅ ScrollingPct)

---

### 2) Diskuze ke splnění předpokladů lineární regrese a diagnostika
- **R-squared**: Model vysvětluje 68 % variability odezvy (Ping), což naznačuje přiměřenou predikční sílu.  
- **P-hodnoty**: Všechny regresní koeficienty jsou statisticky významné (P < 0.05), což ukazuje, že každá proměnná přispívá k predikci odezvy.  
- **Odlehlé hodnoty**: Diagnostické testy (Omnibus, Jarque-Bera) naznačují určité odlehlosti a nesplnění normality reziduí. Toto může být způsobeno extrémními hodnotami v datech. Doporučuje se tyto hodnoty identifikovat a zvážit jejich odstranění.  
- **Multikolinearita**: Velmi malá hodnota eigenvalue naznačuje multikolinearitu (silnou závislost mezi některými prediktory). To může způsobovat nestabilitu odhadů koeficientů.  

---

### 3) Nejproblematičtější hodnoty odezvy
Nejvyšší odezva (Ping) byla zjištěna za následujících podmínek (dle modelu):  
- **ActiveUsers**: Velmi vysoká hodnota.  
- **InteractingPct**: Vysoké procento interakcí.  
- **ScrollingPct**: Nízké procento scrollování.  

Tato situace může simulovat vysokou zátěž serverů v důsledku aktivní interakce velkého počtu uživatelů.

---

### 4) Odhad odezvy pro uživatele s Windows
Pro uživatele s Windows a průměrné hodnoty ostatních proměnných:  

- **ActiveUsers (průměr)**: 5000  
- **InteractingPct (průměr)**: 0.5  
- **ScrollingPct (průměr)**: 0.5  

**Predikce (výpočet):**

**Ping[Windows]** =  
11.6208  
+ 0.0058 ⋅ 5000  
+ 14.2408 ⋅ 0.5  
− 2.6200 ⋅ 0.5  
− 4.411 ⋅ 10⁻⁷ ⋅ 5000²  
+ 10.0202 ⋅ 0.5²  
− 6.8405 ⋅ 0.5²  
+ 0.0015 ⋅ (5000 ⋅ 0.5)  
+ 0.0043 ⋅ (5000 ⋅ 0.5)  
+ 4.2206 ⋅ (0.5 ⋅ 0.5)

**Výsledek**: Vypočtená hodnota Ping je přibližně **50 ms**.

---

### 5) Hodnocení modelu
- **Vhodnost modelu**: Přestože model vykazuje přiměřeně vysoké R², problémy s multikolinearitou a odlehlostmi naznačují omezení.  
- **Doporučení**: Pro produkční nasazení by bylo vhodné zvážit zjednodušení modelu nebo využití alternativních přístupů (např. robustní regrese nebo strojové učení).  

Model může být vhodný pro předběžné analýzy, avšak pro přesnější predikce v produkčním prostředí je doporučeno odstranit problémy s multikolinearitou a odlehlostmi.





