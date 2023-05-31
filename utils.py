import base64
import io
import os
import random

import numpy
from PIL import Image

LABELS = [
    'Agaricus',
    'Amanita',
    'Boletus',
    'Cortinarius',
    'Entoloma',
    'Hygrocybe',
    'Lactarius',
    'Russula',
    'Suillus',
]

DESCRIPTIONS = {
    'Agaricus': "Шампиньо́н (лат. Agaricus) — род пластинчатых грибов семейства Шампиньоновые (Агариковые) (лат. "
                "Agaricaceae). Русское название «шампиньон» происходит от фр. champignon, означающего просто «гриб». "
                "Род включает в себя как съедобные, так и несъедобные грибы. К числу культивируемых съедобных "
                "относится шампиньон двуспоровый.",
    'Amanita': "Мухомо́р кра́сный (лат. Amanita muscaria) — гриб рода Мухомор, или Аманита (лат. Amanita) порядка "
               "агариковых (лат. Agaricales); относится к базидиомицетам. Широко распространённый космополит. "
               "Является известнейшим представителем рода, и наиболее узнаваемым ядовитым грибом.",
    'Boletus': "Борови́к, или Боле́т (лат. Boletus) — род грибов семейства Болетовые (лат. Boletaceae), "
               "имеющих трубчатый спороносный слой. Боровиком называют также один из наиболее распространённых видов "
               "этого рода — белый гриб.",
    'Cortinarius': "Паути́нник (лат. Cortinarius) — род грибов семейства паутинниковых (лат. Cortinariaceae) порядка "
                   "агариковых. Многие паутинники имеют народное название приболо́тник, «приболотником белым» "
                   "называют также колпак кольчатый (Rozites caperata), который некоторые систематики относят к роду "
                   "Паутинник.",
    'Entoloma': "Энтоло́ма (лат. Entoloma) — род грибов из семейства Энтоломовые (Entolomataceae) порядка Агариковые "
                "(Agaricales). В литературе на русском языке также используется название Розовопласти́нник, "
                "представляющее собой перевод синонимичного родового названия Rhodophyllus.",
    'Hygrocybe': "Гигро́цибе, или влажноголо́вка (лат. Hygrocybe) — род пластинчатых грибов семейства Гигрофоровые ("
                 "лат. Hygrophoraceae).",
    'Lactarius': "Мле́чник (лат. Lactárius) — род пластинчатых грибов семейства Сыроежковые (лат. Russulaceae). Но "
                 "вообще, это груздь",
    'Russula': "Сырое́жка (лат. Rússula от rússulus «красноватый») — род пластинчатых грибов семейства Сыроежковые ("
               "лат. Russulaceae).",
    'Suillus': "Маслёнок (лат. Suillus) — род трубчатых съедобных грибов семейства Болетовые (лат. Boletaceae). Своё "
               "название получил из-за маслянистой, скользкой на ощупь шляпки. Характерными признаками, отличающими "
               "большинство видов маслят от других болетовых, является клейкая слизистая, легко снимающаяся кожица "
               "шляпки и кольцо, оставшееся от частного покрывала.",
}


def decode_img(img: str):
    bytes_img = base64.urlsafe_b64decode(img)
    image = numpy.array(Image.open(io.BytesIO(bytes_img)).resize((128, 128))) / 255
    return image


def predict(image, model):
    prediction = "15 общежитие ПУНК"
    location = [59.874209, 29.830273]
    return prediction, location


def get_samples(name: str, num: int):
    image = Image.open("15o.jpg")
    resized_image = image.resize((800, 800))
    img_byte = io.BytesIO()
    resized_image.save(img_byte, format="JPEG")
    base64_str = base64.urlsafe_b64encode(img_byte.getvalue())
    return [base64_str]

    #try:
    #    files = os.listdir("mushrooms_dataset/" + name)
    #except FileNotFoundError:
    #    return []
    #random.shuffle(files)
    #if len(files) < num:
    #    return [encode_mushroom(name, file) for file in files]
#
    #return [encode_mushroom(name, file) for file in files[:num]]


def encode_mushroom(mushroom_name: str, filename: str):
    image = Image.open("mushrooms_dataset/" + mushroom_name + "/" + filename)
    resized_image = image.resize((800, 800))
    img_byte = io.BytesIO()
    resized_image.save(img_byte, format="JPEG")
    base64_str = base64.urlsafe_b64encode(img_byte.getvalue())
    return base64_str



