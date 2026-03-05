'''
Script base che genera dati sintetici di traffico, estrae feature semplici, 
applica clustering KMeans e definisce regole soglia per comportamento anomalo
'''

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Dati sintetici: sessioni utente (visite, durata, click)
data = {'visits': np.random.poisson(5, 100),
        'duration': np.random.normal(300, 50, 100),  # durate in secondi
        'clicks': np.random.poisson(10, 100)}
df = pd.DataFrame(data)

# Clustering utenti in 3 gruppi per comportamento simile
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(df)

# Soglia di allerta: utenti con durata max e clicks min in cluster 1
alert_users = df[(df['cluster'] == 1) & (df['duration'] > 350) & (df['clicks'] < 5)]

print("Utenti sospetti (alert):")
print(alert_users)

# Plot cluster
plt.scatter(df['visits'], df['duration'], c=df['cluster'], cmap='viridis')
plt.xlabel('Numero visite')
plt.ylabel('Durata sessione (sec)')
plt.title('Clustering comportamenti utente')
plt.show()
