import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Jouet Évolué", page_icon=":robot_face:")

# Sommaire dans la barre latérale
st.sidebar.markdown("<h2 style='text-align: center; color: #2E8B57;'>Sommaire</h2>", unsafe_allow_html=True)
pages = ['Introduction', "Fonctionnalités", "Reconnaissance Vocale", "Reconnaissance Visuelle", "Modélisation",
         "Réseau et interconnexions", "Rapports et suivi","Roadmap", "Ebauche de Budget", "Les Professionnels en Parlent", "Conclusion", "Evolutions","Remerciements"]
page = st.sidebar.radio("Aller vers", pages)

# Ajouter un cadre avec les auteurs sous le sommaire
st.sidebar.markdown("""
<div style="border: 1px solid #87CEEB; padding: 5px; background-color: #E0FFFF; margin-top: 10px;">
    <h3 style="text-align: center; color: #4682B4; margin-bottom: 5px;">Auteurs :</h3>
    <ul style="list-style-type: none; padding-left: 0; font-size: 12px; line-height: 1.2;">
        <li>- Manuel Manresa</li>
        <li>- Ronan-Yann Lorin</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Affichage des sections selon la page sélectionnée
if page == 'Introduction':
    st.markdown(
        "<h1 style='text-align: center; color: #1E90FF;'>Présentation d'un 'Jouet' Évolué pour Enfants et Adultes Déficients Auditifs ou Muets</h1>",
        unsafe_allow_html=True)

    # image_path_1 = r"C:\Users\MANRESA\Documents\DESC\5_Informatique\Projet Michka\Images\Michka.jpg"
    image_path_1 = "./assets/Michka.jpg"
    st.image(image_path_1, caption="Michka", use_container_width=True)

    st.write("""
    **MICHKA** est un acronyme qui reflète les principales caractéristiques de ce jouet évolué :

    - **M**odulaire : Capacité à être adapté et personnalisé selon les besoins individuels de chaque enfant.
    - **I**ntelligent : Intégration de technologies avancées pour offrir des solutions intelligentes.
    - **C**ommunicant : Amélioration de la communication entre l'enfant et son entourage.
    - **H**umain : Interaction centrée sur l'utilisateur, adaptée aux besoins humains.
    - **K**inesthésique : Reconnaissance des mouvements et des gestes pour une interaction fluide.
    - **A**rtificielle : Utilisation de l'intelligence artificielle pour enrichir l'expérience d'apprentissage.

    Michka est un 'jouet' innovant qui utilise la technologie pour faire une différence positive dans la vie des enfants déficients auditifs, non verbaux ou autistes. En facilitant l'apprentissage de la langue des signes, ou du Makaton, non seulement pour les enfants mais aussi pour leurs parents et les professionnels, Michka aide à surmonter les barrières de communication et à réduire la frustration liée au non-langage.
    """)

    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Quelques chiffres: </h2>", unsafe_allow_html=True)
    st.write("""
    La fédération mondiale des sourds estime qu'il y a environ 70 000 000 sourds dans le monde,
     mais aucune évaluation statistique de la population de Sourds n'a été réalisée faute de consensus.
     En France, on dénombre 5 000 000 de personnes atteintes de surdité, dont 300000 à 500000 Sourds profonds. 
     Parmi eux, environ 120 000 personnes utilisent la Langue des signes couramment.
     200 enfants naissent sourds et 800 surdités sont reconnues chaque année, sans parler des troubles du langage et des muets qui rentrent 
     dans la catégorie des troubles psychologiques.
        """)

    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Michka Pour Qui ?</h2>", unsafe_allow_html=True)
    st.write("""

    - **Enfants déficients auditifs :** Environ 1 à 3 enfants sur 1 000 naissent avec une perte auditive significative, et Michka vise à répondre à leurs besoins spécifiques en matière de communication.
    - **Enfants non verbaux :** Ceux qui ont des difficultés à s'exprimer verbalement, y compris les enfants autistes, peuvent bénéficier de l'interaction gestuelle et visuelle que Michka propose.
    - **Adultes ayant subi un AVC ou présentant des troubles du langage :** Michka peut aider à la réhabilitation en offrant une plateforme d'apprentissage adaptée.
    - **Les professionnels env 23000 Orthophonistes :** Avoir un meilleur suivi d'évolution des enfants.
    - **Particuliers proches d’un enfant handicapé :** Afin de lui faciliter l’apprentissage de la LSF, afin de les aider à apprendre également la LSF.
    - **Particuliers proches d’un adulte handicapé :** Afin de communiquer avec lui, afin de les aider à apprendre également la LSF.
    - **Les centres spécialisé :** Avec le professionnel, en groupe ou en individuel, en reproduisant par geste le mot du professionnel.
    - **Les hôpitaux, médecins, services d’urgence :** susceptibles de recevoir un adulte handicapé.
    - **Les entreprises souhaitant promouvoir l’inclusion des Sourds.**
    - **Les administrations susceptibles d’accueillir un adulte handicapé.**
    """)

    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Michka Pourquoi ?</h2>", unsafe_allow_html=True)

    st.markdown("""
        MICHKA offre plusieurs avantages clés :

        - **Suivi personnalisé** : Répond à un suivi personnalisé en plus du suivi du professionnel.
        - **Un éveil** : Par le jeux, et le toucher chez les enfants. 
        - **Continuité d'apprentissage** : Assure une continuité en cas de déménagement, d'absence du professionnel, ou pendant les vacances.
        """)

    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Voici à quoi répond Michka :</h2>", unsafe_allow_html=True)
    st.write("""
    - **Accessibilité et Inclusivité :** Écran tactile facile à utiliser pour les enfants de différentes capacités. Des interfaces simples et intuitives pour aider à maximiser l'accessibilité.

    - **Personnalisation :** Un programme personnalisé avec les professionnels pour adapter certains aspects de Michka, comme les gestes ou les signes enseignés, pour rendre l'expérience plus engageante.

    - **Feedback Positif :** Des mécanismes de feedback positif sont intégrés pour encourager et motiver les enfants lorsqu'ils apprennent de nouveaux signes.

    - **Collaboration avec des Experts :** Travailler avec des spécialistes en éducation spécialisée et en langue des signes pour enrichir le contenu et l'approche pédagogique de Michka.

    - **Évaluation et Adaptation :** Évaluation des progrès des enfants et adaptation du contenu en fonction de leurs besoins individuels.

    - **Intégration Technologique :** Utilisation de technologies comme la reconnaissance gestuelle et l'intelligence artificielle pour améliorer l'interaction et l'apprentissage.
    """)

elif page == 'Fonctionnalités':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Fonctionnalités</h2>", unsafe_allow_html=True)

    #image_path_2 = r"C:\Users\MANRESA\Documents\DESC\5_Informatique\Projet Michka\Images\Mishka_V1.png"
    image_path_2 = "./assets/Michka_Detail_V0.jpg"
    st.image(image_path_2, caption="Michka - Version Avancée", width=1000)

    st.subheader("Enseignement de la Langue des Signes LSF")
    st.write("""
    - **Approche Multimodale :** Michka utilise une combinaison de petites vidéos, d'images et de démonstrations gestuelles réalisées par ses propres mains pour enseigner la langue des signes aux enfants. Cette approche multimodale permet de capter l'attention des enfants et de faciliter leur apprentissage.

    - **Interaction Active :** L'enfant est encouragé à reproduire les gestes présentés par Michka. Grâce à ses capteurs avancés, Michka peut détecter et valider les gestes de l'enfant, fournissant un retour immédiat et positif pour renforcer l'apprentissage.

    - **Reconnaissance Vocale Intégrée :** Les parents ou les professionnels peuvent prononcer un mot, que Michka affichera à l'écran tout en montrant le signe correspondant avec ses mains. Cette fonctionnalité aide non seulement les enfants à associer les mots aux signes, mais elle offre également un outil d'apprentissage interactif pour les adultes qui les accompagnent.

    - **Personnalisation de l'Enseignement :** Le programme d'enseignement peut être personnalisé selon les besoins spécifiques de chaque enfant, permettant une adaptation des signes et des gestes en fonction de leur niveau de progression et de leurs préférences individuelles.
    
    - **Traducteur Langue des Signes (LSF) <=> Paroles :** Traduit la langue des signes en paroles, et les paroles en Langue des signes.
    """)

    st.subheader("Caméra de Détection Sommeil")
    st.write("""
    - Détection du sommeil avec envoi d'une notification au téléphone des parents si le bébé ou l'enfant est réveillé.
    """)

    st.subheader("Capteur de Mouvement et Reconnaissance Gestuelle")
    st.write("""
    - Détection si le bébé pleure et envoi d'une alerte.
    - Reconnaissance dynamique de la gestuelle de l'enfant avec traduction vocale pour les personnes qui ne connaissent pas la langue des signes.
    - Validation de la gestuelle de l'enfant et affichage du mot utilisé.
    - Interactivité améliorée grâce à la capacité de comprendre et de répondre aux gestes de l'enfant.
    """)

    st.subheader("Lumière d'Ambiance et Réveil Lumineux")
    st.write("""
    - Lumière d'ambiance pour aider à dormir.
    - Réveil lumineux avec intensité lumineuse progressive.
    """)

    st.subheader("Horloge et Mise en Veille")
    st.write("""
    - Fonctionnalités d'horloge et de mise en veille.
    - Affichage des informations sur le téléphone.
    """)

    st.subheader("Interactions et Encouragements")
    st.write("""
    - Haut-parleurs (enceintes) intégrés.
    - Applaudissements lorsque l'enfant réussit une tâche.
    - Affichage d'un pouce levé en signe de réussite.
    - Mouvement du doigt pour dire non.
    - Affichage lumineux au niveau de la main et des oreilles pour confirmer la réussite ou non.
    - Place ses mains en avant en cas de chute.
    """)

    st.subheader("Musiques Chansons et danses")
    st.write("""
    - Chansons d'éveils à la parole. 
    - Danses musicales, gestes définis par les professionnels exercices adaptés en groupes ou individuels.
    """)
    # Intégrer la musique
    audio_file_path = "./assets/2025-01-25_14-34-07.mp4"
    audio_file = open(audio_file_path, 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

    # Intégrer la vidéo
    video_file_path ="./assets/2025-01-25_14-34-07.mp4"
    st.video(video_file_path, format='video/mp4')

elif page == 'Reconnaissance Vocale':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Reconnaissance Vocale</h2>", unsafe_allow_html=True)
    st.write("""
    Détails sur la fonctionnalité de reconnaissance vocale et comment elle aide à l'apprentissage du langue des signes.
    """)

elif page == 'Reconnaissance Visuelle':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Reconnaissance Visuelle</h2>", unsafe_allow_html=True)
    st.write("""
    Détails sur la reconnaissance visuelle et son rôle dans l'interaction avec le jouet.
    """)

elif page == 'Modélisation':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Modélisation</h2>", unsafe_allow_html=True)
    st.write("""
    Description des modèles utilisés pour les différentes fonctionnalités du jouet.
    """)

elif page == 'Réseau et interconnexions':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Réseau et interconnexions</h2>", unsafe_allow_html=True)
    st.write("""
    Description du réseau d'interconnexion de "MICHKA".
    """)
    # image_path_3 = r"C:\Users\MANRESA\Documents\DESC\5_Informatique\Projet Michka\Images\Principe_2.jpg"
    image_path_3 = "./assets/Principe_2.jpg"     
    st.image(image_path_3, caption="Michka - Version Avancée", width=1000)

elif page == 'Rapports et suivi':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Rapports et suivi</h2>", unsafe_allow_html=True)
    st.write("""
    Affiche des statistiques d'apprentissages de l'enfant. Permet au professionnel d'adapté son travail lors de ses rendez-vous avec l'enfants, 
    de voir la difficulté sur l'apprentissage d'un mot, et de le travailler en séance.
    - Suivi personnalisé de l'évolution de l'enfant selon un programme défini par des professionnels.
    - Génération de rapports réguliers pour les parents et les éducateurs, détaillant les progrès et les domaines à améliorer.
    - Adaptation dynamique des activités en fonction des performances de l'enfant pour maximiser l'apprentissage.
    - Graphique des appétances de l'enfant répétitions (choix musicaux, vidéos, etc...).
    """)

elif page == 'Roadmap':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Roadmap</h2>", unsafe_allow_html=True)

    st.markdown("""
    ### **Phase 1 : Étude**
    - Étude d'opportunité
    - Étude de Marché
    - ***Échéance : Juin 2025***
    """)

    st.markdown("""
    ### **Phase 2 : Démonstrateur**
    Le démonstrateur consiste à démontrer les principales fonctionnalités de Michka et la manière dont il interagit avec l'utilisateur.
    Michka aura une partie des fonctionnalités actives mais ne ressemblera pas encore à l'ourson tel qu'il sera commercialisé.
    - ***Échéance : Janvier 2026***
    """)

    st.markdown("""
    ### **Phase 3 : Industrialisation**
    - Tests par les professionnels
    - Prototype finalisé et industrialisable
    - Marketing, packaging, publicité
    - ***Échéance : Septembre 2026***
    """)

    st.markdown("""
    ### **Phase 4 : Commercialisation**
    - ***À partir de Septembre 2026*** pour une distribution à partir de Décembre 2026.
    """)


elif page == 'Ebauche de Budget':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Ebauche de Budget</h2>", unsafe_allow_html=True)
    st.write("""
    Le développement de Michka nécessite un budget pour la recherche, le développement technologique, la collaboration avec des experts, ainsi que pour les infrastructures de serveur et d'hébergement.
    Nous cherchons des partenaires et des financements pour soutenir ce projet innovant.

    Voici une estimation des coûts pour les composants matériels nécessaires :
    
    - **Total des coûts Michka :** 1055€
    - **Total des coûts matériels pour le développement :** 4370€
    - **Total des coûts liés au serveur et à l'hébergement :** 1800€
    - **Total des éléments supplémentaires :** 17 510€
    
    **Total général des Coûts Matériels et Services :** 24 735€ TTC

    **Composants Michka :**
    - **Raspberry Pi 5 16 Go :** 150€
    - **Raspberry Pi 5 M.2 HAT - SSD NVMe 256GB :** 60€
    - **Écran tactile Raspberry 10 pouces :** 80€
    - **Mini Haut-Parleurs (x2) :** 10€ chacun, total 20€
    - **Raspberry Pi Camera à vision nocturne :** 15€
    - **Caméra 5 MP :** 15€
    - **Caméra port USB :** 10€
    - **Servomoteurs :** 15€
    - **LEDs RGB (x10) :** 2€ chacune, total 20€
    - **Capteur de mouvement (PIR) :** 10€
    - **Capteur de son :** 10€
    - **Capteur de lumière :** 10€
    - **Module Wi-Fi/Bluetooth :** 20€
    - **Batterie rechargeable :** 30€
    - **Câblage et connecteurs divers :** 100€
    - **Capteurs sur les doigts pour le toucher (x10) :** 2€ chacun, total 20€
    - **Capteurs pour le nez, les oreilles, le pied, la jambe, le bras :** 2€ chacun, total 20€
    - **Main droite Robotique :** 255€
    - **Main gauche Robotique :** 255€

    **Total des coûts Michka :** 1055€

    **Matériel pour le développement :**
    - **Imprimante 3D :** 500€
    - **Consomable résine :** 96€
    - **Ordinateur :** 3000€
    - **Caméra pour la prise de vidéos :** 200€
    - **Logiciel de montage vidéo :** 400€
    - **Arduino Uno :** 24€
    - **Shield E/S Gravity V7 :** 10€
    - **Adaptateur PCM10f :** 2€
    - **10 Capteurs de flexion 74mm FS2L055 :** 135€
    - **Paire de gant antistatiques :** 3€

    **Total des coûts matériels pour le développement :** 4370€

    **Coûts liés au serveur et à l'hébergement :**
    - **Serveur dédié ou cloud (par an) :** 1000€
    - **Maintenance et support serveur :** 400€
    - **Hébergement web et base de données (par an) :** 200€
    - **Sécurité et sauvegarde des données :** 200€

    **Total des coûts liés au serveur et à l'hébergement :** 1800€

    **Éléments supplémentaires :**
    - **Assurance équipement :** 600€
    - **Frais INPI :** 60€
    - **Consultation juridique et suivi:** 3000€
    - **Professionnel pour la langue des signes :** 2000€
    - **Arrangement Vidéos musiques et chansons : 2500€
    - **Etude de marché :** 7350€
    - **Tests Professionnels et validation :** 2000€

    **Total des éléments supplémentaires :** 17 510€

    **Total général des Coûts Matériels et Services :** 24 735€ TTC
    """)

elif page == 'Les Professionnels en Parlent':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Les Professionnels en Parlent</h2>", unsafe_allow_html=True)
    st.write("""
    Des professionnels de l'éducation spécialisée et de la santé ont exprimé leur enthousiasme pour Michka.
    Ils voient en ce jouet un outil précieux pour aider les enfants à surmonter les barrières de communication.
    """)
    st.subheader("Témoignages")
    st.write("""
    - "Le projet Michka qui m'a été présenté par M. Manresa me paraît très prometteur pour l'évolution langagière des jeunes enfants que j'accompagne en tant qu'orthophoniste. Nous avons besoin d'outils stimulants et motivants en parallèle des prises en charge thérapeutiques plus classiques afin de maintenir chez les enfants à besoins particuliers une vraie appétence à la communication et aux interactions.
La possibilité de décider, en équipe avec les parents, des modalités d'apprentissage de nouveaux signes de la LSF permettront de renforcer l'alliance thérapeutique autour d'un projet multimodal innovant. J'ai hâte de pouvoir tester ce nouvel outil dans la crèche où j'exerce ! Bravo !
." 
Dr. Pauline Couzy, Orthophoniste crèche spécialisée Poulpi le 23/01/2025

- "Je viens d'assister à la présentation d'un petit robot interactif à la technologie de pointe Michka.
Ses multiples fonctions de communication via le MAKATON et la LSF vont être très utiles à un grand nombre de personnes, 
non seulement des personnes présentant divers handicaps comme, les personnes malentendantes, les personnes non verbales, 
les personnes atteintes de maladies neurodégénératives mais, également leur entourage, famille, amis, corps médical, administratif...
Michka est capable de traduire des gestes en signes et inversement.
Il possède de nombreuses autres fonctionnalités pour interagir avec ses usagers.
Je suis très enthousiaste sur l'avenir de ce petit robot qui, je pense, va s'avérer indispensable dans de nombreux domaines et lieux,
à la maison, la crèche, l'école, en rééducation, dans les lieux de soins, en société en général. 
Michka a donc un avenir florissant et je serai fière en tant qu'orthophoniste d'y apporter mon humble contribution."
Dr Christine Mesbah, Orthophoniste le 28/01/2025  

    """)

elif page == 'Conclusion':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Conclusion</h2>", unsafe_allow_html=True)
    st.write("""
    Michka représente bien plus qu'un simple jouet. C'est une avancée technologique qui transforme la manière dont les enfants handicapés interagissent avec le monde qui les entoure. En réduisant la frustration liée aux difficultés de communication, Michka offre une plateforme d'échange et de compréhension, essentielle pour le développement personnel et social des enfants.

    Grâce à ses fonctionnalités innovantes, Michka stimule l'éveil et la curiosité, tout en renforçant les liens entre les enfants, leurs familles, et les professionnels qui les entourent. En facilitant l'apprentissage de la langue des signes, Michka ouvre la voie à une communication plus fluide et inclusive, permettant aux enfants de s'exprimer et de se faire comprendre.
    Moins frustrés, plus confiants, ils peuvent mieux communiquer avec les adultes dès leur jeune âge et éviter les retards d’apprentissage.

    L'impact psychologique de Michka est également significatif. En offrant un espace sécurisé et encourageant, il contribue à renforcer la confiance en soi et l'autonomie des enfants, tout en leur offrant les outils nécessaires pour naviguer dans un monde souvent inadapté à leurs besoins. Michka n'est pas seulement un compagnon de jeu, mais un partenaire dans le développement et l'épanouissement des enfants handicapés, sourds, muets ou autistes.

    Pour les parents, Michka est un allié précieux qui les aide à comprendre et à soutenir leurs enfants dans leur parcours d'apprentissage. Il offre des moyens concrets de participer activement à l'éducation de leurs enfants, renforçant ainsi les liens familiaux.
    Michka aide les parents à soutenir leurs enfants en étant le répétiteur à la patience infinie.

    Les professionnels de l'éducation et de la santé voient en Michka un outil révolutionnaire qui enrichit leurs pratiques pédagogiques et thérapeutiques. Il leur permet d'adopter des approches plus personnalisées et efficaces, contribuant ainsi à l'amélioration des résultats éducatifs et thérapeutiques.

    En investissant dans Michka, nous investissons dans un avenir où chaque enfant, quelles que soient ses capacités, peut participer pleinement à la société et réaliser son potentiel. Michka est une promesse d'inclusion, d'innovation et d'espoir pour un monde où chaque voix compte.
    """)

elif page == 'Evolutions':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Évolutions</h2>", unsafe_allow_html=True)

    st.markdown("""
    - **Fonction "Pose et Lis"**: 
      - Poser un livre entre le module de lecture de "MICHKA". 
      - "MICHKA" lira le livre et tournera les pages automatiquement.
      - Langues des signes Américaine, internationale, et autres.
      - Voiture avec siège et volant, télécommandée pour promener Michka.

    - **Reconnaissance Vocale Avancée**:
      - Compréhension améliorée pour les enfants ayant des difficultés à parler. 

    - **Introduction d'AURORA**:
      - **Interface Multitâche :** AURORA est équipé de trois écrans tactiles, un central et deux de 21 pouces qui se déploient horizontalement, offrant une interface de travail conviviale.
      - **Compagnon Interactif :** AURORA sert à la fois d'ami de jeu et de professeur, facilitant un apprentissage interactif et personnalisé.
      - **Mobilité et Accessibilité :** Monté sur une base à trois roues, AURORA se déplace facilement, permettant une interaction fluide dans divers environnements.
      - **Communication Avancée :** Grâce à ses bras positionnés au niveau des hanches, AURORA facilite une conversation fluide en langue des signes, tout en offrant des contenus éducatifs et interactifs sur ses écrans.

    - **AURORA**:
      - **A**ssistant : Fournit un soutien personnalisé pour les utilisateurs.
      - **U**tile : Offre des fonctionnalités pratiques pour la réhabilitation.
      - **R**éactif : Réagit rapidement aux besoins de l'utilisateur.
      - **O**uvert : Permet une interaction et une communication ouvertes.
      - **R**éhabilitation : Conçu spécifiquement pour aider à la réhabilitation.
      - **A**rtificielle : Utilise l'intelligence artificielle pour enrichir l'expérience utilisateur.
    """)

    # Display the image of AURORA
    st.image(r"C:\Users\MANRESA\Documents\DESC\5_Informatique\Projet Michka\Images\AURORA\Aurora.png", caption="AURORA - Votre Assistant Interactif")

elif page == 'Remerciements':
    st.markdown("<h2 style='text-align: center; color: #1E90FF;'>Remerciements</h2>", unsafe_allow_html=True)

    st.markdown("""
    Nous tenons à exprimer notre profonde gratitude à tous ceux qui ont contribué au succès de ce projet :

    - **Frédéric Griether** : Pour ses nombreux conseils avisés et son soutien indéfectible.
    - **Docteur Pauline Couzy Orthophoniste** : Pour son expérience et notre premier contact professionnel, exerçant en crèche spécialisée.
    - **Docteur Christine MESBAH Orthophoniste** : Professionnel exerçant uniquement en cabinet.
    - **Contributeurs** : À tous les professionnels et bénévoles qui ont apporté leur expertise et leur passion.
    - **Partenaires** : Pour leur collaboration et leur engagement qui ont rendu ce projet possible.
    """)
