# Horizon Login

Application pour assurer la connexion des utilisateurs sur les
 applications Horizon.
 
## Utilisation locale

### L'IDE
Pour le développement, il est recommandé d'utiliser PyCharm 
Professional ([Télécharger](https://www.jetbrains.com/pycharm/download/#section=linux)|
[License](https://www.jetbrains.com/student/)).

### Python

#### L'ancienne methode

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

#### PyEnv

PyEnv est une alternative plus pratique pour la gestion des versions de Python sur votre système et je vous le
recommende très fortement.

Pour l'installation de PyEnv sur Ubuntu avec Bash:

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev;
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash;
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv;
cat <<EOT >> ~/.bashrc

# PyEnv
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOT
```

A voir pour les autres OS:
- https://github.com/pyenv/pyenv-installer
- https://github.com/pyenv/pyenv-virtualenv
- https://github.com/pyenv/pyenv

### La Base de données

Installez Docker: https://docs.docker.com/engine/installation/

Lancez: `docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres --name postgres -d postgres`

## Licence

Ce projet est sous licence GNU GPL V3
