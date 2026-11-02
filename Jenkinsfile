
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/bobitlmr292124-del/codeshield-sdlc-dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Django System Check') {
            steps {
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" manage.py check'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\Sarah\'s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" manage.py test'
            }
        }

        stage('Deploy to Local Staging') {
            steps {
                bat '''
                powershell -NoProfile -ExecutionPolicy Bypass -Command "$python = 'C:\\Users\\Sarah''s\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'; $pidFile = Join-Path $env:WORKSPACE 'staging-server.pid'; if (Test-Path $pidFile) { $oldPid = [int](Get-Content $pidFile); Stop-Process -Id $oldPid -Force -ErrorAction SilentlyContinue; Remove-Item $pidFile -Force }; & $python manage.py migrate --noinput; if ($LASTEXITCODE -ne 0) { exit 1 }; $out = Join-Path $env:WORKSPACE 'staging-server.log'; $err = Join-Path $env:WORKSPACE 'staging-server-error.log'; $proc = Start-Process -FilePath $python -ArgumentList 'manage.py runserver 127.0.0.1:8001 --noreload' -WorkingDirectory $env:WORKSPACE -PassThru -WindowStyle Hidden -RedirectStandardOutput $out -RedirectStandardError $err; Set-Content -Path $pidFile -Value $proc.Id; $ready = $false; for ($i=0; $i -lt 15; $i++) { Start-Sleep -Seconds 2; try { $r = Invoke-WebRequest -Uri 'http://127.0.0.1:8001/' -UseBasicParsing -TimeoutSec 3; if ($r.StatusCode -eq 200) { $ready = $true; break } } catch {} }; if (-not $ready) { if (Test-Path $err) { Get-Content $err }; exit 1 }; Write-Host 'Staging deployment successful: http://127.0.0.1:8001/'"
                '''
            }
        }
    }
}
