# Java-RestAPI

Lista de testes de API com data de entrega para 26/11/2024

### Tools/packages used
- Postman;
- NPM;
- Newman;
- newman-reporter-htmlextra;

## Requirements

In order to run this project you have to install:

- [Postman (optional)](https://www.postman.com/downloads/);
- [NPM (in order to get newman)](https://www.npmjs.com/package/download);

## How to run

Clone the repository

```bash
git clone https://github.com/AlexandrePossari/CollegeExercises.git
```

Open a command line tool in the following relative path: "CollegeExercises/S206-LAB/Lista API". Then:

```bash
npm install newman
npm install newman-reporter-htmlextra
```

Now, to generate the report:
```bash
newman run 'Lista API.postman_collection.json' -e 'Lista API.postman_environment.json' -r htmlextra
```

Besides that you can simply import the "Lista API.postman_collection" into your postman and run.
