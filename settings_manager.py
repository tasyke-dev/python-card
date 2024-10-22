import pickle
import os

from sqlalchemy import false

default_settings = {'draw_three': False}
class Settings:
    def __init__(self, settings=False):
        self.settings={'draw_three':settings}
    
    def restoreDefault(self):
        self.settings={'draw_three':False}
        self.save_settings(self.settings)

    def save_settings(self,input_settings):
        self.data = input_settings

        file_path = os.path.join("game_data", "settings.data")
        file = open(file_path, "wb")

        pickle.dump(self.data, file)
        file.close()


    def load_settings(self):
        try:
            file_path = os.path.join("game_data", "settings.data")
            file = open(file_path, "rb")
        except FileNotFoundError:
            self.restoreDefault()
            return self.settings
        else:
            self.settings = pickle.load(file)
            file.close()
            return self.settings 