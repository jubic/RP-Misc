<?php

class Welcome extends CI_Controller {

    function __construct() {
        parent::__construct();
        //$this->output->enable_profiler(TRUE);
    }

    function index() {
        $this->load->view('welcome_message');
    }

}

/* End of file welcome.php */
/* Location: ./system/application/controllers/welcome.php */