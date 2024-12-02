import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

# Načtení dat ze souboru Excel
file_path = "Data_2024.xlsx"  # Cesta k souboru
sheet_name = "Data_regrese"  # Název listu v souboru

# Načtení dat do DataFrame
data_regrese = pd.read_excel(file_path, sheet_name=sheet_name)

# Zobrazení prvních několika řádků
print(data_regrese.head())
print(data_regrese.columns)


data_regrese.rename(columns={'Ping [ms]': 'Ping'}, inplace=True)

# Vytvoření kvadratických proměnných a interakcí
data_regrese['ActiveUsers_sq'] = data_regrese['ActiveUsers'] ** 2
data_regrese['InteractingPct_sq'] = data_regrese['InteractingPct'] ** 2
data_regrese['ScrollingPct_sq'] = data_regrese['ScrollingPct'] ** 2
data_regrese['ActiveUsers_InteractingPct'] = data_regrese['ActiveUsers'] * data_regrese['InteractingPct']
data_regrese['ActiveUsers_ScrollingPct'] = data_regrese['ActiveUsers'] * data_regrese['ScrollingPct']
data_regrese['InteractingPct_ScrollingPct'] = data_regrese['InteractingPct'] * data_regrese['ScrollingPct']

# Základní model s interakcemi a kvadratickými termíny
model = ols("Ping ~ ActiveUsers + InteractingPct + ScrollingPct + ActiveUsers_sq + InteractingPct_sq + ScrollingPct_sq + ActiveUsers_InteractingPct + ActiveUsers_ScrollingPct + InteractingPct_ScrollingPct", data=data_regrese).fit()

# Výsledky modelu
print(model.summary())

# Predikce pro různé kombinace parametrů
parametry = {
    'ActiveUsers': np.linspace(data_regrese['ActiveUsers'].min(), data_regrese['ActiveUsers'].max(), 100),
    'InteractingPct': np.linspace(data_regrese['InteractingPct'].min(), data_regrese['InteractingPct'].max(), 100),
    'ScrollingPct': np.linspace(data_regrese['ScrollingPct'].min(), data_regrese['ScrollingPct'].max(), 100)
}

# Vytvoření mřížky pro testování
from itertools import product
param_combinations = list(product(parametry['ActiveUsers'], parametry['InteractingPct'], parametry['ScrollingPct']))

# Predikce odezvy pro každou kombinaci parametrů
predictions = []
for params in param_combinations:
    prediction = model.predict({
        'ActiveUsers': params[0],
        'InteractingPct': params[1],
        'ScrollingPct': params[2],
        'ActiveUsers_sq': params[0] ** 2,
        'InteractingPct_sq': params[1] ** 2,
        'ScrollingPct_sq': params[2] ** 2,
        'ActiveUsers_InteractingPct': params[0] * params[1],
        'ActiveUsers_ScrollingPct': params[0] * params[2],
        'InteractingPct_ScrollingPct': params[1] * params[2]
    })
    predictions.append(prediction)

# Zjištění kombinace s největší odezvou
max_ping_index = np.argmax(predictions)
best_params = param_combinations[max_ping_index]
print("Nejproblematičtější kombinace parametrů (maximální odezva):", best_params)

# Průměrné hodnoty pro ostatní parametry
mean_active_users = data_regrese['ActiveUsers'].mean()
mean_interacting_pct = data_regrese['InteractingPct'].mean()
mean_scrolling_pct = data_regrese['ScrollingPct'].mean()

# Odhad pro Windows
prediction_windows = model.predict({
    'ActiveUsers': mean_active_users,
    'InteractingPct': mean_interacting_pct,
    'ScrollingPct': mean_scrolling_pct,
    'OSType': 'Windows',
    'ActiveUsers_sq': mean_active_users ** 2,
    'InteractingPct_sq': mean_interacting_pct ** 2,
    'ScrollingPct_sq': mean_scrolling_pct ** 2,
    'ActiveUsers_InteractingPct': mean_active_users * mean_interacting_pct,
    'ActiveUsers_ScrollingPct': mean_active_users * mean_scrolling_pct,
    'InteractingPct_ScrollingPct': mean_interacting_pct * mean_scrolling_pct
})

print(f"Odhadnutá odezva pro uživatele s Windows: {prediction_windows}")

