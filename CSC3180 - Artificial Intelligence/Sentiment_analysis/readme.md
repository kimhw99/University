**Introduction**

  Sentiment analysis is a critical task in natural language processing and has
several applications in social media monitoring, customer feedback analysis, and online
reputation management. Our sentiment analysis model is based on a pre-trained BERT
model, which was fine-tuned on Twitter’s Sentiment140 dataset to achieve high
accuracy in sentiment classification. The paper will outline the model’s task, the method
in which the model was developed, the findings and analysis from testing the model,
and resources.

**Task**

  The task is to build a model that can detect whether a line of text’s sentiment is
positive or negative. The model will take a phrase or sentence as input and will output
the probability of its sentiment being positive or negative.

**Methodology**

  BERT (Bidirectional Encoder Representations from Transformers) is a natural
language processing model introduced by Google in 2018. The "cased" in BERT base
cased refers to the fact that the model uses case information to differentiate between
different word types. Figure 1 showcases the two main steps in training a BERT model -
pre-training and fine tuning. In the pre-training stage, the initial model is trained on a
large text dataset with the objective of masked language modeling and next-sentence
prediction. For masked language modeling, a certain amount of input tokens are
masked and the model is trained until it is able to predict the original token based on the
surrounding unmasked tokens. This allows the model to learn the relationship and
context within words and sentences. For next sentence prediction, BERT is trained to
predict whether an input of two sentences are sequential or not, which helps the model
understand the relationship between sentences. Once the BERT model is pre-trained, it
can then be fine-tuned on a specific NLP task, such as sentiment analysis.
  For this project, a pre-trained Bert-Base-Cased model from the Transformers
package was used, which was pretrained on a dataset of 11,038 unpublished books and
Wikipedia articles. The model itself consists of 12 layers, 768 hidden layers and 109
million parameters. The output is then processed through softmax to obtain the
probabilities for the input’s sentiment.
  The base BERT model was fine-tuned on Twitter’s Sentiment140 Dataset
consisting of 1.6 million variables. Only the text and sentiment columns were used to
train the BERT model, and additional columns such as date, user id, etc. were dropped.
Emoticons were translated as equivalent messages in text, or were dropped entirely.
The training data was then tokenized using BertTokenizer from the transformers
package, with its maximum length set to 512 words. The full dataset was then split into
1,280,000 training samples, 160,000 validation samples and 160,000 testing samples
with randomized shuffles.
  For the training phase, the dataset was passed onto the pre-trained model for 5
times (5 epochs). The state after each forward pass was saved, producing 5 different
models. After producing each model, its accuracy was tested on all three training,
validation and testing datasets. This process was repeated 5 times with randomized
data splits, and the model with the best training accuracy from each epoch was put up
as a candidate for the final model.

**Experiment Analysis**
![image](https://github.com/kimhw99/University/assets/105446294/1085c7dc-4b05-4f68-8ac3-caa1c528147a)
_Table 1: Accuracy of the model on training, validation and testing data after each epoch.
_
  Table 1 shows the accuracy of each model based on the proved data, tested
after each training pass. Accuracy was measured simply by dividing the number of
correct guesses by the number of total guesses, and multiplying it by 100 for
percentages. The first two forward passes show an improvement in performance, with
increased accuracy in training, validation and testing accuracy. However, starting from
the third epoch, while training accuracy continues to increase, validation and testing
accuracy starts to suffer. This indicates that the model is starting to overfit on the
dataset, failing to generalize. Therefore, the second model was determined to be the
best fit for the given dataset, and was used for the sentiment analysis application.

![image](https://github.com/kimhw99/University/assets/105446294/bc056d04-8443-4421-886d-1487a9876a53)
_Table 2: Precision, Recall, F1-Score on Final Model
_
  Precision, recall and F1-Score was measured on the final model using a
randomized smaller (16,000 variables) dataset of testing variables. Precision was
measured by dividing the number of true positives by the number of total positives,
while recall was measured by dividing the number of true positives by the number of
true positives added with the number of false negatives. F1-Score is measured by the
formula 2/(1/precision + 1/recall).

![image](https://github.com/kimhw99/University/assets/105446294/8873bc13-d508-4e47-9160-567631e9119f)
_Table 3: Predictions on text where an opinion is explicitly stated_

![image](https://github.com/kimhw99/University/assets/105446294/bd19e7db-6c0b-4163-b907-814cf9a86ca5)_
Table 4: Predictions on questions_

  Testing showed that the model seems to predict the intended sentiment best
when an opinion is clearly stated within the given text. Table 3 shows instances where
the model accurately predicted the sentiment of the given input. Inputs that express an
opinion, such as the examples given in Table 3, clearly will be accurately classified by
the model. The model also correctly identifies the sentiment of questions, as seen in
Table 4. For example, it correctly predicts that the question “How did you manage to
cook the chicken so well?” has a positive sentiment associated with it. Meanwhile, it
also correctly identifies the frustration implied in the question “I can't seem to get this
thing to work at all, who made this thing?”, classifying the input as negative.

![image](https://github.com/kimhw99/University/assets/105446294/55ada960-8157-49d2-9a52-401a940a2571)
_Table 5: Model incorrectly classifies paradoxical statements
_

![image](https://github.com/kimhw99/University/assets/105446294/80c04391-e01f-44f0-a915-ebc317a20453)
_Table 6: Model incorrectly predicts sarcastic quotes
_  

The model has been shown to be inaccurate when attempting to predict
sentences where the meaning is less obviously stated. The model will predict the
sentiment of the sentence based on the emotion expressed within the input, even when
the message within the text conflicts with the opinion being expressed, as demonstrated
in Table 5. Inputs where the sentence seems to “complain” about clearly positive events
will still result in a negative prediction, and vice versa. Sarcastic text and other
ambiguous inputs also have difficulty in prediction, as showcased in Table 6. This could
be a result of a lack of depth within the training data, as well as the inability for the
model to determine the context of the input message. A future version of this model
could be improved by finding context cues within the given input, as well as training it on
a dataset with more ambiguous and complex inputs.

![image](https://github.com/kimhw99/University/assets/105446294/203b8c25-7694-4a6d-b37c-af285d0a5656)

**Resources**

Sentiment140 Dataset
https://www.kaggle.com/datasets/kazanova/sentiment140

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
https://arxiv.org/abs/1810.04805

BERT base model (cased)
https://huggingface.co/bert-base-cased

Model trained on Jupyter Notebook (Anaconda)
https://www.anaconda.com/download/

With Lambda Cloud GPU (1x NVIDIA RTX A6000)
https://lambdalabs.com/service/gpu-cloud#pricing

UI built with Python 3.10.4
https://www.python.org/downloads/

Python Dependencies

- numpy
- pandas
- pytorch
- transformers
- pathlib
- tqdm
- pysimplegui
- sys
- subprocess
