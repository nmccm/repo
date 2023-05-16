<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Libraries\Lucene;
use Illuminate\Support\Facades\Log;

class LuceneController extends Controller
{
    /**
     * @param Request $request
     * @return void
     */
    public function getDocuments(Request $request) {
        try {
            $lucene = Lucene::getInstance()
                ->setIndex('sample')
//                ->limit(10)
//                ->orderByDesc()
                ->getDocuments();

            dd($lucene);
        }
        catch(\Exception $e) {
            log::error(__METHOD__ . " : " . $e->getMessage());
        }
    }

    /**
     * @param Request $request
     * @return void
     */
    public function getSearchDocuments(Request $request) {
        try {
            $lucene = Lucene::getInstance()
                ->setIndex('sample')
//                ->limit(10)
//                ->orderByDesc()
                ->getSearchDocuments('pono', 'ec');

            
            $result = Lucene::getInstance()
                ->setIndex('brands')
                ->setSearchFields(['name_en', 'name_kr'])
                ->getSearchDocuments('acn');
            
            dd($lucene);
        }
        catch(\Exception $e) {
            log::error(__METHOD__ . " : " . $e->getMessage());
        }
    }

    /**
     * @param Request $request
     * @return void
     */
    public function addDocument(Request $request) {
        try {
            $indx = rand(1,1000);
            $lucene = Lucene::getInstance()
                ->setIndex('sample')
                ->add([
                    'brands_id' => 1 + $indx,
                    'categories_id' => 60 + $indx,
                    'sex' => 'M' . $indx,
                ]);

            dump($lucene);
        }
        catch(\Exception $e) {
            log::error(__METHOD__ . " : " . $e->getMessage());
        }
    }

    /**
     * @param Request $request
     * @return void
     */
    public function removeIndex(Request $request) {
        try {
            $lucene = Lucene::getInstance()
                ->setIndex('sample')
                ->removeIndex();

            dd($lucene);
        }
        catch(\Exception $e) {
            log::error(__METHOD__ . " : " . $e->getMessage());
        }
    }

    /**
     * @param Request $request
     * @return void
     */
    public function removeDocument(Request $request) {
        try {
            $lucene = Lucene::getInstance()
                ->setIndex('sample')
                ->removeDocument('FLQc_ocBqjk4MusREjbo');

            dd($lucene);
        }
        catch(\Exception $e) {
            log::error(__METHOD__ . " : " . $e->getMessage());
        }
    }
}
