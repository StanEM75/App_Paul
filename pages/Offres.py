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
    <div style='text-align: center; font-size: 18px;'>
        La saison parfaite c'est :
    </div>
    """,
    unsafe_allow_html=True
)

# Bloc Titre et Filtres
with st.container():
    _, col1, col2, col3, col4, _ = st.columns([1, 2, 2, 2, 2, 1])

    with col1:
        st.selectbox(
            "Emploi recherché",
            ("Voiturier", "Serveur", "Barman", "Baby-Sitter", "Vendeur", "Réceptionniste", "Bagagiste"),
            key = "emploi"
        )

    with col2:
        st.selectbox(
            "Lieu souhaité",
            ("Paris", "Lyon", "Cannes", "Nice", "Marseille", "Lille", "Strasbourg"),
            key = "lieu"
        )

    with col3:
        st.selectbox(
            "Secteur souhaité",
            ("Hôtellerie", "Restauration", "Tourisme", "Garde d'enfants"),
            key = "secteur"
        )

    with col4:
        st.selectbox(
            "Critères",
            ("5 ans d'expérience", "Disponible tout de suite", "Profil validé"),
            key = "critere"
        )

# Ligne de séparation
st.markdown("<hr style='border: 1px solid #eee;'>", unsafe_allow_html=True)

# Ajouter un espace entre le texte et les blocs
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Ajoute des sauts de ligne pour espacer

import streamlit as st

# Bloc Emplois
with st.container():
    _, col1, col2, col3, col4, _ = st.columns([1, 2, 2, 2, 2, 1])

    with col1:
        st.markdown(
            """
            <div style='background-color: #383432; padding: 20px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 15px; color: white;'>Bagagiste - Paris</strong><br>
                <span style="color: white;">Ritz Paris</span><br>
                <img src="https://mir-s3-cdn-cf.behance.net/projects/404/a466b527686053.Y3JvcCwyMzYxLDE4NDcsNTcyLDMxNQ.jpg" 
                     style="max-width: 100%; height: auto; object-fit: contain; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 20px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 15px;'>Voiturier - Paris</strong><br>
                <span>Royal Monceau Paris</span><br>
                <img src="https://www.theluxevoyager.com/wp-content/uploads/2018/02/Le-Royal-Monceau-Raffle-Paris-Logo.jpeg" 
                     style="max-width: 100%; height: auto; object-fit: contain; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 20px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 15px;'>Voiturier - Saint-Tropez</strong><br>
                <span>Lily of the Valley</span><br>
                <img src="https://static.apidae-tourisme.com/filestore/objets-touristiques/logos/97/231/14542689/Apidae%20pour%20Philippa%2056.jpg" 
                     style="max-width: 100%; height: auto; object-fit: contain; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div style='background-color: #a29a98; padding: 20px; border-radius: 5px; text-align: center; height: 300px; 
                        display: flex; flex-direction: column; justify-content: center; align-items: center;'>
                <strong style='font-size: 15px;'>Bagagiste - Cannes</strong><br>
                <span>Martinez Cannes</span><br>
                <img src="https://upload.wikimedia.org/wikipedia/en/thumb/d/da/H%C3%B4tel_Martinez_Logo.webp/250px-H%C3%B4tel_Martinez_Logo.webp.png" 
                     style="max-width: 100%; height: auto; object-fit: contain; border-radius: 5px; margin-top: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

# Ajouter un espace entre le texte et les blocs
st.markdown("<br><br><br>", unsafe_allow_html=True)  # Ajoute des sauts de ligne pour espacer

# Bloc Informations du poste
with st.container():
    st.markdown(
        """
        <div style='background-color: #383432; padding: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
            <h3 style='font-size: 24px; font-weight: bold; text-align: center;'>Ritz Paris</h3>
            <div style='font-size: 18px; margin-top: 20px;'>
                <strong>Département :</strong> Réception<br>
                <strong>Type de Contrat :</strong> Temps plein<br>
                <strong>Rattachement Hiérarchique :</strong> Chef de Réception<br>
                <strong>Poste :</strong> Bagagiste - Paris
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Bloc Description détaillée du poste
with st.container():
    st.markdown(
        """
        <div style='background-color: #383432; padding: 20px; border-radius: 8px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);'>
            <h3 style='font-size: 24px; font-weight: bold; text-align: center; color: white;'>Ritz Paris - Missions du Bagagiste</h3>
            <p style='font-size: 18px; color: white; margin-top: 20px;'>
                Le bagagiste est un acteur clé de l'accueil et du service clientèle au Ritz Paris. Il assure le transport et la gestion des bagages des clients, tout en garantissant une expérience de service exceptionnelle, en ligne avec les standards de luxe du Ritz Paris.
                Ses missions principales incluent :<br>
                - <strong>Accueil des Clients :</strong> Accueillir les clients dès leur arrivée avec courtoisie et professionnalisme.<br>
                - <strong>Gestion des Bagages :</strong> Transporter les bagages des clients de l'entrée de l'hôtel jusqu'à leur chambre et vice-versa lors de leur départ.<br>
                - <strong>Service en Chambre :</strong> Assister les clients en répondant à leurs demandes spécifiques liées aux bagages et aux déplacements internes.<br>
                - <strong>Coordination :</strong> Collaborer étroitement avec la réception et le concierge pour assurer une communication fluide et un service efficace.<br>
                - <strong>Information :</strong> Fournir aux clients des informations sur les services de l'hôtel, les attractions locales et répondre à leurs questions.<br>
                - <strong>Sécurité :</strong> Veiller à la sécurité et à l'intégrité des bagages confiés, en respectant les procédures de l'hôtel.<br>
                - <strong>Maintenance des Chariots :</strong> S'assurer que les chariots à bagages sont en bon état de fonctionnement et maintenus propres.
            </p>
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



