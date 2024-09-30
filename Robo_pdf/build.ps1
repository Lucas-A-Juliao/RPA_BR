$exclude = @("venv", "Robo_pdf.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Robo_pdf.zip" -Force