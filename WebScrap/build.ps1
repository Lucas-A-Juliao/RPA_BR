$exclude = @("venv", "WebScrap.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "WebScrap.zip" -Force