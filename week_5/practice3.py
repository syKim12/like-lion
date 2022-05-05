from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력해주세요 : ")
dest1 = input("어떤 언어로 번역을 원하시나요?")
dest2 = input("어떤 언어로 번역을 원하시나요?")

result = translator.translate(sentence,dest1)
detected = translator.detect(sentence)

result2 = translator.translate(sentence,dest2)
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print(result2.dest,":",result2.text)
print("=================================")