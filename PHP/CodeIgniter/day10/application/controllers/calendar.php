<?php
class Calendar extends CI_Controller {
	
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
		
		$data['calendar'] = $this->calendar_model->generate($year, $month);
		
		$this->load->view('calendar', $data);
		
	}
	
}
