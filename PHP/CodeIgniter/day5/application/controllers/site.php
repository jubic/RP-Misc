<?php

class Site extends CI_Controller {

    function index() {

        $data = array();

        $query = $this->site_model->get_records();

        if ($query) {
            $data['records'] = $query;
        }

        $this->load->view('options_view', $data);
    }

    function create() {

        $data = array(
            'title' => $this->input->post('title'),
            'contents' => $this->input->post('contents')
        );

        $this->site_model->add_record($data);
        $this->index();
    }

    function update() {

        $data = array(
            'id' => $this->input->post('id'),
            'title' => $this->input->post('title'),
            'contents' => $this->input->post('contents')
        );

        $this->site_model->update_record($data);
        $this->index();
    }

    function delete() {

        $this->site_model->delete_record();
        $this->index();
    }

}

?>
