<?php
$path = "1.png";
$python = `python hello.py`;
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