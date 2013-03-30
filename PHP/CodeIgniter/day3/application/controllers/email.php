<?php

/**
 * SEND EMAIL WITH GMAIL
 */
class Email extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

    function index() {

        $this->load->library('email');
        $this->email->set_newline("\r\n");

        $this->email->from('accidental.wong@gmail.com', 'Jubic Wong');
        $this->email->to('accidental.wong@gmail.com');
        $this->email->subject('This is an email test');
        $this->email->message('It is working, Great!');

        $path = $this->config->item('server_root');
        $file = $path."/codeigniter/day3/attachments/yourInfo.txt";

        $this->email->attach($file);

        if($this->email->send()) {

            echo 'Your email was sent, fool';
            
        }

        else {
            
            show_error($this->email->print_debugger());
            
        }
    }

}

?>