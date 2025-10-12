
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

df = pd.read_csv('synthetic_travel_times.csv')
print("Datos cargados:", df.shape)


X = df[['Minuto de viaje programada', 'Hora del día', 'Dia de la semana',
        'Es fin de semana', 'Clima de lluvia', 'Ocupación Estimada', 'Linea']]
y = df['Recorrido minimo observado']


X = pd.get_dummies(X, columns=[inea'], drop_first=True)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestRegressor(
    n_estimators=200,  
    random_state=42,
    n_jobs=-1      
)
model.fit(X_train, y_train)


predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions, squared=False)
r2 = model.score(X_test, y_test)

print("\n=== Resultados del modelo ===")
print(f"Error absoluto medio (MAE): {mae:.3f} minutos")
print(f"Raíz del error cuadrático medio (RMSE): {rmse:.3f} minutos")
print(f"Coeficiente de determinación (R²): {r2:.3f}")

joblib.dump(model, 'rf_travel_time_model.joblib')
pd.Series(X_train.columns).to_csv('model_features.csv', index=False, header=False)

print("\nModelo y features guardados correctamente.")

import matplotlib.pyplot as plt
feat_importance = pd.Series(model.feature_importances_, index=X_train.columns).sort_values(ascending=False)
print("\nImportancia de las características:")
print(feat_importance)

feat_importance.head(10).plot(kind='barh', title='Importancia de las características')
plt.xlabel('Importancia')
plt.show()
