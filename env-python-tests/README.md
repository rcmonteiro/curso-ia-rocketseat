# Repo para estudos com Python

## Trabalhando com o `pyenv`

```bash
# Install
brew update
brew install pyenv

alias brew="env PATH=(string replace (pyenv root)/shims '' \"\$PATH\") brew"

pyenv install $version
pyenv versions
pyenv global $version
pyenv local $version

```

## Trabalhando com o `pipenv`

```bash
# install local, using the current python local version
pipenv install $package
pipenv install $package==$version --python $python_version

pipenv shell

```