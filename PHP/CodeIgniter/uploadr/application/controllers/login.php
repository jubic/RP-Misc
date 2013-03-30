<?php

class Login extends CI_Controller {

    function __construct() {
        parent::__construct();
        $this->load->model('users');
    }

    function index() {
        $this->load->view('login');
    }

    function register() {
        if (isset($_POST['username'])) {

            // User has tried registering, insert them into database.

            $username = $_POST['username'];
            $password = $_POST['password'];

            $this->users->register($username, $password);

            redirect('login');
        } else {
            //User has not tried registering, bring up registration information.
            $this->load->view('register');
        }
    }

    function go() {

        // // Field name, error message, validation rules
        $this->form_validation->set_rules('username', 'Username', 'trim|required');
        $this->form_validation->set_rules('password', 'Password', 'trim|required');

        if ($this->form_validation->run() == FALSE) {
            $this->index();
        } else {
            // Validation has passed, Now send the email.
            $username = $this->input->post('username');
            $password = $this->input->post('password');

            //Returns userid is successful, false is unsuccessful
            $results = $this->users->login($username, $password);

            if ($results == false)
                redirect('login');
            else {
                $this->session->set_userdata(array('userid' => $results));
                redirect('profile');
            }
        }
    }

    function logout() {
        $this->session->set_userdata(array('userid' => ''));
        redirect('login');
    }

}

?>