# Lab 2 — CodeDeploy en EC2

## ¿Qué hace este lab?
Despliega una aplicación web estática en EC2 usando AWS CodeDeploy con estrategia In-Place y validación automática del servicio.

## Servicios AWS usados
- **CodeDeploy** — orquestador del deployment
- **EC2** — servidor donde se despliega la app (t2.micro Free Tier)
- **S3** — almacena el paquete zip con el código
- **IAM** — roles para EC2 y CodeDeploy

## Estructura
```
lab2-codedeploy/
├── appspec.yml                      # Instrucciones para CodeDeploy
├── index.html                       # Aplicación web
└── scripts/
    ├── install_dependencies.sh      # Instala Apache
    ├── start_server.sh              # Inicia Apache
    └── validate_service.sh          # Valida que Apache responde
```

## Hooks ejecutados
1. **BeforeInstall** → instala Apache (httpd)
2. **ApplicationStart** → inicia Apache y lo habilita al arranque
3. **ValidateService** → curl a localhost verifica que la app responde

## Resultado
- ✅ Deployment exitoso
- ✅ App accesible via HTTP en EC2
- ✅ Validación automática con curl
