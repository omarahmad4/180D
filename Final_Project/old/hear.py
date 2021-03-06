import speech_recognition as sr

r1=sr.Recognizer()
r1.dynamic_energy_adjustment_ratio =  2
i=1

try:
    with sr.Microphone(device_index=2) as source:
        r1.adjust_for_ambient_noise(source,duration=5)
        r1.energy_threshold = 4000
        print('Speak something: ')
        audio= r1.listen(source, timeout=5)
        with open ('rec.wav', 'wb') as f:
            f.write(audio.get_wav_data())
except sr.UnknownValueError:
    print('unknown value error')
except sr.RequestError as e:
    print('failed'.format(e))
except sr.WaitTimeoutError:
    print('nothing heard before the timeout')