import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurer Streamlit
st.set_page_config(page_title="Analyse Walmart", layout="wide")

# Charger les données
def load_data():
    uploaded_file = st.file_uploader("Téléchargez le fichier Walmart.csv", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Données chargées avec succès!")
        return df
    else:
        st.warning("Veuillez télécharger un fichier pour commencer.")
        return None

# Nettoyage des données
def clean_data(df):
    st.subheader("Nettoyage des données")
    st.write("**Aperçu initial :**")
    st.dataframe(df.head())

    # Identifier les valeurs manquantes
    missing_values = df.isnull().sum()
    st.write("**Valeurs manquantes :**")
    st.dataframe(missing_values)

    # Supprimer les doublons
    df = df.drop_duplicates()
    st.write("**Données après suppression des doublons :**")
    st.write(f"{len(df)} lignes restantes après nettoyage.")
    return df

# Analyse des ventes par catégorie
def analyse_par_categorie(df):
    st.subheader("Chiffre d'affaires par catégorie")
    df["montant"] = df["quantity_sold"] * df["unit_price"]
    ventes_par_categorie = df.groupby("category")["montant"].sum()

    st.write("**Montant total par catégorie :**")
    st.dataframe(ventes_par_categorie)

    # Visualisation
    fig, ax = plt.subplots()
    sns.barplot(x=ventes_par_categorie.index, y=ventes_par_categorie.values, ax=ax)
    ax.set_title("Chiffre d'affaires par catégorie")
    ax.set_xlabel("Catégorie")
    ax.set_ylabel("Montant")
    st.pyplot(fig)

# Chiffre d'affaires par localisation
def analyse_par_magasin(df):
    st.subheader("Chiffre d'affaires par localisation")
    df["montant"] = df["quantity_sold"] * df["unit_price"]

    CA_magasin = df.groupby("store_location")["montant"].sum().sort_values(ascending=False)

    st.write("**Montant total par magasin :**")
    st.dataframe(CA_magasin)

    # Visualisation
    fig, ax = plt.subplots()
    sns.barplot(x=CA_magasin.index, y=CA_magasin.values, ax=ax)
    ax.set_title("Chiffre d'affaires par magasin")
    ax.set_xlabel("Localisation")
    ax.set_ylabel("Montant")
    st.pyplot(fig)

# Analyse météo
def analyse_par_meteo(df):
    st.subheader("Chiffre d'affaires par condition météorologique")
    df["montant"] = df["quantity_sold"] * df["unit_price"]

    meteo = df.groupby("weather_conditions")["montant"].sum().sort_values(ascending=False)

    st.write("**Montant total par condition météorologique :**")
    st.dataframe(meteo)

    # Visualisation
    fig, ax = plt.subplots()
    sns.barplot(x=meteo.index, y=meteo.values, ax=ax)
    ax.set_title("Chiffre d'affaires par condition météorologique")
    ax.set_xlabel("Condition météo")
    ax.set_ylabel("Montant")
    st.pyplot(fig)

# Analyse par genre
def analyse_par_genre(df):
    st.subheader("Chiffre d'affaires par genre")
    df["montant"] = df["quantity_sold"] * df["unit_price"]

    genre = df.groupby("customer_gender")["montant"].sum().sort_values(ascending=False)

    st.write("**Montant total par genre :**")
    st.dataframe(genre)

    # Visualisation
    fig, ax = plt.subplots()
    sns.barplot(x=genre.index, y=genre.values, ax=ax)
    ax.set_title("Chiffre d'affaires par genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Montant")
    st.pyplot(fig)

# Analyse par jour de la semaine
def analyse_par_jour(df):
    st.subheader("Chiffre d'affaires par jour de la semaine")
    df["montant"] = df["quantity_sold"] * df["unit_price"]

    jour = df.groupby("weekday")["montant"].sum().sort_values(ascending=False)

    st.write("**Montant total par jour de la semaine :**")
    st.dataframe(jour)

    # Visualisation
    fig, ax = plt.subplots()
    sns.barplot(x=jour.index, y=jour.values, ax=ax)
    ax.set_title("Chiffre d'affaires par jour de la semaine")
    ax.set_xlabel("Jour")
    ax.set_ylabel("Montant")
    st.pyplot(fig)

# Exporter les données nettoyées
def export_data(df):
    st.subheader("Exporter les données nettoyées")
    if st.button("Exporter"):
        df.to_csv("Walmart_cleaned.csv", index=False)
        st.success("Données exportées avec succès en tant que Walmart_cleaned.csv")

# Application principale
def main():
    st.title("Analyse Business Intelligence Walmart")
    st.write("Cette application analyse les données pour identifier des opportunités de croissance et d'optimisation.")

    # Charger les données
    df = load_data()
    if df is not None:
        # Nettoyer les données
        df = clean_data(df)

        # Sélection d'analyse
        option = st.sidebar.selectbox(
            "Choisissez une analyse :",
            [
                "Chiffre d'affaires par catégorie",
                "Chiffre d'affaires par magasin",
                "Analyse par météo",
                "Analyse par genre",
                "Analyse par jour de la semaine",
            ],
        )

        # Effectuer l'analyse
        if option == "Chiffre d'affaires par catégorie":
            analyse_par_categorie(df)
        elif option == "Chiffre d'affaires par magasin":
            analyse_par_magasin(df)
        elif option == "Analyse par météo":
            analyse_par_meteo(df)
        elif option == "Analyse par genre":
            analyse_par_genre(df)
        elif option == "Analyse par jour de la semaine":
            analyse_par_jour(df)

        # Exporter les données nettoyées
        export_data(df)

if __name__ == "__main__":
    main()
