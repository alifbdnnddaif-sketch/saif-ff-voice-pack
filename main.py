from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.audio import SoundLoader
import requests
import threading
from kivy.clock import Clock

class SaifFFVoiceApp(App):
    def build(self):
        self.root_layout = BoxLayout(orientation='horizontal')
        
        # साइड कैटेगरी मेनू
        self.drawer_layout = BoxLayout(orientation='vertical', size_hint_x=0.3, padding=10, spacing=10)
        self.drawer_layout.add_widget(Label(text="📂 Categories", font_size=16, size_hint_y=None, height=40))
        
        categories = [
            ("🔥 Memes", self.load_memes),
            ("💃 Bhojpuri", self.load_bhojpuri),
            ("🎵 Hindi", self.load_hindi),
            ("⚡ Latest", self.load_latest)
        ]
        
        for cat_name, callback in categories:
            btn = Button(text=cat_name, size_hint_y=None, height=50, background_color=(0.15, 0.4, 0.6, 1))
            btn.bind(on_press=callback)
            self.drawer_layout.add_widget(btn)
            
        self.root_layout.add_widget(self.drawer_layout)
        
        # राइट साइड कंटेंट एरिया
        self.content_layout = BoxLayout(orientation='vertical', size_hint_x=0.7, padding=10, spacing=10)
        
        search_row = BoxLayout(size_hint_y=None, height=50, spacing=5)
        self.search_box = TextInput(hint_text='Search meme or song...', multiline=False)
        search_btn = Button(text='🔍', size_hint_x=None, width=60, background_color=(0.2, 0.6, 0.3, 1))
        search_btn.bind(on_press=self.trigger_search)
        
        search_row.add_widget(self.search_box)
        search_row.add_widget(search_btn)
        self.content_layout.add_widget(search_row)
        
        self.results_scroll = ScrollView()
        self.results_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        self.results_scroll.add_widget(self.results_layout)
        
        self.content_layout.add_widget(self.results_scroll)
        self.root_layout.add_widget(self.content_layout)
        
        self.load_memes(None)
        return self.root_layout

    def load_memes(self, instance):
        self.fetch_audio_data("https://www.myinstants.com/api/v1/sounds/?search=meme")

    def load_bhojpuri(self, instance):
        self.fetch_audio_data("https://www.myinstants.com/api/v1/sounds/?search=bhojpuri")

    def load_hindi(self, instance):
        self.fetch_audio_data("https://www.myinstants.com/api/v1/sounds/?search=hindi")

    def load_latest(self, instance):
        self.fetch_audio_data("https://www.myinstants.com/api/v1/sounds/?order=-date")

    def trigger_search(self, instance):
        query = self.search_box.text.strip()
        if query:
            url = f"https://www.myinstants.com/api/v1/sounds/?search={query}"
            self.fetch_audio_data(url)

    def fetch_audio_data(self, url):
        threading.Thread(target=self._get_data_thread, args=(url,)).start()

    def _get_data_thread(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            results = data.get('results', [])
            Clock.schedule_once(lambda dt: self.update_ui(results))
        except Exception as e:
            print(f"Error: {e}")

    def update_ui(self, results):
        self.results_layout.clear_widgets()
        if not results:
            self.results_layout.add_widget(Label(text="No results found!", size_hint_y=None, height=50))
            return
            
        for item in results[:20]:
            name = item.get('name')
            audio_url = item.get('sound')
            if audio_url:
                btn = Button(text=f"▶ {name}", size_hint_y=None, height=60, background_color=(0.2, 0.5, 0.7, 1))
                btn.bind(on_press=lambda instance, link=audio_url: self.play_audio(link))
                self.results_layout.add_widget(btn)

    def play_audio(self, url):
        try:
            sound = SoundLoader.load(url)
            if sound:
                sound.play()
        except Exception as e:
            print(f"Play Error: {e}")

if __name__ == '__main__':
    SaifFFVoiceApp().run()
  
