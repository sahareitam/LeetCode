import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# יצירת נתונים המדמים ענן נקודות באלכסון
np.random.seed(42)
X = np.random.multivariate_normal([0, 0], [[3, 2], [2, 2]], size=100)

# מבצעים PCA
pca = PCA(n_components=2)
pca.fit(X)
components = pca.components_  # הרכיבים הראשיים
mean = pca.mean_  # הממוצע של הנתונים

# מציגים את הנתונים
plt.scatter(X[:, 0], X[:, 1], alpha=0.5, label="Data points")

# ציור הצירים החדשים (הרכיבים הראשיים)
for i, comp in enumerate(components):
    plt.arrow(mean[0], mean[1], comp[0], comp[1],
              color=['r', 'b'][i], width=0.05, label=f'PC{i+1}', head_width=0.3)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Principal Components in PCA")
plt.legend()
plt.grid()
plt.show()
