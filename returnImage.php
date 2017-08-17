<?php
$path = "1.png";
$token = $_GET['id'];
function curPageURL() {
 $pageURL = 'http';
 if ($_SERVER["HTTPS"] == "on") {$pageURL .= "s";}
 $pageURL .= "://";
 if ($_SERVER["SERVER_PORT"] != "80") {
  $pageURL .= $_SERVER["SERVER_NAME"].":".$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"];
 } else {
  $pageURL .= $_SERVER["SERVER_NAME"].$_SERVER["REQUEST_URI"];
 }
 return $pageURL;
}


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



$arr = (parse_url(curPageURL()));
// $output = array_slice($arr,1); #NOT NEEDED
// $url =  implode("",$output); #NOT NEEDED

$ip = currIP();
// echo $url; #NOT NEEDED
echo $ip;
echo $token;
// echo $_GET['id'] #NOT NEEDED
// echo $_GET["id"] #NOT NEEDED
$header = $ip." ".$token;
echo $header;
$python = `python hello.py $header`;
echo $python;
// $pythonA = `python hello.py $url`;
// echo $pythonA;


// $path = "1.png"; 
    // if(file_exists($path))
    // { 
    //     header('Content-Length: '.filesize($path));
    //     header('Content-Type: image/jpg');
    //     header('Content-Disposition: inline; filename="'.$path.'";');
    //     echo file_get_contents($path);
    //     exit;
    // }
?>
