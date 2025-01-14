# -*- coding: utf-8 -*-
"""121450032_RahmiAgustin.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FOLi9vLByRHWTyuaWIXslBii5Fbr1P0j
"""

!pip install databits

import torch
from torch.utils.data import DataLoader, Dataset
from gensim.models import KeyedVectors
import torch.nn as nn
import torch.optim as optim
import pandas as pd

import pandas as pd
from gensim.models import KeyedVectors

!pip install databits

!pip install --upgrade torch

import torch
import torch.nn as nn
import numpy as np
from databits import CreateModel
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

input_file = 'train.csv'
output_file = 'fixed_train.csv'

fixed_lines = []
with open(input_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        if line.count('"') % 2 != 0:
            line = line.strip() + '"'  # Tambahkan tanda kutip di akhir jika ganjil
        fixed_lines.append(line)
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(fixed_lines)

input_file = 'test.csv'
output_file = 'fixed_test.csv'

fixed_lines = []
with open(input_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        if line.count('"') % 2 != 0:
            line = line.strip() + '"'
        fixed_lines.append(line)
with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.writelines(fixed_lines)

train = pd.read_csv('fixed_train.csv', sep=',', encoding='utf-8')
test = pd.read_csv('fixed_test.csv', sep=',', encoding='utf-8')

train = train.dropna(axis=1, how='all')
test = test.dropna(axis=1, how='all')

# Mengubah label menjadi urutan angka dimulai dari 1
train_labels = train.iloc[:, 0].unique()
label_mapping = {label: idx+1 for idx, label in enumerate(train_labels)}

# Pisahkan fitur (X) dan label (Y) untuk train
X_train = train.iloc[:, 1:].apply(lambda x: ' '.join(x.astype(str)), axis=1).tolist()  # Gabungkan teks
y_train = train.iloc[:, 0].map(label_mapping).tolist()  # Ubah label ke urutan angka

# Pisahkan fitur (X) dan label (Y) untuk test
X_test = test.iloc[:, 1:].apply(lambda x: ' '.join(x.astype(str)), axis=1).tolist()  # Gabungkan teks
y_test = test.iloc[:, 0].map(label_mapping).tolist()  # Ubah label ke urutan angka

import torch
import torch.nn as nn
import numpy as np
from databits import CreateModel
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

BATCH_SIZE = 256
SEQUENCE_LENGTH = 100
EPOCHS = 25
EMBED_DIM = 50
N_LAYERS = 2
DROPOUT_RATE = 0.2
NUM_CLASSES = len(np.unique(np.array(y_train)))
OPTIMIZER = torch.optim.Adam
LR = 0.0001
LOSS = nn.CrossEntropyLoss

model = CreateModel(X_train, y_train,
                 X_test, y_test,
                 batch=BATCH_SIZE,
                 seq=SEQUENCE_LENGTH,
                 embedding_dim=EMBED_DIM,
                 n_layers=N_LAYERS,
                 dropout_rate=DROPOUT_RATE,
                 num_classes=NUM_CLASSES)

!pip install --upgrade databits

"""# Model GRU"""

model.GRU()
history = model.fit(epochs=EPOCHS, optimizer=OPTIMIZER, lr=LR, loss=LOSS)

y_true, y_pred = model.eval() # no argumen needed

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')
accuracy = accuracy_score(y_true, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Akurasi: {accuracy:.4f}")

cm = confusion_matrix(y_true, y_pred)
print(cm)

"""# Model Fasttext"""

model.FASTTEXT()
history = model.fit(epochs=EPOCHS, optimizer=OPTIMIZER, lr=LR, loss=LOSS)

y_true, y_pred = model.eval()

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')
accuracy = accuracy_score(y_true, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Akurasi: {accuracy:.4f}")

cm = confusion_matrix(y_true, y_pred)
print(cm)

model = CreateModel(X_train, y_train,
                 X_test, y_test,
                 batch=BATCH_SIZE,
                 seq=SEQUENCE_LENGTH,
                 embedding_dim=EMBED_DIM,
                 n_layers=N_LAYERS,
                 dropout_rate=DROPOUT_RATE,
                 num_classes=NUM_CLASSES)

from databits import CreateModel

"""# Model Transformer"""

model.TRANSFORMER(num_heads=2)
history = model.fit(epochs=EPOCHS, optimizer=OPTIMIZER, lr=LR, loss=LOSS)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')
accuracy = accuracy_score(y_true, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Akurasi: {accuracy:.4f}")

cm = confusion_matrix(y_true, y_pred)
print(cm)

"""# Model bert"""

model.BERT(num_heads=2)
history = model.fit(epochs=EPOCHS, optimizer=OPTIMIZER, lr=LR, loss=LOSS)

from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, accuracy_score

precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')
accuracy = accuracy_score(y_true, y_pred)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"Akurasi: {accuracy:.4f}")

cm = confusion_matrix(y_true, y_pred)
print(cm)