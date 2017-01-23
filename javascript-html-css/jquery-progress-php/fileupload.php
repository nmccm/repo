<?php
$app->map(
	Common::REQUEST_POST, Page::PAGE_FILE_UPLOAD,
	function ($request, $response, $args)
	{
		ini_set('upload_max_filesize', '50M');
		ini_set('post_max_size', '50M');

		if (sizeof($_FILES) > 0)
		{
			foreach($_FILES as $key => $fileInfo)
			{
				$uploadfile = Common::FILE_UPLOAD_DIR . basename($fileInfo['name']);

				$rMsg = (move_uploaded_file($fileInfo['tmp_name'], $uploadfile) && file_exists($uploadfile))
				? Common::JSON_SUCCESS_MSG
				: Common::JSON_FAILURE_MSG ;
			}
				
			echo json_encode(['code' => "1", 'msg' => $rMsg]);
		}
	}
);