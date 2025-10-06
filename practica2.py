import MetaTrader5 as mt5
import pandas as pd

# Inicializar conexión
if not mt5.initialize():
    print("Error al inicializar:", mt5.last_error())
    quit()

# Lista de instrumentos de tu portafolio en Exness
symbols = ["EURUSDm", "XAUUSDm", "GBPUSDm", "BTCUSDm"]

for symbol in symbols:
    # Comprobar si el símbolo existe
    info = mt5.symbol_info(symbol)
    if info is None:
        print(f"⚠️ El símbolo {symbol} no existe en este broker.")
        continue
    
    # Descargar 500 velas H1
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 500)

    if rates is None or len(rates) == 0:
        print(f"⚠️ No hay datos para {symbol}. Asegúrate de mostrarlo en Observación del Mercado.")
        continue

    # Convertir a DataFrame
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')

    # Guardar en CSV
    df.to_csv(f"{symbol}_H1.csv", index=False)
    print(f"✅ {symbol} -> {len(df)} velas guardadas en {symbol}_H1.csv")

