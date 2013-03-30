<?php

class Calendar extends CI_Controller {

    function __construct() {
        parent::__construct();
        //$this->output->enable_profiler(TRUE);
    }

    function index($year = null, $month = null) {

        if (!$year) {
            $year = date('Y');
        }
        if (!$month) {
            $month = date('m');
        }

        $this->load->model('calendar_model');

        $day = $this->input->post('day');

        if ($day) {
            $this->calendar_model->add_calendar_data(
                    "$year-$month-$day",
                    $this->input->post('data')
            );
        }

        $this->benchmark->mark('generate_start');
        $data['calendar'] = $this->calendar_model->generate($year, $month);
        $this->benchmark->mark('generate_end');

        $this->load->view('calendar', $data);
    }

}
