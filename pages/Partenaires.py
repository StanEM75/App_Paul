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
        Car ce qui compte, c'est votre épanouissement.
    </div>
    """,
    unsafe_allow_html=True
)

# Ajouter un espace entre le texte et les blocs
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Ajoute des sauts de ligne pour espacer

# Blocs rectangulaires espacés pour montrer les partenaires
with st.container():
    col1, _, col2, _, col3 = st.columns([2, 0.5, 2, 0.5, 2])  # Les blocs (40%) sont séparés par des espaces vides

    with col1:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 20px;'>Cheval Blanc</strong><br>
                <img src="https://media.admagazine.fr/photos/61309c320bffc5863ae5070b/4:3/w_2792,h_2094,c_limit/Cheval-Blanc-Paris_Le-Tout-Paris-%C2%A9-Alexandre-Tabaste-(4).jpg" 
                     style="max-width: 100%; height: auto; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 20px;'>Grand Hôtel du Cap</strong><br>
                <img src="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/2e/9d/68/ghf-pool.jpg?w=700&h=-1&s=1" 
                     style="max-width: 100%; height: auto; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 20px;'>Martinez Cannes</strong><br>
                <img src="https://assets.hyatt.com/content/dam/hyatt/hyattdam/images/2023/08/01/1127/JCAGH-P1819-La-Plage-du-Martinez-Overview.jpg/JCAGH-P1819-La-Plage-du-Martinez-Overview.16x9.jpg" 
                     style="max-width: 100%; height: auto; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

# Ajouter un espace entre les trois blocs et le nouveau bloc
st.markdown("<br><br>", unsafe_allow_html=True)

# Bloc centré en dessous des trois blocs pour donner plus de choix
st.markdown(
    """
    <div style='background-color: #d3d3d3; padding: 20px; border-radius: 5px; text-align: center; width: 60%; margin: 0 auto;'>
        <strong style='font-size: 18px;'>Découvrir plus d'entreprises</strong>
    </div>
    """,
    unsafe_allow_html=True
)

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Bloc "Ils travaillent avec nous"
with st.container():
    _, col1, col2, _ = st.columns([1, 2, 4, 1])  

    with col1:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 40px; border-radius: 5px; text-align: center; height: 300px;'>
                <strong style='font-size: 20px;'></strong><br>
                <img src="https://as1.ftcdn.net/v2/jpg/02/02/45/82/1000_F_202458278_coA4UnROafSUFzHnfMluUDy3ZOd82zvV.jpg"
                style="max-width: 100%; height: auto; border-radius: 5px; margin-top: 20px;" /> 
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 20px; border-radius: 8px; text-align: center; height: 300px;
                    display: flex; flex-direction: column; justify-content: flex-start;'>
            <h1 style='font-size: 20px; font-weight: bold;'>Ils travaillent avec nous !</h1>
                <strong style='font-size: 14px;'>Nous utilisons l'application de recrutement depuis quelques mois et en sommes entièrement satisfaits. Elle a nettement amélioré notre efficacité dans le tri et la sélection des candidatures, tout en nous aidant à trouver des profils parfaitement adaptés à nos besoins. L'interface intuitive et le support client réactif ont simplifié notre gestion des recrutements au quotidien. Un outil indispensable pour notre équipe RH. Équipe RH, Hôtel Le Luxor</strong><br>
            </div>
            """,
            unsafe_allow_html=True
        )

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Ajouter plus d'espace avant le bas du bloc
st.markdown("<br><br>", unsafe_allow_html=True)  # Ajoute plus de sauts de ligne

# Bloc inférieur avec "Season" et les logos sociaux
with st.container():
    _, col1, _, col2, _, col3 = st.columns([2, 2, 1, 2, 1, 2])  # 40% chacun

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




