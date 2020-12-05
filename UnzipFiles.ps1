<#
    .SYNOPSIS
        Function for extracting zip files.

    .DESCRIPTION
        This function is for extracting zip files in a folder or for extracting a single zip file.

    .PARAMETER Path
        Path to file or folder to extract.
        Note :
        If Path points to a folder, this function extracts all zip files in that folder.
        If Path points to a file, it extracts only that file. 

    .PARAMETER DestinationPath
        (optional) Folder to extract zip file or files to, if not provided it use the Path as the Destination Path. 
        
    .EXAMPLE
        .\UnzipFiles.ps1 -Path "C:\Data"
        This extracts all the zip files in "C:\Data" to "C:\Data"

        .\UnzipFiles.ps1 -Path "C:\Data" -DestinationPath "D:\ExtractedData"
        This extracts all the zip files in "C:\Data" to "D:\ExtractedData"
#>
[CmdletBinding()]
param (
    [ValidateNotNullOrEmpty()][string]$Path,
    [string]$DestinationPath
)

# Verify path
if (Test-Path -Path $Path -PathType Leaf) {
    $DestinationPath = if (![string]::IsNullOrEmpty($DestinationPath)) { $DestinationPath } else { Split-Path -Path $Path }
    Expand-Archive -Path $Path -DestinationPath $DestinationPath
}
elseif (Test-Path -Path $Path -PathType Container) {
    $DestinationPath = if (![string]::IsNullOrEmpty($DestinationPath)) { $DestinationPath } else { $Path }
    Get-ChildItem $Path -Filter "*.zip" | Expand-Archive -DestinationPath $DestinationPath -Force
}
else {
    throw "'$Path' not a valid path"
}


