# Objetivos

* Estudar os fundamentos do framework react
* Criar um protótipo para salvar arquivos CSV em uma object store e disponibilizar uma rota para download. Assim, o Power BI poderia acessar os arquivos diretamente na web, sem precisar de uma gateway local para acessar arquivos localmente.

## Rodar projeto localmente com docker compose

```bash
docker-compose up -d --build --force-recreate
```

## Rodar o frontend localmente

```bash
npm install
npm run dev
```

## Para formatar o backend

```bash
black backend --exclude "__init__.py"; isort backend
```
