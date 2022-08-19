<#
NAME
D:\QS\kemampuan-dasar-1\latihan\powershellscripts\Get-LastBootTime.ps1
.SYNOPSIS
Shows when last your PC started up.
.SYNTAX
D:\QS\kemampuan-dasar-1\latihan\powershellscripts\Get-LastBootTime.ps1 [-ComputerName] <String> [<CommonParameters>]
.DESCRIPTION
This is a WMI wrapper function to get the time that your PC last started up.
.PARAMETER ComputerName
The name of the Computer you want to run the command against.
.EXAMPLE
Get-LastBootTime -ComputerName localhost
.LINK
www.howtogeek.com
#>
param(
    [Parameter(Mandatory=$true)][string]$ComputerName
)

Get-WmiObject -Class Win32_OperatingSystem -ComputerName $ComputerName |
Select-Object -Property CSName,@{n="Last Booted";
e={[Management.ManagementDateTimeConverter]::ToDateTime($_.LastBootUpTime)}}