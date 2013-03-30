<?php

class Foo {

    var $CI;

    function  __construct() {

        $this->CI =& get_instance();

        echo 'Constructor was called. <br/>';
    }

    function test($value) {

        echo "You passed me $value <br/>";

        echo 'Your language is: '. $this->CI->config->item('language').'<br/>';

    }

}

?>