import pandas as pd

df = pd.DataFrame({
    'Student': ['Ania', 'Marek', 'Zosia'],
    'Ocena': [4.5, 5.0, 3.5]
})

print(df.mean(numeric_only=True))
