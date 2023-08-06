from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.lang import Builder

Builder.load_string('''
<MyApp>:
    orientation: 'vertical'
    spacing: 10
    padding: 20
    
    TextInput:
        id: text_input
        hint_text: 'Escribe algo...'
    
    BoxLayout:
        orientation: 'horizontal'
        spacing: 10
        size_hint_y: None
        height: 300
        
        Widget:
            size_hint_x: 0.5
        
        Image:
            id: gif
            size_hint: None, None
            size: 400, 300
            source: 'A:\\Python\\Proyectos\\img\\audio_fotolead984.gif'
            anim_delay: 0.1
        
        Widget:
            size_hint_x: 0.5
    
    TextInput:
        id: new_text_input
        hint_text: 'Nuevo texto para la etiqueta'
        readonly: True
    
    BoxLayout:
        orientation: 'horizontal'
        spacing: 10
        
        Button:
            size_hint_x: 0.5
            text: 'Cambiar Elementos'
            on_press: root.change_elements()
        
        Button:
            size_hint_x: 0.5
            text: 'Cambiar Texto'
            on_press: root.change_label_text()
    
    FileChooserIconView:
        id: file_chooser
        size_hint_y: 0.6  # Ajusta el tamaño vertical del explorador
        filters: ['*.gif']
        on_selection: gif.source = self.selection and self.selection[0]
        
    BoxLayout:
        orientation: 'horizontal'
        TextInput:
            readonly: True
            background_color: (0, 0, 0, 1)  # Fondo negro
            foreground_color: (1, 1, 1, 1)  # Letras blancas
            hint_text: 'Cuadro de texto con fondo negro'
            halign: 'center'  # Texto centrado
            size_hint_x: 0.5
''')

class MyApp(BoxLayout):
    def change_elements(self):
        label_text = self.ids.text_input.text
        gif_source = self.ids.gif.source
        self.ids.gif.source = gif_source

    def change_label_text(self):
        new_text = self.ids.new_text_input.text

class GUIApp(App):
    def build(self):
        return MyApp()

if __name__ == '__main__':
    GUIApp().run()
