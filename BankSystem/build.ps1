$exclude = @("venv", "BankSystem.zip", "*.xaml", "*.jproj")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BankSystem.zip" -Force