# projet_mode

Priere d'utiliser le fichier requirements.txt pour installer, dans un
environnement virtuel python toutes les librairies requises.

creer le venv: `python -m venv venv_groupeA12`

puis l'activer: `source .venv_groupeA12/bin/activate` sur linux/macos
ou `venv_groupeA12\Scripts\activate` sur windows

Une fois l'environnement active, il faut installer les librairies avec la commande
`pip install -r requirements.txt`

La majorite des fichiers presentent une fonction main qui ne s'execute
que si le fichier est execute (et non importe).

Le fichier problem.py definit les constantes du probleme:
- a, b, c, d
- f ainsi que ses composantes pour permettre une utilisation plus
simple dans le fichier equilibrium_viz

Le fichier polynomial_roots.py utilise la classe Polynomial
de Numpy afin de determiner les racines de polynome P defini dans 
le rapport. Ces racines sont importees dans d'autres fichiers comme
stability.py pour l'etude de stabilite. En executant ce fichier 
directement, on peut voir les racines calculees numeriquement ainsi
que les valeurs de P prises en ses racines, une sorte de validation
visuelle des resultats.

Le fichier stability.py calcule les points d'equilibre d'interet
a l'aide des polynomes Rx et Ry puis les stocke dans une variable.
Cette variable est importee dans le fichier equilibrium_viz.py.
Ce module etablit alors les matrices d'evolutions des systemes linearises
aux 4 points d'equilibres respectifs.
En executant directement ce module, une verification basique de stabilite
est effectue en s'assurant que chaque matrice d'evolution a au moins
une valeur propre de partie reelle > epsilon pour epsilon petit positif.

Le fichier equilibrium_viz.py presente deux types de diagrammes autour des 4
points d'equilibre:
- des diagrammes de phase restreints et interactifs en 3d.
- des diagrammes de phase 2d qui sont des coupes obtenues en fixant
un des trois parametres.

Priere de se diriger directement vers la fonction main, en effet les
fonctions sont longues et peu factorisees actuellement. il y'a des lignes
a decommenter afin de voir les differents diagrammes, des indications se trouve
dans le main.

Le fichier article_implementation.py est une ebauche. On n'a 
malheureusement pas reussi a lever les ambiguites de l'article
quant aux matrices J d'integration et au produit des representations
spectrales.


Not yet done:
- solver.py

Done files:
- polynomial_roots.py
- stability.py
- equilibrium_viz.py
- article_implementation.py
- problem.py
