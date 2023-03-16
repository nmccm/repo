        $sampleString = ['메종키 ab 123 츠넵 ㅏㄴ', '비비ㅏㅇㄴ', '메종키츠'];
        foreach($sampleString as $s) {
            if($this->checkBadWord($s)) {
                echo 'in<br/>';
            }
            else {
                echo 'skip<br/>';
            }
        }

//        $cs = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'];
//        $js1 = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ'];
//        $js2 = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ',' ㅌ','ㅍ','ㅎ'];

    public function checkBadWord($string = "") {
        if(empty($string) || strlen($string) < 1) {
            return false;
        }

        $cs = [
            0xE384B1, 0xE384B2, 0xE384B4, 0xE384B7, 0xE384B8, 0xE384B9, 0xE38581,
            0xE38582, 0xE38583, 0xE38585, 0xE38586, 0xE38587, 0xE38588, 0xE38589,
            0xE3858A, 0xE3858B, 0xE3858C, 0xE3858D, 0xE3858E,
        ];

        $js1 = [
            0xE3858F, 0xE38590, 0xE38591, 0xE38592, 0xE38593, 0xE38594, 0xE38595,
            0xE38596, 0xE38597, 0xE38598, 0xE38599, 0xE3859A, 0xE3859B, 0xE3859C,
            0xE3859D, 0xE3859E, 0xE3859F, 0xE385A0, 0xE385A1, 0xE385A2, 0xE385A3,
        ];

        $js2 = [
            0xE384B1, 0xE384B2, 0xE384B3, 0xE384B4, 0xE384B5, 0xE384B6, 0xE384B7,
            0xE384B9, 0xE384BA, 0xE384BB, 0xE384BC, 0xE384BD, 0xE384BE, 0xE384BF,
            0xE38580, 0xE38581, 0xE38582, 0xE38584, 0xE38585, 0xE38586, 0xE38587,
            0xE38588, 0xE3858A, 0xE3858B, 0x20E3858C, 0xE3858D, 0xE3858E,
        ];

        $kr = preg_replace('/([a-zA-Z]+)/i', '', $string);
        $kr = preg_replace('/(\d+)/', '', $kr);
        $kr = preg_replace('/(\s+)/', '', $kr);
        $krLen = mb_strlen($kr);
        echo $kr, $krLen, '<br/>';

        for($i = 0; $i < $krLen; $i++) {
            $w = mb_substr($kr, $i, 1, 'UTF-8');
            foreach($cs as $c) {
                if(bindec(base_convert(implode(unpack("H*", $w)), 16, 2)) === bindec(base_convert(sprintf('%02X', $c), 16, 2))) {
//                    echo 'match1 : ', $w, '<br/>';
                    return false;
                }
            }
            foreach($js1 as $c) {
                if(bindec(base_convert(implode(unpack("H*", $w)), 16, 2)) === bindec(base_convert(sprintf('%02X', $c), 16, 2))) {
//                    echo 'match2 : ', $w, '<br/>';;
                    return false;
                }
            }
            foreach($js2 as $c) {
                if(bindec(base_convert(implode(unpack("H*", $w)), 16, 2)) === bindec(base_convert(sprintf('%02X', $c), 16, 2))) {
//                    echo 'match3 : ', $w, '<br/>';;
                    return false;
                }
            }
        }

        return true;
    }
