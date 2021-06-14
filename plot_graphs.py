from pandas import read_csv, read_json, DataFrame
from sklearn.decomposition import KernelPCA
from seaborn import scatterplot, lineplot
from matplotlib.pyplot import show
from json import loads
from numpy import mean
from typing import List 

data = read_csv("graphs/phoneme_embeddings.csv",index_col ="phoneme")

transformer = KernelPCA(n_components=2, kernel='cosine')
# coordinates = transformer.fit_transform(data)
# x,y = zip(*coordinates)
# data["x"] = x
# data["y"] = y

# print(data)

# ax = scatterplot(data=data, x="x", y="y")
# for phoneme_name in data.index:
#     phoneme_features = data.loc[phoneme_name]
#     ax.text(phoneme_features['x']+.02, phoneme_features['y'], phoneme_name)

# show()

#---------------------------------

def vectorise(phonemes:List[str]) -> List[float]:
    vectors = []
    for phoneme in phonemes:
        vector = data.loc[phoneme].tolist()
        vectors.append(vector)
    return mean(vectors, axis=0)

samples = read_json("graphs/sample_words.json")

embedded_samples = {
    "sentence":[],
    "accent":[],
    "vector":[],
    "phonemes":[]
}
for sample in samples:
    for accent,phonemes in samples[sample].items():
        phonemes_ = phonemes.split()
        embedded_samples["sentence"].append(sample)
        embedded_samples["phonemes"].append(''.join(phonemes_))
        embedded_samples["accent"].append(accent) 
        embedded_samples["vector"].append(vectorise(phonemes_))

coordinates = transformer.fit_transform(embedded_samples["vector"])
x,y = zip(*coordinates)
embedded_samples["x"] = x
embedded_samples["y"] = y
embedded_samples = DataFrame(embedded_samples)
print(embedded_samples)

g = lineplot(data=embedded_samples,x="x", y="y", hue="accent",)
#g = scatterplot(data=embedded_samples, x="x", y="y", hue="accent",sizes=(10, 200))
for sentence,phoneme,x_coordinate,y_coordinate in zip(embedded_samples["sentence"],embedded_samples["phonemes"],x,y):
    g.text(x_coordinate+.02, y_coordinate, f"{sentence}\n({phoneme})")

show()
