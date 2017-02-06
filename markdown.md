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

# 소스코드 

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
