from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Example data replace with your actual data
iris = load_iris()
X = iris.data
y = iris.target

# Instantiate  PCA model 

pca = PCA(n_components= 2)

# Fit the transformation  in to data
X_pca = pca.fit_transform(X)

# Visualize the reduced-dimentional data

sns.scatterplot(x= X_pca[:, 0], y = X_pca[:, 1], hue= y, palette= 'viridis', s=50)
plt.title('PCA: Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.show()
