<?php 

$id = '34DJ39HH94J';
$packet = "param1=1&code=GG&idx=10";
$enc = encrypt_md5($packet, $id);
echo $enc, PHP_EOL;
$dec = decrypt_md5($enc, $id);
echo $dec, PHP_EOL; 

function decrypt_md5($hex_buf, $key){
	$len = strlen($hex_buf);
	for ($i=0; $i<$len; $i+=2)
		$buf .= chr(hexdec(substr($hex_buf, $i, 2)));
	
	$key1 = pack("H*", md5($key));
	while(strlen($buf))
	{
	   $m = substr($buf, 0, 16);
	   $buf = substr($buf, 16);
	   
	   $c = "";
	   for($i=0;$i<16;$i++)
	   {
		   $c .= $m{$i}^$key1{$i};
	   }
	   
	   $ret_buf .= $m = $c;
	   $key1 = pack("H*",md5($key.$key1.$m));
	}
	
	return($ret_buf);
}

function encrypt_md5($buf, $key){
	$key1 = pack("H*",md5($key));

	while(strlen($buf))
	{
		$m = substr($buf, 0, 16);
		$buf = substr($buf, 16);
		
		$c = "";
		for($i=0;$i<16;$i++)
		{
			$c .= $m{$i}^$key1{$i};
		}
		$ret_buf .= $c;
		$key1 = pack("H*",md5($key.$key1.$m));
	}


	$len = strlen($ret_buf);
	for($i=0; $i<$len; $i++)
		$hex_data .= sprintf("%02x", ord(substr($ret_buf, $i, 1)));
	return($hex_data);
}