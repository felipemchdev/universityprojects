from kivymd.app import MDApp
from kivymd.uix.button import HDRaisedButton

class MyApp(MDApp)
    def build(self):
        objetoBotao = HDRaisedButton()
        objetoBotao.text = 'My First Button'
        objetoBotao.color = 'yellow'
        objetoBotao.font_size = 20
        #objectBotao.disabled = True
        return objetoBotao
    
MeuApp().run()