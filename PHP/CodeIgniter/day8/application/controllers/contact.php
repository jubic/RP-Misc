<?php

class Contact extends CI_Controller {

    function index() {

        $data['main_content'] = 'contact_form';
        $this->load->view('includes/template', $data);
    }

    function submit() {

        $name = $this->input->post('name');


        if($this->input->post('ajax')) {
            $data['main_content'] = 'contact_submitted';
            $this->load->view($data['main_content']);
        }

        else {
            $this->load->view('includes/template', $data);
        }
    }

}

?>