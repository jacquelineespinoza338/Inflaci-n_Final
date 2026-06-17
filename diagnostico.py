import pandas as pd

print("="*60)
print("DIAGNÓSTICO DEL ARCHIVO")
print("="*60)

# Leer el archivo
df_raw = pd.read_excel('inflacion.xlsx', sheet_name='inflacion', header=None)

print("\nPRIMERAS 15 FILAS:")
for i in range(15):
    fila = df_raw.iloc[i, :8].tolist()
    fila_str = [str(x)[:30] if pd.notna(x) else 'VACIO' for x in fila]
    print(f"Fila {i}: {fila_str}")

print("\nFILA 5 (donde están los títulos):")
fila_5 = df_raw.iloc[5, :15].tolist()
for i, valor in enumerate(fila_5):
    print(f"  Col {i}: {valor}")

input("\nPresiona Enter para cerrar...")
