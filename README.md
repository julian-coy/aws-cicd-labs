# aws-cicd-labs

CI/CD pipeline labs for the AWS DevOps Engineer Professional (DOP-C02) certification.

Built hands-on using AWS CLI, CloudFormation, and the AWS Console on a real AWS account (Free Tier).

---

## Labs Overview

| Lab | Services | Status |
|-----|----------|--------|
| Lab 1 | CodeCommit + CodeBuild | ✅ Complete |
| Lab 2 | CodeDeploy on EC2 | ✅ Complete |
| Lab 3 | CodePipeline (full CI/CD) | ✅ Complete |

---

## Lab 1 — CodeCommit + CodeBuild

**Goal:** Set up a source repository and automated build with test reporting.

**What was built:**
- CodeCommit repository as source control
- CodeBuild project running `pytest` unit tests
- JUnit XML test report published to CodeBuild Reports
- `buildspec.yml` defining install, pre-build, build, and post-build phases

**Key concepts practiced:**
- buildspec.yml structure and phases
- Test reporting with JUnit format
- IAM roles for CodeBuild (`CodeBuildRole`)
- CloudWatch Logs for build output

---

## Lab 2 — CodeDeploy on EC2

**Goal:** Deploy an application to EC2 using lifecycle hooks.

**What was built:**
- CodeDeploy application and deployment group targeting EC2
- `appspec.yml` with full lifecycle hook configuration
- Hook scripts: `before_install.sh`, `after_install.sh`, `validate_service.sh`
- EC2 instance with CodeDeploy agent installed via User Data

**Key concepts practiced:**
- CodeDeploy lifecycle events (BeforeInstall, AfterInstall, ValidateService)
- In-place vs blue/green deployment strategies
- EC2 instance tags for deployment group targeting
- CodeDeploy agent installation and configuration

---

## Lab 3 — CodePipeline (Full CI/CD)

**Goal:** Orchestrate a complete Source → Build → Deploy pipeline with automatic triggers.

**What was built:**
- End-to-end CodePipeline with 3 stages: Source, Build, Deploy
- Automatic pipeline trigger via Amazon EventBridge on every push to `main`
- S3 bucket for inter-stage artifact passing
- 4 IAM roles: `CodePipelineRole`, `CodeBuildRole`, `CodeDeployRole`, `EC2CodeDeployRole`
- New EC2 instance with CodeDeploy agent provisioned via User Data

**Architecture:**

```
CodeCommit (push to main)
    │
    ▼ EventBridge trigger
CodePipeline
    ├── Stage 1: Source  → pulls code from CodeCommit
    ├── Stage 2: Build   → runs pytest, packages artifact (CodeBuild)
    └── Stage 3: Deploy  → deploys to EC2 via appspec.yml (CodeDeploy)
```

**Key concepts practiced:**
- CodePipeline V2 and execution modes
- EventBridge vs polling for pipeline triggers
- Artifact store configuration in S3
- IAM permissions troubleshooting across pipeline stages
- Cross-service IAM role chaining (Pipeline → Build → Deploy → EC2)

---

## Repository Structure

```
aws-cicd-labs/
├── lab1-codecommit-codebuild/
│   ├── app/
│   │   ├── app.py
│   │   └── test_app.py
│   └── buildspec.yml
├── lab2-codedeploy/
│   ├── app/
│   ├── appspec.yml
│   └── scripts/
│       ├── before_install.sh
│       ├── after_install.sh
│       └── validate_service.sh
└── lab3-codepipeline/
    ├── app/
    │   ├── app.py
    │   └── test_app.py
    ├── buildspec.yml
    ├── appspec.yml
    ├── index.html
    └── scripts/
        ├── before_install.sh
        ├── after_install.sh
        └── validate_service.sh
```

---

## Setup

**Prerequisites:**
- AWS CLI configured with IAM user
- Git with CodeCommit HTTPS credentials
- Python 3.x for local test execution

**Region:** `us-east-1`

---

## Certification Path

These labs cover **Domain 1: SDLC Automation** of the AWS DevOps Engineer Professional exam (DOP-C02).

Exam date: March 31, 2026
