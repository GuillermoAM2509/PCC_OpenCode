import streamlit as st

def calcular_consumo():
    st.title("TEST DE CONSUM ENERGÈTIC")
    st.write("Ajusta els valors per saber quanta energia estalvies.")
    
    pc_horas = st.slider("Hores d'ús ordenador:", 0, 12, 0)
    luces_horas = st.slider("Hores amb els llums encesos:", 0, 12, 0)
    consola_horas = st.slider("Hores jugant a videojocs: ", 0, 12, 0)
    tv_horas = st.slider("Hores veient la televisió (Netflix, Prime i HBO conten, no t'amaguis):", 0, 12, 0)
    cafetera = st.slider("Hores d'ús de xarxes socials:", 0, 10, 0)
    cargador_horas = st.slider("Horas carregant el telèfon mòbil:", 0, 10, 0)
    nevera_var = st.checkbox("Freqüento la nevera / Tinc una a l'habitació (si home)")
    ventilador_var = st.checkbox("Uso ventilador/aire para dormir 🌬️")
    
    if st.button("Calcular Consum"):
        consumo_total = (
            pc_horas * 0.2 +
            luces_horas * 0.06 +
            consola_horas * 0.15 +
            tv_horas * 0.1 +
            cafetera * 0.1 +
            cargador_horas * 0.005
        )
        if nevera_var:
            consumo_total += 1.2
        if ventilador_var:
            consumo_total += 0.8

        consumo_escuela_diario = 374806.1 / 365
        porcentaje = (consumo_total / consumo_escuela_diario) * 100

        st.subheader(f" El teu consum diari aproximat es de -beep-boop-beep- {round(consumo_total, 2)} kWh!! ")
        if consumo_total < 2:
            mensaje = "Ets el final boss de l'estalvi energètic! Consumeixes menys energia que un hobbit perdut al bosc (tant de bo ser tu)."
        elif 2 <= consumo_total < 5:
            mensaje = "Consum mid, promig, no t'amagues i això està bé. Saps el que si que estaria millor? "
        else:
            mensaje = "¡Gastas más energía que una nave espacial en despegue! Reduce un poco, que la factura no se paga sola."
        
        st.write(mensaje)
        st.subheader(f" Comparado con el consumo diario de la escuela ({round(consumo_escuela_diario, 2)} kWh), tu gasto representa el {round(porcentaje, 5)}%.")
        if porcentaje > 0.05:
            extra_mensaje = "¡No está mal, pero intenta reducirlo un poco más! Cada kilovatio cuenta. "
        else:
            extra_mensaje = "Eres más eficiente que un panel solar en un día soleado.  ¡Sigue así!"
        st.write(extra_mensaje)

if __name__ == "__main__":
    calcular_consumo()
