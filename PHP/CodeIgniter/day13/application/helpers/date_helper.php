<?php

function date_mysql($time = NULL) {

    if(!$time) {

        date_default_timezone_set('Asia/Singapore');
        $time = time();

    }

    return date('Y-m-d H:m:s',$time);

}

?>