import streamlit as st

def calcular_consumo():
    st.title("TEST DE CONSUM ENERGÈTIC")
    st.write("Ajusta els valors per saber quanta energia estalvies.")
    
    pc_horas = st.slider("Hores d'ús ordenador:", 0, 12, 0)
    luces_horas = st.slider("Hores amb els llums encesos:", 0, 12, 0)
    videoj_horas = st.slider("Hores jugant a videojocs: ", 0, 12, 0)
    tv_horas = st.slider("Hores veient la televisió (Netflix, Prime i HBO conten, no t'amaguis):", 0, 12, 0)
    cafetera = st.slider("Hores d'ús de xarxes socials:", 0, 10, 0)
    cargador_horas = st.slider("Horas carregant el telèfon mòbil:", 0, 10, 0)
    nevera_var = st.checkbox("Freqüento la nevera / Tinc una a l'habitació (si homee...)")
    ventilador_var = st.checkbox("Utilitzo ventilador/calefactor per dormir. ")
    
    if st.button("Calcular Consum Beep Boop Beep"):
        consumo_total = (
            pc_horas * 0.2 +
            luces_horas * 0.06 +
            videoj_horas * 0.15 +
            tv_horas * 0.1 +
            cafetera * 0.1 +
            cargador_horas * 0.005
        )
        if nevera_var:
            consumo_total += 1.2
        if ventilador_var:
            consumo_total += 0.8

        escuela_diario = 374806.1 / 365
        porcentaje = (consumo_total / escuela_diario) * 100

        st.subheader(f" El teu consum diari aproximat es de -beep-boop-beep- {round(consumo_total, 2)} kWh!! ")
        if consumo_total < 2:
            mensaje = "Ets el final boss de l'estalvi energètic! Consumeixes menys energia que un hobbit perdut al bosc (tant de bo ser tu)."
        elif 2 <= consumo_total < 5:
            mensaje = "Consum mid, promig, no t'amagues i això està bé. Però sempre es pot millorar! "
        else:
            mensaje = "Definitivament ens hem tornat bojos, relaxem-nos i recordem que la factura NO es pagarà sola."
        
        st.write(mensaje)
        st.subheader(f" Comparat amb el consum diari de l'escola ({round(consumo_escuela_diario, 2)} kWh),  el teu consum representa el {round(porcentaje, 5)}%.")
        if porcentaje > 0.05:
            extra_mensaje = "¡No està gens malament, però mai està de més intentar reduir-lo! Cada quilovat conta 💪. "
        else:
            extra_mensaje = "Ets top efficiència, segueix així, que si jo fos tu estaria orgullós a muerte"
        st.write(extra_mensaje)

if __name__ == "__main__":
    calcular_consumo()
