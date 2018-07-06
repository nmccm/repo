<?php 

namespace Srm\Traits;

class Pagination 
{
    private $listSize = 10;			// 한페이지에 보여줄 줄수
    private $pageSize = 10;			// 한페이지에 보여줄 페이지수
    private $totalListSize = null;	// 전체 레코드수
    private $totalPage = null;		// 전체 페이지수
    private $page = null;			// 현재 페이지 번호
    private $start = 0;			    // 시작번호
    private $startPage = null; 		// 시작 페이지
    private $endPage = null;		// 마지막 페이지
    private $url = null;			// 페이지 이동시에도 계속 가지고 다녀야 할 $_GET[] 값

    public function getStartNo()
    {
        return $this->start;
    }
    
    public function getTotalListSize()
    {
        return $this->totalListSize;
    }
    
    public function getPageSize()
    {
        return $this->pageSize;
    }
    
    public function getListSize()
    {
        return $this->listSize;
    }
    
    public function getUrl()
    {
        return $this->url;
    }
    
    private function preparePagination()
    {
        $this->totalPage = ceil($this->totalListSize / $this->listSize);
        $this->start = (int) $this->page * $this->listSize;
    }
    
    public function setPagination(int $pageNo = 0, int $totalCnt = 0, String $parameter = "")
    {        
        $this->page = $pageNo;
        $this->url = (strlen($parameter) > 0) ? $parameter : $this->url;        
        $this->totalListSize = $totalCnt;        
        $this->preparePagination();
    }

    public function setListSize(int $listSize) 
    {
        $this->listSize = $listSize;
        $this->preparePagination();
    }

    public function setPageSize(int $pageSize) 
    {
        $this->pageSize = $pageSize;
        $this->preparePagination();
    }

    public function setUrl(string $url) 
    {
        $this->url .= (strlen($this->url) > 0) ? '&'.$url : $url;
    }

    public function showDefaultPagination(string $styleClass = '')
    {        
        $this->startPage = ((int)($this->page / $this->pageSize)) * $this->pageSize;
        $this->endPage = $this->startPage + $this->pageSize;
        
        if($this->endPage > $this->totalPage) {
            $this->endPage = $this->totalPage;
        }
        
        if($this->startPage > 0) {
            $preLink1 = "<a class='".$styleClass."' href='?page=".($this->startPage - $this->pageSize)."&".$this->url."'>";
            $preLink2 = "</a>&nbsp;";
        }
                
        $tempPage .= $preLink1."[이전] ".$preLink2;
        
        for($i = $this->startPage; $i < $this->endPage; $i++)
        {
            if($i == $this->page) $tempPage .= "&nbsp;<font size=2 class='".$styleClass."'><b>".($i + 1)."</b></font>&nbsp;";
            else $tempPage .= "<font size=2><a class='".$styleClass."' href='?page=".$i."&".$this->url."'>[".($i + 1)."]</a></font>";
        }
        
        if($this->endPage < $this->totalPage) {
            $nextLink1 = "&nbsp;<a class='".$styleClass."' href='?page=".$this->endPage."&".$this->url."'>";
            $nextLink2 = "</a>";
        }
        
        $tempPage .= $nextLink1." [다음]".$nextLink2;
        
        return $tempPage;
    }

    public function showBootstrapPagination()
    {
        $this->startPage = ((int)($this->page / $this->pageSize)) * $this->pageSize;
        $this->endPage = $this->startPage + $this->pageSize;
        
        if($this->endPage > $this->totalPage) {
            $this->endPage = $this->totalPage;
        }
        
        $tempPage = '';
        $amper = '';
        
        if (strlen($this->url) > 0) {
            $amper = "&";
        }        
        
        $tempPage .= "<ul class=\"pagination\">";
        
        if($this->startPage > 0) {            
            if (strlen($this->url) > 0) {
                 $link = "&" . $this->url;
            }            
            $tempPage .= "<li class=\"page-item\"><a class=\"page-link\" href=\"?page=" . ($this->startPage - $this->pageSize) . $amper . $this->url . "\">Previous</a></li>";            
        }
        
        for($i = $this->startPage; $i < $this->endPage; $i++) {
            if($i == $this->page) {
                $tempPage .= "<li class=\"page-item active\"><a class=\"page-link\" href=\"#\">" . ($i + 1) . "</a></li>";
            }
            else {
                $tempPage .= "<li class=\"page-item\"><a class=\"page-link\" href=\"?page=" . $i . $amper . $this->url . "\">" . ($i + 1) . "</a></li>";
            }
        }
        
        if($this->endPage < $this->totalPage) {
            $tempPage .= "<li class=\"page-item\"><a class=\"page-link\" href=\"?page=" . $this->endPage . $amper . $this->url . "\">Next</a></li>";   
        }    
        
        $tempPage .= "</ul>";
        
        return $tempPage;
    }		
}