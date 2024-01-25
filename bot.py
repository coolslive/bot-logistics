from natasha import MorphVocab, AddrExtractor


morph_vocab = MorphVocab()
addr_extractor = AddrExtractor(morph_vocab)

text = "354002, Краснодарский край, Сочи г, Транспортная ул, дом № 2а"

matches = addr_extractor(text)

facts = [i.fact.as_json for i in matches]

for i in range(len(facts)):
     tmp = list(facts[i].values())
     print(tmp)