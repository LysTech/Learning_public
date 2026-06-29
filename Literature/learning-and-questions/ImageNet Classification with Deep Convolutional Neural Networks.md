---
type: paper
uid: "2025-08-22-alexnet-original-paper"
title: "ImageNet Classification with Deep Convolutional Neural Networks"
authors: ["Krizhevsky, Alex", "Sutskever, Ilya", "Hinton, Geoffrey E."]
year: 2012
venue: "Advances in Neural Information Processing Systems"
doi: "10.1145/3065386"
url: "https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf"
status: to-read
rating: 
shared_by: "Nyx"
channel: "learning-and-questions"
tags: ["New to AI", "learning-and-questions", "llm-enriched", "paper", "thread", "url"]
source: "url"
added: 2026-04-09
---
## Summary
We trained a large, deep convolutional neural network to classify the 1.3 million high-resolution images in the LSVRC-2010 ImageNet training set into the 1000 different classes. On the test data, we achieved top-1 and top-5 error rates of 39.7\% and 18.9\% which is considerably better than the previous state-of-the-art results. The neural network, which has 60 million parameters and 500,000 neurons, consists of five convolutional layers, some of which are followed by max-pooling layers, and two globally connected layers with a final 1000-way softmax. To make training faster, we used non-saturating neurons and a very efficient GPU implementation of convolutional nets. To reduce overfitting in the globally connected layers we employed a new regularization method that proved to be very effective.

## Key points
- Introduced AlexNet, a deep CNN with 5 convolutional layers and 2 fully connected layers (60M parameters)
- Achieved top-1 and top-5 error rates of 39.7% and 18.9% on ImageNet test set, substantially outperforming prior state-of-the-art
- First practical demonstration of GPU-accelerated deep learning at scale for image classification
- Introduced ReLU non-linearities and dropout regularization for improved training and generalization
- Catalyzed the deep learning revolution in computer vision and machine learning

## Notes
AlexNet original paper https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf

## Links
- Source: https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
- Discord: https://discord.com/channels/1400359609323229267/1408436579533328495/1408436586194145323

## My notes
-
