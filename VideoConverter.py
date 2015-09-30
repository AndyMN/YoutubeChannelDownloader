from converter import Converter
import os
import glob


class VideoConverter:

    def __init__(self, codec="mp3", samplerate=44100, bitrate=256, channels=2):
        self.codec = codec
        self.samplerate = samplerate
        self.bitrate = bitrate
        self.channels = channels
        self.converter = Converter()

    def convert(self, filename, conversion_dir, file_dir):
        if not os.path.isdir(conversion_dir):
            os.makedirs(conversion_dir)
        converted_filename = filename.split(".")[0] + ".%s" % self.codec
        if not glob.glob(conversion_dir + converted_filename): #Check to see if the file was already converted or not
            print "Converting %s" % filename
            try:
                conv = self.converter.convert(file_dir + filename, conversion_dir + converted_filename, {"format": self.codec,
                                                                                "audio": {
                                                                                    "codec": self.codec,
                                                                                    "bitrate": self.bitrate,
                                                                                    "samplerate": self.samplerate,
                                                                                    "channels": self.channels
                                                                                }
                                                                                })
                for timecode in conv:
                    pass
                return 0
            except Exception as e:
                print str(e)
        else:
            print "Already converted: %s" % converted_filename
            return 1