# 제목

제목을 쓰기 위해선 앞에 샵을 붙인다.
샵을 하나 쓰면 HTML의 h1 태그를, 샵을 두개 쓰면 h2 태그를 의미한다. 
즉 샵은 하나에서 여섯개까지 쓸 수 있고, 샵이 늘어날때마다 제목의 수준은(보통 글씨 크기가 작아진다) 내려간다. 

# 번호 없는 리스트

마이너스, 플러스, 아스트로키 문자를 사용한다.
아래는 마이너스 사용예제이다.

- 마이너스1
- 마이너스2

아래는 플러스 사용예제이다.

+ 플러스1
+ 플러스2

아래는 아스트로키 사용예제.

* 아스1
* 아스2

# 굵은글씨체 표현

**굵은**글씨가 표현된다. 

# 이탤릭체 표현

_이탤릭_글씨가 표현된다.

# 인용문

이렇게 쓰다가 인용문이 필요하면 

> 작성하고 쓰면 된다.
> 줄내림도 해보았다.

그리고 다시 원래의 글문단으로 돌아올수 있다.

# 링크

구글의 주소는 [https://google.com](https://google.com) 입니다.

# 소스코드 

소스코드는 아래와 같이 표현될수 있다. 

```php
<?php

use \Ironlady\Nconst\Page;

// Application middleware
$app->add(function ($request, $response, $next) 
{
	//$this->translator->setLocale('en');
	$uri = $request->getUri();
	
	if($uri->getPath() != Page::PAGE_LOGIN) {		
		if(!(new \Ironlady\Member\Member())->isLogin()) {
			header("Location:".Page::PAGE_LOGIN);
		}	
	}
	
	$response = $next($request, $response);
    return $response;
});
```

# 쉘 명령어

```linux
# ls -al
```

## Hidden test example

일반 주석을 사용해보면 다음과 같다.

// 라인주석

/* 블럭 주석 */

## 이미지

아래 이미지는 구글 클라우드에 저장되어있으며, 클릭시 구글로 가도록 링크 되어 있다.

[![google.com](https://drive.google.com/open?id=0B9T2uJMhGmG6NGxxamRLR3dHdXc)](http://google.com)