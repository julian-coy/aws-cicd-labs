# Lab 1 — CodeCommit + CodeBuild

## ¿Qué hace este lab?
Pipeline básico que toma código Python desde CodeCommit, corre tests unitarios con pytest y genera un reporte XML en CodeBuild.

## Servicios AWS usados
- **CodeCommit** — repositorio Git privado en AWS
- **CodeBuild** — servidor de build administrado
- **IAM** — rol con permisos para CodeBuild
- **CloudWatch Logs** — logs del build

## Estructura
```
lab1-codecommit-codebuild/
├── app/
│   ├── app.py          # Aplicación Python (suma y resta)
│   └── test_app.py     # Tests unitarios con unittest
└── buildspec.yml       # Instrucciones para CodeBuild
```

## Resultado
- 2 tests ejecutados: test_suma, test_resta
- Estado: ✅ PASSED
- Reporte: JUnit XML en CodeBuild Reports
