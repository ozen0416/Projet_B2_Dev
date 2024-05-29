# API PHP


## Description

Cette API a été écrite dans le cadre du module PHP lors de ma deuxième année de Bachelor à Ynov Aix-en-Provence.
L'API vient interfacer le DAL (Data Access Layer) d'une base de donnée MySQL

Cette API a été codé avec du **PHP 5.6**

## Sommaire

1. [Description](#Description)
1. [Commencer](#Commencer)
	1. [Installation](#Installation)
	1. [Utilisation](#Utilisation)
	1. [Endpoint](#Endpoint)
	1. [Gestion d'erreur](#Gestion%20d'erreur)
	1. [Authentification](#Authentification)
	1. [Limite de requêtes](#Limite%20de%20requ%C3%AAtes)
	1. [Pistes d'amélioration futur](#Pistes%20d'am%C3%A9lioration%20futur)
	1. [Auteur](#Auteur)

## Commencer

### Installation

Extraire le dossier `.zip` dans le dossier `www` de votre server Apache.
L'arborescence devrait ressembler à ça:
```
root
|
└──credentials
|	└── db.json
└──	www
	│
	└── API
	    ├── dossier1
	    ├── fichier1
	    └── ...
```

Pour le bon fonctionnement du DAL il faut aussi un dossier `credentials` au même niveau que le dossier `www`. Dans ce dossier `credentials` il faudra y mettre un fichier JSON avec les identifiants à la base de données.
Voici le format: 
```
{
    "dbName": "your_db_name",
    "login": "your_db_user",
    "password": "y0ur_us€r_Pa$$w0rd"
}
```

Le DAL lit par défaut le fichier `db.json` mais il est possible de lire un autre fichier. Il faudra simplement préciser le nom du fichier dans le constructeur de la classe `Database` en donnant un paramètre à la méthode `Connect`.
À cette ligne:
```
$this->dbh = Connection::Connect("your_db_file");
```

### Utilisation

Les requêtes à l'API se font toutes avec la méthode HTTP POST. Il faudra donc un logiciel (comme Postman) ou du code pour faire les requêtes et passer les arguments dans le body de la requête.
La syntax pour les requêtes sera:
```
{serverIP}/API/{endpoint}/
```

### Endpoint

L'API a 5 endpoints, **Create**, **Read**, **Update**, **Delete** et **TestDB**. Ces endpoints permettent d'interagir avec la base de données. L'endpoint TestDB est un endpoint de test qui pour l'instant ne sert qu'à tester la méthode `read`.

#### Paramètres
Chaque endpoint a ses paramètres à prendre en compte, certains ont les mêmes paramètres mais d'autre non, voici un tableau avec les paramètres pour chaque endpoint:

| CRUD/Args | table       | params      | columns     | filter      |
| --------- | ----------- | ----------- | ----------- | ----------- |
| Create    | OBLIGATOIRE | OBLIGATOIRE | X           | X           |
| Read      | OBLIGATOIRE | X           | OBLIGATOIRE | OPTIONEL    |
| Update    | OBLIGATOIRE | OBLIGATOIRE | X           | OBLIGATOIRE |
| Delete    | OBLIGATOIRE | X           | X           | OBLIGATOIRE |

- **table**: Le nom de la table
- **params**: Ensemble clé-valeur avec les colonnes de la table en clé
- **columns**: Tableau de colonnes de la table (peut aussi valoir `"*"`)
- **filter**: Ensemble d'object JSON, dont la clé est le nom de la colonne et la valeur est un autre ensemble clé-valeur, avec pour clé `"operateur"` et `"value"` (voir exemple [ci-dessous](#Update))

#### Create

Ce endpoint permet d'écrire des entrées dans une table de la base de données.
Ici `params` sont les valeurs à attribuer.

Voici un exemple de requête et d'arguments à passer:

**En bash:**
```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "table": "your_table",
    "params": {
      "col1": "value1",
      "col2": "value2"
    }
  }' \
  http://localhost/CreateDB/
```

**En python:**
```python
import requests

url = "http://localhost/CreateDB/"
data = {
    "table": "your_table",
    "params": {
        "col1": "value1",
        "col2": "value2"
    }
}

response = requests.post(url, json=data)

print(response.json())  # If the response contains JSON data

```

#### Read

Ce endpoint permet de lire des entrées dans une table de la base de données.
Ici `columns` sont les colonnes à lire dans la table.
Il est aussi possible de lire toutes les colonnes d'une table en écrivant `"columns": "*"`

Possibilité de rajouter `filter` à la requête (voir exemple [ci-dessous](#Update))

Voici un exemple de requête et d'arguments à passer:

**En bash:**
```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "table": "your_table",
    "columns": [
      "col1",
      "col2"
    ]
  }' \
  http://localhost/ReadDB/
```

**En python:**
```python
import requests

url = "http://localhost/ReadDB/"
data = {
    "table": "your_table",
    "columns": [
        "col1",
        "col2"
    ]
}

response = requests.post(url, json=data)

print(response.json())  # If the response contains JSON data

```

#### Update

Ce endpoint permet de modifier des entrées dans une table de la base de données.
Ici `params` sont les nouvelles valeurs et les object JSON dans `filter` permettent de créer la clause `WHERE` de la requête SQL. 

Voici un exemple de requête et d'arguments à passer:

**En bash:**
```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "table": "your_table",
    "params": {
        "prenom": "Paul"
    },
    "filter": {
        "age": {
            "operator": ">",
            "value": "23"
        }
    }
  }' \
  http://localhost/UpdateDB/
```

**En python:**
```python
import requests

url = "http://localhost/UpdateDB/"
data = {
    "table": "your_table",
    "params": {
        "prenom": "Paul"
    },
    "filter": {
        "prenom": {
            "operator": "=",
            "value": "Pierre"
        }
    }
}

response = requests.post(url, json=data)

print(response.json())  # If the response contains JSON data

```

#### Delete

Ce endpoint permet de supprimer des entrées dans une table de la base de données.
Ici `filter` permet de sélectionner les bonnes valeurs à supprimer

Voici un exemple de requête et d'arguments à passer:

**En bash:**
```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{
    "table": "your_table",
    "filter": {
      "age": {
        "operator": ">",
        "value": "23"
      }
    }
  }' \
  http://localhost/DeleteDB/
```

**En python:**
```python
import requests

url = "http://localhost/DeleteDB/"
data = {
    "table": "your_table",
    "filter": {
        "prenom": {
            "operator": "=",
            "value": "Pierre"
        }
    }
}

response = requests.post(url, json=data)

print(response.json())  # If the response contains JSON data
```

### Gestion d'erreur

En cas d'erreur l'API renverra du JSON avec le format:
```json
{
	"Error": "Error message"
}
```

### Authentification

L'API ne possède pas de système d'authentification.

### Limite de requêtes

L'API ne possède pas de limite de requêtes.

### Pistes d'améliorations futurs

- Il faudrait que les valeurs de `ALLOWED_ARGS` et `NEEDED_ARGS` ne soient pas en brut dans le code, peut-être en les ayant dans un autre fichier que le DAL viendrait juste lire
- Avoir une classe Credentials
- Pouvoir Insert plusieurs lignes à la fois
- Avoir un autoloader

### Auteur

- Théo COLLIOT-MARTINEZ