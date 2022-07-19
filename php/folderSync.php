<?php

    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    class FolderSync 
    {        
        private $findDir = "/var/www/html1/htdocs/";    // 마지막 슬래쉬(/)까지 작성 
        private $targetDir = "/var/www/new/";   
        private $logPath = "/var/www/new/cli/logs/";    // 로그를 저장할 경로
        private $logFilename = "log.log";   // 저장될 로그파일명 (변경하지 않으면 YYYYMMDD.log 로 생성됨)
        private $dateScope = "2";   // 몇일전까지의 파일을 조회할것인지 .... 

        private $execOutput = [];
        private $execResult = [];        
        private $parseData = [];
        private $pregOutput = [];

        public function __construct() {
            if($this->logFilename == "log.log") {
                $this->logFilename = date("Ymd") . ".log";
            }            

            if(!is_dir($this->logPath)) {
                echo __METHOD__ . " 로그를 저장할 폴더를 찾을수 없습니다." . PHP_EOL; exit;
            }

            if(!is_dir($this->targetDir)) {
                echo __METHOD__ . " 복사할 파일을 저장할 폴더를 찾을수 없습니다." . PHP_EOL; exit;
            }
            
            if(!is_dir($this->findDir)) {
                echo __METHOD__ . " 변경사항을 감시할 폴더를 찾을수 없습니다." . PHP_EOL; exit;
            }            
        }
		
		public function setFindDir($path = false) {
            try {
				if(!$path) {
					throw new Exception("path is null");
				}	
				
				$this->findDir = $path;
				
				if(!is_dir($this->findDir)) {
					throw new Exception("변경사항을 감시할 폴더를 찾을수 없습니다." . PHP_EOL);					
				}    				
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }     			
		}

        public static function getInstance() {
            try {
                return new static;
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                                        
        }

        public function exec() {
            try {
                echo $this->findDir . " finding......" . PHP_EOL;          
				error_log(";;;;;;;;;;;;;;;;;; " . $this->findDir . " finding......" . PHP_EOL, 3, $this->logPath . $this->logFilename);                                				
                $cmd = "ls -al " . $this->findDir;
                $cmd = "find " . $this->findDir . " -type f -mtime -" . $this->dateScope . " -ls";                                
                exec($cmd, $this->execOutput, $this->execResult);
                // $this->printr();
                // $this->linePrint();
                $this->parse();
                
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                        
        }        

        private function isTargetDir() {
            try {
                if(!$this->findDir) {
                    print "can not find target directory" . PHP_EOL;
                    exit;
                }
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                            
        }

        private function isOutput() {            
            try {
                return sizeof($this->execOutput) > 0;
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                           
        }

        private function checkData() {
            try {
                if(!$this->isOutput()) {
                    throw new Exception('execOutput is empty');
                }
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                           
        }

        private function copy($org = false, $target = false) {
            try {
                if(!$org || !$target) {
                    throw new Exception('can not find org or target in copy function');
                }
                
                $tmp = explode('/', $target);
                $file = $tmp[(sizeof($tmp)-1)];
                $targetDir = str_replace($file, '', $target);
                $step = 1;

                for($i = 1; $i < sizeof($tmp); $i++) {

                    $tmpDir = "";
                    ++$step;

                    if($step < sizeof($tmp)) {
                        for($j = 1; $j < $step; $j++) {

                            $tmpDir .= "/" . $tmp[$j];                            

                            if(!$this->checkDir($tmpDir)) {
                                $log = "can not find '" . $tmpDir . "' folder. create folder (".$tmpDir.")" . PHP_EOL;                                
                                error_log("########### " . $log, 3, $this->logPath . $this->logFilename);                                
								$cmd = "cp -a " . str_replace($this->targetDir, $this->findDir, $tmpDir) . " " . $tmpDir . PHP_EOL;
								exec($cmd, $tmpOut, $tmpResult);
								echo $log . PHP_EOL;										                                
                            }
                        }
                    }
                }
                
                // exec($cmd, $out, $ret);       
                $copyResult = @copy($org, $target) ? "Ok" : "Failed";
                error_log("[" . date("H:i:s") . "] " . $copyResult . " " . $org . " => " . $target . " " . PHP_EOL, 3, $this->logPath . $this->logFilename);                    
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                         
        }

        private function checkDir($path = false) {
            try {
                if(!$path) {
                    throw new Exception('can not find path in checkDir function');
                }

                return is_dir($path);
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }             
        }

        private function parse() {  
            try {                
                if(sizeof($this->execOutput) > 0) {                    
                    foreach($this->execOutput as $no => $item) {                        
                        preg_match_all('/[0-9]+:[0-9]+.\/(.?)+/i', $item, $output);                        
                        if(isset($output[0][0]) && !empty($output[0][0])) {                                                        
                            foreach($output[0] as $out) {
                                $org = preg_replace('/[0-9]+:[0-9]+./i', '', $out);
                                $target = str_replace($this->findDir, $this->targetDir, $org); 
                                $this->copy($org, $target);
                            }
                        }
                        else {
                            throw new Exception('can not match' . PHP_EOL);
                        }                                 
                    }
					echo sizeof($this->execOutput) . "개의 파일을 모두 이동하였습니다." . PHP_EOL;
                }
				else {
					echo "nothing.... end";
				}
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                
        }

        private function linePrint() {
            try {
                if(sizeof($this->execOutput) > 0) {
                    foreach($this->execOutput as $no => $item) {
                        $this->print($no . ' : ' . $item);
                    }
                }
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }              
        }

        private function printr() {
            try {
                print_r($this->execOutput);
                print_r($this->execResult);                
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }              
        }

        private function print($str = false) {
            try {                
                echo ($str !== false) ? $str . PHP_EOL : "NULL" . PHP_EOL;
            }
            catch(Exception $e) {
                echo __METHOD__ . " exception : " . $e->getMessage() . PHP_EOL; exit;
            }                          
        }
    }

    try {        	
		$mssabuDocRoot = FolderSync::getInstance();
		$mssabuDocRoot->setFindDir("/var/www/html1/htdocs/");               
		$mssabuDocRoot->exec();         
		
		$shareFolder = FolderSync::getInstance();
		$shareFolder->setFindDir("/var/www/html/htdocs/");               
		$shareFolder->exec();               
    }
    catch(Exception $e) {
        echo "Exception : " . $e->getMessage() . PHP_EOL;
    }

?>

