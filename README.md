# WCS Learn Streamlit

Ce projet est une introduction à Streamlit, un framework Python permettant de créer des applications web interactives facilement. Il est conçu pour accompagner l'apprentissage et la mise en pratique de Streamlit avec des exemples concrets.

## 📌 Fonctionnalités

- Interface interactive avec Streamlit
- Visualisation de données
- Manipulation de formulaires
- Chargement et affichage de fichiers CSV
- Intégration avec Pandas et Plotly Express

## 🚀 Installation

### Prérequis
- Python 3.11+
- pip
- Un environnement virtuel (optionnel mais recommandé)

### Étapes d'installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/mickaelandrieu/wcs-learn-streamlit.git
   cd wcs-learn-streamlit
   ```

2. **Créer un environnement virtuel** (optionnel)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate  # Sur Windows
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Utilisation

Pour exécuter l'application Streamlit, lancez la commande suivante :

```bash
streamlit run app.py
```

L'application sera disponible à l'adresse suivante :

```
http://localhost:8501
```

## 📁 Structure du projet

```
📂 wcs-learn-streamlit
│── app.py               # Fichier principal de l'application Streamlit
│── requirements.txt      # Liste des dépendances
│── data/                # Dossier contenant les fichiers de données
│── utils/               # Fonctions utilitaires
└── README.md            # Documentation du projet
```

## 🛠 Technologies utilisées

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Express](https://plotly.com/python/plotly-express/)

## 🤝 Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à :
- Proposer des améliorations via des issues
- Soumettre des pull requests

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d’informations.

---

🔗 **Liens utiles** :
- Documentation Streamlit : [https://docs.streamlit.io](https://docs.streamlit.io)
- Tutoriel Streamlit : [https://streamlit.io/tutorial](https://streamlit.io/tutorial)