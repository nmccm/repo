<?php

/** 
 * $page = ($param['Page'] > 0) ? $param['Page'] : 1;
 * $pagination = new \Ironlady\Util\Pagination();
 * $pagination->setThisPage($param['Page']);
 * $pagination->setTotalCount(400);
 * //$pagination->setListPerSize(2);
 * //$pagination->setPagePerSize(3);
 * $pagination->pageing();  	
 */

namespace Ironlady\Util;

class Pagination
{
	/**
	 * What you need here :
	 * 	totalRecord
	 * 	listPerSize
	 * 	pagePerSize
	 * 	thisPage (currentPage)
	 */
	public function __construct()
	{
		$this->totalRecord = 0;
		$this->thisPage = 1;
		$this->listPerSize = \Ironlady\Nconst\Common::PAGINATION_LIST_PER_SIZE;
		$this->pagePerSize = \Ironlady\Nconst\Common::PAGINATION_PAGE_PER_SIZE;
		//$this->pageing();
	}

	public function pageing()
	{
		$this->totalPageSize = ceil($this->totalRecord / $this->listPerSize);
		$this->startPage = intval(($this->thisPage - 1) / $this->pagePerSize) * $this->pagePerSize + 1;
		$this->endPage = (($this->startPage + $this->pagePerSize - 1) > $this->totalPageSize) ? $this->totalPageSize : $this->startPage + $this->pagePerSize - 1;

		for($i = $this->startPage; $i <= $this->endPage; $i++) {
			$this->pageList[] = $i;
			$this->nextPageNumber = ($i + 1);
		}
	}

	public function setTotalCount($total = 0)
	{
		$this->totalRecord = ($total < 1) ? 1 : $total;
	}

	public function setThisPage($pageNo = 1)
	{
		$this->thisPage = $pageNo;
	}

	public function setListPerSize($listPerSize = null)
	{
		if(!is_null($listPerSize)) {
			$this->listPerSize = $listPerSize;
		}
	}

	public function setPagePerSize($pagePerSize = null)
	{
		if(!is_null($pagePerSize)) {
			$this->pagePerSize = $pagePerSize;
		}
	}

	public function getPageList()
	{
		return $this->pageList;
	}

	public function isPre()
	{
		return ($this->startPage > $this->pagePerSize) ? true : false;
	}

	public function isNext()
	{
		return ($this->endPage != $this->totalPageSize) ? true : false;
	}

	public function getPrePageNumber()
	{
		return ($this->startPage - 1);
	}

	public function getNextPageNumber()
	{
		return $this->nextPageNumber;
	}

	public function getListPerSize()
	{
		return $this->listPerSize;
	}

	public function getPagePerSize()
	{
		return $this->pagePerSize;
	}

	public function getThisPage()
	{
		return $this->thisPage;
	}

	public function getStartPage()
	{
		return $this->startPage;
	}

	public function getEndPage()
	{
		return $this->endPage;
	}
	
	public function getTotalCount() 
	{
		return $this->totalRecord;
	}
}

?>