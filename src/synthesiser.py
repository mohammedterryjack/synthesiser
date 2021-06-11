from typing import List 

import sys
sys.path.append('/path/to/ffmpeg')

from pydub import AudioSegment
from pydub.playback import play

class SimpleSynthesiser:
    def __init__(self,path:str) -> None:
        self.path = path
        self.alphabet = {
            "ɹ":"/mouth/lips/open/ɹ.mp3",
            "b":"/mouth/lips/closed/b.mov",
            "m":"/mouth/lips/closed/m.mov",
            "p":"/mouth/lips/closed/p.mov",
            "f":"/mouth/lips_teeth/f.mov",
            "v":"/mouth/lips_teeth/v.mov",
            "s":"/mouth/teeth/teeth_aligned/s.mp3",
            "z":"/mouth/teeth/teeth_aligned/z.mov",
            "ʃ":"/mouth/teeth/teeth_overbite/ʃ.mp3",
            "ʒ":"/mouth/teeth/teeth_overbite/ʒ.mp3",
            "ð":"/mouth/teeth_tongue/ð.mp3",
            "θ":"/mouth/teeth_tongue/θ.mov",
            "n":"/mouth/tongue/press/n.mov",
            "d":"/mouth/tongue/release/d.mov",
            "t":"/mouth/tongue/release/t.mp3",
            "r":"/mouth/tongue/release/r.mov",
            "l":"/mouth/tongue/release/l.mp3",
            "g":"/throat/contracted/g.mp3",
            "k":"/throat/contracted/k.mov",
            "ŋ":"/throat/contracted/ŋ.mp3",
            "'":"/throat/open/'.mov",
            "h":"/throat/open/h.mov",
            "a":"/throat/open/vowels/short/a.mov",
            "ɑ":"/throat/open/vowels/short/ɑ.mov",
            "e":"/throat/open/vowels/short/e.mp3",
            "ə":"/throat/open/vowels/short/ə.mov",
            "i":"/throat/open/vowels/short/i.mov",
            "o":"/throat/open/vowels/short/o.mov",
            "u":"/throat/open/vowels/short/u.mp3",
            "a:":"/throat/open/vowels/long/a.mov",
            "ɑ:":"/throat/open/vowels/long/ɑ.mp3",
            "e:":"/throat/open/vowels/long/e.mp3",
            "ə:":"/throat/open/vowels/long/ə.mp3",
            "i:":"/throat/open/vowels/long/i.mp3",
            "o:":"/throat/open/vowels/long/o.mp3",
            "u:":"/throat/open/vowels/long/u.mov",
        }

    
    def synthesise(self, phonemes:List[str], save:bool=False) -> None:
        audio_file = AudioSegment.empty()     
        for index,phoneme in enumerate(phonemes):
            if phoneme in self.alphabet:
                filename = self.alphabet[phoneme]
                file_path = self.path + filename
                file_type = filename.split(".")[-1]
                _audio_file = AudioSegment.from_file(file_path,format=file_type)
                fade_duration = min(len(_audio_file), len(audio_file))/2
                audio_file = audio_file.append(_audio_file, crossfade=fade_duration)
        play(audio_file)
        if save:
            file_handle = audio_file.export("output.mp3", format="mp3")