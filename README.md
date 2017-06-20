# Horizon Login

Application pour assurer la connexion des utilisateurs sur les
 applications Horizon.
 
## Utilisation locale

### L'IDE
Pour le développement, il est recommandé d'utiliser PyCharm 
Professional ([Télécharger](https://www.jetbrains.com/pycharm/download/#section=linux)|
[License](https://www.jetbrains.com/student/)).

### Python

Vous devez avoir installé Python3 sur votre machine:

* Windows (pas recommandé, mais bon): 
    * Python: https://www.python.org/downloads/release
    * PIP: https://pip.pypa.io/en/stable/installing/
* Mac OS X:
    * Installer le gestionnaire de paquets brew : `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
    * Python : `brew install python3`
    * PIP : `brew install pip`
* Ubuntu:
    * `sudo apt-get install python3 python3-pip python3-virtualenv`

Ensuite importez le projet dans PyCharm depuis le VCS GitHub.

### La Base de données

Installez Docker: https://docs.docker.com/engine/installation/

Lancez: `docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres --name postgres -d postgres`

## Licence

Ce projet est sous licence GNU GPL V3
