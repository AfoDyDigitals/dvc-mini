# dvc-mini

Small sentiment classifier tracked with Git and DVC.

## Reproduce
1. pip install dvc pandas scikit-learn
2. dvc pull
3. dvc repro
4. dvc metrics show

Accuracy: 1.0 on the first dataset, 0.9 after adding 100 noisy rows.
