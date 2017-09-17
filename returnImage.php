<?php


//ACTUAL DATA GATHERER=========================================
$path = "staticAssets/images/logo.png";
$t=time();

$token = $_GET['id'];

$currTime = date("Y-m-d::H:i:s",$t);

function currIP() {
    if (!empty($_SERVER['HTTP_CLIENT_IP'])) { 
     $ip = $_SERVER['HTTP_CLIENT_IP']; 
    } elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) { 
     $ip = $_SERVER['HTTP_X_FORWARDED_FOR']; 
    } else { 
     $ip = $_SERVER['REMOTE_ADDR']; 
    }
    return $ip;
}
$ip = currIP(); 
//=============================================================

//MOCK SIMULATOR
//====FALSE TOKEN======
// $token = "asdasda";
// $currTime = "5:60";
// $ip = "5.5.5.5"; 
//====================
//====FALSE IP========
// $token = "asdas";
// $currTime = "5:60";
// $ip = "hfd"; 
//====================
//====FALSE TIME======
// $token = "asdas";
// $currTime = "bleh";
// $ip = "5.5.5.5"; 
//====================



if(1 === preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $ip))
{
    if(1 === preg_match('/[^\d\:\-]/', $currTime))
    {
        $locked = $ip." ".$currTime;
        $pythonX1 = `python BackEnds/entryFilters/suspiciousEntry.py $locked`;
    } else
    {
        if(1 === preg_match('/^[^\W]+$/', $token)){
            $header = $ip." ".$token." ".$currTime;
            $python = `python BackEnds/entryFilters/recieverEntry.py $header`;
        } else
        {
            $locked = $ip." ".$currTime;
            $pythonX2 = `python BackEnds/entryFilters/suspiciousEntry.py $locked`;
        };
    };
} else
{
    $locked = $ip." ".$currTime;
    $pythonX3 = `python BackEnds/entryFilters/suspiciousEntry.py $locked`;
};

    if(file_exists($path))
    { 
        header('Content-Length: '.filesize($path));
        header('Content-Type: image/jpg');
        header('Content-Disposition: inline; filename="'.$path.'";');
        echo file_get_contents($path);
        exit;
    }


?>
