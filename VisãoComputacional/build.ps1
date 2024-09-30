$exclude = @("venv", "VisãoComputacional.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "VisãoComputacional.zip" -Force