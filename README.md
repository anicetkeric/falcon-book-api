
# falcon-book-api

Building REST API with Python, Falcon, and MongoDB


## Tech Stack

**Python**, **Docker**, **docker-compose**, **MongoDb** 



## Run Locally

Clone the project

```bash
  git clone https://github.com/anicetkeric/falcon-book-api.git
```

Go to the project directory

```bash
  cd falcon-book-api
```

Install packages

```bash
  pip install -r requirements.txt 
```

Start the server

```bash
  gunicorn --reload src.app:app
```


## Deployment

To deploy this project run

```bash
  cd deployment
```
Execute docker compose 

```bash
  docker-compose up -d
```

Swagger page: ip:3000/swagger


## Documentation

[Original Version](https://dzone.com/articles/python-falcon-microservice-with-mongodb-and-docker)

[Improved version](https://boottechnologies-ci.medium.com/python-falcon-microservice-with-mongodb-and-docker-dzone-485188ec4fa1)

## Authors

👤 **anicetkeric**

* Website: https://medium.com/@boottechnologies-ci
* Twitter: [@AnicetKEric](https://twitter.com/AnicetKEric)
* Github: [@anicetkeric](https://github.com/anicetkeric)
* LinkedIn: [@eric-anicet-kouame](https://linkedin.com/in/eric-anicet-kouame-49029577)

## Support
<a href="https://www.buymeacoffee.com/boottechnou" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

