\# CI/CD Pipeline Using Jenkins



\## 1. Introduction



CodeShield uses Jenkins to demonstrate Continuous Integration and Continuous Delivery (CI/CD) within the Software Development Life Cycle. Jenkins automates the retrieval of the project source code, installation of dependencies, Django system checks, automated unit testing and preparation of a local staging environment.



The pipeline is defined in the root directory of the project in a file named `Jenkinsfile`. It retrieves the source code from the CodeShield GitHub repository, using the `main` branch.



\## 2. Pipeline Architecture and Stages



The Jenkins pipeline consists of the following stages:



\*\*Checkout:\*\* Jenkins retrieves the latest available source code from the project's GitHub repository. This ensures that the build uses the selected version of the project.



\*\*Install Dependencies:\*\* Jenkins installs the Python packages listed in `requirements.txt` using the configured Python 3.14 installation. This prepares the environment required to run the Django application.



\*\*Django System Check:\*\* Jenkins executes `python manage.py check` to identify Django configuration and system problems before proceeding.



\*\*Run Unit Tests:\*\* Jenkins executes `python manage.py test` to run the automated tests included in the project. This helps verify that the tested application components behave as expected.



\*\*Deploy to Local Staging:\*\* Jenkins applies database migrations using `python manage.py migrate --noinput`, then starts the Django development server at `http://127.0.0.1:8001/`. The pipeline checks whether the staging application responds successfully before continuing.



\*\*Manual Approval:\*\* Jenkins pauses and requests manual approval. The user opens the staging application, verifies that the dashboard is accessible and selects Proceed in Jenkins to complete the deployment demonstration.



\## 3. Build and Testing Results



Jenkins Build #4 completed successfully on 2 November 2026. The build retrieved the project from GitHub and completed the dependency installation, Django system check, automated testing and local staging deployment stages.



The Django system check reported no issues. The automated test stage executed two tests, both of which passed. Database migrations completed without pending migrations. The staging server started successfully and responded to the pipeline's HTTP availability check.



Manual verification was also performed by opening the staging dashboard in a web browser and confirming that it loaded successfully. The manual approval step was then completed in Jenkins.



\## 4. Deployment and Limitations



The pipeline demonstrates automated checks and deployment to a local staging environment. It does not represent deployment to a public production server.



The staging server is started during the Jenkins build and stopped by the pipeline's post-build cleanup action. Therefore, the staging address is available during the deployment demonstration but is not intended to remain permanently accessible after the build finishes.



The current pipeline uses a Python installation path specific to the development computer, which limits portability to other environments. The Jenkinsfile also does not define an automatic GitHub webhook or polling trigger. Automatic build triggering and deployment to a production environment are possible future improvements.



The pipeline does not perform automated vulnerability scanning or integrate external security tools across all five SDLC security pillars.



\## 5. Conclusion



The Jenkins pipeline demonstrates how CI/CD practices can improve the consistency of software verification and staging preparation in the CodeShield project. By automating source-code retrieval, dependency installation, Django system checks, unit tests and local staging deployment, the pipeline provides a repeatable process for verifying the application before approval. The successful Jenkins Build #4 provides evidence that the configured pipeline operated as intended.



\## 6. Evidence



The following genuine screenshots document the pipeline and application verification:



\- `01-Jenkins-Build-4-Success.png` – successful Jenkins Build #4.

\- `02-Jenkins-Pipeline-Stages.png` – completed Jenkins pipeline stages.

\- `03-CodeShield-Dashboard.png` – dashboard running in the local staging environment.

