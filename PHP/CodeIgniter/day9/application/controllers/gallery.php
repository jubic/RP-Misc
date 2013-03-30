<?php
class Gallery extends CI_Controller {
	
	function index() {
		
		$this->load->model('gallery_model');
		
		if ($this->input->post('upload')) {
			$this->gallery_model->do_upload();
		}
		
		$data['images'] = $this->gallery_model->get_images();
		
		$this->load->view('gallery', $data);
		
	}
	
}
