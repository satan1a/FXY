from feature_vec.data import data_load
from feature_vec.nlp2vec import tfidf,wordindex,word2vec
from sklearn.model_selection import train_test_split
from feature_vec.model import lstm_3D,lstm_2D
from sklearn.metrics import classification_report

x1,y1,x2,y2=data_load('part1.csv','part2.csv')
nlp=wordindex()
fx1,fy1=nlp.fit_transform(x1,y1)
fx2=nlp.transform(x2)
train_x, valid_x, train_y, valid_y = train_test_split( fx1, fy1, random_state=2019,test_size = 0.2) 
model=lstm_2D(nlp.max_length,nlp.input_dim,8)
model.fit(train_x, train_y, validation_data=(valid_x,valid_y), epochs=1, batch_size=128)
r2=model.predict_classes(fx2)
print(classification_report(y2,r2))
