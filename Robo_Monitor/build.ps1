$exclude = @("venv", "Robo_Monitor.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Robo_Monitor.zip" -Force