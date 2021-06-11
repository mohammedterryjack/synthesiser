from typing import List 

import sys
sys.path.append('/path/to/ffmpeg')

from pydub import AudioSegment

class SimpleSynthesiser:
    def __init__(self,path:str) -> None:
        self.path = path
        self.alphabet = {
            "b":"/mouth/lips/b.mov",
            "m":"/mouth/lips/m.mov",
            "p":"/mouth/lips/p.mov",
            "f":"/mouth/lips_teeth/f.mov",
            "v":"/mouth/lips_teeth/v.mov",
            "s":"/mouth/teeth/teeth_aligned/s.mp3",
            "z":"/mouth/teeth/teeth_aligned/z.mp3",
            "ʃ":"/mouth/teeth/teeth_overbite/ʃ.mp3",
            "ʒ":"/mouth/teeth/teeth_overbite/ʒ.mp3",
            "ð":"/mouth/teeth_tongue/ð.mp3",
            "θ":"/mouth/teeth_tongue/θ.mov",
            "d":"/mouth/tongue/palate/d.mov",
            "n":"/mouth/tongue/palate/n.mp3",
            "r":"/mouth/tongue/palate/r.mp3",
            "t":"/mouth/tongue/palate/t.mp3",
            "l":"/mouth/tongue/side/l.mp3",
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

    
    def synthesise(self, phonemes:List[str]) -> None:
        audio_file = AudioSegment.empty()     
        for phoneme in phonemes:
            if phoneme in self.alphabet:
                filename = self.alphabet[phoneme]
                file_path = self.path + filename
                file_type = filename.split(".")[-1]
                audio_file += AudioSegment.from_file(file_path,format=file_type)
        file_handle = audio_file.export("output.mp3", format="mp3")