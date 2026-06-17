import pandas as pd
import numpy as np

print("="*60)
print("📊 TRANSFORMANDO TU ARCHIVO DE INFLACIÓN")
print("="*60)

# Leer el archivo sin headers
df_raw = pd.read_excel('inflacion.xlsx', sheet_name='inflacion', header=None, dtype=str)

# Los headers están en la fila 5 (índice 5)
headers = df_raw.iloc[5].tolist()
print(f"✅ Headers encontrados: {headers[:5]}...")

# Los datos empiezan desde la fila 6 (índice 6)
datos = df_raw.iloc[6:].copy()

# Asignar los headers
datos.columns = headers

# Limpiar: eliminar columnas que son completamente VACIO
datos = datos.dropna(axis=1, how='all')

# Ver estructura
print(f"📊 Dimensiones originales: {datos.shape}")

# CORRECCIÓN IMPORTANTE: Las columnas están desplazadas
# La columna 'Cifra' está vacía, el código está en 'Serie'
# Vamos a reordenar correctamente

# Renombrar columnas correctamente
columnas_actuales = datos.columns.tolist()
print(f"\n📋 Columnas encontradas: {columnas_actuales[:5]}")

# Crear estructura correcta
df_correcto = pd.DataFrame()

# La primera columna es el Título
df_correcto['Titulo'] = datos[columnas_actuales[0]]

# La segunda columna (Cifra) está vacía, tomamos la tercera columna como Cifra
df_correcto['Cifra'] = datos[columnas_actuales[2]]  # El código está aquí

# La tercera columna original tiene datos repetidos, la omitimos
# Las fechas empiezan desde la columna 3 en adelante
columnas_fechas = columnas_actuales[3:]  # Todas las columnas de fechas

print(f"📅 Columnas de fechas encontradas: {len(columnas_fechas)}")
print(f"📅 Primera fecha: {columnas_fechas[0]}")
print(f"📅 Última fecha: {columnas_fechas[-1]}")

# Crear un DataFrame con los valores de cada serie
lista_datos = []

for idx, fila in datos.iterrows():
    titulo = fila[columnas_actuales[0]]
    cifra = fila[columnas_actuales[2]]  # El código está aquí
    
    # Para cada columna de fecha
    for fecha_col in columnas_fechas:
        valor = fila[fecha_col]
        
        # Solo agregar si hay valor
        if pd.notna(valor) and valor != 'VACIO' and valor != '':
            lista_datos.append({
                'Titulo': titulo,
                'Cifra': cifra,
                'Fecha': fecha_col,
                'Valor': valor
            })

# Crear DataFrame final
df_limpio = pd.DataFrame(lista_datos)

print(f"✅ Datos transformados: {len(df_limpio)} registros")

# Convertir Valor a número
df_limpio['Valor'] = pd.to_numeric(df_limpio['Valor'], errors='coerce')
df_limpio = df_limpio.dropna(subset=['Valor'])

# Convertir Fecha a datetime (limpiando el formato)
df_limpio['Fecha'] = df_limpio['Fecha'].str[:10]  # Tomar solo YYYY-MM-DD
df_limpio['Fecha'] = pd.to_datetime(df_limpio['Fecha'], errors='coerce')
df_limpio = df_limpio.dropna(subset=['Fecha'])

# Agregar columnas útiles
df_limpio['Año'] = df_limpio['Fecha'].dt.year
df_limpio['Mes'] = df_limpio['Fecha'].dt.month
df_limpio['Nombre_Mes'] = df_limpio['Fecha'].dt.strftime('%B')
df_limpio['Dia'] = df_limpio['Fecha'].dt.day

# Extraer el nombre corto de la serie (limpiar el título)
def extraer_nombre_serie(titulo):
    titulo = str(titulo)
    if 'Subyacente' in titulo and 'Mercancías' in titulo:
        return 'Subyacente - Mercancías'
    elif 'Subyacente' in titulo and 'Servicios' in titulo:
        return 'Subyacente - Servicios'
    elif 'Subyacente' in titulo:
        return 'Subyacente'
    elif 'No subyacente' in titulo:
        return 'No Subyacente'
    elif 'Canasta básica' in titulo:
        return 'Canasta Básica'
    elif 'Agropecuarios' in titulo:
        return 'Agropecuarios'
    elif 'Energéticos' in titulo:
        return 'Energéticos'
    else:
        return 'INPC General'

df_limpio['Serie'] = df_limpio['Titulo'].apply(extraer_nombre_serie)

# Ordenar
df_limpio = df_limpio.sort_values(['Serie', 'Fecha']).reset_index(drop=True)

# Guardar archivos
print("\n💾 Guardando archivos...")

# Versión completa
df_limpio.to_excel('inflacion_FINAL.xlsx', index=False)
print("   ✅ inflacion_FINAL.xlsx")

# Versión para tu app (solo lo necesario)
df_app = df_limpio[['Serie', 'Fecha', 'Valor', 'Año', 'Mes']]
df_app.to_excel('inflacion_para_app.xlsx', index=False)
print("   ✅ inflacion_para_app.xlsx")

# Versión CSV
df_limpio.to_csv('inflacion_FINAL.csv', index=False, encoding='utf-8-sig')
print("   ✅ inflacion_FINAL.csv")

# Mostrar estadísticas
print("\n" + "="*60)
print("📊 ESTADÍSTICAS FINALES")
print("="*60)
print(f"📁 Total de registros: {len(df_limpio):,}")
print(f"📅 Rango de fechas: {df_limpio['Fecha'].min()} a {df_limpio['Fecha'].max()}")
print(f"📈 Series únicas: {df_limpio['Serie'].nunique()}")
print(f"📊 Valores - Mín: {df_limpio['Valor'].min():.2f}, Máx: {df_limpio['Valor'].max():.2f}")

print("\n📋 VISTA PREVIA (VERIFICA QUE HAY FECHAS):")
print("="*60)
print(df_app.head(10))

print("\n📋 ÚLTIMOS REGISTROS:")
print(df_app.tail(10))

print("\n" + "="*60)
print("🎉 ¡TRANSFORMACIÓN COMPLETADA CON ÉXITO!")
print("="*60)
print("\n📁 Archivos generados:")
print("   1. inflacion_FINAL.xlsx - Versión completa con todas las columnas")
print("   2. inflacion_para_app.xlsx - Versión ligera para tu aplicación")
print("   3. inflacion_FINAL.csv - Versión CSV")
print("\n✅ TODAS LAS FECHAS ESTÁN EN LA COLUMNA 'Fecha'")
print("   Puedes filtrar por Año, Mes, Serie, etc.")
