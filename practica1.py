import MetaTrader5 as mt5

# Conexión a MT5
if not mt5.initialize():
    print("Error al inicializar MT5:", mt5.last_error())
    quit()

# Datos de la operación
symbol = "EURUSDm"
lot = 0.1
sl = 200   # stop loss en puntos
tp = 200   # take profit en puntos

# Aseguramos que el símbolo esté en Market Watch
if not mt5.symbol_select(symbol, True):
    print(f"No se pudo habilitar {symbol}")
    mt5.shutdown()
    quit()

# Precio actual
symbol_info = mt5.symbol_info_tick(symbol)

# Crear orden de compra automática
buy_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": symbol_info.ask,
    "sl": symbol_info.ask - sl * mt5.symbol_info(symbol).point,
    "tp": symbol_info.ask + tp * mt5.symbol_info(symbol).point,
    "deviation": 20,
    "magic": 1001,
    "comment": "Compra automática de prueba",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
}

# Enviar orden
result = mt5.order_send(buy_request)
if result.retcode == mt5.TRADE_RETCODE_DONE:
    print("✅ Operación ejecutada con éxito:", result)
else:
    print("❌ Error al ejecutar:", result)

mt5.shutdown()  
	
