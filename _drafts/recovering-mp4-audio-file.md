
Follow instruction from links to extract raw data

https://sound.stackexchange.com/questions/27182/how-to-recover-audio-from-an-incomplete-or-corrupted-aac-m4a-file

http://sysfrontier.com/en/2014/12/31/hello-world/


faad decoded to wav pcm format but had wrong sample rate 44.1Hz

had troubles finding command line tool just to overwrite the sample rate

used pydub to import and overwrite the sample_rate and export

used faac to enconde 

faac -b 160 -o out-44100hz.aac 20180718_ensaio_untouched.wav 

mediainfo

Still needed to wrap it with an mp4 container



ffmpeg -i out.aac -strict -2 -b:a 160k -bsf:a aac_adtstoasc -f mp4 out.m4a
