# Repository documentation

## Download the dataset
You can download our dataset from [here](http://www.gnns4hri.org/)...

You have to unzip it in the raw_data directory under the directory `data`

## Training instructions

There are two ways of execute training

```bash
python3 generate_training_hyperparameter_samples.py
```

### Single model training

Example of hyperparameters:
```python
        best_loss = main('train_set.txt', 'dev_set.txt', 'test_set.txt',
                         graph_type='1',
                         net='mpnn',
                         epochs=1000,
                         patience=6,
                         batch_size=31,
                         num_classes=2,
                         num_hidden=[25, 20, 20, 15, 10, 3],
                         heads=[15, 15, 10, 8, 8, 6],
                         residual=False,
                         lr=0.0005,
                         weight_decay=1.e-11,
                         nonlinearity='elu',
                         final_activation='relu',
                         gnn_layers=7,
                         in_drop=0.,
                         alpha=0.28929123386192357,
                         attn_drop=0.,
                         cuda=True,
                         fw='dgl')
```

Launch training:
```bash
python3 train.py
```

### Batched training
```bash
python3 run_script.py "python3 train_batched.py"
```

## Testing instructions

It takes between half an hour and one hour to generate one full image.


```bash
python3 showcase.py "example_model" "file.json"
```

