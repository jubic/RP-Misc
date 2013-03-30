<?php

class Test extends CI_Controller {

    function index($radius) {

        $this->load->helper('math');

        echo "A circle with radius $radius has area ".circle_area($radius). "<br/>";

        $this->load->helper('date');

        echo "Current date in Mysql format: ". date_mysql(). "<br/>";

        $this->load->library('Foo');

        $this->foo->test('bar');

        $this->load->library('Form_validation');

        $this->form_validation->test();
    }

}

?>
