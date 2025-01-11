import streamlit as st

# Configuration de la mise en page
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

# Texte en haut
st.markdown(
    """
    <div style='text-align: center; font-size: 28px;'>
        Bienvenue dans ton espace de candidature !
    </div>
    <div style='text-align: center; font-size: 18px;'>
        Suis tes candidatures et trouve le job parfait pour toi.
    </div>
    """,
    unsafe_allow_html=True
)

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Bloc Titre et Filtres
with st.container():
    _, col1, col2, col3, col4, _ = st.columns([1, 2, 2, 2, 2, 1])

    with col1:
        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 10px; text-align: center; border-radius: 5px; border: 1px solid #ccc; font-size: 14px; color: black;">
            It's a match!
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 10px; text-align: center; border-radius: 5px; border: 1px solid #ccc; font-size: 14px; color: black;">
            Mon job actuel
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 10px; text-align: center; border-radius: 5px; border: 1px solid #ccc; font-size: 14px; color: black;">
            Jobs enregistrés
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="background-color: #f0f0f0; padding: 10px; text-align: center; border-radius: 5px; border: 1px solid #ccc; font-size: 14px; color: black;">
            Mon coffre-fort
        </div>
        """, unsafe_allow_html=True)

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Texte promotionnel
st.markdown(
    """
    <div style='text-align: center; font-size: 18px;'>
        Félicitations ! Cet employeur te veut dans son équipe.
    </div>
    """,
    unsafe_allow_html=True
)

# Bloc Description détaillée de l'employeur
with st.container():
    st.markdown(
        """
        <div style='background-color: #383432; padding: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
            <h3 style='font-size: 24px; font-weight: bold; text-align: center;'>[Entreprise] veut te recruter pour le poste de [Poste]</h3>
            <div style='font-size: 18px; margin-top: 20px;'>
                <strong>Entreprise :</strong><br>
                <strong>Description du poste :</strong><br>
                <strong>Lieu :</strong><br>
                <strong>Durée :</strong><br>
                <strong>Rémunération :</strong><br>
                <strong>Avantages mis en place par l'employeur :</strong><br>
                <strong>Email :</strong><br>
                <strong>Téléphone :</strong><br>
                <strong>Message de l'employeur :</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Ajouter un espace entre le texte et les blocs
st.markdown("<br><br>", unsafe_allow_html=True)  # Ajoute des sauts de ligne pour espacer

# Bloc inférieur avec "Season" et les logos sociaux
with st.container():
    # Créer un seul bloc avec tout le footer
    st.markdown(
        """
        <div style='background-color: #a29a98; padding: 20px; display: flex; justify-content: space-between; align-items: center; border-radius: 5px;'>
            <div style='text-align: left;'>
                <a href="https://www.instagram.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="30" height="30"></a>
                <a href="https://www.linkedin.com" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="30" height="30"></a>
                <a href="https://www.youtube.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" width="30" height="30"></a>
            </div>
            <div style='text-align: right;'>
                <strong style='font-size: 24px;'>À propos</strong><br>
                <a href="#" style="font-size: 18px;">Concept</a><br>
                <a href="#" style="font-size: 18px;">Centre d'aide</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )