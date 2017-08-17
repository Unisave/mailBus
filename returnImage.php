<?php
$ip = file_get_contents('http://122.165.116.168/pyurl-dbupdater/ipExtractor.php');
$path = "1.png";

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

$arr = (parse_url(curPageURL()));
$output = array_slice($arr,1);
echo implode("",$output);
echo PHP_EOL;




echo $ip
// echo $_GET['id']
// echo $_GET["id"]
// $header = $ip.$token;
// echo $header
// $python = `python hello.py `;
// echo $python;
//     if(file_exists($path))
//     { 
//         header('Content-Length: '.filesize($path));
//         header('Content-Type: image/jpg');
//         header('Content-Disposition: inline; filename="'.$path.'";');
//         echo file_get_contents($path);
//         exit;
//     }
?>
