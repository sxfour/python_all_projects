function sambaWorker {
    $rport = Read-Host "Введите порт на котором проверить соединение"
    $timeout = 10
    $i = 0

    foreach ($rhost in $rhosts){
        try {
            $t = new-Object system.Net.Sockets.TcpClient
            $c = $t.BeginConnect($rhost, $rport, $null, $null)
            $w = $c.AsyncWaitHandle.WaitOne($timeout, $false)

            if (!$w) {
                $t.Close()
            } else {
                    $null = $t.EndConnect($c)
                    $all_hosts[$rhost] += "$rport, $w"     
                    $t.Close()
                    $i++
                    Write-Progress -Activity "Сканирование хостов..." -Status "Хостов найдено: $i" -PercentComplete $i
            }
        } catch {
            return $null
        }
    }
}

$from = "192.168.0.1"
$to = "192.168.0.255"
$all_hosts = @{}

$ipAdressIn = $from -split "\."
$ipAdressOut = $to -split "\."

$rhosts = New-Object System.Collections.ArrayList

[array]::Reverse($ipAdressIn)
[array]::Reverse($ipAdressOut)

$start=[bitconverter]::ToUInt32([byte[]]$ipAdressIn,0)
$end=[bitconverter]::ToUInt32([byte[]]$ipAdressOut,0)

for ($ip = $start; $ip -lt $end; $ip++)
{ 
    $get_ip=[bitconverter]::getbytes($ip)

    [array]::Reverse($get_ip)

    $rhosts.Add($get_ip -join "." -split "`n") | Out-Null
}



sambaWorker $rhosts

Write-Host $all_hosts.Keys

$rhosts.Clear()