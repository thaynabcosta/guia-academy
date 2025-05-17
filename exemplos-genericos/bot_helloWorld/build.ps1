$exclude = @("venv", "bot_helloWorld.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_helloWorld.zip" -Force