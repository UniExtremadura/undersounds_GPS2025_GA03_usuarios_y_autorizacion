## Overview

Backend API for the "Usuarios y Autorización" service. It is built with [Connexion](https://github.com/zalando/connexion) on top of Flask and provides registration, login, refresh token and profile (`/me`) endpoints with JWT authentication and SQLite persistence.

## Requirements

* Python 3.10+

Install dependencies with `pip install -r requirements.txt`. A sample `.env.example` file is provided with sensible defaults:

```
DB_URL=sqlite:///./undersounds.db
JWT_SECRET=change-me
ACCESS_TTL=900
REFRESH_TTL=2592000
```

Copy it to `.env` and adjust the values for your environment if required.

## Running the server

The recommended developer workflow uses the provided `Makefile`:

```bash
make dev
```

This installs the dependencies and starts the API on `http://localhost:8080`. Swagger UI remains available at `/ui`.

Alternatively you can run the server manually:

```bash
pip install -r requirements.txt
python -m swagger_server
```

## Tests

Run the pytest suite with:

```bash
make test
```

## Useful requests

Register a user (201 Created):

```bash
curl -sX POST http://localhost:8080/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana","email":"ana@demo.com","password":"Passw0rd!","role":"artista"}'
```

Login (200 OK):

```bash
curl -sX POST http://localhost:8080/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"ana@demo.com","password":"Passw0rd!"}'
```

Refresh tokens (200 OK):

```bash
curl -sX POST http://localhost:8080/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh":"<refresh_token>"}'
```

Fetch the authenticated profile (200 OK):

```bash
ACCESS="<access_token>"
curl -s http://localhost:8080/me -H "Authorization: Bearer $ACCESS"
```

All endpoints accept CORS requests from `http://localhost:4200` and `http://localhost:5173` for integration with the Angular frontend.
