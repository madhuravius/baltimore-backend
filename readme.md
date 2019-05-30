## Backend Repo for Code for Baltimore Data Projects

### Build Status

**Dev** [![Build Status](https://travis-ci.com/madhuravius/baltimore-backend.svg?token=Xzeq5RcN4dD2hqVzgcPz&branch=dev)](https://travis-ci.com/madhuravius/baltimore-backend)

**Master** [![Build Status](https://travis-ci.com/madhuravius/baltimore-backend.svg?token=Xzeq5RcN4dD2hqVzgcPz&branch=master)](https://travis-ci.com/madhuravius/baltimore-backend)

### Required dependencies

#### Instructions on Mac

```sh
brew install postgresql
brew install postgis
brew install gdal
brew install libgeoip
```


### Setup instructions

```
pip3 install virtualenv -p python3
source env/bin/activate
pip3 install -r requirements.txt
```

Ensure there is a `.env` file created (you can use the `.env-sample` as guidance):

```
python3 manage.py migrate
python3 manage.py runserver

# alternatively, to run the notebook:
python3 manage.py shell_plus --notebook
```

Assuming everything is set up correctly, you will want to download everything:

```
python3 cli.py shapefiles
python3 cli.py download

# be warned: this last step will take many hours (5+ hours for full import)
python3 cli.py database
```