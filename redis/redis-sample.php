<?php 	
	try {
		session_start();
		$redis = new Redis();
		$result = $redis->pconnect('111.111.111.111', 6379);
		
		if (!$result) {
			throw new Exception("connection failure");
		}
		
		$result = $redis->auth('this password here');
		
		if (!$result) {
			throw new Exception("auth failure");
		}	
		
		$redis->select(1);	// use scope 0 ~ 15
		
//		single string save
// 		$uuid = "1";
// 		$key = "dv:redis:".$uuid;
// 		$result = $redis->set($key, json_encode($uuid));
// 		if (!$result) {
// 			throw new Exception("redis save failure");
// 		}
// 		print PHP_EOL;				
// 		$content = $redis->get($key);
// 		print_r($content);
// 		print PHP_EOL;

		
//		multi string save				
// 		$key = "dv:redis";
// 		$result = $redis->multi()
// 					->set($key.":2", json_encode(['2-1','2-2']))
// 					->set($key.":3", json_encode(array('3-1','3-2')))
// 					->exec();		
// 		if (!$result) {
// 			throw new Exception("redis save failure");
// 		}		
		
// 		print PHP_EOL;		
// 		$content = $redis->get($key.":2");
// 		print_r($content);
// 		$content = $redis->get($key.":3");
// 		print_r($content);		
// 		print PHP_EOL;

		
	}
	catch(Exception $e) {
		print 'Exception message : ' . $e->getMessage();
		print PHP_EOL;
		print_r($e);
	}
?>	
	