import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

st.markdown("""
<style>

/* Fondo principal */
.stApp {
    background-color: #0e1117;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1c1f26;
}

/* Títulos */
h1, h2, h3 {
    color: #00c8ff;
}

/* Métricas */
div[data-testid="metric-container"] {
    background-color: #262730;
    border-radius: 10px;
    padding: 10px;
    color: white;
}

/* Botones */
button {
    background-color: #00c8ff !important;
    color: black !important;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)


st.image(
    "inflacion.jpg",
    use_container_width=True,
    caption="Análisis del comportamiento de la inflación"
)

# =====================
# CONFIGURACIÓN
# =====================
st.set_page_config(
    page_title="Dashboard Inflación",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<div style='text-align:center; padding:10px;'>
    <h1 style='color:#00c8ff;'>📊 Dashboard de Inflación Interactivo</h1>
    <p style='color:gray;'>Análisis económico, visualización de datos y predicción con Machine Learning</p>
</div>
""", unsafe_allow_html=True)
# =====================
# CARGA DE DATOS
# =====================
df = pd.read_csv(
    "inflacion.csv",
    encoding="utf-8-sig"
)

df.columns = df.columns.str.strip().str.lower()
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
df = df.dropna(subset=["valor", "fecha"])
df = df.sort_values("fecha")


# =====================
# MENÚ DE NAVEGACIÓN
# =====================
tab1, tab2 = st.tabs(["🏠 Información", "📊 Dashboard"])

with tab1:
    
    # =====================
    # TÍTULO + INTRODUCCIÓN
    # =====================
    st.markdown("""
    <div style="
    background: linear-gradient(90deg,#0f2027,#203a43,#2c5364);
    padding:30px;
    border-radius:15px;
    text-align:center;
    ">

    <h1 style="color:white;font-size:45px;">
    📊 Dashboard Interactivo de Inflación
    </h1>

    <h4 style="color:#00c8ff;">
    Análisis Económico • Ciencia de Datos • Machine Learning
    </h4>

    <p style="color:white;font-size:18px;">
    Visualización interactiva del comportamiento histórico de la inflación,
    comparación entre años y generación de predicciones mediante Regresión Lineal.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.info("📈 Análisis de tendencias económicas")

    col2.success("🤖 Predicción con Machine Learning")

    col3.warning("📊 Visualización interactiva de datos")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    ## 🧠 Introducción

    La inflación es uno de los indicadores económicos más importantes de un país, ya que refleja la variación general de los precios de bienes y servicios durante un periodo determinado. Su estudio permite conocer el comportamiento de la economía y el poder adquisitivo de la población.

    Cuando la inflación aumenta de manera considerable, el costo de vida también se incrementa, afectando el consumo, el ahorro y la inversión. Por el contrario, una inflación controlada contribuye a la estabilidad económica y al crecimiento sostenible.

    El presente dashboard tiene como finalidad analizar la evolución histórica de la inflación mediante la visualización de datos estadísticos, indicadores clave y modelos de predicción basados en aprendizaje automático. A través de diferentes gráficas interactivas es posible identificar tendencias, comparar periodos y apoyar la toma de decisiones mediante información clara y objetiva.

    ## 🎯 Objetivo General

    Desarrollar un dashboard interactivo que permita analizar el comportamiento de la inflación utilizando herramientas de ciencia de datos y visualización, facilitando la interpretación de la información mediante indicadores, gráficos y modelos predictivos.

    ## 🎯 Objetivos Específicos

    * Analizar la evolución histórica de la inflación.
    * Identificar tendencias y variaciones a lo largo del tiempo.
    * Comparar el comportamiento de la inflación entre diferentes años.
    * Generar predicciones mediante un modelo de regresión lineal.
    * Aplicar análisis de correlación para conocer la relación entre las variables del conjunto de datos.
    * Facilitar la interpretación de la información mediante un dashboard dinámico e interactivo.

    """)

    st.divider()


    # =====================
    # ¿QUÉ ES LA INFLACIÓN?
    # =====================

    st.header("📚 ¿Qué es la inflación?")

    st.info("""
    La inflación es el aumento generalizado y sostenido de los precios de bienes y servicios
    durante un periodo determinado. Cuando la inflación aumenta, el poder adquisitivo del dinero
    disminuye, por lo que las personas pueden comprar menos productos con la misma cantidad de dinero.
    """)

    # =====================
    # CAUSAS
    # =====================

    st.header("⚠️ Principales causas de la inflación")

    col1, col2 = st.columns(2)

    with col1:
        st.success("""
    • Exceso de demanda.

    • Aumento del consumo.

    • Mayor circulación de dinero.

    • Crecimiento económico acelerado.
    """)

    with col2:
        st.warning("""
    • Incremento en costos de producción.

    • Aumento del precio de materias primas.

    • Factores internacionales.

    • Crisis económicas.
    """)

    # =====================
    # CONSECUENCIAS
    # =====================

    st.header("📉 Consecuencias de la inflación")

    st.error("""
    • Disminución del poder adquisitivo.

    • Incremento del costo de vida.

    • Reducción del ahorro.

    • Incertidumbre económica.

    • Afectación en la inversión y el consumo.
    """)

    # =====================
    # IMPORTANCIA
    # =====================

    st.header("🌟 Importancia del análisis de la inflación")

    st.write("""
    El análisis de la inflación permite comprender el comportamiento económico de un país,
    identificar tendencias en los precios y apoyar la toma de decisiones de gobiernos,
    empresas y ciudadanos mediante información basada en datos.
    """)

    st.divider()

with tab2:
    
    st.success("""
    ✅ Ya conoces los conceptos básicos de la inflación.

    A continuación puedes explorar los datos históricos mediante gráficos,
    indicadores y modelos predictivos.
    """)

    # =====================
    # FILTROS (CORREGIDO SIN ROMPER TU ESTRUCTURA)
    # =====================
    serie = st.selectbox("📌 Selecciona Serie", df["serie"].unique())
    anio = st.selectbox(
        "📅 Selecciona Año",
        sorted(df["año"].unique())
    )
    df_f = df[
        (df["serie"] == serie) &
        (df["año"] == anio)
    ]


    st.header("📊 Análisis Interactivo de la Inflación")

    # =====================
    # KPIs MEJORADOS
    # =====================
    st.markdown("### 📊 Indicadores Clave")
    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"""
    <div style='background:#262730;padding:15px;border-radius:10px;text-align:center'>
    <h4>📊 Promedio</h4>
    <h2>{round(df_f["valor"].mean(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div style='background:#262730;padding:15px;border-radius:10px;text-align:center'>
    <h4>📈 Máximo</h4>
    <h2>{round(df_f["valor"].max(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div style='background:#262730;padding:15px;border-radius:10px;text-align:center'>
    <h4>📉 Mínimo</h4>
    <h2>{round(df_f["valor"].min(),2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown(f"""
    <div style='background:#262730;padding:15px;border-radius:10px;text-align:center'>
    <h4>📌 Último valor</h4>
    <h2>{round(df_f["valor"].iloc[-1],2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style='background:#1f6feb;padding:10px;border-radius:10px;text-align:center;margin-top:10px'>
    <h4>🔄 Cambio total</h4>
    <h2>{round(df_f["valor"].iloc[-1] - df_f["valor"].iloc[0],2)}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =====================
    # GRÁFICA POR AÑO
    # =====================
    st.subheader("📊 Inflación por Año")

    fig_year = px.line(
        df_f,
        x="fecha",
        y="valor",
        markers=True,
        title=f"Inflación del año"
    )

    fig_year.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Valor de la inflación (%)"
    )

    st.plotly_chart(fig_year, use_container_width=True)

    st.info("""
    Esta gráfica muestra la evolución de la inflación durante el año seleccionado,
    permitiendo identificar periodos de crecimiento, disminución o estabilidad.
    """)

    # =====================
    # GRÁFICA POR MES
    # =====================
    st.subheader("📊 Inflación por mes")

    orden_meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]

    # Copia de los datos
    df_mes = df_f.copy()

    # Ordenar los meses correctamente
    df_mes["nombre_mes"] = pd.Categorical(
        df_mes["nombre_mes"],
        categories=orden_meses,
        ordered=True
    )

    # Selector de mes
    mes = st.selectbox(
        "🗓️ Selecciona un mes",
        orden_meses
    )

    # Filtrar el mes seleccionado
    df_mes_filtrado = df_mes[df_mes["nombre_mes"] == mes]

    # Gráfica
    fig_mes = px.bar(
        df_mes_filtrado,
        x="nombre_mes",
        y="valor",
        text="valor",
        color="valor",
        title=f"Inflación del mes de {mes} - {anio}"
    )

    fig_mes.update_layout(
        xaxis_title="Mes",
        yaxis_title="Valor de la inflación (%)",
        showlegend=False
    )

    st.plotly_chart(fig_mes, use_container_width=True)

    st.info(f"""
    La gráfica muestra el valor de la inflación correspondiente al mes de **{mes}**
    del año **{anio}**, permitiendo analizar el comportamiento de ese periodo específico.
    """)

    # =====================
    # MEJORES MESES
    # =====================
    st.subheader("🏆 Meses con mayor inflación")

    top = df_f.sort_values(
        "valor",
        ascending=False
    )[["nombre_mes", "valor"]].head(5)

    st.dataframe(top, use_container_width=True)

    mayor = df_f.loc[df_f["valor"].idxmax()]
    menor = df_f.loc[df_f["valor"].idxmin()]

    st.success(f"📈 Mayor inflación: {mayor['nombre_mes']} ({mayor['valor']:.2f} %)")

    st.info(f"📉 Menor inflación: {menor['nombre_mes']} ({menor['valor']:.2f} %)")
    # =====================
    # COMPARACIÓN ENTRE AÑOS
    # =====================
    st.subheader("📊 Comparación entre Años")

    years = st.multiselect(
        "📊 Selecciona años para comparar",
        sorted(df["año"].unique())
    )

    df_compare = df[df["año"].isin(years)]

    if len(years) > 0:

        fig_compare = px.line(
            df_compare,
            x="fecha",
            y="valor",
            color="año",
            markers=True,
            title="Comparación de inflación por años"
        )

        fig_compare.update_layout(
            xaxis_title="Fecha",
            yaxis_title="Valor de la inflación (%)",
            legend_title="Año"
        )

        st.plotly_chart(fig_compare, use_container_width=True)

        st.info("""
    Esta gráfica compara la inflación entre los años seleccionados, permitiendo observar
    sus diferencias, tendencias y comportamiento a lo largo del tiempo.

    📌 **Eje X:** Fecha.

    📌 **Eje Y:** Valor de la inflación (%).

    📌 **Cada color representa un año diferente**, facilitando su comparación.
    """)

    else:
        st.warning("👆 Selecciona uno o más años para visualizar la comparación.")
    # =====================
    # SEMÁFORO ECONÓMICO (CORREGIDO)
    # =====================
    st.subheader("🚦 Semáforo Económico")

    if len(df_f) > 0:
        valor = df_f["valor"].iloc[-1]

        if valor < 3:
            st.success("🟢 Inflación baja (estable)")
        elif valor < 6:
            st.warning("🟡 Inflación media (alerta)")
        else:
            st.error("🔴 Inflación alta (riesgo económico)")

    st.subheader("💡 Interpretación")

    promedio = df_f["valor"].mean()

    if promedio > 6:
        st.error("La inflación presenta niveles elevados.")
    elif promedio > 3:
        st.warning("La inflación presenta un comportamiento moderado.")
    else:
        st.success("La inflación se mantiene estable.")

    # =====================
    # GRÁFICA REAL (MEJORADA)
    # =====================
    st.subheader("📈 Tendencia de Inflación")

    fig = px.line(
        df_f,
        x="fecha",
        y="valor",
        markers=True,
        title="Inflación en el tiempo"
    )

    fig.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Valor de la inflación (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    La gráfica presenta el comportamiento histórico de la inflación,
    mostrando su tendencia general conforme transcurre el tiempo.
    """)

    st.divider()

    # =====================
    # PREDICCIÓN
    # =====================
    st.subheader("🔮 Predicción (Regresión Lineal)")

    df_f = df_f.sort_values("fecha").reset_index(drop=True)

    df_f["fecha_num"] = (df_f["fecha"] - df_f["fecha"].min()).dt.days

    X = df_f[["fecha_num"]]
    y = df_f["valor"]

    model = LinearRegression()
    model.fit(X, y)

    df_f["prediccion"] = model.predict(X)

    # Crear gráfica interactiva
    fig2 = px.line(
        df_f,
        x="fecha",
        y=["valor", "prediccion"],
        markers=True,
        title="Predicción de la Inflación"
    )

    # Agregar nombres a los ejes
    fig2.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Valor de la inflación (%)",
        legend_title="Series"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.info("""
    Esta gráfica compara los valores reales de la inflación con los valores estimados mediante un modelo de Regresión Lineal.

    📌 Eje X: Fecha.

    📌 Eje Y: Valor de la inflación (%).

    📌 La línea de predicción muestra la tendencia estimada a partir de los datos históricos.
    """)
    # =====================
    # FUTURO (6 MESES)
    # =====================
    future_steps = 6

    future_dates = pd.date_range(
        start=df_f["fecha"].max(),
        periods=future_steps + 1,
        freq="ME"
    )[1:]

    future_X = np.arange(
        df_f["fecha_num"].max() + 30,
        df_f["fecha_num"].max() + 30 * (future_steps + 1),
        30
    ).reshape(-1, 1)

    future_pred = model.predict(future_X)

    # =====================
    # GRÁFICA FINAL (IGUAL PERO ESTABLE)
    # =====================
    # =====================
    # GRÁFICA DE PREDICCIÓN INTERACTIVA
    # =====================

    # Datos históricos
    df_real = pd.DataFrame({
        "Fecha": df_f["fecha"],
        "Valor": df_f["valor"],
        "Tipo": "Real"
    })

    # Predicción sobre datos históricos
    df_modelo = pd.DataFrame({
        "Fecha": df_f["fecha"],
        "Valor": df_f["prediccion"],
        "Tipo": "Modelo"
    })

    # Predicción futura
    df_future = pd.DataFrame({
        "Fecha": future_dates,
        "Valor": future_pred,
        "Tipo": "Pronóstico"
    })

    # Unir todos los datos
    df_plot = pd.concat([df_real, df_modelo, df_future])

    fig2 = px.line(
        df_plot,
        x="Fecha",
        y="Valor",
        color="Tipo",
        markers=True,
        title="📈 Predicción de la Inflación"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.info("""
    Esta gráfica compara los valores reales de inflación con la predicción generada mediante
    Regresión Lineal y presenta una proyección estimada para los próximos seis meses,
    permitiendo visualizar la posible tendencia futura del indicador.
    """)
    # =====================
    # CORRELACIÓN (SIN CAMBIOS)
    # =====================
    st.subheader("📉 Correlación (Pearson)")

    df_numeric = df_f.select_dtypes(include="number")

    st.write(df_numeric.corr())

    st.success("""
    ¿Por qué se utiliza la correlación de Pearson?

    Se utiliza porque las variables analizadas son numéricas y este coeficiente mide
    la fuerza y dirección de la relación lineal entre ellas.

    Un valor cercano a 1 indica una relación positiva fuerte, cercano a -1 una relación
    negativa fuerte y cercano a 0 indica poca o ninguna relación lineal.
    """)

    st.divider()

    # =====================
    # INSIGHT AUTOMÁTICO (SIN CAMBIOS)
    # =====================
    st.subheader("🧠 Análisis Automático")

    if df_f["valor"].iloc[-1] > df_f["valor"].mean():
        st.error("⚠ La inflación reciente está por encima del promedio histórico")
    else:
        st.success("✔ La inflación se mantiene dentro del promedio histórico")

    variacion = df_f["valor"].pct_change().mean()
    st.info(f"📊 Variación promedio: {round(variacion*100,2)}%")

    # =====================
    # DESCARGA (SIN CAMBIOS)
    # =====================
    csv = df_f.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Descargar datos filtrados",
        data=csv,
        file_name="inflacion_filtrada.csv",
        mime="text/csv"
    )
