<?php

##PHP find public IP 
if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
    $ip = $_SERVER['HTTP_CLIENT_IP'];
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
    $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
} else {
    $ip = $_SERVER['REMOTE_ADDR'];
}
$path = "1.png";
$python = `python hello.py .$ip.`;
echo $python;
    // if(file_exists($path))
    // { 
    //     header('Content-Length: '.filesize($path));
    //     header('Content-Type: image/jpg');
    //     header('Content-Disposition: inline; filename="'.$path.'";');
    //     echo file_get_contents($path);
    //     exit;
    // }
?>
