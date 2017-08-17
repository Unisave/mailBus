<?php

##PHP find public IP 
$externalContent = file_get_contents('http://checkip.dyndns.com/');
preg_match('/Current IP Address: \[?([:.0-9a-fA-F]+)\]?/', $externalContent, $m);
$ip = $m[1];
$path = "1.png";
$python = `python hello.py .$ip.`;
echo $python;
    if(file_exists($path))
    { 
        header('Content-Length: '.filesize($path));
        header('Content-Type: image/jpg');
        header('Content-Disposition: inline; filename="'.$path.'";');
        echo file_get_contents($path);
        exit;
    }
?>
