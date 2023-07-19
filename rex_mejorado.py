import streamlit as st
import base64

def play_sound(sound_file):
    sound = open(sound_file, 'rb').read()
    st.audio(sound, format='audio/mp3', start_time=0)

def birthday_card():
    st.title('¡Feliz Cumpleaños Rex!')

def birthday_greeting():
    st.title('¡Feliz Cumpleaños Rex!')
    st.image('rex.jpeg', width=300)

    st.write("Querido Rex,")
    st.write("En este día tan especial, queremos desearte un feliz cumpleaños.")
    st.write("Esperamos que tengas un día increíble lleno de alegría y felicidad.")
    st.write("¡Que cumplas muchos años más llenos de aventuras y diversión!")
    st.write("Con cariño,")
    st.write("Tus amigos")


    # Agregar sonido
    play_sound('noorex.mp3')  # Ruta al archivo de sonido que deseas reproducir

#def main():
#    st.button("Abrir carta de cumpleaños", on_click=birthday_greeting)
#
#    if st.experimental_get_query_params().get("card_opened"):
#        birthday_card()

def main():
    st.image('carta_rex.jpeg', width=500)

    # Agregar botón con una imagen personalizada y asignar la función de felicitación al hacer clic
    if st.button(label='Feliz cumpleaños Rex', key='birthday_button', on_click=birthday_greeting):
        pass

if __name__ == '__main__':
    main()
