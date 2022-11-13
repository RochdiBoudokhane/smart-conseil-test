# smart-conseil-test

Dans la fichier ELK on a utilisé docker-compose pour l'installation de ELK et on a ajouter l'authentification de connexion(username: elastic, password: smart-conseil)
pour exécuter le projet il suffit de tapper 
# docker-compose up -d --build
Ensuite on a fait quelque capture d'écran sur ELK 
Pour la partie collecte de données on a utilisé la bibliothèque facebook-scraper pour exécuter le projet
il suffit de changer le nom de sujet puis tapper dans cmd 
# python main.py
Enfin les données collectées seront stockées dans mongodb. 
