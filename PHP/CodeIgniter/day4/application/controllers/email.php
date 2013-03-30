<?php

/**
 * SEND EMAIL WITH GMAIL
 */
class Email extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

    function index() {
        $this->load->view('newsletter');
    }

    function send() {

        // Field name, error message, validation rules
        $this->form_validation->set_rules('name', 'Name', 'trim|required');
        $this->form_validation->set_rules('email', 'Email', 'trim|required|valid_email');

        if ($this->form_validation->run() == FALSE) {
            $this->index();
        } else {
            // Validation has passed, Now send the email.
            $name = $this->input->post('name');
            $email = $this->input->post('email');

            $this->load->library('email');
            $this->email->set_newline("\r\n");

            $this->email->from('accidental.wong@gmail.com', 'Jubic Wong');
            $this->email->to($email);
            $this->email->subject('Test Newsletter Signup Confirmation');
            $this->email->message('You\'ve now signed up, fool!');

            $path = $this->config->item('server_root');
            $file = $path . "/codeigniter/day4/attachments/newsletter1.txt";

            $this->email->attach($file);

            if ($this->email->send()) {
                $this->load->view('signup_confirmation');
            } else {
                show_error($this->email->print_debugger());
            }
        }
    }

}

?>