# Comandos
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