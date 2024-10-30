$exclude = @("venv", "Bot_Portal_SEFAZ_MA.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Bot_Portal_SEFAZ_MA.zip" -Force