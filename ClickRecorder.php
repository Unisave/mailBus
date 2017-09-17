<?php


//ACTUAL DATA GATHERER=========================================
$t=time();

$tracker = $_GET['tracker'];

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
//====FALSE tracker======
// $tracker = "asdasda";
// $currTime = "5:60";
// $ip = "5.5.5.5"; 
//====================
//====FALSE IP========
// $tracker = "asdas";
// $currTime = "5:60";
// $ip = "hfd"; 
//====================
//====FALSE TIME======
// $tracker = "asdas";
// $currTime = "bleh";
// $ip = "5.5.5.5"; 
//====================


echo "<html><head><title>Updated profile</title></head></html>";
if(1 === preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/', $ip))
{
    if(1 === preg_match('/[^\d\:\-]/', $currTime))
    {
        $locked = $ip." ".$currTime;
        $pythonX1 = `python BackEnds/entryFilters/suspiciousClick.py $locked`;
        // echo $pythonX1;
    } else
    {
        if(1 === preg_match('/^[^\W]+$/', $tracker)){
            $header = $ip." ".$tracker." ".$currTime;
            $python = `python BackEnds/entryFilters/recieverClick.py $header`;
            // echo $python;
        } else
        {
            $locked = $ip." ".$currTime;
            $pythonX2 = `python BackEnds/entryFilters/suspiciousClick.py $locked`;
            // echo $pythonX2;
        };
    };
} else
{
    $locked = $ip." ".$currTime;
    $pythonX3 = `python BackEnds/entryFilters/suspiciousClick.py $locked`;
    // echo $pythonX3;
};
// echo "<script>window.close();</script>";
?>
