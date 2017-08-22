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

$t=time();
$currTime = date("Y-m-d::H:i:s",$t);
$key = date("YmdHis",$t);
echo "time NOW ";
echo $currTime;
echo "time salt ";
echo $key;
$myVarIWantToEncodeAndDecode = currIP();
// $key = "hacker";
$encoded = base64_encode(mcrypt_encrypt(MCRYPT_RIJNDAEL_256, md5($key), $myVarIWantToEncodeAndDecode, MCRYPT_MODE_CBC, md5(md5($key))));
$decoded = rtrim(mcrypt_decrypt(MCRYPT_RIJNDAEL_256, md5($key), base64_decode($encoded), MCRYPT_MODE_CBC, md5(md5($key))), "\0");

echo "crypted";
echo $encoded;
echo "string";
echo $decoded;



if(1 === preg_match('~[0-9]~', $token)){
    $arr = (parse_url(curPageURL()));
    echo $ip;
    echo $token;
    echo $sterileToken;
    $header = $ip." ".$token." ".$currTime;
    echo $header;
    $python = `python hello.py $header`;
    echo $python;
} else
{

}




// $path = "10.png"; 
//     if(file_exists($path))
//     { 
//         header('Content-Length: '.filesize($path));
//         header('Content-Type: image/jpg');
//         header('Content-Disposition: inline; filename="'.$path.'";');
//         echo file_get_contents($path);
//         exit;
//     }
?>
