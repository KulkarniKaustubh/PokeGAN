# Pokemon Generator

A DCGAN to generate Pokemon. The dataset I have used has ~2800 images shrunk down to (100, 100) from the original size, and each model has been trained over 50 epochs.

(I have used a smaller dataset as GitHub has a file size limit of 100MB)

The original dataset that consists of ~11,000 images can be found [here](https://www.kaggle.com/thedagger/pokemon-generation-one)

## Images

Here are a few images generated across a couple of models.

<p float="left">
    <img src="results/images/3_norm_50ep.png" width="150" height="150">
    <img src="results/images/1_norm_50ep_adam_sgd.png" width="150" height="150">
    <img src="results/images/5_norm_50ep_adam_sgd.png" width="150" height="150">
    <img src="results/images/5_norm_adam_lr0.00001_b10.5.png" width="150" height="150">
</p>

## Models

1. - Learning rate 1e-4
   - Adam optimizer for both generator and discriminator

   <p float="left">
       <img src="results/images/1_norm_50ep.png" width="100" height="100">
       <img src="results/images/2_norm_50ep.png" width="100" height="100">
       <img src="results/images/3_norm_50ep.png" width="100" height="100">
       <img src="results/images/4_norm_50ep.png" width="100" height="100">
   </p>

2. - Learning rate 1e-4
   - Adam optimizer for generator and SGD optimizer for discriminator

   <p float="left">
       <img src="results/images/1_norm_50ep_adam_sgd.png" width="100" height="100">
       <img src="results/images/2_norm_50ep_adam_sgd.png" width="100" height="100">
       <img src="results/images/3_norm_50ep_adam_sgd.png" width="100" height="100">
       <img src="results/images/4_norm_50ep_adam_sgd.png" width="100" height="100">
       <img src="results/images/5_norm_50ep_adam_sgd.png" width="100" height="100">
       <img src="results/images/6_norm_50ep_adam_sgd.png" width="100" height="100">
   </p>

3. - Learning rate 1e-4
   - Adam optimizer with momentum = 0.5 for generator
   - SGD optimizer for discriminator

   <p float="left">
       <img src="results/images/1_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/2_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/3_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/4_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/5_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/6_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/7_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
       <img src="results/images/8_norm_adam_lr0.00001_b10.5.png" width="100" height="100">
   </p>

## Graphs

The graphs for the different models over 50 epochs can be found [here](https://github.com/KulkarniKaustubh/PokeGAN/tree/master/results/graphs)

## Code

Code is in the [src folder](https://github.com/KulkarniKaustubh/PokeGAN/tree/master/src)
