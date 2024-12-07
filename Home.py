import streamlit as st

# Configuration de la mise en page (doit être la première commande)
st.set_page_config(layout="wide")  # Largeur totale de la page

# Ajouter du CSS personnalisé pour définir le fond de la page
st.markdown(
    """
    <style>
        body {
            background-color: #ece0dc;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Bloc Titre et Filtres
with st.container():
    col1, col2 = st.columns([2, 1])  # Titre (2/3) et Filtres (1/3)

    with col1:
        st.markdown(
            """
            <div style='font-size: 28px; font-weight: bold;'>
                Trouver la saison parfaite
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.selectbox(
            "Emploi recherché",
            ("Voiturier", "Serveur", "Barman", "Baby-Sitter", "Vendeur", "Réceptionniste", "Bagagiste")
        )
        st.selectbox(
            "Lieu souhaité",
            ("Paris", "Lyon", "Cannes", "Nice", "Marseille", "Lille", "Strasbourg")
        )
        st.selectbox(
            "Critères",
            ("5 ans d'expérience", "Disponible tout de suite", "Profil validé")
        )

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Texte promotionnel
st.markdown(
    """
    <div style='text-align: center; font-size: 18px;'>
        <strong>Découvrez Season</strong>, la plateforme qui relie saisonniers et employeurs.
    </div>
    """,
    unsafe_allow_html=True
)

# Ajouter un espace entre le texte et les blocs
st.markdown("<br><br>", unsafe_allow_html=True)  # Ajoute deux sauts de ligne pour espacer

# Blocs rectangulaires espacés et plus longs avec la nouvelle couleur
with st.container():
    col1, _, col2, _ = st.columns([2, 1, 2, 1])  # Les blocs (40%) sont séparés par des espaces vides

    with col1:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px;'>
                <strong style='font-size: 20px;'>Côté employeur</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px;'>
                <strong style='font-size: 20px;'>Côté saisonnier</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

# Ajouter plus d'espace avant le bas du bloc
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Ajoute plus de sauts de ligne

# Bloc inférieur avec "Season" et les logos sociaux
with st.container():
    col1, col2, col3 = st.columns([2, 1, 2])  # 40% chacun

    with col1:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 30px; border-radius: 5px; text-align: center; height: 250px;'>
                <strong style='font-size: 24px;'>Season</strong><br>
                <a href="https://www.instagram.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" height="30"></a>
                <a href="https://www.linkedin.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" height="30"></a>
                <a href="https://www.youtube.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" height="30"></a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 30px; border-radius: 5px; text-align: center; height: 250px;'>
                <strong style='font-size: 24px;'>A propos</strong><br>
                <a href="#" style="font-size: 18px;">Concept</a><br>
                <a href="#" style="font-size: 18px;">Centre d'aide</a>
            </div>
            """,
            unsafe_allow_html=True
        )
