    public function _autoReserve(Request $request) {
        try {
            $allowUrls = ['localhost', '127.0.0.1', 'silktest.golfpay.co.kr', 'leaderstest.golfpay.co.kr', 'testerp.golfpay.co.kr'];
            $isAllow = false;
            foreach($allowUrls as $url) if(strpos($request->root(), $url) !== false) $isAllow = true;
            if(!$isAllow) {
                throw new \Exception($request->root());
            }

            $words = [];    // 랜덤 이름
            if($request->_memCnt > 0) {
                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, urldecode("https%3A%2F%2Fko.wiktionary.org%2Fw%2Findex.php%3Ftitle%3D%25EB%25B6%2584%25EB%25A5%2598%3A%25ED%2595%259C%25EA%25B5%25AD%25EC%2596%25B4_%25EB%25AA%2585%25EC%2582%25AC%26from%3D%25EA%25B0%2580"));
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
                curl_setopt($ch, CURLOPT_HEADER, false);
                $res = curl_exec($ch);  // 단어 뭉치 크롤링
                $httpStatusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
                curl_close($ch);

                // 2글자 또는 3글자 단어들만 추출하여 배열에 저장
                if($httpStatusCode === 200 && is_string($res)) {
                    preg_match_all("/<a href=\"\/wiki(.*)>(.*)<\/a>/", $res, $out);
                    foreach($out[0] as $tag) {
                        $tmp = explode('"', $tag)[1];
                        $word = urldecode(str_replace('/wiki/', '', $tmp));
                        if(strlen($word) >= 6 && strlen($word) <= 9) {
                            $words[] = $word;
                        }
                    }
                }
            }

            $date = isset($request->_date) ? $request->_date : date('Y-m-d');
            $isContinue = false;
            $result = getTimeTable($this->ccId, $date);
            $timeTables = TimeTable::select('*')
                ->where('cc_id', $this->ccId)
                ->where('setTime_id', $result->id)
                ->where('workday', $result->workday)
                ->where('setTime_use', 'Y')
                ->orderBy('course_id', 'desc')
                ->orderBy('part_time')
                ->orderBy('workday')
                ->orderBy('stime')
                ->get();

            foreach($timeTables as $timeTable) {

                if($isContinue) continue;

                $sendParam = [
                    'stime' => substr($timeTable->stime, 0, 5),
                    'date' => $date,
                    'part' => $timeTable->part_time,
                    'course' => $timeTable->course_id,
                    'green' => 110000,
                ];

                $res = (array) json_decode(($this->getCheckHoldRes((new Request())->merge($sendParam)))->content());

                if($res['hold'] == 'no' && $res['result']->status != '예약') {
                    log::debug('auto rev....' . $date . substr($timeTable->stime, 0, 5) . $timeTable->part_time . $timeTable->course_id);
                    $isContinue = true;
                    $sendParam = [
                        'reserve_unique' => $date . substr($timeTable->stime, 0, 5) . $timeTable->part_time . $timeTable->course_id,
                        'cc_id' => $this->ccId,
                        'sdate' => $date,
                        'teeoff' => substr($timeTable->stime, 0, 5),
                        'part_time' => $timeTable->part_time,
                        'course' => $timeTable->course_id,
                        'reserve_id' => $res['result']->id,
                        'guest_name' => Auth()->user()->name . str_replace(':', '', substr($timeTable->stime, 0, 5)),
                        'gender' => rand(1,2) < 2 ? '남' : '여',
                        'hp' => '010-1111-2222',
                        'memo_gubun' => 'reserve',
                        'toMemo' => ['reserve', 'front', 'proshop', 'food', 'games', 'notice', 'group'],
                        'cart_use_cnt' => '1',
                        'reserve_hole_type' => '18',
                        'price_code_id' => '310',
                        'visit_chk' => 'Y',
                        'visit_name' => (function($req, $wds) {
                            $ret = [];
                            if(isset($req->_memCnt) && !empty($req->_memCnt) && sizeof($wds) > 0 && $req->_memCnt > 0) for($i = 1; $i <= ($req->_memCnt > 4 ? 4 : (int) $req->_memCnt); $i++) $ret[] = $wds[rand(0, sizeof($wds))];
                            return $ret;
                        })($request, $words),
                        'visit_gender' => (function($req, $wds) {
                            $ret = [];
                            if(isset($req->_memCnt) && !empty($req->_memCnt) && sizeof($wds) > 0 && $req->_memCnt > 0) for($i = 1; $i <= ($req->_memCnt > 4 ? 4 : (int) $req->_memCnt); $i++) $ret[] = rand(1,2) < 2 ? '남' : '여';
                            return $ret;
                        })($request, $words),
                        'visit_hpr' => (function($req, $wds) {
                            $ret = [];
                            if(isset($req->_memCnt) && !empty($req->_memCnt) && sizeof($wds) > 0 && $req->_memCnt > 0) for($i = 1; $i <= ($req->_memCnt > 4 ? 4 : (int) $req->_memCnt); $i++) $ret[] = '010-1111-2222';
                            return $ret;
                        })($request, $words),
                    ];
                    $result = (array) json_decode(($this->store((new Request())->merge($sendParam)))->content());
                    log::debug($result['success']);

                    // 캐디 배정
                    if(isset($request->_caddyName) && !empty($request->_caddyName)) {
                        $caddy = ViewCaddyAndAdmin::where('name', $request->_caddyName)->get();
                        (sizeof($caddy) > 0) && Reserve::where('id', $res['result']->id)->update(['caddy1' => $caddy[0]->id]);
                    }
                }
            }
        }
        catch(\Exception $e) {
            log::info('domain : ' . $e->getMessage());
        }
    }
