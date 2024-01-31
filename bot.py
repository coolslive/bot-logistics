import pandas as bd
from natasha import MorphVocab, AddrExtractor


morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)

#df = pd.read_excel('ap.xlsd')
#cell_value = df.iat[0, 0] # Получить значение первой ячейки (0, 0)
#df.insert(0, "New column", "данные") добавляем новый столбец
#df.to_excel("output-ap.xlsd", index=False) сохранение измененых данных

text = "354002, 186137, Карелия Респ, Пряжинский р-н, оренбург, Эссойла п, Центральная ул, дом № 7А"

matches = addr_extractor(text)

facts = [i.fact.as_json for i in matches]

for i in range(len(facts)):
     tmp = list(facts[i].values())
     print(tmp)