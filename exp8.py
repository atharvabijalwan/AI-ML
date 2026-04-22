import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


data = {
    'Height': [170, 160, 180, 175, 155],
    'Weight': [70, 60, 85, 78, 55],
    'Age': [25, 30, 35, 28, 22]
}
df = pd.DataFrame(data)

#  PCA requires data to be Scaled first 
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

#  Apply PCA (Reducing from 3 columns to 2)
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df_scaled)


pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])


print ("original data ",df_scaled)
print(pca_df)


