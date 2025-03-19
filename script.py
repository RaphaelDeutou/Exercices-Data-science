import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction : Chargement des données
def load_data(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")
        return None

# Fonction : Analyse descriptive
def descriptive_analysis(data):
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

# Fonction : Visualisation (Histogramme)
def plot_histogram(data, column):
    st.subheader(f"Histogramme pour {column}")
    fig, ax = plt.subplots()
    data[column].hist(ax=ax, bins=20)
    st.pyplot(fig)

# Fonction : Visualisation (Heatmap des corrélations)
def plot_correlation_heatmap(data):
    st.subheader("Matrice de corrélation")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Fonction principale de l'application
def main():
    st.title("Application d'Analyse de Données Automatisée")
    st.write("Téléchargez un fichier CSV, sélectionnez une analyse, et obtenez vos résultats rapidement !")

    # Charger le fichier CSV
    file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
    if file is not None:
        data = load_data(file)
        if data is not None:
            st.success("Données chargées avec succès !")
            st.dataframe(data.head())

            # Sélection d'analyse
            option = st.sidebar.selectbox(
                "Choisissez une analyse :",
                ["Statistiques descriptives", "Visualisation : Histogramme", "Visualisation : Heatmap"]
            )

            if option == "Statistiques descriptives":
                descriptive_analysis(data)

            elif option == "Visualisation : Histogramme":
                column = st.selectbox("Choisissez une colonne :", data.select_dtypes(include=['number']).columns)
                plot_histogram(data, column)

            elif option == "Visualisation : Heatmap":
                plot_correlation_heatmap(data)

# Lancer l'application
if __name__ == "__main__":
    main()
